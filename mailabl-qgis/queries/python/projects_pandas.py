import pandas as pd
from PyQt5.uic import loadUi
import requests
import webbrowser
import subprocess
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QStyledItemDelegate, QMessageBox
from .DataLoading_classes import Graphql_project, GraphQLQueryLoader
from .statusManager import Statuses
from .query_tools import requestBuilder
from ...Functions.item_selector_tools import properties_selectors
from ...config.settings import OpenLink
from ...config.ui_directories import PathLoaderSimple
from .MapTools.selector import visibleSelector
from ...config.settings import SettingsDataSaveAndLoad





header_id = 'ID'
header_number = 'Number'
header_name = 'Nimetus'
header_deadline = 'Tähtaeg'
header_color = 'Color'
header_responsible = 'Vastutaja'
header_property_number = 'Kataster'
header_properties_icon ='propertiesIcon'
header_parent_id = 'Parent_id'
header_webLink_button = 'web_link_button'
header_documents = 'Dokumendid'
header_file_path = "file_path_button"
header_statuses = 'Staatus'


class GetProjectsWhere:
    """
    Query the properties related to a project identified by the given ID.

    """
    def query_projects_related_properties(self, id_value):

        #print(f"id value in query {id_value}")
        #Load the project query using the loader instance
        
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query_for_projects(self,query_loader.Q_where_Projects_related_properties)
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        #Initialize variables for pagination
        end_cursor = None  # Initialize end_cursor before the loop
        total_fetched = 0        # Initialize an empty list to store fetched items
        properties_items = []
        
        while (desired_total_items is None or total_fetched < desired_total_items):
            # Construct variables for the GraphQL query
            variables = {
                    "propertiesFirst": items_for_page,
                    "propertiesAfter": end_cursor if end_cursor else None,
                    "id": id_value
                    }
            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                #edges = data.get("data", {}).get("project", {}).get("properties", {}).get("edges", {})
                #print("egdges")
                #print(edges)
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
        items_for_page = 50  # Adjust this to your desired value
        projects_end_cursor = None  # Initialize end_cursor before the loop
        total_fetched = 0
        fetched_items = []
        
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
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
        items_for_page = 50
        projects_end_cursor = None
        total_fetched = 0
        fetched_items = []
                    
        while (desired_total_items is None or total_fetched < desired_total_items):
            variables = {
                "first": items_for_page,
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

        
    def hex_to_rgb(self, hex_code):
        clean_hex_code = hex_code.strip('#')
        return tuple(int(clean_hex_code[i:i+2], 16) for i in (0, 2, 4))

class WebLinkDelegate(QStyledItemDelegate):
    def __init__(self, id_column_index, parent=None):
        super(WebLinkDelegate, self).__init__(parent)
        self.id_column_index = id_column_index
    
    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                id_value = model.data(model.index(index.row(), self.id_column_index), Qt.DisplayRole)
                self.open_project_in_mailabl(id_value)
                return True
        return super().editorEvent(event, model, option, index)

    def open_project_in_mailabl(self, project_id):
        web_link = OpenLink.web_link_single_projects()
        project_link = f"{web_link}{project_id}"
        try:
            response = requests.get(project_link, timeout=10, verify=False)
            webbrowser.open(response.url)
        except requests.Timeout:
            print("Request timed out.")
        except requests.RequestException as e:
            print(f"Error: {e}")
            
            
class FileDelegate(QStyledItemDelegate):
    def __init__(self, file_column_index, parent=None):
        super(FileDelegate, self).__init__(parent)
        self.file_column_index = file_column_index
    
    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                file_value = model.data(model.index(index.row(), self.file_column_index), Qt.DisplayRole)
                self.open_folder_in_local_file_browser(file_value)
                return True
        return super().editorEvent(event, model, option, index)

    def open_folder_in_local_file_browser(self, file_id):
        #print(f"file_id: {file_id}")
        # Use subprocess to open the local file explorer
        subprocess.Popen(['explorer', file_id.replace('/', '\\')], shell=True)

class SelectMapElementsDelegate(QStyledItemDelegate):
    def __init__(self, ID_column_index, parent=None):
        super(SelectMapElementsDelegate, self).__init__(parent)
        self.ID_column_index = ID_column_index

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                id_value = str(model.data(model.index(index.row(), self.ID_column_index), Qt.DisplayRole))
                values = GetProjectsWhere.query_projects_related_properties(self, id_value)
                layer_type = "active"
                properties_selectors.show_connected_cadasters(values, layer_type)
                return True
        return super().editorEvent(event, model, option, index)
        
class ProjectsWithPandas_2:
    def __init__(self, cmbProjectState):
        self.header_id = header_id
        self.header_number = header_number
        self.header_name = header_name
        self.header_deadline =header_deadline
        self.header_color = header_color
        self.header_responsible = header_responsible
        self.header_property_number = header_property_number
        self.header_properties_icon = header_properties_icon
        self.header_parent_id = header_parent_id
        self.header_webLinkButton = header_webLink_button
        self.header_Documents = header_documents
        self.header_file_path = header_file_path
        self.header_statuses = header_statuses
        self.Project_state = cmbProjectState

    def table_view_from_active_projects_statuses(self, statusValue):
        # Set header labels
        header_labels = [header_id, header_number, 
                            header_name, header_deadline,
                            header_color, header_responsible,
                            header_property_number, header_properties_icon,
                            header_parent_id, header_webLink_button, 
                            header_documents, header_file_path, 
                            header_statuses]
        #print(f" header_webLinkButton: {header_webLinkButton}")
        #print(f"header_labels: {header_labels}")
        # Get projects status types that are active
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        #print("statuses")
        #print(statuses)
        data = ProjectsWithPandas.query_active_main_projects_by_status(self, statusValue)
        
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
                header_id: node.get("id", "") or "",
                header_number: node.get("number", "") or "",
                header_name: node.get("name", "") or "",
                header_deadline: node.get("dueAt", "") or "",
                header_statuses: node.get("status", {}).get("name", "") if node.get("status") else "",
                header_color: node.get("status", {}).get("color", "") if node.get("status") else "",
                header_property_number: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                header_id: node.get("id", ""),
                header_parent_id: node.get("parentID", ""),
                header_webLink_button: "",
                header_documents: node.get("filesPath","")or "",
                header_file_path: "",
                header_responsible: ",".join(resposnisble_name) if resposnisble_name else "",
                header_properties_icon: ""
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
        header_labels = [header_id, header_number, 
                            header_name, header_deadline,
                            header_color, header_responsible,
                            header_property_number, header_properties_icon,
                            header_parent_id, header_webLink_button, 
                            header_documents, header_file_path, 
                            header_statuses]
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        
        #unique_projects = set()
        all_projects = []

        
        all_projects = ProjectsWithPandas.QueryProjects_by_number(self, project_number)
        # Append all project dictionaries to the list
        QCoreApplication.processEvents()
        total_projects = len(all_projects)
        if  total_projects == 0:
            QMessageBox.information(None, "Oi Oi Oi", "Ei leidnud antud numbriga projekti")
            return None

        else:
            # Convert the list of dictionaries to a set to remove duplicates based on the 'id'
            print(f"total len of all projects: '{len(all_projects)}'")
            #data = {project['id']: project for project in all_projects}.values()
            #print(f"data: {data}")

            #data = ProjectsWithPandas.QueryProjects_Parent_Active_Open(self, statuses)
            #data_count = len(data)
            #print(f"total data  {data_count}")
            progress_value = 0
            # Build a pandas DataFrame
            df_data = []
            for item in all_projects:
                node = item.get("node", {})
                properties = node.get("properties", {}).get("edges", [])
                propertie_cadastralNr = [propertie["node"]["cadastralUnitNumber"] for propertie in properties]
                responsibles = node.get("responsible",{}).get("edges",[])
                resposnisble_name = [responsible["node"]["displayName"] for responsible in responsibles]
                row_data = {
                    header_id: node.get("id", "") or "",
                    header_number: node.get("number", "") or "",
                    header_name: node.get("name", "") or "",
                    header_deadline: node.get("dueAt", "") or "",
                    header_statuses: node.get("status", {}).get("name", "") if node.get("status") else "",
                    header_color: node.get("status", {}).get("color", "") if node.get("status") else "",
                    header_property_number: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                    header_id: node.get("id", ""),
                    header_parent_id: node.get("parentID", ""),
                    header_webLink_button: "",
                    header_documents: node.get("filesPath","")or "",
                    header_file_path: "",
                    header_responsible: ",".join(resposnisble_name) if resposnisble_name else "",
                    header_properties_icon: ""
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
    def __init__(self, cmbProjectState):
        self.header_id = header_id
        self.header_number = header_number
        self.header_name = header_name
        self.header_deadline =header_deadline
        self.header_color = header_color
        self.header_responsible = header_responsible
        self.header_property_number = header_property_number
        self.header_properties_icon = header_properties_icon
        self.header_parent_id = header_parent_id
        self.header_webLinkButton = header_webLink_button
        self.header_Documents = header_documents
        self.header_file_path = header_file_path
        self.header_statuses = header_statuses
        self.Project_state = cmbProjectState
    #@staticmethod
    def Create_Project_tableView_for_zoom(self, selected_features):
        # Set header labels
        header_labels = [header_id, header_number, 
                            header_name, header_deadline,
                            header_color, header_responsible,
                            header_properties_icon, #6
                            header_parent_id, header_webLink_button,  #8
                            header_documents, header_file_path, #10
                            header_statuses]
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        print(f"selected features: '{selected_features}' total:'{len(selected_features)}'")
        
        # Splitting the list into sublists with a maximum of 4 items each
        package_size = 25
        sublists = [selected_features[i:i+package_size] for i in range(0, len(selected_features), package_size)]
        
        #unique_projects = set()
        all_projects = []

        count = 0
        sleepPackage = 25
        sleep_duration = 2
        import time
        
        for feature in sublists:
            #print(f"feature: '{feature}'")
            projects_data = visibleSelector.get_projects_list_connected_with_view_properties(self, feature)
            #print(f"project_data: {projects_data}")
        
            all_projects.extend(projects_data)  # Append all project dictionaries to the list
            count += 25
            print(f"count: {count}")
            # Sleep to avoid hitting server too frequently
            if count %sleepPackage == 0:
                time.sleep(sleep_duration)
                print("sleepy sleepy")
            QCoreApplication.processEvents()
        total_projects = len(all_projects)
        if  total_projects == 0:
            QMessageBox.information(self, "Eureka", "antud piirkonnas puuduvad teadaolevad projektid")
            return None

        else:
            # Convert the list of dictionaries to a set to remove duplicates based on the 'id'
            data = {project['id']: project for project in all_projects}.values()
            print(f"total len of all projects: '{len(all_projects)}'")
            print(f"data: {data}")

            # Build a pandas DataFrame
            df_data = []
            for node in data:
                #node = project_data.get("node", {})
                #properties = node.get("properties", {}).get("edges", [])
                #propertie_cadastralNr = [propertie["node"]["cadastralUnitNumber"] for propertie in properties]
                responsibles = node.get("responsible",{}).get("edges",[])
                resposnisble_name = [responsible["node"]["displayName"] for responsible in responsibles]
                row_data = {
                    header_id: node.get("id", "") or "",
                    header_number: node.get("number", "") or "",
                    header_name: node.get("name", "") or "",
                    header_deadline: node.get("dueAt", "") or "",
                    header_statuses: node.get("status", {}).get("name", "") if node.get("status") else "",
                    header_color: node.get("status", {}).get("color", "") if node.get("status") else "",
                    #header_property_number: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                    #header_id: node.get("id", ""),
                    header_parent_id: node.get("parentID", ""),
                    header_webLink_button: "",
                    header_documents: node.get("filesPath","")or "",
                    header_file_path: "",
                    header_responsible: ",".join(resposnisble_name) if resposnisble_name else "",
                    header_properties_icon: ""
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
