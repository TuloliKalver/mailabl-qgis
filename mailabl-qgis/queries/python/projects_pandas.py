# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-nam



import pandas as pd
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from .DataLoading_classes import Graphql_project, GraphQLQueryLoader
from .query_tools import requestBuilder
from.fetchers.ModulePropertiesFetcher import PropertiesModuleFetcher

from ...config.ui_directories import PathLoaderSimple
from ...KeelelisedMuutujad.messages import Headings
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...utils.DataExtractors.DataExtractors import DataExtractor
from ...KeelelisedMuutujad.modules import Module
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...utils.messagesHelper import ModernMessageDialog


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
  
    
class ProjectsQueries:

    @staticmethod
    def _fetch_active_main_projects_by_status(self, statuses):
        
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
   
            #TODO: add loading of projects by pages         
            fetched_items.extend(fetched_data)
            total_fetched += len(fetched_data)
    
            QCoreApplication.processEvents()

            if not projects_end_cursor or (desired_total_items is not None and total_fetched >= desired_total_items) or not projects_hasNextPage:
                break

        return fetched_items[:desired_total_items]

    @staticmethod    
    def _fetch_projects_by_number(self, project_number):
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
        
        data = ProjectsQueries._fetch_active_main_projects_by_status(self, status_value)
        
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
        data = ProjectsQueries._fetch_projects_by_number(self, project_number)
        # Append all project dictionaries to the list
        total_projects = len(data)
        if  total_projects == 0:
            text = "Antud numbriga projekti ei leitud"
            heading = pealkiri.infoSimple
            ModernMessageDialog.Info_messages_modern(heading,text)
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
    def _model_for_module_zoomed_map_properties(selected_features: list, language: str, module: str):
        #print(f"selected features: '{selected_features}', total selected features: '{len(selected_features)}'")
        #//TODO: add loading bar and if needed can roll back to old version 
        # Splitting the list into sublists with a maximum of 4 items each
        #sublists = [selected_features[i:i+Constants.items_for_page_medium] for i in range(0, len(selected_features), Constants.items_for_page_medium)]
        value = 0

        MAX_ITEMS_PER_SET = 15

        grouped_cadasters = [selected_features[i:i + MAX_ITEMS_PER_SET] 
                    for i in range(0, len(selected_features), MAX_ITEMS_PER_SET)]

        #print(f"grouped_cadasters: '{grouped_cadasters}'")
        data_total = []
        idx = 0
        for group in grouped_cadasters:
            #print(f"feature: '{group}'")
            data = PropertiesModuleFetcher._fetch_module_feature_conneted_with_propertie_list(group, module)
            #print(f"project_data: {data}")

            data_total.extend(data)  # Append all project dictionaries to the list
            #print(f"data_total: {data_total}")
            
            QCoreApplication.processEvents()
            # Ensure progress bar reaches 100% at the end
            
        # Convert the list of dictionaries to a set to remove duplicates based on the 'id'
        data_optimal = {project['id']: project for project in data_total}.values()
        #print(f"total len of all projects: '{len(data_total)}'")

    
        headers = HeaderKeys.ALL_HEADER_KEYS
        display_headers = TableHeaders_new(language)
        df_data = []
        for project_data in data_optimal:
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
        progress.close()
        return model
