
import pandas as pd
from PyQt5.QtCore import Qt, QCoreApplication
from ..Statuses.statusManager import Statuses
from ..DataLoading_classes import GraphQLQueryLoader, GraphqlContracts
from ..query_tools import requestBuilder
from ....KeelelisedMuutujad.modules import Module

class ContractsQueries_list:
    @staticmethod
    def query_contracts_by_status(self, statuses):
        #print(statuses)
        # Load the project query using the loader instance

        module = Module.CONTRACT
        query_name =  GraphqlContracts.ALL_CONTRACTS
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)


        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        items_for_properties_page = 50
        end_cursor = None  # Initialize end_cursor before the loop
        properties_end_cursor = None
        total_fetched = 0        # Initialize an empty list to store fetched items
        fetched_items = []
        
        while (desired_total_items is None or total_fetched < desired_total_items):
            # Construct variables for the GraphQL query
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None,
                "propertiesFirst": items_for_properties_page,
                "propertiesAfter": properties_end_cursor if properties_end_cursor else None,
                "where": {
                    "AND": [
                        {
                            "column": "STATUS",
                            "operator": "IN",
                            "value": statuses
                        }
                    ]
                }
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get("contracts", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("contracts", {}).get("pageInfo", {})
                properties_page_info = data.get("data", {}).get("contracts", {}).get("properties",{}).get("pageInfo",{})
                properties_end_cursor = properties_page_info.get("endCursor")
                #print(f"propesties_end_cursor: '{properties_end_cursor}'")
                end_cursor = pageInfo.get("endCursor")
                hasNextPage = pageInfo.get("hasNextPage")
                fetched_items.extend(fetched_data)
                total_fetched += len(fetched_data)

                # Check whether the last page of projects has been reached
                if not end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items or not hasNextPage):
                    break

            else:
                #print(f"Error: {response.status_code}")
                return None

            QCoreApplication.processEvents()

        # Return only the desired number of items
        return fetched_items[:desired_total_items]
