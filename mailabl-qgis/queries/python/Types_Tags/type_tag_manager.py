from PyQt5.QtCore import QCoreApplication

from ....queries.python.DataLoading_classes import GraphqlQueriesContracts, GraphqlQueriesEasements
from ....queries.python.query_tools import requestBuilder
from ....config.settings import SettingsDataSaveAndLoad
from ....config.mylabl_API.modules import MODULE_CONTRACTS, MODULE_EASEMENTS

class InsertTypesToComboBox:
    def add_elementTypes_to_listview (self, combo_box, preferred_items, module):
        # Clear existing items in the combo box
        combo_box.clear()

        # Populate the combo box with items and associate each item's text with its ID
        if module == MODULE_CONTRACTS:
            types = ContractTypes.contract_types(self)
        if module == MODULE_EASEMENTS:
            types = easementTypes.easement_types(self)

        for item_text, item_id in types:
            combo_box.addItem(item_text)
            combo_box.setItemData(combo_box.count() - 1, item_id)

        selected_types = []

        # Split the text by newline characters
        lines = preferred_items.split('\n')
        for line in lines:
            # Split each line by comma and add items to selected_types list
            items = line.split(',')
            selected_types.extend(item.strip() for item in items if item.strip())

        combo_box.setCheckedItems(selected_types)
        

class ContractTypes:
    def contract_types(self):

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
            

class easementTypes:
    def easement_types(self):

        query_loader = GraphqlQueriesEasements()
        query = GraphqlQueriesEasements.load_query_for_easements(self, query_loader.easement_types)        
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
                easement_types_data = data.get("data", {}).get("easementTypes", {}).get("edges", [])
                #print("fetched_data")
                #print(contract_types)
                pageInfo = data.get("data", {}).get("easementTypes", {}).get("pageInfo", {})
                #print("page_info")
                #print(pageInfo)
                #print(f"propesties_end_cursor: '{properties_end_cursor}'")
                end_cursor = pageInfo.get("endCursor")
                for easement_type_info in easement_types_data:
                    # Access the node information
                    node_info = easement_type_info.get('node', {})
                    #print(f"node info: {node_info}")
                    easement_type_name = node_info.get('name',"")
                    #print(f"contract type name: {contract_type_name}")
                    easement_type_id = node_info.get('id',"")
                    #print(f"contract_type_id: {contract_type_id}")
                    # Append the node_info to the list
                    contract_types.append((easement_type_name, easement_type_id))
                    
                QCoreApplication.processEvents()
                #print(f"contract_types: {contract_types}")
                return contract_types
            else:
                print(f"Error: {response.status_code}")
                return None
