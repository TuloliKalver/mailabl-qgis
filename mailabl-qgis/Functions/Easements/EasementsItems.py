# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

import pandas as pd

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableView, QMessageBox

from ..tableViewAdjust import ColumnResizer
from ...queries.python.DataLoading_classes import GraphqlQueriesEasements
from ...queries.python.query_tools import requestBuilder
from ...utils.table_utilys import ModelHandler
from ...utils.delegates.DelegateMainTable import DelegatesForTables
from ...config.settings import SettingsDataSaveAndLoad, MailablWebModules
from ...queries.python.MapTools.selector import visibleSelector
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts


class Constants:
    package_size = 25
    sleep_duration = 2 #time for sleep
    total_fetched = 0
    items_for_page_minimum = 1
    items_for_page_medium = 25
    items_for_page_large = 50
    sleepPackage = items_for_page_medium
    

header_id = 'ID'
header_number = 'Number'
header_name = 'Nimetus'
header_deadline = 'Tähtaeg'
header_color = 'Color'
header_creator = 'Looja'
header_property_number = 'Kataster'
header_properties_icon ='propertiesIcon'
header_parent_id = 'Parent_id'
header_webLinkButton = 'web_link_button'
header_Documents = 'Dokumendid'
header_file_path = "file_path_button"
header_statuses = 'Staatus'

class EasementssMain:
    @staticmethod
    def main_asements (self, table, types, statuses):

        result = queryHandling.easments_basic_data(self, types, statuses)
        if result is not None:
            InputeasmentsToTable.input_data_to_table(self,result, table)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            QMessageBox.warning(None, heading, text)

    def easmenets_by_number(self, table, search_values):
        result = queryHandling.easments_search(self, search_values)
        if result is not None:
            InputeasmentsToTable.input_data_to_table(self,result, table)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            QMessageBox.warning(None, heading, text)


class InputeasmentsToTable:
    def input_data_to_table(self, result, table):
        eas_model, header_labels = result
        if eas_model.rowCount() == 0:
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
            QMessageBox.information(None, heading, text)
        
        else:
            table_headers = queryHandling()
            
            number_column_index = header_labels.index(table_headers.header_number)
            name_column_index = header_labels.index(table_headers.header_name)
            #LP_ID_column_index = header_labels.index(table_headers.header_parent_id)
            creator_column_index = header_labels.index(table_headers.header_creator)        
            ID_column_index = header_labels.index(table_headers.header_id)

            for row_index in range(eas_model.rowCount()):
                eas_model.item(row_index, ID_column_index)

                number_item =  eas_model.item(row_index, number_column_index)
                creator_item = eas_model.item(row_index,creator_column_index)   
                
                number_item.setTextAlignment(Qt.AlignCenter)  
                creator_item.setTextAlignment(Qt.AlignCenter)

                date_column_index = ModelHandler.format_date_item(eas_model, row_index, header_labels)

                status_column_index, color_column_index = ModelHandler.set_status_item_colors_from_model(eas_model, row_index, header_labels)
                # Call format_cadastral_item method
                cadastral_column_index, cadastralButton_Column_index = ModelHandler.format_cadastral_item(eas_model, row_index, header_labels)
                # Call format_dok_item method
                dokAddress_column_index, dokButton_column_index = ModelHandler.format_dok_item(eas_model, row_index, header_labels)
                # Call build_mailabl_link_button method
                webButton_Column_index = ModelHandler.build_mailabl_link_button(eas_model, row_index, header_labels)

            module = MailablWebModules().easements
            DelegatesForTables.setup_delegates_by_module(table, header_labels, module)

            table.setModel(eas_model)
            # Set the row height to 20 pixels
            table.verticalHeader().setDefaultSectionSize(20)
                
            # Define the columns to hide
            columns_to_hide = [color_column_index,  dokAddress_column_index]
            # Hide the specified columns
            for column_index in columns_to_hide:
                table.hideColumn(column_index)

            
            resizes = ColumnResizer(table)
            columns_to_resize = [number_column_index,  date_column_index, creator_column_index, status_column_index]
            for column_index in columns_to_resize:
                resizes.resizeColumnByIndex(table, column_index)
                
            columns_width_icons = [ID_column_index, number_column_index, name_column_index, cadastral_column_index,
                                webButton_Column_index, dokButton_column_index, 
                                cadastralButton_Column_index]
            column_widths = [0,100,250,0,10,10,10]
            resizes.setColumnWidths(table, columns_width_icons, column_widths)
            # Hide certain column labels
            newLabel_for_cadastral = ""  # Replace with your actual column labels
            newLabel_documents = ""
            newLabel_Link = ""
            #newLabel_ID = ""
            newLabel_CadastralShow = ""
            #eas_model.setHorizontalHeaderItem(ID_column_index, QStandardItem(newLabel_ID))
            eas_model.setHorizontalHeaderItem(cadastral_column_index, QStandardItem(newLabel_for_cadastral))
            eas_model.setHorizontalHeaderItem(dokButton_column_index, QStandardItem(newLabel_documents))
            eas_model.setHorizontalHeaderItem(webButton_Column_index, QStandardItem(newLabel_Link))
            eas_model.setHorizontalHeaderItem(cadastralButton_Column_index, QStandardItem(newLabel_CadastralShow))
            table.verticalHeader().setVisible(False)
            # Set selection behavior to select entire rows
            table.setSelectionBehavior(QTableView.SelectRows)
            # Set selection mode to single selection
            table.setSelectionMode(QTableView.SingleSelection)

            # Set sorting behavior
            table.setSortingEnabled(True)
            # Trigger a refresh of the view to reflect the changes
            table.update()  # Refresh the view

class queryHandling:
    def __init__(self):
        self.header_id = header_id
        self.header_number = header_number
        self.header_name = header_name
        self.header_deadline = header_deadline
        self.header_color = header_color
        self.header_creator = header_creator
        self.header_property_number = header_property_number
        self.header_properties_icon = header_properties_icon
        self.header_parent_id = header_parent_id
        self.header_webLinkButton = header_webLinkButton
        self.header_Documents = header_Documents
        self.header_file_path = header_file_path
        self.header_statuses = header_statuses
        
    @staticmethod
    def easments_basic_data(self, types, statuses):
            # Set header labels
        header_labels = [header_id, header_number, header_name, header_deadline, header_creator, header_color, header_property_number, header_properties_icon,header_webLinkButton, header_Documents, header_file_path,  header_statuses]
       
        data = EasmentsSearch.query_easements_by_type_status_elements(self, types, statuses)
        #print("recived data is")
        #print(data)
        #data_count = len(data)
        # Build a pandas DataFrame
        model = queryHandling.create_data_model(header_labels, data)

        return model, header_labels
    
    def easments_search(self, search_values):
        header_labels = [header_id, header_number, header_name, header_deadline, header_creator, header_color, header_property_number, header_properties_icon,header_webLinkButton, header_Documents, header_file_path,  header_statuses]
       
        data = EasmentsSearch.query_easements_by_number(self, search_values)
        #print("recived data is")
        #print(data)
        #data_count = len(data)
        # Build a pandas DataFrame
        model = queryHandling.create_data_model(header_labels, data)

        return model, header_labels
    

    def create_data_model(header_labels, data):
        df_data = []
        df = pd.DataFrame(df_data)
        for project_data in data:
            node = project_data.get("node", {})
            properties = node.get("properties", {}).get("edges", [])
            propertie_cadastralNr = [property["node"]["cadastralUnitNumber"] for property in properties] 
            members = node.get("members",{}).get("edges",[])
            member_name = [creator["node"]["displayName"] for creator in members]
            #print(f"creator_name: {creator_name}")
            row_data = {
                    header_number: node.get("number", "") or "",
                    header_name: node.get("name", "") or "",
                    header_deadline: node.get("dueAt", "") or "",
                    header_statuses: node.get("status", {}).get("name", "") if node.get("status") else "",
                    header_color: node.get("status", {}).get("color", "") if node.get("status") else "",
                    header_property_number: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                    header_properties_icon: "",
                    header_id: node.get("id", ""),
                    #'LP_ID': node.get("parentID", ""),
                    header_webLinkButton: "",
                    header_file_path: "",
                    header_Documents: node.get("filesPath","") if ("filePath") else "Dokumendid puuduvad",
                    header_creator: ",".join(member_name) if member_name else ""
                }
            #print(f"row_data: '{row_data}'")
            
            df_data.append(row_data)    
        #print("df_data")
        #print(df_data)

        QCoreApplication.processEvents()
        df = pd.DataFrame(df_data)

        # Create a QStandardItemModel and set header labels
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        # Populate QStandardItemModel with data from the pandas DataFrame
        for row_index, row_data in df.iterrows():
            data_items = [QStandardItem(str(row_data[label])) for label in header_labels]
            model.appendRow(data_items)

        return model

class EasmentsSearch:    
    def query_easements_by_type_status_elements(self, type_values, statuses):
        print(f"type_values: '{type_values}'")
        #print(statuses)
        # Load the project query using the loader instance
        query_loader = GraphqlQueriesEasements()
        query = GraphqlQueriesEasements.load_query_for_easements(self, query_loader.Q_where_easements_type_status)        
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
                "search": None,
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
                    "column": "NAME",
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
                fetched_data = data.get("data", {}).get("easements", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("easements", {}).get("pageInfo", {})
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
    def query_easements_by_number(self, easement_number):
        #print(statuses)
        # Load the project query using the loader instance
        query_loader = GraphqlQueriesEasements()
        query = query_loader.load_query_for_easements(query_loader.Q_where_easements_type_status)        
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
                        {"column": "NUMBER", "operator": "IN", "value": [easement_number]}
                    ]
                }
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get("easements", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("easements", {}).get("pageInfo", {})
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
class getEasementsWhere:
    @staticmethod
    def query_easement_related_properties(self, id_value):
        #print(f"id value in query {id_value}")
        #Load the project query using the loader instance
        query_loader = GraphqlQueriesEasements()
        query = query_loader.load_query_for_easements(query_loader.Q_where_easement_related_properties)
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
                project_data = data.get("data", {}).get("easement", {})
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
                print(f"properties_items: {properties_items}")
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
