import pandas as pd
from typing import List
from PyQt5.QtCore import QCoreApplication
from datetime import datetime


from ...queries.python.FileLoaderHelper import GraphqlStatuses, GraphqlCoordinations, GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ...KeelelisedMuutujad.modules import Module
from ...utils.DataExtractors.DataModelHelpers import DataModelBuilder
#from ...utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
from ...utils.ProgressHelper import ProgressDialogModern    

class Constants:
    package_size = 25
    sleep_duration = 2 #time for sleep
    total_fetched = 0
    items_for_page_minimum = 1
    items_for_page_medium = 25
    items_for_page_large = 50
    sleepPackage = items_for_page_medium
    



class CoordinationsMain:
    @staticmethod
    def load_main_Coordinations_by_type_and_status (self, table, types, statuses, language="et"):
        #Adding progress
        from ...utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
        module = Module.COORDINATION
        module_text = "Kooskõlastuste"
        progress = ProgressDialogModern(title=f"Andmete laadimine", value=0)
        progress.update(1, purpouse="{module_text} laadimine", text1="Palun oota...")
        model = CoordinationsModels._model_for_Coordinations_by_types_and_statuses(self, types, statuses, language=language)

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
    def load_coordinations_details(id):

        module = Module.COORDINATION
        module_text = "Kooskõlastuste"
        data = CoordinationsQueries._query_Coordinations_notes(id)

        return data

class CoordinationsModels: 
    @staticmethod
    def _model_for_Coordinations_by_types_and_statuses(self, types, statuses, language):

        data = CoordinationsQueries._query_Coordinations_by_type_status_elements(types, statuses)
        model = DataModelBuilder.build_model_from_records(data, language, module = Module.COORDINATION)
        return model

    @staticmethod
    def _model_for_Coordinations_search_results(name, language):
        # Set header labels
       
        data = CoordinationsQueries._query_Coordinations_by_name(name)
        model = DataModelBuilder.build_model_from_records(data, language, module = Module.COORDINATION)
        
        return model

class CoordinationsQueries:

    @staticmethod
    def _query_Coordinations_by_name(name):
        module = Module.ASBUILT
        query_name =  GraphqlTasks.AsBUILT
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        end_cursor = None        
        total_fetched = 0        
        fetched_items = []

        
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None,
                "where": {
                    "AND": [
                        {"column": "TITLE", "operator": "LIKE", "value": [f"{name}%"]}
                    ]
                }
            }
            
            response = requestBuilder.construct_and_send_request(query, variables) #/TODO None can be replaced with self if needed

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get(f"{module}s", {}).get("edges", [])
                pageInfo = data.get("data", {}).get(f"{module}s", {}).get("pageInfo", {})
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
    def _query_Coordinations_by_type_status_elements(type_values, statuses):

        #print(statuses)
        # Load the project query using the loader instance

        module = Module.COORDINATION
        query_name =  GraphqlCoordinations.COORDINATIONS
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
                        },
                        {
                        "column": "STATUS",
                        "operator": "IN",
                        "value": statuses
                        }
                    ]
                    },
                    "orderBy": [
                    {
                        "column": "STATUS",
                        "order": "ASC"
                    }
                    ],
                    "trashed": "WITHOUT"
                }



            response = requestBuilder.construct_and_send_request(query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get(f"{module}s", {}).get("edges", [])
                pageInfo = data.get("data", {}).get(f"{module}s", {}).get("pageInfo", {})
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

    def _query_Coordinations_notes(id):
        module = Module.COORDINATION
        query_name =  GraphqlCoordinations.RELATED_NOTES
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        variables = {
            "id": id
        }
        response = requestBuilder.construct_and_send_request(query, variables)

        if response.status_code == 200:
            
            table_rows, desc_and_terms = CoordinationsQueries.extract_all_coordination_details(response.json())
            return table_rows, desc_and_terms
        else:
            #print(f"Error: {response.status_code}")
            return None
       


    def extract_all_coordination_details(node: dict) -> tuple[str, str]:
        fallback = "—"
        fallback_date = "01.01.2022"
        default_poem = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 🌿\n"
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. ✨"
        )

        c = node.get("data", {}).get("coordination", {})

        # Handle due date formatting and day difference
        raw_due = c.get("dueAt")
        if raw_due:
            try:
                due_dt = datetime.strptime(raw_due, "%Y-%m-%d")
                today = datetime.today()
                days_remaining = (due_dt - today).days
                dueAt = due_dt.strftime("%d.%m.%Y")
            except Exception:
                dueAt = fallback_date
                days_remaining = "?"
        else:
            dueAt = fallback_date
            days_remaining = "?"

        table_rows = f"""
        <table style="margin-top: 10px; border-collapse: collapse; width: 100%;">
            <tr><td><b>📁 Töö nr:</b></td><td>{c.get("jobNumber", "2390")}</td></tr>
            <tr><td><b>🔤 Töö nimetus:</b></td><td>{c.get("jobName", "Asd")}</td></tr>
            <tr><td><b>🏷️ Väline kood:</b></td><td>{c.get("externalCode", "902902")}</td></tr>
            <tr><td><b>📅 Algus:</b></td><td>{c.get("startAt", fallback_date)}</td></tr>
            <tr><td><b>📩 Vastuvõtt:</b></td><td>{c.get("receivedAt", fallback_date)}</td></tr>
            <tr><td><b>✅ Kooskõlastatud:</b></td><td>{c.get("agreedAt", fallback_date)}</td></tr>
            <tr style="background-color: rgba(255,255,255,0.06); font-weight: bold;">
                <td>📆 Tähtaeg:</td><td>{dueAt} ({days_remaining} päeva)</td>
            </tr>
            <tr><td><b>⚙️ Etapp:</b></td><td>{c.get("stage", "Kavandamisel")}</td></tr>
            <tr><td><b>🏷️ Märgised:</b></td><td>{c.get("tags", {}).get("pageInfo", {}).get("total", 2)} tk</td></tr>
        </table>
        """

        desc_and_terms = f"""
        <div style="margin-top: 8px;">
            <b>📝 Märkused:</b><br/>
            <div style="white-space: pre-wrap; word-break: break-word; color: #f5f5f5;">
                {c.get("description") or default_poem}
            </div>
        </div>
        <div style="margin-top: 6px;">
            <b>📚 Eri tingimused:</b><br/>
            <div style="white-space: pre-wrap; word-break: break-word; color: #f5f5f5;">
                {c.get("terms") or default_poem}
            </div>
        </div>
        """

        return table_rows, desc_and_terms
