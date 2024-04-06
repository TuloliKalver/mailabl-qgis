# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QTableView, QMessageBox
from ...MapTools.selector import visibleSelector
from ...projects_pandas import ProjectsWithPandas_2, ProjectsWithPandas_3, TableHeaders
from .....utils.delegates.DelegateMainTable import DelegatesForTables
from .....Functions.tableViewAdjust import ColumnResizer
from .....config.settings import SettingsDataSaveAndLoad
from .....utils.table_utilys import ModelHandler
from .....processes.infomessages.messages import Headings, HoiatusTexts
 
pealkiri = Headings()

class Projects:
    @staticmethod
    def load_mailabl_projects_list(table, status_value):
        #print(f"in 'load_Mailabl_projects_list(self, table, statusValue)': {statusValue}")
        pandas = ProjectsWithPandas_2()
        result = pandas.table_view_from_active_projects_statuses(status_value)

        if result is not None:
            p_model, header_labels = result

            if p_model.rowCount() == 0:
                text = HoiatusTexts().ostingu_tulemused_puuduvad
                heading = Headings().warningSimple
                print(f"{heading}, {text}")
                QMessageBox.information(None, heading, text)
            else:

                table_headers = TableHeaders()
                
                number_column_index = header_labels.index(table_headers.header_number)
                name_column_index = header_labels.index(table_headers.header_name)
                LP_ID_column_index = header_labels.index(table_headers.header_parent_id)
                responsible_column_index = header_labels.index(table_headers.header_responsible)        
                ID_column_index = header_labels.index(table_headers.header_id)

                for row_index in range(p_model.rowCount()):
                    p_model.item(row_index, ID_column_index)

                    number_item =  p_model.item(row_index, number_column_index)
                    responsible_item = p_model.item(row_index,responsible_column_index)   
                    
                    number_item.setTextAlignment(Qt.AlignCenter)  
                    responsible_item.setTextAlignment(Qt.AlignCenter)

                    date_column_index = ModelHandler.format_date_item(p_model, row_index, header_labels)

                    status_column_index, color_column_index = ModelHandler.set_status_item_colors_from_model(p_model, row_index, header_labels)
                    # Call format_cadastral_item method
                    cadastral_column_index, cadastralButton_Column_index = ModelHandler.format_cadastral_item(p_model, row_index, header_labels)
                    # Call format_dok_item method
                    dokAddress_column_index, dokButton_column_index = ModelHandler.format_dok_item(p_model, row_index, header_labels)
                    # Call build_mailabl_link_button method
                    webButton_Column_index = ModelHandler.build_mailabl_link_button(p_model, row_index, header_labels)


                DelegatesForTables.setup_delegates_standard_table(table, header_labels)

                table.setModel(p_model)
                # Set the row height to 20 pixels
                table.verticalHeader().setDefaultSectionSize(20)
                    
                # Define the columns to hide
                columns_to_hide = [color_column_index, LP_ID_column_index, dokAddress_column_index]
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
        layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        selected_features = visibleSelector.get_visible_features(layer_name)
        if len(selected_features) < 500:
                
            pandas = ProjectsWithPandas_3()
            table_headers = TableHeaders()
    
            result = pandas.Create_Project_tableView_for_zoom(selected_features)
            if result is not None:
                p_model, header_labels = result
                number_column_index = header_labels.index(table_headers.header_number)
                name_column_index = header_labels.index(table_headers.header_name)
                LP_ID_column_index = header_labels.index(table_headers.header_parent_id)
                responsible_column_index = header_labels.index(table_headers.header_responsible)        
                ID_column_index = header_labels.index(table_headers.header_id)

                for row_index in range(p_model.rowCount()):
                    p_model.item(row_index, ID_column_index)

                    number_item =  p_model.item(row_index, number_column_index)
                    responsible_item = p_model.item(row_index,responsible_column_index)   
                    
                    number_item.setTextAlignment(Qt.AlignCenter)  
                    responsible_item.setTextAlignment(Qt.AlignCenter)

                    date_column_index = ModelHandler.format_date_item(p_model, row_index, header_labels)

                    status_column_index, color_column_index = ModelHandler.set_status_item_colors_from_model(p_model, row_index, header_labels)
                    # Call format_cadastral_item method
                    cadastral_column_index, cadastralButton_Column_index = ModelHandler.format_cadastral_item(p_model, row_index, header_labels)
                    # Call format_dok_item method
                    dokAddress_column_index, dokButton_column_index = ModelHandler.format_dok_item(p_model, row_index, header_labels)
                    # Call build_mailabl_link_button method
                    webButton_Column_index = ModelHandler.build_mailabl_link_button(p_model, row_index, header_labels)


                DelegatesForTables.setup_delegates_standard_table(table, header_labels)


                table.setModel(p_model)
                # Set the row height to 20 pixels
                table.verticalHeader().setDefaultSectionSize(20)
                    
                # Define the columns to hide
                columns_to_hide = [color_column_index, LP_ID_column_index, dokAddress_column_index]
                # Hide the specified columns
                for column_index in columns_to_hide:
                    table.hideColumn(column_index)
                        
                resizes = ColumnResizer(table)
                columns_to_resize = [number_column_index, responsible_column_index, date_column_index, status_column_index]
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
            else:
                # Handle the case where no projects have been found
                print("No projects found.")

        else:
            text = ("Ala on projektide laadimiseks liiga suur\nZoomi lähemale")
            heading = pealkiri.warningSimple
            QMessageBox.warning(None, heading, text)
            return

class searchProjectsValue:
    @staticmethod
    def load_Mailabl_projects_by_number(project_number, table):
        pandas = ProjectsWithPandas_2()
        table_headers = TableHeaders()
        #p_model,header_labels = pandas.Create_Project_tableView_for_search(project_number)
        result = pandas.Create_Project_tableView_for_search(project_number)
        if result is not None:
            p_model, header_labels = result
            # Rest of your code using p_model and header_labels
        
            number_column_index = header_labels.index(table_headers.header_number)
            name_column_index = header_labels.index(table_headers.header_name)
            LP_ID_column_index = header_labels.index(table_headers.header_parent_id)
            responsible_column_index = header_labels.index(table_headers.header_responsible)        
            ID_column_index = header_labels.index(table_headers.header_id)

            for row_index in range(p_model.rowCount()):
                p_model.item(row_index, ID_column_index)

                number_item =  p_model.item(row_index, number_column_index)
                responsible_item = p_model.item(row_index,responsible_column_index)   
                
                number_item.setTextAlignment(Qt.AlignCenter)  
                responsible_item.setTextAlignment(Qt.AlignCenter)

                date_column_index = ModelHandler.format_date_item(p_model, row_index, header_labels)

                status_column_index, color_column_index = ModelHandler.set_status_item_colors_from_model(p_model, row_index, header_labels)
                # Call format_cadastral_item method
                cadastral_column_index, cadastralButton_Column_index = ModelHandler.format_cadastral_item(p_model, row_index, header_labels)
                # Call format_dok_item method
                dokAddress_column_index, dokButton_column_index = ModelHandler.format_dok_item(p_model, row_index, header_labels)
                # Call build_mailabl_link_button method
                webButton_Column_index = ModelHandler.build_mailabl_link_button(p_model, row_index, header_labels)


            DelegatesForTables.setup_delegates_standard_table(table, header_labels)



            table.setModel(p_model)
            # Set the row height to 20 pixels
            table.verticalHeader().setDefaultSectionSize(20)
                
            # Define the columns to hide
            columns_to_hide = [color_column_index, LP_ID_column_index, dokAddress_column_index]
            # Hide the specified columns
            for column_index in columns_to_hide:
                table.hideColumn(column_index)
                    
            resizes = ColumnResizer(table)
            columns_to_resize = [number_column_index,  responsible_column_index, date_column_index ,status_column_index]
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
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
            #QMessageBox.warning(None, heading, text)            
            # Handle the case when no projects are found
