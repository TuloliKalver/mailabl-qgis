# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-nam



import pandas as pd
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox
from .DataLoading_classes import Graphql_project, GraphQLQueryLoader
from .query_tools import requestBuilder
from ...config.ui_directories import PathLoaderSimple
from .MapTools.selector import visibleSelector
from ...processes.infomessages.messages import Headings
 
pealkiri = Headings()

HEADER_ID = 'ID'
HEADER_NUMBER = 'Number'
HEADER_NAME = 'Nimetus'
HEADER_DEADLINE = 'Tähtaeg'
HEADER_COLOR = 'Color'
HEADER_RESPONSIBLE = 'Vastutaja'
HEADER_PROPERTY_NUMBER = 'Kataster'
HEADER_PROPERTIES_ICON ='propertiesIcon'
HEADER_PROJECTS_PARENT_ID = 'Parent_id'
HEADER_WEB_LINK_BUTTON = 'web_link_button'
HEADER_DOCUMENTS = 'Dokumendid'
HEADER_FILE_PATH = "file_path_button"
HEADER_STATUS = 'Staatus'

class TableHeaders:
    def __init__(self):
        self.header_id = HEADER_ID
        self.header_number = HEADER_NUMBER
        self.header_name = HEADER_NAME
        self.header_deadline =HEADER_DEADLINE
        self.header_color = HEADER_COLOR
        self.header_responsible = HEADER_RESPONSIBLE
        self.header_property_number = HEADER_PROPERTY_NUMBER
        self.header_properties_icon = HEADER_PROPERTIES_ICON
        self.header_parent_id = HEADER_PROJECTS_PARENT_ID
        self.header_web_link_button = HEADER_WEB_LINK_BUTTON
        self.header_documents = HEADER_DOCUMENTS
        self.header_file_path = HEADER_FILE_PATH
        self.header_statuses = HEADER_STATUS
        
class Constants:
    package_size = 25
    sleep_duration = 2 #time for sleep
    total_fetched = 0
    items_for_page_minimum = 1
    items_for_page_medium = 25
    items_for_page_large = 50
    sleepPackage = items_for_page_medium
    
    desired_total_items = None
    
class GetProjectsWhere:
    def query_projects_related_properties(self, id_value):
        #print(f"id value in query {id_value}")
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query_for_projects(self,query_loader.Q_where_Projects_related_properties)
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        #Initialize variables for pagination
        end_cursor = None  # Initialize end_cursor before the loop
        total_fetched = 0        
        properties_items = [] # Initialize an empty list to store fetched items
        
        while (desired_total_items is None or total_fetched < desired_total_items):
            # Construct variables for the GraphQL query
            variables = {
                    "propertiesFirst": Constants.items_for_page_large,
                    "propertiesAfter": end_cursor if end_cursor else None,
                    "id": id_value
                    }
            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                project_data = data.get("data", {}).get("project", {})
                properties_data = project_data.get("properties", {})
                edges = properties_data.get("edges", [])
                #print("edges")
                #print(edges)
                pageInfo = properties_data.get("pageInfo", {})
                #print(f"pageInfo: {pageInfo}")
                end_cursor = pageInfo.get("endCursor")
                hasNextPage = pageInfo.get("hasNextPage")
                count = pageInfo.get('count')
                #print(f"count {count}")
                for edge in edges:
                    node = edge.get("node", {})
                    cadastral_unit_number = node.get("cadastralUnitNumber", "")
                    #print(cadastral_unit_number)
                    properties_items.append(cadastral_unit_number)
                #print(f"{properties_items}")
                #print(count)
                total_fetched += count
                #print(total_fetched)
                # Check whether the last page of projects has been reached
                if not end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not hasNextPage:
                    break
                QCoreApplication.processEvents()
            else:
                print(f"Error: {response.status_code}")
                return None
        # Return only the desired number of items
        return properties_items

class ProjectsWithPandas:    
    def query_active_main_projects_by_status(self, statuses):
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        label_2 = progress_widget.label_2
        progress_bar.setMaximum(100)
        progress_widget.setWindowTitle("Laen projekte")
        progress_widget.show()
        
        # Load the project query using the loader instance
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query(self,query_loader.Q_Where_By_status_Projects)
        desired_total_items = None  # Adjust this to your desired value
        projects_end_cursor = None  # Initialize end_cursor before the loop
        total_fetched = 0
        fetched_items = []
        
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": Constants.items_for_page_large,
                "after": projects_end_cursor if projects_end_cursor else None,
                "where": {
                    "AND": [
                        {"column": "STATUS", "operator": "IN", "value": statuses},
                        {"column": "PARENT_ID", "value": None},
                        {"column": "IS_PUBLIC", "value": True}
                    ]
                }
            }
            
            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                return None
            
            data = response.json()
            fetched_data = data.get("data", {}).get("projects", {}).get("edges", [])
            projects_pageInfo = data.get("data", {}).get("projects", {}).get("pageInfo", {})
            
            projects_end_cursor = projects_pageInfo.get("endCursor")
            projects_hasNextPage = projects_pageInfo.get("hasNextPage")
            last_page = projects_pageInfo.get("lastPage")
            current_page = projects_pageInfo.get("currentPage")
            total = projects_pageInfo.get("total")
            
            fetched_items.extend(fetched_data)
            total_fetched += len(fetched_data)
            
            text = "Projekte kokku"
            if current_page == 1:
                label_2.setText(f"{text}: {total}")
                progress_bar.setMaximum(last_page)
                
            label_2.setText(f"{text}: {total}")
            progress_bar.setValue(current_page)
            QCoreApplication.processEvents()

            if not projects_end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not projects_hasNextPage:
                break

        return fetched_items[:desired_total_items]

    def QueryProjects_by_number(self, project_number):
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        label_2 = progress_widget.label_2
        progress_bar.setMaximum(100)
        progress_widget.setWindowTitle("Laen projekte")
        progress_widget.show()
        
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query(self, query_loader.Q_Where_By_status_Projects)
        
        desired_total_items = None
        projects_end_cursor = None
        total_fetched = 0
        fetched_items = []
                    
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": Constants.items_for_page_large,
                "after": projects_end_cursor if projects_end_cursor else None,
                "where": {
                    "AND": [
                        {"column": "NUMBER", "operator": "IN", "value": [project_number]}
                    ]
                }
            }
            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                fetched_data = data.get("data", {}).get("projects", {}).get("edges", [])
                projects_page_info = data.get("data", {}).get("projects", {}).get("pageInfo", {})
                
                projects_end_cursor = projects_page_info.get("endCursor")
                projects_has_next_page = projects_page_info.get("hasNextPage")
                total_fetched += len(fetched_data)
                fetched_items.extend(fetched_data)
                total = projects_page_info.get("total")
                current_page = projects_page_info.get("currentPage")
                last_page = projects_page_info.get("lastPage")
                label_2.setText(f"Projekte kokku: {total}")
                progress_bar.setMaximum(last_page)
                progress_bar.setValue(current_page)
                QCoreApplication.processEvents()

                if not projects_end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not projects_has_next_page:
                    break
            else:
                print(f"Error: {response.status_code}")
                return None
            QCoreApplication.processEvents()
        
        return fetched_items[:desired_total_items]            

class ProjectsWithPandas_2:

    def table_view_from_active_projects_statuses(self, status_value):
        # Set header labels
        header_labels = [HEADER_ID, HEADER_NUMBER,
                            HEADER_NAME, HEADER_DEADLINE,
                            HEADER_COLOR, HEADER_RESPONSIBLE,
                            HEADER_PROPERTY_NUMBER, HEADER_PROPERTIES_ICON,
                            HEADER_PROJECTS_PARENT_ID, HEADER_WEB_LINK_BUTTON,
                            HEADER_DOCUMENTS, HEADER_FILE_PATH,
                            HEADER_STATUS]
        #print(f" header_webLinkButton: {header_webLinkButton}")
        #print(f"header_labels: {header_labels}")
        # Get projects status types that are active
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        #print("statuses")
        #print(statuses)
        data = ProjectsWithPandas.query_active_main_projects_by_status(self, status_value)
        
        # Build a pandas DataFrame
        df_data = []
        for project_data in data:
            node = project_data.get("node", {})
            properties = node.get("properties", {}).get("edges", [])
            properties_page_info = node.get("properties",{}).get('pageInfo',{})          
            propertie_cadastralNr = [propertie["node"]["cadastralUnitNumber"] for propertie in properties]
            responsibles = node.get("responsible",{}).get("edges",[])
            resposnisble_name = [responsible["node"]["displayName"] for responsible in responsibles]
            row_data = {
                HEADER_ID: node.get("id", "") or "",
                HEADER_NUMBER: node.get("number", "") or "",
                HEADER_NAME: node.get("name", "") or "",
                HEADER_DEADLINE: node.get("dueAt", "") or "",
                HEADER_STATUS: node.get("status", {}).get("name", "") if node.get("status") else "",
                HEADER_COLOR: node.get("status", {}).get("color", "") if node.get("status") else "",
                HEADER_PROPERTY_NUMBER: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                HEADER_ID: node.get("id", ""),
                HEADER_PROJECTS_PARENT_ID: node.get("parentID", ""),
                HEADER_WEB_LINK_BUTTON: "",
                HEADER_DOCUMENTS: node.get("filesPath","")or "",
                HEADER_FILE_PATH: "",
                HEADER_RESPONSIBLE: ",".join(resposnisble_name) if resposnisble_name else "",
                HEADER_PROPERTIES_ICON: ""
                }
            df_data.append(row_data)
        
        QCoreApplication.processEvents()
        df = pd.DataFrame(df_data)
        # Create a QStandardItemModel and set header labels

        # Populate QStandardItemModel with data from the pandas DataFrame
        for row_index, row_data in df.iterrows():
            data_items = [QStandardItem(str(row_data[label])) for label in header_labels]
            model.appendRow(data_items)
        
        return model, header_labels


    def Create_Project_tableView_for_search(self, project_number):
        # Set header labels
        header_labels = [HEADER_ID, HEADER_NUMBER, 
                            HEADER_NAME, HEADER_DEADLINE,
                            HEADER_COLOR, HEADER_RESPONSIBLE,
                            HEADER_PROPERTY_NUMBER, HEADER_PROPERTIES_ICON,
                            HEADER_PROJECTS_PARENT_ID, HEADER_WEB_LINK_BUTTON, 
                            HEADER_DOCUMENTS, HEADER_FILE_PATH, 
                            HEADER_STATUS]
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)        
        #unique_projects = set()
        all_projects = []
        all_projects = ProjectsWithPandas.QueryProjects_by_number(self, project_number)
        # Append all project dictionaries to the list
        QCoreApplication.processEvents()
        total_projects = len(all_projects)
        if  total_projects == 0:
            text = "Antud numbriga projekti ei leitud"
            heading = pealkiri.informationSimple
            QMessageBox.information(None, heading, text)
            return None

        else:
            # Convert the list of dictionaries to a set to remove duplicates based on the 'id'
            print(f"total len of all projects: '{len(all_projects)}'")

            # Build a pandas DataFrame
            df_data = []
            for item in all_projects:
                node = item.get("node", {})
                properties = node.get("properties", {}).get("edges", [])
                propertie_cadastralNr = [propertie["node"]["cadastralUnitNumber"] for propertie in properties]
                responsibles = node.get("responsible",{}).get("edges",[])
                resposnisble_name = [responsible["node"]["displayName"] for responsible in responsibles]
                row_data = {
                    HEADER_ID: node.get("id", "") or "",
                    HEADER_NUMBER: node.get("number", "") or "",
                    HEADER_NAME: node.get("name", "") or "",
                    HEADER_DEADLINE: node.get("dueAt", "") or "",
                    HEADER_STATUS: node.get("status", {}).get("name", "") if node.get("status") else "",
                    HEADER_COLOR: node.get("status", {}).get("color", "") if node.get("status") else "",
                    HEADER_PROPERTY_NUMBER: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                    HEADER_ID: node.get("id", ""),
                    HEADER_PROJECTS_PARENT_ID: node.get("parentID", ""),
                    HEADER_WEB_LINK_BUTTON: "",
                    HEADER_DOCUMENTS: node.get("filesPath","")or "",
                    HEADER_FILE_PATH: "",
                    HEADER_RESPONSIBLE: ",".join(resposnisble_name) if resposnisble_name else "",
                    HEADER_PROPERTIES_ICON: ""
                    }
                df_data.append(row_data)
            
                QCoreApplication.processEvents()
                df = pd.DataFrame(df_data)
            # Create a QStandardItemModel and set header labels

            # Populate QStandardItemModel with data from the pandas DataFrame
            for row_index, row_data in df.iterrows():
                data_items = [QStandardItem(str(row_data[label])) for label in header_labels]
                model.appendRow(data_items)
            
            return model, header_labels


class ProjectsWithPandas_3:

    #@staticmethod
    def Create_Project_tableView_for_zoom(self, selected_features):
        # Set header labels
        header_labels = [HEADER_ID, HEADER_NUMBER,
                            HEADER_NAME, HEADER_DEADLINE,
                            HEADER_COLOR, HEADER_RESPONSIBLE,
                            HEADER_PROPERTY_NUMBER, HEADER_PROPERTIES_ICON,
                            HEADER_PROJECTS_PARENT_ID, HEADER_WEB_LINK_BUTTON,
                            HEADER_DOCUMENTS, HEADER_FILE_PATH,
                            HEADER_STATUS]
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        print(f"selected features: '{selected_features}' total:'{len(selected_features)}'")
        
        # Splitting the list into sublists with a maximum of 4 items each
        sublists = [selected_features[i:i+Constants.items_for_page_medium] for i in range(0, len(selected_features), Constants.items_for_page_medium)]
        
        #unique_projects = set()
        all_projects = []

        count = 0
        
        for feature in sublists:
            #print(f"feature: '{feature}'")
            projects_data = visibleSelector.get_projects_list_connected_with_view_properties(self, feature)
            #print(f"project_data: {projects_data}")
        
            all_projects.extend(projects_data)  # Append all project dictionaries to the list
            count += Constants.items_for_page_medium
            print(f"count: {count}")
            # Sleep to avoid hitting server too frequently
            if count % Constants.sleepPackage == 0:
                import time
                time.sleep(Constants.sleep_duration)
                print("sleepy sleepy")
            QCoreApplication.processEvents()
        total_projects = len(all_projects)
        if  total_projects == 0:
            text = "Piirkonnas puuduvad teadaolevad projektid"
            heading = pealkiri.informationSimple
            QMessageBox.information(None, heading, text)
            return None

        else:
            # Convert the list of dictionaries to a set to remove duplicates based on the 'id'
            data = {project['id']: project for project in all_projects}.values()
            #print(f"total len of all projects: '{len(all_projects)}'")
            print(f"data: {data}")

            # Build a pandas DataFrame
            df_data = []
            for node in data:
                #node = data.get("node", {})
                properties = node.get("properties", {}).get("edges", [])
                propertie_cadastralNr = [propertie["node"]["cadastralUnitNumber"] for propertie in properties]
                responsibles = node.get("responsible",{}).get("edges",[])
                resposnisble_name = [responsible["node"]["displayName"] for responsible in responsibles]
                row_data = {
                    HEADER_ID: node.get("id", "") or "",
                    HEADER_NUMBER: node.get("number", "") or "",
                    HEADER_NAME: node.get("name", "") or "",
                    HEADER_DEADLINE: node.get("dueAt", "") or "",
                    HEADER_STATUS: node.get("status", {}).get("name", "") if node.get("status") else "",
                    HEADER_COLOR: node.get("status", {}).get("color", "") if node.get("status") else "",
                    HEADER_PROPERTY_NUMBER: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                    HEADER_ID: node.get("id", ""),
                    HEADER_PROJECTS_PARENT_ID: node.get("parentID", ""),
                    HEADER_WEB_LINK_BUTTON: "",
                    HEADER_DOCUMENTS: node.get("filesPath","")or "",
                    HEADER_FILE_PATH: "",
                    HEADER_RESPONSIBLE: ",".join(resposnisble_name) if resposnisble_name else "",
                    HEADER_PROPERTIES_ICON: ""
                    }    
                df_data.append(row_data)
            
                QCoreApplication.processEvents()
                df = pd.DataFrame(df_data)
            # Create a QStandardItemModel and set header labels

            # Populate QStandardItemModel with data from the pandas DataFrame
            for row_index, row_data in df.iterrows():
                data_items = [QStandardItem(str(row_data[label])) for label in header_labels]
                model.appendRow(data_items)
            
            return model, header_labels
