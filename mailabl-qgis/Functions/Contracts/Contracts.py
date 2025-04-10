# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

import pandas as pd
from typing import List
from PyQt5.QtCore import QCoreApplication

from ...queries.python.FileLoaderHelper import GraphqlContracts, GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ...KeelelisedMuutujad.modules import Module
from ...utils.DataExtractors.DataModelHelpers import DataModelBuilder
from ...utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
from ...utils.ProgressHelper import ProgressDialogModern    

class Constants:
    package_size = 25
    sleep_duration = 2 #time for sleep
    total_fetched = 0
    items_for_page_minimum = 1
    items_for_page_medium = 25
    items_for_page_large = 50
    sleepPackage = items_for_page_medium
    



class ContractsMain:
    @staticmethod
    def load_main_contracts_by_type_and_status (self, table, types, statuses, language="et"):
        #Adding progress
        module = Module.CONTRACT
        progress = ProgressDialogModern(title=f"{module} laadimine", value=0)
        progress.update(1, purpouse="Lepingute laadimine", text1="Palun oota...")
        model = ContractModels._model_for_contracts_by_types_and_statuses(self, types, statuses, language=language)

        if model is not None:
            progress.update(50)
            ModuleTableBuilder.setup(table, model, module, language)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
        progress.update(98)
        progress.close()
        
    @staticmethod
    def load_contracts_by_query (query, table, language="et"):
        module = Module.CONTRACT
        progress = ProgressDialogModern(title=f"{module} laadimine", value=0)
        progress.update(1, purpouse="Lepingute laadimine", text1="Palun oota...")

        model = ContractModels._model_for_contract_search_results(query, language)

        if model is not None:
            progress.update(50)
            ModuleTableBuilder.setup(table, model, module, language)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
        progress.update(98)
        progress.close()

class ContractModels: 
    @staticmethod
    def _model_for_contracts_by_types_and_statuses(self, types, statuses, language):

        data = ContractsQueries._query_contracts_by_type_status_elements(self, types, statuses)
        model = DataModelBuilder.build_model_from_records(data, language)
        return model

    @staticmethod
    def _model_for_contract_search_results(contract_number, language):
        # Set header labels
       
        data = ContractsQueries._query_contracts_by_number(contract_number)
        model = DataModelBuilder.build_model_from_records(data, language)
        return model


class ContractsQueries:

    @staticmethod
    def _query_contracts_by_number(contract_number):
        #print(statuses)
        # Load the project query using the loader instance
        module = Module.CONTRACT
        query_name =  GraphqlContracts.ALL_CONTRACTS
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        #items_for_properties_page = 50
        end_cursor = None  # Initialize end_cursor before the loop
        total_fetched = 0        # Initialize an empty list to store fetched items
        fetched_items = []

        
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None,
                "where": {
                    "AND": [
                        {"column": "NUMBER", "operator": "IN", "value": [contract_number]}
                    ]
                }
            }
            
            response = requestBuilder.construct_and_send_request(None, query, variables) #/TODO None can be replaced with self if needed

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get("contracts", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("contracts", {}).get("pageInfo", {})
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
    @staticmethod
    def _query_contracts_by_type_status_elements(self, type_values, statuses):

        #print(statuses)
        # Load the project query using the loader instance

        module = Module.CONTRACT
        query_name =  GraphqlContracts.WHERE_CONTRACTS_TYPE_STATUS
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)

     
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        #items_for_properties_page = 50
        end_cursor = None  # Initialize end_cursor before the loop
        end_cursor = None
        total_fetched = 0        # Initialize an empty list to store fetched items
        
        # Splitting the list into sublists with a maximum of 4 items each
        #sublists = [selected_features[i:i+Constants.items_for_page_medium] for i in range(0, len(selected_features), Constants.items_for_page_medium)]
                
        fetched_items = []

        count = 0
            
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None,
                "where": {
                    "AND": [
                        {
                        "column": "TYPE",
                        "operator": "IN",
                        "value": type_values
                        #"value": ["1", "2", "3"]
                        },
                        {
                        "column": "STATUS",
                        "operator": "IN",
                        "value": statuses
                        #"value": ["62"]
                        }
                    ]
                    },
                    "orderBy": [
                    {
                        "column": "NUMBER",
                        "order": "ASC"
                    }
                    ],
                    "trashed": "WITHOUT"
                }



            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get("contracts", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("contracts", {}).get("pageInfo", {})
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

