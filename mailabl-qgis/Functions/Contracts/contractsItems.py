# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

import pandas as pd

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableView, QMessageBox

from ...utils.table_view_utils import ColumnResizer
from ...queries.python.DataLoading_classes import GraphqlQueriesContracts
from ...queries.python.query_tools import requestBuilder
from ...utils.table_utilys import ModelHandler
from ...utils.delegates.DelegateMainTable import DelegatesForTables, ModuleButtonDelegate
from ...config.settings import SettingsDataSaveAndLoad, MailablWebModules
from ...config.QGISSettingPaths import LayerSettings, SettingsLoader
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
header_responsible = 'Vastutaja'
header_property_number = 'Kataster'
header_properties_icon ='propertiesIcon'
header_parent_id = 'Parent_id'
header_webLinkButton = 'web_link_button'
header_Documents = 'Dokumendid'
header_file_path = "file_path_button"
header_statuses = 'Staatus'

class ContractsMain:
    @staticmethod
    def main_contracts (self, table, types, statuses):

        result = queryHandling.contracts_basic_data(self, types, statuses)

        if result is not None:
            con_model, header_labels = result
            if con_model.rowCount() == 0:
                text = HoiatusTexts().ostingu_tulemused_puuduvad
                heading = Headings().warningSimple
                print(f"{heading}, {text}")
                QMessageBox.information(None, heading, text)
            
            else:
                table_headers = queryHandling()
                
                number_column_index = header_labels.index(table_headers.header_number)
                name_column_index = header_labels.index(table_headers.header_name)
                #LP_ID_column_index = header_labels.index(table_headers.header_parent_id)
                responsible_column_index = header_labels.index(table_headers.header_responsible)        
                ID_column_index = header_labels.index(table_headers.header_id)

                for row_index in range(con_model.rowCount()):
                    con_model.item(row_index, ID_column_index)

                    number_item =  con_model.item(row_index, number_column_index)
                    responsible_item = con_model.item(row_index,responsible_column_index)   
                    
                    number_item.setTextAlignment(Qt.AlignCenter)  
                    responsible_item.setTextAlignment(Qt.AlignCenter)

                    date_column_index = ModelHandler.format_date_item(con_model, row_index, header_labels)

                    status_column_index, color_column_index = ModelHandler.set_status_item_colors_from_model(con_model, row_index, header_labels)
                    # Call format_cadastral_item method
                    cadastral_column_index, cadastralButton_Column_index = ModelHandler.format_cadastral_item(con_model, row_index, header_labels)
                    # Call format_dok_item method
                    dokAddress_column_index, dokButton_column_index = ModelHandler.format_dok_item(con_model, row_index, header_labels)
                    # Call build_mailabl_link_button method
                    webButton_Column_index = ModelHandler.build_mailabl_link_button(con_model, row_index, header_labels)

                module = MailablWebModules().contracts
                DelegatesForTables.setup_delegates_by_module(table, header_labels, module)

                table.setModel(con_model)
                # Set the row height to 20 pixels
                table.verticalHeader().setDefaultSectionSize(20)
                    
                # Define the columns to hide
                columns_to_hide = [color_column_index,  dokAddress_column_index]
                # Hide the specified columns
                for column_index in columns_to_hide:
                    table.hideColumn(column_index)

                
                resizes = ColumnResizer(table)
                columns_to_resize = [number_column_index,  date_column_index, responsible_column_index, status_column_index]
                for column_index in columns_to_resize:
                    resizes.resizeColumnByIndex(table, column_index)
                    
                columns_width_icons = [ID_column_index, name_column_index, cadastral_column_index,
                                    webButton_Column_index, dokButton_column_index, 
                                    cadastralButton_Column_index]
                column_widths = [0,250,0,10,10,10]
                resizes.setColumnWidths(table, columns_width_icons, column_widths)
                # Hide certain column labels
                newLabel_for_cadastral = ""  # Replace with your actual column labels
                newLabel_documents = ""
                newLabel_Link = ""
                #newLabel_ID = ""
                newLabel_CadastralShow = ""
                #con_model.setHorizontalHeaderItem(ID_column_index, QStandardItem(newLabel_ID))
                con_model.setHorizontalHeaderItem(cadastral_column_index, QStandardItem(newLabel_for_cadastral))
                con_model.setHorizontalHeaderItem(dokButton_column_index, QStandardItem(newLabel_documents))
                con_model.setHorizontalHeaderItem(webButton_Column_index, QStandardItem(newLabel_Link))
                con_model.setHorizontalHeaderItem(cadastralButton_Column_index, QStandardItem(newLabel_CadastralShow))
                table.verticalHeader().setVisible(False)
                # Set selection behavior to select entire rows
                table.setSelectionBehavior(QTableView.SelectRows)
                # Set selection mode to single selection
                table.setSelectionMode(QTableView.SingleSelection)

                # Set sorting behavior
                table.setSortingEnabled(True)
                # Trigger a refresh of the view to reflect the changes
                table.update()  # Refresh the view
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")

    def search_contracts (self, query, table):
        result = ContractsSearch.contracts_search_results(self, query)
        print (f"contract search results : {result}")

        if result is not None:
            con_model, header_labels = result

            table_headers = queryHandling()
            
            number_column_index = header_labels.index(table_headers.header_number)
            name_column_index = header_labels.index(table_headers.header_name)
            #LP_ID_column_index = header_labels.index(table_headers.header_parent_id)
            responsible_column_index = header_labels.index(table_headers.header_responsible)        
            ID_column_index = header_labels.index(table_headers.header_id)

            for row_index in range(con_model.rowCount()):
                con_model.item(row_index, ID_column_index)

                number_item =  con_model.item(row_index, number_column_index)
                responsible_item = con_model.item(row_index,responsible_column_index)   
                
                number_item.setTextAlignment(Qt.AlignCenter)  
                responsible_item.setTextAlignment(Qt.AlignCenter)

                date_column_index = ModelHandler.format_date_item(con_model, row_index, header_labels)

                status_column_index, color_column_index = ModelHandler.set_status_item_colors_from_model(con_model, row_index, header_labels)
                # Call format_cadastral_item method
                cadastral_column_index, cadastralButton_Column_index = ModelHandler.format_cadastral_item(con_model, row_index, header_labels)
                # Call format_dok_item method
                dokAddress_column_index, dokButton_column_index = ModelHandler.format_dok_item(con_model, row_index, header_labels)
                # Call build_mailabl_link_button method
                webButton_Column_index = ModelHandler.build_mailabl_link_button(con_model, row_index, header_labels)

                module = MailablWebModules().contracts
                DelegatesForTables.setup_delegates_by_module(table, header_labels, module)

                table.setModel(con_model)
                # Set the row height to 20 pixels
                table.verticalHeader().setDefaultSectionSize(20)
                    
                # Define the columns to hide
                columns_to_hide = [color_column_index, dokAddress_column_index]
                # Hide the specified columns
                for column_index in columns_to_hide:
                    table.hideColumn(column_index)

                resizes = ColumnResizer(table)
                columns_to_resize = [number_column_index, date_column_index, responsible_column_index, status_column_index]
                for column_index in columns_to_resize:
                    resizes.resizeColumnByIndex(table, column_index)
                    
                columns_width_icons = [ID_column_index, name_column_index, cadastral_column_index,
                                    webButton_Column_index, dokButton_column_index, 
                                    cadastralButton_Column_index]
                column_widths = [0,250,0,10,10,10]
                resizes.setColumnWidths(table, columns_width_icons, column_widths)
                # Hide certain column labels
                newLabel_for_cadastral = ""  # Replace with your actual column labels
                newLabel_documents = ""
                newLabel_Link = ""
                #newLabel_ID = ""
                newLabel_CadastralShow = ""
                #con_model.setHorizontalHeaderItem(ID_column_index, QStandardItem(newLabel_ID))
                con_model.setHorizontalHeaderItem(cadastral_column_index, QStandardItem(newLabel_for_cadastral))
                con_model.setHorizontalHeaderItem(dokButton_column_index, QStandardItem(newLabel_documents))
                con_model.setHorizontalHeaderItem(webButton_Column_index, QStandardItem(newLabel_Link))
                con_model.setHorizontalHeaderItem(cadastralButton_Column_index, QStandardItem(newLabel_CadastralShow))
                table.verticalHeader().setVisible(False)
                # Set selection behavior to select entire rows
                table.setSelectionBehavior(QTableView.SelectRows)
                # Set selection mode to single selection
                table.setSelectionMode(QTableView.SingleSelection)

                # Set sorting behavior
                table.setSortingEnabled(True)
                # Trigger a refresh of the view to reflect the changes
                table.update()  # Refresh the view
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
            QMessageBox.information(None, heading, text)

class queryHandling:
    def __init__(self):
        self.header_id = header_id
        self.header_number = header_number
        self.header_name = header_name
        self.header_deadline = header_deadline
        self.header_color = header_color
        self.header_responsible = header_responsible
        self.header_property_number = header_property_number
        self.header_properties_icon = header_properties_icon
        self.header_parent_id = header_parent_id
        self.header_webLinkButton = header_webLinkButton
        self.header_Documents = header_Documents
        self.header_file_path = header_file_path
        self.header_statuses = header_statuses
        
    @staticmethod
    def contracts_basic_data(self, types, statuses):
            # Set header labels
        header_labels = [header_id, header_number, header_name, header_deadline, header_responsible, header_color, header_property_number, header_properties_icon,header_webLinkButton, header_Documents, header_file_path,  header_statuses]
       
        #statuses = Statuses.by_module_and_state(self, MODULE_CONTRACTS, STATE_OPEN)
        #print("statuses")
        #print(statuses)

        data = ContractsSearch.query_contracts_by_type_status_elements(self, types, statuses)
        #print("recived data is")
        #print(data)
        #data_count = len(data)
        # Build a pandas DataFrame
        df_data = []
        df = pd.DataFrame(df_data)
        for project_data in data:
            node = project_data.get("node", {})
            properties = node.get("properties", {}).get("edges", [])
            propertie_cadastralNr = [property["node"]["cadastralUnitNumber"] for property in properties] 
            responsibles = node.get("responsible",{}).get("edges",[])
            responsible_name = [responsible["node"]["displayName"] for responsible in responsibles]
            print(f"responsible_name: {responsible_name}")
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
                    header_responsible: ",".join(responsible_name) if responsible_name else ""
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

        return model, header_labels

class ContractsQueries_list:
    @staticmethod
    def query_contracts_by_status(self, statuses):
        #print(statuses)
        # Load the project query using the loader instance
        query_loader = GraphqlQueriesContracts()
        query = GraphqlQueriesContracts.load_query_for_contracts(self,query_loader.Q_All_contracts)        
        # Set the desired total number of items to fetch
        desired_total_items = None  # Adjust this to your desired value
        items_for_page = 50  # Adjust this to your desired value
        items_for_properties_page = 50
        end_cursor = None  # Initialize end_cursor before the loop
        properties_end_cursor = None
        total_fetched = 0        # Initialize an empty list to store fetched items
        fetched_items = []
        
        while (desired_total_items is None or total_fetched < desired_total_items):
            # Construct variables for the GraphQL query
            variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None,
                "propertiesFirst": items_for_properties_page,
                "propertiesAfter": properties_end_cursor if properties_end_cursor else None,
                "where": {
                    "AND": [
                        {
                            "column": "STATUS",
                            "operator": "IN",
                            "value": statuses
                        }
                    ]
                }
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                data = response.json()
                #print("data")
                #print(data)
                fetched_data = data.get("data", {}).get("contracts", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("contracts", {}).get("pageInfo", {})
                properties_page_info = data.get("data", {}).get("contracts", {}).get("properties",{}).get("pageInfo",{})
                properties_end_cursor = properties_page_info.get("endCursor")
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

class ContractsSearch:

    @staticmethod
    def contracts_search_results(self, contract_number):
        # Set header labels
        header_labels = [header_id, header_number, header_name, header_deadline, header_responsible, header_color, header_property_number, header_properties_icon,header_webLinkButton, header_Documents, header_file_path,  header_statuses]
       
        data = ContractsSearch.query_contracts_by_number(self, contract_number)
        df_data = []
        df = pd.DataFrame(df_data)
        for project_data in data:
            node = project_data.get("node", {})
            properties = node.get("properties", {}).get("edges", [])
            propertie_cadastralNr = [property["node"]["cadastralUnitNumber"] for property in properties] 
            responsibles = node.get("responsible",{}).get("edges",[])
            responsible_name = [responsible["node"]["displayName"] for responsible in responsibles]
            print(f"responsible_name: {responsible_name}")
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
                    header_responsible: ",".join(responsible_name) if responsible_name else ""
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

        return model, header_labels

    @staticmethod
    def contracts_zoomed_items(self, cadastral_units):
        # Set header labels
        header_labels = [header_id, header_number, header_name, header_deadline, header_responsible, header_color, header_property_number, header_properties_icon,header_webLinkButton, header_Documents, header_file_path,  header_statuses]
       
        data = ContractsSearch.query_contracts_for_zoomed_elements(self, cadastral_units)
        #print("recived data is")
        #print(data)
        #data_count = len(data)
        # Build a pandas DataFrame
        df_data = []
        df = pd.DataFrame(df_data)
        for project_data in data:
            node = project_data.get("node", {})
            properties = node.get("properties", {}).get("edges", [])
            propertie_cadastralNr = [property["node"]["cadastralUnitNumber"] for property in properties] 
            responsibles = node.get("responsible",{}).get("edges",[])
            responsible_name = [responsible["node"]["displayName"] for responsible in responsibles]
            print(f"responsible_name: {responsible_name}")
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
                    header_responsible: ",".join(responsible_name) if responsible_name else ""
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

        return model, header_labels

    @staticmethod
    def query_contracts_by_number(self, contract_number):
        #print(statuses)
        # Load the project query using the loader instance
        query_loader = GraphqlQueriesContracts()
        query = GraphqlQueriesContracts.load_query_for_contracts(self,query_loader.Q_All_contracts)        
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

    def query_contracts_by_type_status_elements(self, type_values, statuses):
        print(f"type_values: '{type_values}'")
        #print(statuses)
        # Load the project query using the loader instance
        query_loader = GraphqlQueriesContracts()
        query = GraphqlQueriesContracts.load_query_for_contracts(self, query_loader.Q_where_contracts_type_status)        
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

