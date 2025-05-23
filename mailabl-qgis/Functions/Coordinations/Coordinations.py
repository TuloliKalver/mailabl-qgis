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
from ...Functions.AsBuilt.TableStyle import TableStyle  # adjust path if needed


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
            
            table_rows = CoordinationsQueries.extract_all_coordination_details(response.json())
            return table_rows
        else:
            #print(f"Error: {response.status_code}")
            return None
       

    @staticmethod
    def extract_all_coordination_details(node: dict) -> str:

        label_color = "#BBB"
        value_color = "#EEE"

        label_width = "25%"
        value_width = "30%"

        c = node.get("data", {}).get("coordination", {})

        def safe(key: str) -> str:
            return c.get(key) or ""

        # Handle due date formatting and day difference
        raw_due = c.get("dueAt")
        if raw_due:
            try:
                due_dt = datetime.strptime(raw_due, "%Y-%m-%d")
                today = datetime.today()
                days_remaining = (due_dt - today).days
                dueAt_display = f"{due_dt.strftime('%d.%m.%Y')} \n({days_remaining} päeva)"
            except Exception:
                dueAt_display = ""
        else:
            dueAt_display = ""
            
        tags = c.get("tags", {})
        tunnused = [edge["node"]["name"] for edge in tags.get("edges", [])]
        tunnused_str = ", ".join(tunnused) if tunnused else ""


        table_rows = f"""
        <tr>
            <!-- [1][1][1][3] = 6 -->
            <td width="{label_width}"><font color="{label_color}"><b>📁 Töö nr:</b></font></td>
            <td width="{value_width}"><font color="{value_color}"><b>{safe("jobNumber")}</b></font></td>
            <td width="{label_width}"><font color="{label_color}"><b>🔤 Töö nimetus:</b></font></td>
            <td colspan="3"><font color="{value_color}"><b>{safe("jobName")}</b></font></td>
        </tr>
        <tr>
            <!-- [1][1][1][1][1][1] = 6 -->
            <td width="{label_width}"><font color="{label_color}"><b>🏷️ EHR kood:</b></font></td>
            <td width="{value_width}"><font color="{value_color}"><b>{safe("externalCode")}</b></font></td>
            <td width="{label_width}"><font color="{label_color}"><b>⚙️ Etapp:</b></font></td>
            <td width="{value_width}"><font color="{value_color}"><b>{safe("stage")}</b></font></td>
            <td width="{label_width}"></td>
            <td width="{value_width}"></td>
        </tr>
        <tr>
            <!-- [1][1][1][1][1][1] = 6 -->
            <td width="{label_width}"><font color="{label_color}"><b>📩 Saabunud:</b></font></td>
            <td width="{value_width}"><font color="{value_color}"><b>{safe("receivedAt")}</b></font></td>
            <td width="{label_width}"><font color="{label_color}"><b>🟢 Alustatud:</b></font></td>
            <td width="{value_width}"><font color="{value_color}"><b>{safe("startAt")}</b></font></td>
        </tr>
        <tr>

            <td width="{label_width}"><font color="{label_color}"><b>📆 Tähtaeg:</b></font></td>
            <td width="{value_width}"><font color="{value_color}"><b>{dueAt_display}</b></font></td>
        </tr>
        <tr>
            <!-- [2][4] = 6 -->
            <td width="{label_width}" colspan="2"><font color="{label_color}"><b>✅ Kooskõlastatud:</b></font></td>
            <td width="80%" colspan="4"><font color="{value_color}"><b>{safe("agreedAt")}</b></font></td>
        </tr>
        <tr>
            <!-- [1][5] = 6 -->
            <td width="{label_width}"><font color="{label_color}"><b>🏷️ Tunnused:</b></font></td>
            <td width="80%" colspan="5"><font color="{value_color}"><b>{tunnused_str}</b></font></td>
        </tr>
        """
        return table_rows
