# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module


from typing import Tuple, Dict
from PyQt5.QtCore import QCoreApplication

from ...queries.python.FileLoaderHelper import GraphqlStatuses, GraphqlTasks, GraphQLQueryLoader, GraphqlStatuses
from ...queries.python.query_tools import requestBuilder
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ...KeelelisedMuutujad.modules import Module, ModuleTranslation
from ...utils.DataExtractors.DataModelHelpers import DataModelBuilder
#from ...utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
from ...utils.ProgressHelper import ProgressDialogModern    
from ...widgets.decisionUIs.DecisionMaker import DecisionDialogHelper
from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...utils.TableUtilys.htmlConverter import HtmlConverter
from ...utils.TableUtilys.FlagIconHelper import FlagIconHelper


class Constants:
    package_size = 25
    sleep_duration = 2 #time for sleep
    total_fetched = 0
    items_for_page_minimum = 1
    items_for_page_medium = 25
    items_for_page_large = 50
    sleepPackage = items_for_page_medium
    



class TaskMain:
    @staticmethod
    def load_task_open_stauses(statuses,types, language="et", module=None):
        
        fetched_data = TaskQueries._query_tasks_open_status(statuses,types, module)
       
        return fetched_data

    @staticmethod
    def load_main_task_by_type_and_status (self, table, types, statuses, language="et", module=None):
        #Adding progress
        from ...utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
        if module is None:
            module = Module.ASBUILT
        elif module == Module.WORKS:
            module = Module.WORKS
        #module_text = ModuleTranslation.module_name(module, language, plural=False)
        module_text = "Teostusjooniste"
        progress = ProgressDialogModern(title=f"{module_text} laadimine", value=0)
        progress.update(1, purpouse="Teostuste laadimine", text1="Palun oota...")
        model, id_status_tuples = TaskModels._model_for_task_by_types_and_statuses(types, statuses, language=language, module=module)

        if model is not None:
            progress.update(50)
            ModuleTableBuilder.setup(table, model, module, language)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
        progress.update(98)

        progress.close()

        return id_status_tuples
        
    @staticmethod
    def load_task_by_query (query, table, language="et", module=None):
        from ...utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
        #print(f"module: {module}")
        if module is None:
            module = Module.ASBUILT
        elif module == Module.WORKS:
            module = Module.WORKS
        progress = ProgressDialogModern(title=f"{module} laadimine", value=0)
        progress.update(1, purpouse="Lepingute laadimine", text1="Palun oota...")

        model = TaskModels._model_for_task_search_results(query, language, module=module)

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
    def load_task_details(id):
        #print(f"id in loading task by id: {id}")
        module = Module.TASK

        table_rows = TaskQueries._query_task_details(id, module)

        return table_rows

    def load_task_data(id):
        module = Module.TASK
        data = TaskQueries._query_task_data(id, module)
        
        return data

class TaskModels: 
    @staticmethod
    def _model_for_task_by_types_and_statuses(types, statuses, language, module):

        data = TaskQueries._query_task_by_type_status_elements(types, statuses)
        #print(f"Task data: {data}")
        
        id_status_tuples = []

        for item in data:
            node = item.get("node", {})
            task_id = node.get("id")
            status_type = node.get("status", {}).get("type")

            if task_id and status_type:
                id_status_tuples.append((task_id, status_type))


        model = DataModelBuilder.build_model_from_records(data, language, module = module)
        return model, id_status_tuples

    @staticmethod
    def _model_for_task_search_results(name, language, module):
        # Set header labels
       
        data = TaskQueries._query_task_by_name(name)
        model = DataModelBuilder.build_model_from_records(data, language, module = module)
        
        return model

class TaskQueries:

    @staticmethod
    def _query_task_by_name(name):
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
    def _query_task_by_type_status_elements( type_values, statuses):
        #print(f"type_values: {type_values}")
        #print(f"statuses: {statuses}")
        # Load the project query using the loader instance

        module = Module.TASK
        query_name =  GraphqlTasks.AsBUILT
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


    @staticmethod
    def _query_AsBuilt_by_id( property_id):

        module = Module.TASK
        query_name =  GraphqlTasks.TaskById
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
            
        variables = {"id": property_id, 
                    }


        response = requestBuilder.construct_and_send_request(query, variables)

        if response.status_code == 200:
            data = response.json()
            #print("data")
            #print(data)
            task = data.get("data", {}).get("task", {})
            description = task.get("description", "")

            QCoreApplication.processEvents()
            return description
            
    def  _update_AsBuilt_by_id(property_id, description):
        
        module = Module.TASK
        query_name =  GraphqlTasks.updatedescription
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)

        variables = {
                "input": {
                    "id": property_id,
                    "description": description
                }
                }
        
        response = requestBuilder.construct_and_send_request(query, variables)
        
        if response.status_code == 200:
            return True
        else:
            print("Response is")
            print(response.status_code)
            buttons={"keep": "Selge"}
            ret = DecisionDialogHelper.ask_user(
                title=Headings.inFO_SIMPLE,
                message=f"Saadud serveri vastus kood\n{response.status_code}",
                options=buttons,
                parent=None,
                type= AnimatedGradientBorderFrame.PROLOOK
                    )

            return False
        
    def _query_task_details(id, module):
        
        query_name =  GraphqlTasks.TASK_DETAILS
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        variables = {
            "id": id
        }
        response = requestBuilder.construct_and_send_request(query, variables)

        if response.status_code == 200:
            table_rows = TaskQueries._extract_all_asBuilt_details(response.json())
            return table_rows
        
    def _query_task_data(id, module):
        
        query_name =  GraphqlTasks.TASK_DETAILS
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        variables = {
            "id": id
        }
        response = requestBuilder.construct_and_send_request(query, variables)

        if response.status_code == 200:
            return response.json()
    @staticmethod
    def _query_tasks_open_status(statuses, type_values, module):
        #print(f"types: {type_values}")
        #print(f"statuses: {statuses}")
        #print(f"module: {module}")
        #print("querying open status works tasks")
        query_name =  GraphqlTasks.TASK_DETAILS_2
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
                QCoreApplication.processEvents()
    


            else:
                #print(f"Error: {response.status_code}")
                return None
        # Return only the desired number of items
        return fetched_items[:desired_total_items]


    def _extract_all_asBuilt_details(node: Dict) -> Tuple[str, str]:
        """
        Extracts HTML fragments for ASBUILT details from a Task node, styled to match the original hover design.

        Returns:
            table_rows: HTML string containing a centered, styled table of key fields.
            desc_and_terms: HTML string wrapping the raw description/details.
        """
        c = node.get("data", {}).get("task", {})

        print(f"Task values: {c}")

        label_color = "#BBB"
        value_color = "#EEE"

        label_width = "25%"
        value_width = "30%"


        # Build the general data table (Üldandmed) with original inline styles
        table_rows = f"""
            <tr>
                <td width="{label_width}"><font color="{label_color}"><b>📝 Pealkiri: </b></font></td>
                <td width="{value_width}"><font color="{value_color}"><b>{c.get("title", "")}</b></font></td>
            </tr>
        
            <tr>
                <td width="{label_width}"><font color="{label_color}"><b>🏷️ Liik:</b></font></td>
                <td width="{value_width}"><font color="{value_color}"><b>{c.get("type", {}).get("name", "")}</b></font></td>

            </tr>
            <tr>
                <td width="{label_width}"><font color="{label_color}"><b>📅 Alguskuupäev:</b></font></td>
                <td width="{value_width}"><font color="{value_color}"><b>{c.get("startAt", )}</b></font></td>
                <td width="{label_width}"><font color="{label_color}"><b>⏰ Tähtaeg:</b></font></td>
                <td width="{value_width}"><font color="{value_color}"><b>{c.get("dueAt", )}</b></font></td>
            </tr>

            <tr>
                <td width="{label_width}"><font color="{label_color}"><b>✅ Lõpetatud:</b></font></td>
                <td width="{value_width}"><font color="{value_color}"><b>{c.get("completedAt", )}</b></font></td>
            </tr>
        """
        #print (desc_and_terms)
        return table_rows
