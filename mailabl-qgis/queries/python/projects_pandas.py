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
from ...KeelelisedMuutujad.messages import Headings
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...utils.DataExtractors.DataExtractors import DataExtractor
from ...utils.ProgressHelper import ProgressHelper

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
    
class ProjectsQueries:
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
            print(f"id_value in query {id_value}")
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

    @staticmethod
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

    @staticmethod    
    def query_projects_by_number(self, project_number):
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

class ProjectModelBuilders:
    @staticmethod
    def _model_for_projects_by_statuses(self, status_value, language):
        
        data = ProjectsQueries.query_active_main_projects_by_status(self, status_value)
        
        headers = HeaderKeys.ALL_HEADER_KEYS
        display_headers = TableHeaders_new(language)
        df_data = []
        for item in data:
            node = item.get("node", {})
            df_data.append(DataExtractor.extract_row_data_from_node(node, language=language))

        QCoreApplication.processEvents()
        df = pd.DataFrame(df_data)

        # Create model and set localized headers
        model = QStandardItemModel()
        localized_labels = [display_headers.get(key) for key in headers]
        model.setHorizontalHeaderLabels(localized_labels)

        # Populate model
        for _, row_data in df.iterrows():
            data_items = [
                QStandardItem(str(row_data[label])) 
                for label in headers 
                if label in row_data
            ]
            model.appendRow(data_items)

        return model        

    @staticmethod
    def _model_for_projects_search_results(self, project_number, language):
        # Set header labels
        data = ProjectsQueries.query_projects_by_number(self, project_number)
        # Append all project dictionaries to the list
        total_projects = len(data)
        if  total_projects == 0:
            text = "Antud numbriga projekti ei leitud"
            heading = pealkiri.informationSimple
            QMessageBox.information(None, heading, text)
            return None

        else:
            headers = HeaderKeys.ALL_HEADER_KEYS
            display_headers = TableHeaders_new(language)


            df_data = []
            for item in data:
                node = item.get("node", {})
                df_data.append(DataExtractor.extract_row_data_from_node(node, language=language))

            QCoreApplication.processEvents()
            df = pd.DataFrame(df_data)

            # Create model and set localized headers
            model = QStandardItemModel()
            localized_labels = [display_headers.get(key) for key in headers]
            model.setHorizontalHeaderLabels(localized_labels)

            # Populate model
            for _, row_data in df.iterrows():
                data_items = [
                    QStandardItem(str(row_data[label])) 
                    for label in headers 
                    if label in row_data
                ]
                model.appendRow(data_items)

            return model             # Populate QStandardItemModel with data from the pandas DataFrame

    @staticmethod
    def _model_for_projects_zoomed_map_properties(self, selected_features, language):
        
        #//TODO: add loading bar and if needed can roll back to old version 
        # Splitting the list into sublists with a maximum of 4 items each
        #sublists = [selected_features[i:i+Constants.items_for_page_medium] for i in range(0, len(selected_features), Constants.items_for_page_medium)]
        
        
        #print(f"selected features len: '{len(selected_features)}'")
        # Define the maximum number of items per sublist
        ProgressHelper.update_progress(value=0, maximum=len(selected_features)+1)
        MAX_ITEMS_PER_SET = 15

        sublists = [selected_features[i:i + MAX_ITEMS_PER_SET] 
                    for i in range(0, len(selected_features), MAX_ITEMS_PER_SET)]

        #unique_projects = set()
        all_projects = []
        ProgressHelper.update_progress(value=5)
        idx = 0
        ProgressHelper
        for feature in sublists:
            #print(f"feature: '{feature}'")
            projects_data = visibleSelector.get_projects_list_connected_with_view_properties(self, feature)
            #print(f"project_data: {projects_data}")
        
            all_projects.extend(projects_data)  # Append all project dictionaries to the list
            idx += Constants.items_for_page_medium
            print(f"count: {idx}")
            # Sleep to avoid hitting server too frequently
            ProgressHelper.update_progress(value=0)
            if idx % Constants.sleepPackage == 0:
                ProgressHelper.update_progressbar_by_current_index(current_index=idx)
                QCoreApplication.processEvents()
                # Ensure progress bar reaches 100% at the end
            ProgressHelper.update_progress(value=0)
                
                #import time
                #time.sleep(Constants.sleep_duration)
                #print("sleepy sleepy")
                #QCoreApplication.processEvents()
        total_projects = len(all_projects)
        #from pprint import pprint	
        #pprint(f"data: {all_projects}")

        if  total_projects == 0:
            text = "Piirkonnas puuduvad teadaolevad projektid"
            heading = pealkiri.informationSimple
            QMessageBox.information(None, heading, text)
            return None

        else:
            # Convert the list of dictionaries to a set to remove duplicates based on the 'id'
            data = {project['id']: project for project in all_projects}.values()
            #print(f"total len of all projects: '{len(all_projects)}'")

            
            headers = HeaderKeys.ALL_HEADER_KEYS
            display_headers = TableHeaders_new(language)
            df_data = []
            for project_data in data:
                # we can equal data to node because we have edges as nodes here
                node = project_data #seams that we are gettin edges as nodes here
                df_data.append(DataExtractor.extract_row_data_from_node(node, language=language))

                QCoreApplication.processEvents()
                df = pd.DataFrame(df_data)

                model = QStandardItemModel()
                localized_labels = [display_headers.get(key) for key in headers]
                model.setHorizontalHeaderLabels(localized_labels)

            # Populate QStandardItemModel with data from the pandas DataFrame
            for row_index, row_data in df.iterrows():
                data_items = [QStandardItem(str(row_data[label])) for label in headers]
                model.appendRow(data_items)
            
            return model
