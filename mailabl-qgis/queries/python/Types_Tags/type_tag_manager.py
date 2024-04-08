from PyQt5.QtCore import QCoreApplication

from ....queries.python.DataLoading_classes import GraphqlQueriesContracts
from ....queries.python.query_tools import requestBuilder


class InsertTypesToComboBox:
    def add_elementTypes_to_listview (self, comboBox, module_name):
        # Clear existing items in the combo box
        comboBox.clear()

        # Populate the combo box with items and associate each item's text with its ID
        types = Types.types_by_module_names(module_name)
        print(types)
        for item_text, item_id in types:
            comboBox.addItem(item_text)
            comboBox.setItemData(comboBox.count() - 1, item_id)
        
        # Ensure the first item is selected
        if comboBox.count() > 0:
            comboBox.setCurrentIndex(0)

class Types:
    def types_by_module_names(self):
        #print(f"selected_features: '{module_name}'")
        #print(statuses)
        # Load the project query using the loader instance
        query_loader = GraphqlQueriesContracts()
        query = GraphqlQueriesContracts.load_query_for_contracts(self, query_loader.contracts_types)        
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        end_cursor = None  # Initialize end_cursor before the loop
        end_cursor = None
        total_fetched = 0        # Initialize an empty list to store fetched items
                        
        fetched_items = []
            
        while total_fetched <= 1:#(desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                print("data")
                print(data)
                #fetched_data = data.get("data", {}).get("contracts", {}).get("edges", [])
                #pageInfo = data.get("data", {}).get("contracts", {}).get("pageInfo", {})
                #print(f"propesties_end_cursor: '{properties_end_cursor}'")
                #end_cursor = pageInfo.get("endCursor")
                #hasNextPage = pageInfo.get("hasNextPage")
                #fetched_items.extend(fetched_data)
                #total_fetched += len(fetched_data)

                # Check whether the last page of projects has been reached
                #if not end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items or not hasNextPage):
                #    break
                total_fetched += 1
            #else:
                #print(f"Error: {response.status_code}")
            #    return None

            QCoreApplication.processEvents()

        # Return only the desired number of items
        #return fetched_items[:desired_total_items]
            