from PyQt5.QtCore import QCoreApplication

from ....queries.python.DataLoading_classes import GraphqlQueriesContracts
from ....queries.python.query_tools import requestBuilder


class InsertTypesToComboBox:
    def add_elementTypes_to_listview (self, combo_box):
        # Clear existing items in the combo box
        combo_box.clear()

        # Populate the combo box with items and associate each item's text with its ID
        types = Types.types_by_module_names(self)
        print(types)
        for item_text, item_id in types:
            combo_box.addItem(item_text)
            combo_box.setItemData(combo_box.count() - 1, item_id)


        checked_items = ['Personal - töövõtuleping','Tellimus-PP']
        combo_box.setCheckedItems(checked_items)
                # Set items as selected based on their IDs
        #for index in range(combo_box.count()):
        #    item_id = combo_box.itemData(index)
        #    if item_id in checked_items:
        #        combo_box.setCurrentIndex(index)

        

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
                        
        contract_types = []
            
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                contract_types_data = data.get("data", {}).get("contractTypes", {}).get("edges", [])
                #print("fetched_data")
                #print(contract_types)
                pageInfo = data.get("data", {}).get("contractTypes", {}).get("pageInfo", {})
                #print("page_info")
                #print(pageInfo)
                #print(f"propesties_end_cursor: '{properties_end_cursor}'")
                end_cursor = pageInfo.get("endCursor")
                hasNextPage = pageInfo.get("hasNextPage")
                for contract_type_info in contract_types_data:
                    # Access the node information
                    node_info = contract_type_info.get('node', {})
                    #print(f"node info: {node_info}")
                    contract_type_name = node_info.get('name',"")
                    #print(f"contract type name: {contract_type_name}")
                    contract_type_id = node_info.get('id',"")
                    #print(f"contract_type_id: {contract_type_id}")
                    # Append the node_info to the list
                    contract_types.append((contract_type_name, contract_type_id))
                    

                # Check whether the last page of projects has been reached
                #if not end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items or not hasNextPage):
                #    break
                #total_fetched += 1
                QCoreApplication.processEvents()
                #print(f"contract_types: {contract_types}")
                return contract_types
            else:
                print(f"Error: {response.status_code}")
                return None

            
        # Return only the desired number of items
        #return fetched_items[:desired_total_items]
            