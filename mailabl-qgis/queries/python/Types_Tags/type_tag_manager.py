from PyQt5.QtCore import QCoreApplication

from ....queries.python.DataLoading_classes import GraphqlQueriesContracts, GraphqlQueriesEasements
from ....queries.python.query_tools import requestBuilder
from ....config.settings import SettingsDataSaveAndLoad
from ....KeelelisedMuutujad.modules import Modules

class InsertTypesToComboBox:
    def add_elementTypes_to_listview (self, combo_box, preferred_items, module):
        # Clear existing items in the combo box
        combo_box.clear()

        # Populate the combo box with items and associate each item's text with its ID
        if module == Modules.MODULE_CONTRACTS:
            types = ContractTypes.contract_types(self)
        if module == Modules.MODULE_EASEMENTS:
            types = EasementTypes.easement_types(self)

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
        query = GraphqlQueriesContracts.load_query_for_contracts(query_loader.contracts_types)        
        # Set the desired total number of items to fetch
        desired_total_items = None  
        items_for_page = 50  
        end_cursor = None  
        end_cursor = None
        total_fetched = 0        
                        
        contract_types = []
            
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                QCoreApplication.processEvents()
                
                contract_types_data = data.get("data", {}).get("contractTypes", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("contractTypes", {}).get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")
                hasNextPage = pageInfo.get("hasNextPage")
                for contract_type_info in contract_types_data:
                    node_info = contract_type_info.get('node', {})
                    contract_type_name = node_info.get('name',"")
                    contract_type_id = node_info.get('id',"")
                    contract_types.append((contract_type_name, contract_type_id))
                    
                QCoreApplication.processEvents()
                return contract_types
            else:
                print(f"Error: {response.status_code}")
                return None
            

class EasementTypes:
    def easement_types(self):

        query_loader = GraphqlQueriesEasements()
        query = GraphqlQueriesEasements.load_query_for_easements(self, query_loader.easement_types)        
        desired_total_items = None 
        items_for_page = 50  
        end_cursor = None
        end_cursor = None
        total_fetched = 0                      
        contract_types = []
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)
            if response.status_code == 200:
                data = response.json()
                QCoreApplication.processEvents()

                easement_types_data = data.get("data", {}).get("easementTypes", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("easementTypes", {}).get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")
                for easement_type_info in easement_types_data:
                    node_info = easement_type_info.get('node', {})
                    easement_type_name = node_info.get('name',"")
                    easement_type_id = node_info.get('id',"")
                    contract_types.append((easement_type_name, easement_type_id))
                    
                QCoreApplication.processEvents()
                return contract_types
            else:
                print(f"Error: {response.status_code}")
                return None
