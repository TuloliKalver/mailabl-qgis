# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon, QStandardItem
from ..queries.python.projects_pandas import TableHeaders
from ..Functions.tableViewAdjust import Colors
from ..config.iconHandler import iconHandler
from ..config.settings import Filepaths, IconsByName
table_headers = TableHeaders()

class ModelHandler:
    @staticmethod
    def set_status_item_colors_from_model(p_model, row_index, headers):
        """
        Sets the background and foreground colors of a QTableWidgetItem based on a color column in the model.
        
        Args:
            item (QTableWidgetItem): The item to set colors for.
            model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
            color_column_index (int): The index of the column containing color information.
    """
        status_column_index = headers.index(table_headers.header_statuses)
        color_column_index = headers.index(table_headers.header_color)
        status_item = p_model.item(row_index, status_column_index)
        if status_item:
            color_item = p_model.item(row_index, color_column_index)
            if color_item:
                color_code = color_item.text()
                if color_code:
                    rgb_color = Colors.hex_to_rgb(color_code)
                    background_color = QColor(*rgb_color)
                    foreground_color = QColor(Qt.black)  # Set foreground color to black
                    status_item.setBackground(background_color)
                    status_item.setForeground(foreground_color)
                    status_item.setTextAlignment(Qt.AlignCenter)
                    
        return status_column_index, color_column_index
                                        
    @staticmethod
    def format_date_item(p_model, row_index, headers):
        """
        Formats a date QTableWidgetItem to display in a specific format and applies conditional coloring.

        Args:
            date_item (QTableWidgetItem): The item containing the date to format.
        """
        date_column_index = headers.index(table_headers.header_deadline)
        date_item  = p_model.item(row_index, date_column_index)
        
        if date_item:
            date_str = date_item.text()
            #print(date_str)
            if date_str:
                original_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                formated_date = original_date.strftime('%d.%m.%Y')
                date_item.setText(formated_date)
                date_item.setTextAlignment(Qt.AlignCenter)
                
                # Apply conditional coloring
                if original_date < datetime.today().date():
                    # Set the text color to red
                    date_color = "#d24848"
                    rgb_color_date = Colors.hex_to_rgb(date_color)
                    date_item.setForeground(QColor(*rgb_color_date))
                    
        return date_column_index

    @staticmethod
    def format_cadastral_item(p_model, row_index, headers):
        """
        Formats a cadastral QTableWidgetItem and inserts an icon if necessary.

        Args:
            p_model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
            cadastral_column_index (int): The index of the column containing cadastral numbers.
            cadastralButton_Column_index (int): The index of the column where the icon should be inserted.
        """
        cadastral_column_index = headers.index(table_headers.header_property_number)
        cadastralButton_Column_index = headers.index(table_headers.header_properties_icon)
        Cadastral_item = p_model.item(row_index, cadastral_column_index)
        if Cadastral_item:
            cadastral_number = Cadastral_item.text()
            if cadastral_number:
                pb_ShowCadasters = QStandardItem()
                text_color1 = QColor("#FFFFFF")  # White
                pb_ShowCadasters.setForeground(QBrush(text_color1))
                pb_ShowCadasters.setSelectable(True)
                pb_ShowCadasters.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)        
                icon_path = Filepaths.get_icon(IconsByName().icon_show_on_map)
                print(icon_path)
                icon = QIcon(icon_path)
                pb_ShowCadasters.setIcon(icon)
                pb_ShowCadasters.setToolTip("Näita kaardil")  # Set tooltip text
                p_model.setItem(row_index, cadastralButton_Column_index, pb_ShowCadasters)
        
        return cadastral_column_index, cadastralButton_Column_index

    @staticmethod
    def format_dok_item(p_model, row_index, headers):
        """
        Formats a dok (document) QTableWidgetItem and inserts an icon if necessary.

        Args:
            p_model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
            dokAddress_column_index (int): The index of the column containing document addresses.
            dokButton_column_index (int): The index of the column where the icon should be inserted.
        """
        
        dokAddress_column_index = headers.index(table_headers.header_documents)
        dokButton_column_index = headers.index(table_headers.header_file_path)
        dokAddress_item = p_model.itemFromIndex(p_model.index(row_index, dokAddress_column_index))
        if dokAddress_item and dokAddress_item.data(Qt.DisplayRole):
            dokLink = dokAddress_item.data(Qt.DisplayRole)
            if dokLink:
                pb_dokLink = QStandardItem()
                pb_dokLink.setData("Ava", Qt.DisplayRole)
                pb_dokLink.setTextAlignment(Qt.AlignCenter)
                folder_icon_path = iconHandler.set_document_icon_based_on_item(dokLink)
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
                pb_dokLink.setToolTip("Ava dokument")  # Set tooltip text
                # Add a button to each row in the 'Button' column (column dokButton_column_index)
                p_model.setItem(row_index, dokButton_column_index, pb_dokLink)
                
        return dokAddress_column_index, dokButton_column_index

    @staticmethod
    def build_mailabl_link_button(p_model, row_index, headers):
        """
        Builds a mailabl link button QTableWidgetItem.

        Args:
            p_model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
        """
        # Extract column index from header labels
        webButton_Column_index = headers.index(table_headers.header_web_link_button)
        pb_openInMailabl = QStandardItem()
        pb_openInMailabl.setData("Ava", Qt.DisplayRole)
        pb_openInMailabl.setTextAlignment(Qt.AlignCenter)
        # Get the path of the Mailabl icon
        icon_path = Filepaths.get_icon(IconsByName().Mailabl_icon_name)
        #print(icon_path)
        icon = QIcon(icon_path)
        pb_openInMailabl.setIcon(icon)
        background_color = QColor("#40414f")
        pb_openInMailabl.setBackground(QBrush(background_color))
        # Set the foreground color (text color) to a contrasting color
        text_color = QColor("#FFFFFF")  # White
        pb_openInMailabl.setForeground(QBrush(text_color))
        # Make the cell selectable and give it a raised effect
        pb_openInMailabl.setSelectable(True)
        pb_openInMailabl.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        pb_openInMailabl.setToolTip("Ava Mailablis detailsema info saamiseks")  # Set tooltip text
        # Add the mailabl link button to the model
        p_model.setItem(row_index, webButton_Column_index, pb_openInMailabl)

        return webButton_Column_index
    
class TableExtractor:
    def __init__(self) -> None:

        pass

    @staticmethod
    def table_header_extractor(table):
        table_headers = []
        model = table.model()
        if model is not None:
            for column in range(model.columnCount()):
                header_label = model.headerData(column, Qt.Horizontal, Qt.DisplayRole)
                table_headers.append(header_label)
        return table_headers

    @staticmethod
    def value_from_selected_row_by_column(table, index) -> str: 
        model = table.model()
        selection_model = table.selectionModel()
        value_text = "" #set standard value if empty

        if selection_model.hasSelection():
            selected_index = selection_model.currentIndex()
            value = model.item(selected_index.row(), index)
            if value is not None:
                value_text = value.text()
        return value_text
    
    @staticmethod
    def values_from_selected_row_by_columns(table, indexes) -> str:
        model = table.model()
        selection_model = table.selectionModel()
        values = []

        if selection_model.hasSelection():
            selected_index = selection_model.currentIndex()
            for index in indexes:
                if 0 <= index < model.columnCount():
                    value = model.item(selected_index.row(), index)
                    if value is not None:
                        values.append(value.text())
        return ", ".join(values)