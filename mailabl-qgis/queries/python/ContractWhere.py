
from PyQt5.QtCore import QCoreApplication
from .FileLoaderHelper import GraphqlContracts, GraphQLQueryLoader
from .query_tools import requestBuilder
from ...KeelelisedMuutujad.modules import Module

class getContractsWhere:
    @staticmethod
    def query_contracts_related_properties(self, id_value):

        module = Module.CONTRACT
        query_name =  GraphqlContracts.RELATED_PROPERTIES
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)



        desired_total_items = None
        items_for_page = 50  
        end_cursor = None  
        total_fetched = 0  
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
                project_data = data.get("data", {}).get("contract", {})
                properties_data = project_data.get("properties", {})
                edges = properties_data.get("edges", [])
                pageInfo = properties_data.get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")
                hasNextPage = pageInfo.get("hasNextPage")
                count = pageInfo.get('count')
                for edge in edges:
                    node = edge.get("node", {})
                    cadastral_unit_number = node.get("cadastralUnitNumber", "")
                    properties_items.append(cadastral_unit_number)
                total_fetched += count
                if not end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not hasNextPage:
                    break
                QCoreApplication.processEvents()
            else:
                print(f"Error: {response.status_code}")
                return None
        return properties_items