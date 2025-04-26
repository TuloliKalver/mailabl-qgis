from PyQt5.QtCore import QCoreApplication
from ..FileLoaderHelper import GraphqlProjects, GraphQLQueryLoader, GraphqlContracts, GraphqlEasements, GraphqlTasks
from ..query_tools import requestBuilder
from ...python.responses import JsonResponseHandler, GetValuFromEdge
from ...python.responses import HandlePropertiesResponses
from ....KeelelisedMuutujad.modules import Module


class Constants:
    package_size = 25
    sleep_duration = 2 #time for sleep
    total_fetched = 0
    items_for_page_minimum = 1
    items_for_page_medium = 25
    items_for_page_large = 50
    sleepPackage = items_for_page_medium
    desired_total_items = None
    

class PropertiesModuleFetcher:
    """
    Fetches properties (e.g., cadastral unit numbers) related to a specific module type (Project, Contract, Easement)
    using paginated GraphQL queries.

    Attributes:
        id_value (str): ID of the parent item (e.g., project ID).
        module (Module): Enum representing the data module.
    """

    def __init__(self, id_value: str, module: Module):
        """
        Initializes the fetcher with a given module and item ID.

        Args:
            id_value (str): The ID of the item whose properties are to be fetched.
            module (Module): The module to fetch from (e.g., Module.PROJECT).
        """
        self.id_value = id_value
        self.module = module
        self.query = self._load_query_by_module_for_froperties()
        self.items_to_fetch = "properties"
        self.path = [module, self.items_to_fetch]

        print(f"id_value: {id_value}, module: {module}")
        print(f"query: {self.query}")

    def _load_query_by_module_for_froperties(self):
        """
        Loads the appropriate GraphQL query based on the selected module.

        Returns:
            str: The GraphQL query string.

        Raises:
            ValueError: If the module is not recognized.
        """
        if self.module == Module.PROJECT:
            query_loader = GraphqlProjects()
            query_name = query_loader.Q_where_Projects_related_properties
            query = GraphQLQueryLoader.load_query_by_module(self.module, query_name)
            return query
        elif self.module == Module.CONTRACT:
            query_name = GraphqlContracts.RELATED_PROPERTIES
            query = GraphQLQueryLoader.load_query_by_module(self.module, query_name)
            return query
        elif self.module == Module.EASEMENT:
            query_name = GraphqlEasements.RELATED_PROPERTIES
            query = GraphQLQueryLoader.load_query_by_module(self.module, query_name)  
            return query
        
        elif self.module == Module.ASBUILT:
            query_name = GraphqlTasks.RELATED_PROPERTIES
            query = GraphQLQueryLoader.load_query_by_module(self.module, query_name)  
            return query

        else:
            raise ValueError(f"Invalid module: {self.module}")


    def _fetch_properties_cadastral_numbers(self, desired_total_items: int = None) -> list:
        """
        Fetches cadastral unit numbers related to the given module and item ID.

        Args:
            desired_total_items (int, optional): Limit the number of properties to fetch. Defaults to None (fetch all).

        Returns:
            list: List of cadastral unit numbers.
        """
        end_cursor = None
        total_fetched = 0
        properties_items = []

        while desired_total_items is None or total_fetched < desired_total_items:
            variables = {
                "propertiesFirst": Constants.items_for_page_large,
                "propertiesAfter": end_cursor if end_cursor else None,
                "id": self.id_value
            }
            #print(f"query before send: {self.query}")
            response = requestBuilder.construct_and_send_request(self.query, variables)
            QCoreApplication.processEvents()

            if response.status_code == 200:
                edges = JsonResponseHandler.get_edges_from_path(response, self.path)
                end_cursor, has_next_page, count = JsonResponseHandler.get_page_detalils_from_path(response, self.path)

                for edge in edges:
                    cadastral_unit_number = GetValuFromEdge.get_cadastral_unit_number(edge)
                    if cadastral_unit_number is not None:
                        properties_items.append(cadastral_unit_number)

                total_fetched += count
                if not end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not has_next_page:
                    break
            else:
                raise Exception(f"Error: {response.status_code}")

        return properties_items


    @staticmethod
    def _fetch_module_feature_conneted_with_propertie_list(cadastral_numbers, module=None):
        #print(f"cadastral_numbers: {cadastral_numbers}")

        my_module = Module.PROJECT

        query_name = GraphqlProjects.Q_Properties_related_projects
        query = GraphQLQueryLoader.load_query_by_module(my_module, query_name)
        
        #print(f"query: {query}")
        items_for_page = 50
        end_cursor = None
        projects_list = []
        variables =        {
                    "first": items_for_page,
                    "after": "",
                    "where": {
                        "AND": [
                            {
                                "column": "CADASTRAL_UNIT_NUMBER",
                                "operator": "IN",
                                "value": cadastral_numbers
                            }
                        ]
                    }
                }
        while True:
            response = requestBuilder.construct_and_send_request(query, variables)
            
            module = (f"{module}s")
            if response.status_code == 200:
                #print(f"YES WE ARE DEVELOPING IN THE RIGHT DIRECTION!")

                #TODO chec for standardizing options
                edge = HandlePropertiesResponses._response_properties_data_edges(response)
                for item in edge:
                    for project in item['node'][module]['edges']:
                        if project['node']['id']:
                            projects_list.append(project['node'])
                    page_info = item['node'][module]['pageInfo']
                    if page_info['hasNextPage']:
                        end_cursor = page_info['endCursor']
                        variables['after'] = end_cursor
                        break
                else:
                    break  # Exit loop if there are no more pages
        return projects_list