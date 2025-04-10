# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

from PyQt5.QtCore import QCoreApplication
from ..FileLoaderHelper import GraphQLQueryLoader, GraphqlContracts, GraphqlEasements, GraphqlStatuses
from ..query_tools import requestBuilder
from ....KeelelisedMuutujad.modules import Module

STATE_OPEN = "OPEN"
STATE_CLOSED = "CLOSED"

class Statuses:

    def get_all_statuses_by_module(self, module):
        print(f"Getting all statuses by module: {module} in getting all statuses")
        status_module = Module.STATUSES
        query_file =  GraphqlStatuses.STATUSES
        query = GraphQLQueryLoader.load_query_by_module(status_module, query_file)

        variables = {
            "where": {
                "AND":[
                {
                "column": "MODULE",
                "value": f"{module}s",
                }
                ]
            }
        }
        response = requestBuilder.construct_and_send_request(self, query, variables)
        if response.status_code == 200:
            data = response.json()
            statuses_data = data.get('data', {}).get('statuses', {}).get('edges', [])
            statuses = []
            for status_info in statuses_data:
                node_info = status_info.get('node', {})
                status_name = node_info.get('name',"")
                status_id = node_info.get('id',"")
                statuses.append((status_name,status_id))
            return statuses


class ContractTypes:

    def get_contract_types(self):

        module = Module.CONTRACT
        query_name =  GraphqlContracts.CONTRACT_TYPES
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)

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
    def get_easement_types(self):


        module = Module.EASEMENT

        query_name = GraphqlEasements.EASMENT_TYPES
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)  


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
