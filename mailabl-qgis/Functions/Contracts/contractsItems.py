
import pandas as pd
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor, QBrush, QIcon
from PyQt5.QtWidgets import QStyledItemDelegate
from ...queries.python.statusManager import Statuses
from ...queries.python.DataLoading_classes import GraphQLQueryLoader, Graphql_contracts
from ...queries.python.query_tools import requestBuilder
from ..tableViewAdjust import colors, ColumnResizer
from ...config.settings import Filepaths
from ..ButtonDelegates import ContractButtonDelegate, FileDelegate
from ...config.iconHandler import iconHandler

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
    def main_contracts(self, table):

        
        con_model, header_labels = queryHandling.contracts_basic_data(self)
        contracts_model = QStandardItemModel()
        contracts_model.setHorizontalHeaderLabels(header_labels)
        
        name_column_index = header_labels.index(header_name) 
        status_column_index = header_labels.index(header_statuses)
        number_column_index = header_labels.index(header_number)
        color_column_index = header_labels.index(header_color)
        Link_Column_index = header_labels.index(header_webLinkButton)
        ID_column_index = header_labels.index(header_id)
        dokAddress_column_index = header_labels.index(header_Documents)
        dokButton_column_index = header_labels.index(header_file_path)
        cadastralUnit_Column_index = header_labels.index(header_property_number)

        
        for row_index in range(con_model.rowCount()):
            number_item = con_model.item(row_index, number_column_index)            
            name_item = con_model.item(row_index, name_column_index)
            status_item = con_model.item(row_index, status_column_index)
            color_item = con_model.item(row_index, color_column_index)
            id_item = con_model.item(row_index, ID_column_index)
            dokAddress_item = con_model.item(row_index, dokAddress_column_index)
            cadastralUnit_item = con_model.item(row_index,cadastralUnit_Column_index)
            
            number_item_text = QStandardItem(number_item.text())
            name_item_text = QStandardItem(name_item.text())
            status_item_text = QStandardItem(status_item.text())
            id_item_text = QStandardItem(id_item.text())
            Address_item_text = QStandardItem(dokAddress_item.text())
            cadastralUnit_text = QStandardItem(cadastralUnit_item.text())
            
            if color_item:
                color_code = color_item.text()
                if color_code:
                    rgb_color = colors.hex_to_rgb(color_code)
                    rgb_black = '#181a1c'
                    rgb_color_black = colors.hex_to_rgb(rgb_black)
                    color = QColor(*rgb_color)
                    color_black = QColor(*rgb_color_black)
                    status_item_text.setBackground(color)
                    status_item_text.setForeground(color_black)
                    status_item_text.setTextAlignment(Qt.AlignCenter)

            contracts_model.setItem(row_index, number_column_index, number_item_text) 
            contracts_model.setItem(row_index, name_column_index, name_item_text)
            contracts_model.setItem(row_index, cadastralUnit_Column_index,cadastralUnit_text)


            dokAddress_index = con_model.index(row_index, dokAddress_column_index)
            dokAddress_item = con_model.itemFromIndex(dokAddress_index)
            contracts_model.setItem(row_index, dokAddress_column_index, Address_item_text)

            if dokAddress_item and dokAddress_item.data(Qt.DisplayRole):
                dokLink = dokAddress_item.data(Qt.DisplayRole)
                print(f"dok Link {dokLink}")
                if dokLink:
                    pb_dokLink = QStandardItem()
                    icon_path = iconHandler.setIcon(dokLink)
                    icon = QIcon(icon_path)
                    pb_dokLink.setIcon(icon)
                    background_color2 = QColor("#40414f")  
                    pb_dokLink.setBackground(QBrush(background_color2))
                    # Set the foreground color (text color) to a contrasting color
                    text_color2 = QColor("#FFFFFF")  # White
                    pb_dokLink.setForeground(QBrush(text_color2))
                    # Make the cell selectable and give it a raised effect
                    pb_dokLink.setSelectable(True)
                    pb_dokLink.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)        
                    # Add a button to each row in the 'Button' column (column link_column_index)
                    contracts_model.setItem(row_index, dokButton_column_index, pb_dokLink)
            
            pb_openInMailabl = QStandardItem()
            Mailabl_icon_path = Filepaths.Mailabl_icon()
            icon = QIcon(Mailabl_icon_path)
            pb_openInMailabl.setIcon(icon)
            pb_openInMailabl.setSelectable(True)
            pb_openInMailabl.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            # Set the item containing the icon to be centered within the cell
            pb_openInMailabl.setTextAlignment(Qt.AlignCenter)
            contracts_model.setItem(row_index, Link_Column_index, pb_openInMailabl)
            contracts_model.setItem(row_index,ID_column_index, id_item_text)
            contracts_model.setItem(row_index, status_column_index, status_item_text)
            
                # Set the customColumn(Link_Column_index, delegate)
            
                    # Set the custom delegate for the button column (column link_column_index)
        button_delegate = ContractButtonDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(Link_Column_index, button_delegate)
            
                # Set the custom delegate for the file column
        file_delegate = FileDelegate(dokAddress_column_index, table)
        print(f"dokAddress_column_index: {dokAddress_column_index}")
        table.setItemDelegateForColumn(dokButton_column_index, file_delegate)


#        show_onMap_delegate = SelectMapElementsDelegate(ID_column_index, table)
#        table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)

            
        table.verticalHeader().setVisible(False)
        table.setSortingEnabled(True)
        table.setModel(contracts_model)
        table.update()  # Refresh the view
        
                # Define the columns to hide
        columns_to_hide = [color_column_index]
        # Hide the specified columns
        for column_index in columns_to_hide:
            table.hideColumn(column_index)
        
        resizes = ColumnResizer(table)
        columns_to_resize = [number_column_index, name_column_index, status_column_index]
        for column_index in columns_to_resize:
            resizes.resizeColumnByIndex(table, column_index)
        
        
        columns_width_icons = [ID_column_index, Link_Column_index, dokButton_column_index, dokAddress_column_index]
        column_widths = [0,10,10,0]
        resizes.setColumnWidths(table,columns_width_icons,column_widths)
        
        # Hide certain column labels
        #newLabel_Kataster = ""  # Replace with your actual column labels
        newLabel_Dokumendid = ""
        newLabel_Link = ""
        #contracts_model.setHorizontalHeaderItem(kataster_column_index, QStandardItem(newLabel_Kataster))
        contracts_model.setHorizontalHeaderItem(dokButton_column_index, QStandardItem(newLabel_Dokumendid))
        contracts_model.setHorizontalHeaderItem(Link_Column_index, QStandardItem(newLabel_Link))
        
            
        
class queryHandling:
    def __init__(self):
        self.header_id = header_id
        self.header_number = header_number
        self.header_name = header_name
        self.header_deadline =header_deadline
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
    def contracts_basic_data(self):
            # Set header labels
        header_labels = [header_number, header_name,  header_color,header_property_number, header_properties_icon,header_webLinkButton, header_Documents, header_file_path,  header_id, header_statuses]
#                            [header_id, header_number, 
#                            header_name, header_deadline,
#                            header_color, header_responsible,
#                            
#                            header_parent_id, header_webLinkButton, 
#                            header_Documents, header_file_path, 
#                            header_statuses]        # Assuming you have the Color column index in the header_labels list
        # Get projects 
        status_class = Statuses()  
        module_for_statuses = status_class.module_contracts
        state_for_statuses = status_class.state_open
        statuses = Statuses.by_module_and_state(self, module_for_statuses, state_for_statuses)
        
        #print("statuses")
        #print(statuses)

        data = ContractsQueries_list.query_contracts_by_status(self, statuses)
        #print("recived data is")
        #print(data)
        #data_count = len(data)
        # Build a pandas DataFrame
        df_data = []
        df = pd.DataFrame(df_data)
        for project_data in data:
            node = project_data.get("node", {})
            properties = node.get("properties", {}).get("edges", [])
            propertie_cadastralNr = [propertie["node"]["cadastralUnitNumber"] for propertie in properties]

            row_data = {
                    header_number: node.get("number", "") or "",
                    header_name: node.get("name", "") or "",
                    #'Tähtaeg': node.get("dueAt", "") or "",
                    header_statuses: node.get("status", {}).get("name", "") if node.get("status") else "",
                    header_color: node.get("status", {}).get("color", "") if node.get("status") else "",
                    header_property_number: ", ".join(propertie_cadastralNr) if propertie_cadastralNr else "",
                    header_properties_icon: "",
                    header_id: node.get("id", ""),
                    #'LP_ID': node.get("parentID", ""),
                    header_webLinkButton: "",
                    header_file_path: "",
                    header_Documents: node.get("filesPath","") if ("filePath") else "Dokumendid puuduvad",
                    #'Vastutav': ",".join(resposnisble_name) if resposnisble_name else ""
                }
            #print(f"row_data: '{row_data}'")
            
            df_data.append(row_data)    
        print("df_data")
        print(df_data)

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
        query_loader = Graphql_contracts()
        query = GraphQLQueryLoader.load_query_for_contracts(self,query_loader.Q_All_contracts)        
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
