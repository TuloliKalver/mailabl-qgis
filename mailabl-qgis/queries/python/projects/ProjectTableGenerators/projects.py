# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon, QStandardItem
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QMessageBox
from .....app.Delegates.WebLink import WebLinkDelegate
from .....app.Delegates.OpenFile import FileDelegate
from .....app.Delegates.SelectMapElements import SelectMapElementsDelegate
from ...projects_pandas import ProjectsWithPandas_2, ProjectsWithPandas_3, TableHeaders
from .....Functions.tableViewAdjust import ColumnResizer
from .....config.settings import SettingsDataSaveAndLoad
from ...MapTools.selector import visibleSelector
from .....utils.table_utilys import ModelHandler



class Projects:
    @staticmethod
    def load_mailabl_projects_list(table, statusValue):
        #print(f"in 'load_Mailabl_projects_list(self, table, statusValue)': {statusValue}")
        pandas = ProjectsWithPandas_2()
        table_headers = TableHeaders()
        p_model,header_labels = pandas.table_view_from_active_projects_statuses(statusValue)
        
        number_column_index = header_labels.index(table_headers.header_number)
        name_column_index = header_labels.index(table_headers.header_name)
        date_column_index = header_labels.index(table_headers.header_deadline)
        color_column_index = header_labels.index(table_headers.header_color)
        status_column_index = header_labels.index(table_headers.header_statuses)
        ID_column_index = header_labels.index(table_headers.header_id)
        LP_ID_column_index = header_labels.index(table_headers.header_parent_id)
        cadastral_column_index = header_labels.index(table_headers.header_property_number)
        responsible_column_index = header_labels.index(table_headers.header_responsible)
        dokAddress_column_index = header_labels.index(table_headers.header_documents)
        dokButton_column_index = header_labels.index(table_headers.header_file_path)
        webButton_Column_index = header_labels.index(table_headers.header_web_link_button)
        cadastralButton_Column_index = header_labels.index(table_headers.header_properties_icon)
        

        for row_index in range(p_model.rowCount()):
            p_model.item(row_index, ID_column_index)

            number_item =  p_model.item(row_index, number_column_index)
            date_item  = p_model.item(row_index, date_column_index)
            responsible_item = p_model.item(row_index,responsible_column_index)   
            
            number_item.setTextAlignment(Qt.AlignCenter)  
            responsible_item.setTextAlignment(Qt.AlignCenter)

            date_item = p_model.item(row_index, date_column_index)
            ModelHandler.format_date_item(date_item)
            status_item = p_model.item(row_index, status_column_index)
            ModelHandler.set_status_item_colors_from_model(status_item, p_model, row_index, color_column_index)
            # Call format_cadastral_item method
            ModelHandler.format_cadastral_item(p_model, row_index, cadastral_column_index, cadastralButton_Column_index)
            # Call format_dok_item method
            ModelHandler.format_dok_item(p_model, row_index, dokAddress_column_index, dokButton_column_index)
            # Call build_mailabl_link_button method
            ModelHandler.build_mailabl_link_button(p_model, row_index, webButton_Column_index)


        # Set the custom delegate for the web link column
        web_link_delegate = WebLinkDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(webButton_Column_index, web_link_delegate)

        # Set the custom delegate for the file column
        file_delegate = FileDelegate(dokAddress_column_index, table)
        table.setItemDelegateForColumn(dokButton_column_index, file_delegate)

        show_onMap_delegate = SelectMapElementsDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)


        table.setModel(p_model)
        # Set the row height to 20 pixels
        table.verticalHeader().setDefaultSectionSize(20)
            
        # Define the columns to hide
        columns_to_hide = [color_column_index, LP_ID_column_index, dokAddress_column_index]
        # Hide the specified columns
        for column_index in columns_to_hide:
            table.hideColumn(column_index)
                
        resizes = ColumnResizer(table)
        columns_to_resize = [number_column_index, name_column_index, status_column_index]
        for column_index in columns_to_resize:
            resizes.resizeColumnByIndex(table, column_index)
            
        columns_width_icons = [ID_column_index, cadastral_column_index,
                            webButton_Column_index, dokButton_column_index, 
                            cadastralButton_Column_index]
        column_widths = [0,0,10,10,10]
        resizes.setColumnWidths(table, columns_width_icons, column_widths)
        # Hide certain column labels
        newLabel_for_cadastral = ""  # Replace with your actual column labels
        newLabel_documents = ""
        newLabel_Link = ""
        newLabel_ID = ""
        newLabel_CadastralShow = ""
        p_model.setHorizontalHeaderItem(ID_column_index, QStandardItem(newLabel_ID))
        p_model.setHorizontalHeaderItem(cadastral_column_index, QStandardItem(newLabel_for_cadastral))
        p_model.setHorizontalHeaderItem(dokButton_column_index, QStandardItem(newLabel_documents))
        p_model.setHorizontalHeaderItem(webButton_Column_index, QStandardItem(newLabel_Link))
        p_model.setHorizontalHeaderItem(cadastralButton_Column_index, QStandardItem(newLabel_CadastralShow))
        table.verticalHeader().setVisible(False)
        # Set selection behavior to select entire rows
        table.setSelectionBehavior(QTableView.SelectRows)
        # Set selection mode to single selection
        table.setSelectionMode(QTableView.SingleSelection)

        # Set sorting behavior
        table.setSortingEnabled(True)
        # Trigger a refresh of the view to reflect the changes
        table.update()  # Refresh the view


class projectsTableDecorator:
    @staticmethod
    def load_Mailabl_projects_list_with_zoomed_map_elements(table):
        load = SettingsDataSaveAndLoad()
        layer_name = load.load_target_cadastral_name()
        selected_features = visibleSelector.get_visible_features(layer_name)
        if len(selected_features) < 500:
                
            pandas = ProjectsWithPandas_3()
            header = TableHeaders()
            result = pandas.Create_Project_tableView_for_zoom(selected_features)
            if result is not None:
                p_model, header_labels = result
                
                number_column_index = header_labels.index(header.header_number)
                name_column_index = header_labels.index(header.header_name)
                date_column_index = header_labels.index(header.header_deadline)
                color_column_index = header_labels.index(header.header_color)
                status_column_index = header_labels.index(header.header_statuses)
                ID_column_index = header_labels.index(header.header_id)
                LP_ID_column_index = header_labels.index(header.header_parent_id)
                responsible_column_index = header_labels.index(header.header_responsible)
                dokAddress_column_index = header_labels.index(header.header_documents)
                dokButton_column_index = header_labels.index(header.header_file_path)
                print(f"dok button index: {dokButton_column_index}")
                webButton_Column_index = header_labels.index(header.header_web_link_button)
                print(f"webButton: {webButton_Column_index}")
                cadastralButton_Column_index = header_labels.index(header.header_properties_icon)
                print(f"cadastralbutton: {cadastralButton_Column_index}")
                

                for row_index in range(p_model.rowCount()):
                    p_model.item(row_index, ID_column_index)
                    number_item =  p_model.item(row_index, number_column_index)
                    responsible_item = p_model.item(row_index,responsible_column_index)   
                    
                    number_item.setTextAlignment(Qt.AlignCenter)  
                    responsible_item.setTextAlignment(Qt.AlignCenter)
                    
                    date_item = p_model.item(row_index, date_column_index)
                    ModelHandler.format_date_item(date_item)
                
                    status_item = p_model.item(row_index, status_column_index)
                    ModelHandler.set_status_item_colors_from_model(status_item, p_model, row_index, color_column_index)
            
                    pb_ShowCadasters = QStandardItem()
                    text_color1 = QColor("#FFFFFF")  # White
                    pb_ShowCadasters.setForeground(QBrush(text_color1))
                    pb_ShowCadasters.setSelectable(True)
                    pb_ShowCadasters.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)        
                    icon_path = ":/images/themes/default/mActionAdd3DMap.svg"
                    icon = QIcon(icon_path)
                    pb_ShowCadasters.setIcon(icon)
                    p_model.setItem(row_index, cadastralButton_Column_index, pb_ShowCadasters)
        
                    # Call format_dok_item method
                    ModelHandler.format_dok_item(p_model, row_index, dokAddress_column_index, dokButton_column_index)                    
                    # Call build_mailabl_link_button method
                    ModelHandler.build_mailabl_link_button(p_model, row_index, webButton_Column_index)

                # Set the custom delegate for the web link column
                web_link_delegate = WebLinkDelegate(ID_column_index, table)
                print(f"webButton_Column_index: {webButton_Column_index}")
                table.setItemDelegateForColumn(webButton_Column_index, web_link_delegate)

                # Set the custom delegate for the file column
                file_delegate = FileDelegate(dokAddress_column_index, table)
                table.setItemDelegateForColumn(dokButton_column_index, file_delegate)

                show_onMap_delegate = SelectMapElementsDelegate(ID_column_index, table)
                table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)


                table.setModel(p_model)
                # Set the row height to 20 pixels
                table.verticalHeader().setDefaultSectionSize(20)
                    
                # Define the columns to hide
                columns_to_hide = [color_column_index] #, dokAddress_column_index, LP_ID_column_index
                # Hide the specified columns
                for column_index in columns_to_hide:
                    table.hideColumn(column_index)
                        
                resizes = ColumnResizer(table)
                columns_to_resize = [number_column_index, name_column_index, status_column_index]
                for column_index in columns_to_resize:
                    resizes.resizeColumnByIndex(table, column_index)
                    
                columns_width_icons = [ID_column_index, #cadastral_column_index,
                                    webButton_Column_index, dokButton_column_index, 
                                    cadastralButton_Column_index]
                column_widths = [0,0,20,10]
                resizes.setColumnWidths(table, columns_width_icons , column_widths) #columns_width_icons,
                # Hide certain column labels
                newLabel_for_cadastral = ""  # Replace with your actual column labels
                newLabel_documents = ""
                newLabel_Link = ""
                newLabel_ID = ""
                newLabel_CadastralShow = ""
                p_model.setHorizontalHeaderItem(ID_column_index, QStandardItem(newLabel_ID))
                #p_model.setHorizontalHeaderItem(cadastral_column_index, QStandardItem(newLabel_for_cadastral))
                p_model.setHorizontalHeaderItem(dokButton_column_index, QStandardItem(newLabel_documents))
                p_model.setHorizontalHeaderItem(webButton_Column_index, QStandardItem(newLabel_Link))
                p_model.setHorizontalHeaderItem(cadastralButton_Column_index, QStandardItem(newLabel_CadastralShow))
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
                # Handle the case where no projects have been found
                print("No projects found.")

        else:
            text = ("Ala on projektide laadimiseks liiga suur\nZoomi lähemale")
            heading = "Hoiatus"
            QMessageBox.warning(None, heading, text)
            return

class searchProjectsValue:
    @staticmethod
    def load_Mailabl_projects_by_number(project_number, table):
        pandas = ProjectsWithPandas_2()
        header = TableHeaders()
        p_model,header_labels = pandas.Create_Project_tableView_for_search(project_number)
        
        number_column_index = header_labels.index(header.header_number)
        name_column_index = header_labels.index(header.header_name)
        date_column_index = header_labels.index(header.header_deadline)
        color_column_index = header_labels.index(header.header_color)
        status_column_index = header_labels.index(header.header_statuses)
        ID_column_index = header_labels.index(header.header_id)
        LP_ID_column_index = header_labels.index(header.header_parent_id)
        cadastral_column_index = header_labels.index(header.header_property_number)
        responsible_column_index = header_labels.index(header.header_responsible)
        dokAddress_column_index = header_labels.index(header.header_documents)
        dokButton_column_index = header_labels.index(header.header_file_path)
        webButton_Column_index = header_labels.index(header.header_web_link_button)
        cadastralButton_Column_index = header_labels.index(header.header_properties_icon)
        

        for row_index in range(p_model.rowCount()):
            p_model.item(row_index, ID_column_index)
            number_item =  p_model.item(row_index, number_column_index)
            responsible_item = p_model.item(row_index,responsible_column_index)   
            
            number_item.setTextAlignment(Qt.AlignCenter)  
            responsible_item.setTextAlignment(Qt.AlignCenter)
        
            date_item = p_model.item(row_index, date_column_index)
            ModelHandler.format_date_item(date_item)
            status_item = p_model.item(row_index, status_column_index)
            ModelHandler.set_status_item_colors_from_model(status_item, p_model, row_index, color_column_index)
            # Call format_cadastral_item method
            ModelHandler.format_cadastral_item(p_model, row_index, cadastral_column_index, cadastralButton_Column_index)
            # Call format_dok_item method
            ModelHandler.format_dok_item(p_model, row_index, dokAddress_column_index, dokButton_column_index)
            # Call build_mailabl_link_button method
            ModelHandler.build_mailabl_link_button(p_model, row_index, webButton_Column_index)

        # Set the custom delegate for the web link column
        web_link_delegate = WebLinkDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(webButton_Column_index, web_link_delegate)

        # Set the custom delegate for the file column
        file_delegate = FileDelegate(dokAddress_column_index, table)
        table.setItemDelegateForColumn(dokButton_column_index, file_delegate)

        show_onMap_delegate = SelectMapElementsDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)


        table.setModel(p_model)
        # Set the row height to 20 pixels
        table.verticalHeader().setDefaultSectionSize(20)
            
        # Define the columns to hide
        columns_to_hide = [color_column_index, LP_ID_column_index, dokAddress_column_index]
        # Hide the specified columns
        for column_index in columns_to_hide:
            table.hideColumn(column_index)
                
        resizes = ColumnResizer(table)
        columns_to_resize = [number_column_index, name_column_index, status_column_index]
        for column_index in columns_to_resize:
            resizes.resizeColumnByIndex(table, column_index)
            
        columns_width_icons = [ID_column_index, cadastral_column_index,
                            webButton_Column_index, dokButton_column_index, 
                            cadastralButton_Column_index]
        column_widths = [0,0,10,10,10]
        resizes.setColumnWidths(table, columns_width_icons, column_widths)
        # Hide certain column labels
        newLabel_for_cadastral = ""  # Replace with your actual column labels
        newLabel_documents = ""
        newLabel_Link = ""
        newLabel_ID = ""
        newLabel_CadastralShow = ""
        p_model.setHorizontalHeaderItem(ID_column_index, QStandardItem(newLabel_ID))
        p_model.setHorizontalHeaderItem(cadastral_column_index, QStandardItem(newLabel_for_cadastral))
        p_model.setHorizontalHeaderItem(dokButton_column_index, QStandardItem(newLabel_documents))
        p_model.setHorizontalHeaderItem(webButton_Column_index, QStandardItem(newLabel_Link))
        p_model.setHorizontalHeaderItem(cadastralButton_Column_index, QStandardItem(newLabel_CadastralShow))
        table.verticalHeader().setVisible(False)
        # Set selection behavior to select entire rows
        table.setSelectionBehavior(QTableView.SelectRows)
        # Set selection mode to single selection
        table.setSelectionMode(QTableView.SingleSelection)

        # Set sorting behavior
        table.setSortingEnabled(True)
        # Trigger a refresh of the view to reflect the changes
        table.update()  # Refresh the view