# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module


from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon, QStandardItem
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QMessageBox
from .....app.Delegates.WebLink import WebLinkDelegate
from .....app.Delegates.OpenFile import FileDelegate
from .....app.Delegates.SelectMapElements import SelectMapElementsDelegate
from .....config.iconHandler import iconHandler
from .....config.settings import Filepaths
from ...projects_pandas import ProjectsWithPandas_2, ProjectsWithPandas_3, TableHeaders
from .....Functions.tableViewAdjust import ColumnResizer, Colors
from .....config.settings import SettingsDataSaveAndLoad
from ...MapTools.selector import visibleSelector



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
            color_item = p_model.item(row_index, color_column_index)
            status_item = p_model.item(row_index, status_column_index)
            Cadastral_item = p_model.item(row_index, cadastral_column_index)
            number_item =  p_model.item(row_index, number_column_index)
            date_item  = p_model.item(row_index, date_column_index)
            responsible_item = p_model.item(row_index,responsible_column_index)   
            
            number_item.setTextAlignment(Qt.AlignCenter)  
            responsible_item.setTextAlignment(Qt.AlignCenter)
            
            
            # input date string in the format 'YYYY-MM-DD'
            date_str = date_item.text()
            if date_str:
                original_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                if original_date < datetime.today().date():
                    #Set the text color to red
                    date_color = "#d24848"
                    rgb_color_date = Colors.hex_to_rgb(date_color)
                    date_item.setForeground(QColor(*rgb_color_date))

                formatted_date = original_date.strftime('%d.%m.%Y')
                date_item.setText(formatted_date)
                # Set alignment for date_item
                date_item.setTextAlignment(Qt.AlignCenter)
        # Iterate through the items in the 'Color' column and set background color                        
            if color_item:
                color_code = color_item.text()
                #styler.set_background_color(color_item, color_code)
                if color_code:
                    rgb_color = Colors.hex_to_rgb(color_code)
                    rgb_black = '#181a1c'
                    rgb_color_black = Colors.hex_to_rgb(rgb_black)
                    color = QColor(*rgb_color)
                    color_black = QColor(*rgb_color_black)
                    status_item.setBackground(color)
                    status_item.setForeground(color_black)
                    status_item.setTextAlignment(Qt.AlignCenter)
                    
            if Cadastral_item:
                cadastral_number = Cadastral_item.text()
                if cadastral_number:
                    pb_ShowCadasters = QStandardItem()
                    text_color1 = QColor("#FFFFFF")  # White
                    pb_ShowCadasters.setForeground(QBrush(text_color1))
                    pb_ShowCadasters.setSelectable(True)
                    pb_ShowCadasters.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)        
                #TODO solve icon centering!
                    icon_path = ":/images/themes/default/mActionAdd3DMap.svg"
                    icon = QIcon(icon_path)
                    pb_ShowCadasters.setIcon(icon)
                    p_model.setItem(row_index, cadastralButton_Column_index, pb_ShowCadasters)

            dokAddress_index = p_model.index(row_index, dokAddress_column_index)
            dokAddress_item = p_model.itemFromIndex(dokAddress_index)
            
            if dokAddress_item and dokAddress_item.data(Qt.DisplayRole):
                dokLink = dokAddress_item.data(Qt.DisplayRole)
                #print(f"dok Link {dokLink}")
                if dokLink:
                    pb_dokLink = QStandardItem()
                    pb_dokLink.setData("Ava", Qt.DisplayRole)
                    pb_dokLink.setTextAlignment(Qt.AlignCenter)
                    #TODO solve icon centering!
                    folder_icon_path = iconHandler.setIcon(dokLink)
                    icon = QIcon(folder_icon_path)
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
                    p_model.setItem(row_index, dokButton_column_index, pb_dokLink)
            
            
        #Build mailabl link button and set icon.
            pb_openInMailabl = QStandardItem()
            pb_openInMailabl.setData("Ava", Qt.DisplayRole)
            pb_openInMailabl.setTextAlignment(Qt.AlignCenter)
            folder_icon_path = Filepaths.Mailabl_icon()
            icon = QIcon(folder_icon_path)
            pb_openInMailabl.setIcon(icon)
            background_color = QColor("#40414f")  
            pb_openInMailabl.setBackground(QBrush(background_color))
        # Set the foreground color (text color) to a contrasting color
            text_color = QColor("#FFFFFF")  # White
            pb_openInMailabl.setForeground(QBrush(text_color))
        # Make the cell selectable and give it a raised effect
            pb_openInMailabl.setSelectable(True)
            pb_openInMailabl.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            p_model.setItem(row_index, webButton_Column_index, pb_openInMailabl)

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
                    color_item = p_model.item(row_index, color_column_index)
                    status_item = p_model.item(row_index, status_column_index)
                    number_item =  p_model.item(row_index, number_column_index)
                    date_item  = p_model.item(row_index, date_column_index)
                    responsible_item = p_model.item(row_index,responsible_column_index)   
                    
                    number_item.setTextAlignment(Qt.AlignCenter)  
                    responsible_item.setTextAlignment(Qt.AlignCenter)
                    
                    # input date string in the format 'YYYY-MM-DD'
                    date_str = date_item.text()
                    if date_str:
                        original_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                        if original_date < datetime.today().date():
                            #Set the text color to red
                            date_color = "#d24848"
                            rgb_color_date = Colors.hex_to_rgb(date_color)
                            date_item.setForeground(QColor(*rgb_color_date))

                        formatted_date = original_date.strftime('%d.%m.%Y')
                        date_item.setText(formatted_date)
                        # Set alignment for date_item
                        date_item.setTextAlignment(Qt.AlignCenter)
                # Iterate through the items in the 'Color' column and set background color                        
                    if color_item:
                        color_code = color_item.text()
                        #styler.set_background_color(color_item, color_code)
                        if color_code:
                            rgb_color = Colors.hex_to_rgb(color_code)
                            rgb_black = '#181a1c'
                            rgb_color_black = Colors.hex_to_rgb(rgb_black)
                            color = QColor(*rgb_color)
                            color_black = QColor(*rgb_color_black)
                            status_item.setBackground(color)
                            status_item.setForeground(color_black)
                            status_item.setTextAlignment(Qt.AlignCenter)
                            
                    pb_ShowCadasters = QStandardItem()
                    text_color1 = QColor("#FFFFFF")  # White
                    pb_ShowCadasters.setForeground(QBrush(text_color1))
                    pb_ShowCadasters.setSelectable(True)
                    pb_ShowCadasters.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)        
                    icon_path = ":/images/themes/default/mActionAdd3DMap.svg"
                    icon = QIcon(icon_path)
                    pb_ShowCadasters.setIcon(icon)
                    p_model.setItem(row_index, cadastralButton_Column_index, pb_ShowCadasters)

                    dokAddress_index = p_model.index(row_index, dokAddress_column_index)
                    dokAddress_item = p_model.itemFromIndex(dokAddress_index)
                    
                    if dokAddress_item and dokAddress_item.data(Qt.DisplayRole):
                        dokLink = dokAddress_item.data(Qt.DisplayRole)
                        print(f"dok Link {dokLink}")
                        if dokLink:
                            pb_dokLink = QStandardItem()
                            pb_dokLink.setData("Ava", Qt.DisplayRole)
                            pb_dokLink.setTextAlignment(Qt.AlignCenter)
                            folder_icon_path = iconHandler.setIcon(dokLink)
                            icon = QIcon(folder_icon_path)
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
                            p_model.setItem(row_index, dokButton_column_index, pb_dokLink)
                    
                    
                #Build mailabl link button and set icon.
                    pb_openInMailabl = QStandardItem()
                    pb_openInMailabl.setData("Ava", Qt.DisplayRole)
                    pb_openInMailabl.setTextAlignment(Qt.AlignCenter)
                    folder_icon_path = Filepaths.Mailabl_icon()
                    icon = QIcon(folder_icon_path)
                    pb_openInMailabl.setIcon(icon)
                    background_color = QColor("#40414f")  
                    pb_openInMailabl.setBackground(QBrush(background_color))
                # Set the foreground color (text color) to a contrasting color
                    text_color = QColor("#FFFFFF")  # White
                    pb_openInMailabl.setForeground(QBrush(text_color))
                # Make the cell selectable and give it a raised effect
                    pb_openInMailabl.setSelectable(True)
                    pb_openInMailabl.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    p_model.setItem(row_index, webButton_Column_index, pb_openInMailabl)

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
            color_item = p_model.item(row_index, color_column_index)
            status_item = p_model.item(row_index, status_column_index)
            Cadastral_item = p_model.item(row_index, cadastral_column_index)
            number_item =  p_model.item(row_index, number_column_index)
            date_item  = p_model.item(row_index, date_column_index)
            responsible_item = p_model.item(row_index,responsible_column_index)   
            
            number_item.setTextAlignment(Qt.AlignCenter)  
            responsible_item.setTextAlignment(Qt.AlignCenter)
            
            
            # input date string in the format 'YYYY-MM-DD'
            date_str = date_item.text()
            if date_str:
                original_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                if original_date < datetime.today().date():
                    #Set the text color to red
                    date_color = "#d24848"
                    rgb_color_date = Colors.hex_to_rgb(date_color)
                    date_item.setForeground(QColor(*rgb_color_date))

                formatted_date = original_date.strftime('%d.%m.%Y')
                date_item.setText(formatted_date)
                # Set alignment for date_item
                date_item.setTextAlignment(Qt.AlignCenter)
        # Iterate through the items in the 'Color' column and set background color                        
            if color_item:
                color_code = color_item.text()
                #styler.set_background_color(color_item, color_code)
                if color_code:
                    rgb_color = Colors.hex_to_rgb(color_code)
                    rgb_black = '#181a1c'
                    rgb_color_black = Colors.hex_to_rgb(rgb_black)
                    color = QColor(*rgb_color)
                    color_black = QColor(*rgb_color_black)
                    status_item.setBackground(color)
                    status_item.setForeground(color_black)
                    status_item.setTextAlignment(Qt.AlignCenter)
                    
            if Cadastral_item:
                cadastral_number = Cadastral_item.text()
                if cadastral_number:
                    pb_ShowCadasters = QStandardItem()
                    text_color1 = QColor("#FFFFFF")  # White
                    pb_ShowCadasters.setForeground(QBrush(text_color1))
                    pb_ShowCadasters.setSelectable(True)
                    pb_ShowCadasters.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)        
                #TODO solve icon centering!
                    icon_path = ":/images/themes/default/mActionAdd3DMap.svg"
                    icon = QIcon(icon_path)
                    pb_ShowCadasters.setIcon(icon)
                    p_model.setItem(row_index, cadastralButton_Column_index, pb_ShowCadasters)

            dokAddress_index = p_model.index(row_index, dokAddress_column_index)
            dokAddress_item = p_model.itemFromIndex(dokAddress_index)
            
            if dokAddress_item and dokAddress_item.data(Qt.DisplayRole):
                dokLink = dokAddress_item.data(Qt.DisplayRole)
                #print(f"dok Link {dokLink}")
                if dokLink:
                    pb_dokLink = QStandardItem()
                    pb_dokLink.setData("Ava", Qt.DisplayRole)
                    pb_dokLink.setTextAlignment(Qt.AlignCenter)
                    #TODO solve icon centering!
                    folder_icon_path = iconHandler.setIcon(dokLink)
                    icon = QIcon(folder_icon_path)
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
                    p_model.setItem(row_index, dokButton_column_index, pb_dokLink)
            
            
        #Build mailabl link button and set icon.
            pb_openInMailabl = QStandardItem()
            pb_openInMailabl.setData("Ava", Qt.DisplayRole)
            pb_openInMailabl.setTextAlignment(Qt.AlignCenter)
            folder_icon_path = Filepaths.Mailabl_icon()
            icon = QIcon(folder_icon_path)
            pb_openInMailabl.setIcon(icon)
            background_color = QColor("#40414f")  
            pb_openInMailabl.setBackground(QBrush(background_color))
        # Set the foreground color (text color) to a contrasting color
            text_color = QColor("#FFFFFF")  # White
            pb_openInMailabl.setForeground(QBrush(text_color))
        # Make the cell selectable and give it a raised effect
            pb_openInMailabl.setSelectable(True)
            pb_openInMailabl.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            p_model.setItem(row_index, webButton_Column_index, pb_openInMailabl)

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
