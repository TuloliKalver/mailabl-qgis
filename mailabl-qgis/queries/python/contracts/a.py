
from PyQt5.QtCore import QCoreApplication
from ..DataLoading_classes import Graphql_contracts, GraphQLQueryLoader
from ..query_tools import requestBuilder

class getContractsWhere:
    @staticmethod
    def QueryProjects_relatedProperties(self, id_value):
        #print(f"id value in query {id_value}")
        #Load the project query using the loader instance
        query_loader = Graphql_contracts()
        query = GraphQLQueryLoader.load_query_for_projects(self,query_loader.Q_where_Contracts_related_properties)
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        #Initialize variables for pagination
        end_cursor = None  # Initialize end_cursor before the loop
        total_fetched = 0        # Initialize an empty list to store fetched items
        properties_items = []
        
        while (desired_total_items is None or total_fetched < desired_total_items):
            # Construct variables for the GraphQL query
            variables = {
                    "propertiesFirst": items_for_page,
                    "propertiesAfter": end_cursor if end_cursor else None,
                    "id": id_value
                    }
            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                #edges = data.get("data", {}).get("project", {}).get("properties", {}).get("edges", {})
                #print("egdges")
                #print(edges)
                project_data = data.get("data", {}).get("contract", {})
                properties_data = project_data.get("properties", {})
                edges = properties_data.get("edges", [])
                #print("edges")
                #print(edges)
                pageInfo = properties_data.get("pageInfo", {})
                #print(f"pageInfo: {pageInfo}")
                end_cursor = pageInfo.get("endCursor")
                hasNextPage = pageInfo.get("hasNextPage")
                count = pageInfo.get('count')
                #print(f"count {count}")
                for edge in edges:
                    node = edge.get("node", {})
                    cadastral_unit_number = node.get("cadastralUnitNumber", "")
                    #print(cadastral_unit_number)
                    properties_items.append(cadastral_unit_number)
                print(f"properties_items: {properties_items}")
                #print(count)
                total_fetched += count
                #print(total_fetched)
                # Check whether the last page of projects has been reached
                if not end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not hasNextPage:
                    break
                QCoreApplication.processEvents()
            else:
                print(f"Error: {response.status_code}")
                return None
        # Return only the desired number of items
        return properties_items