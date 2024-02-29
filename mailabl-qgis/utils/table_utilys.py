# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon, QStandardItem
from ..Functions.tableViewAdjust import Colors
from ..config.iconHandler import iconHandler
from ..config.settings import Filepaths


class ModelHandler:
    @staticmethod
    def set_status_item_colors_from_model(item, model, row_index, color_column_index):
        """
        Sets the background and foreground colors of a QTableWidgetItem based on a color column in the model.
        
        Args:
            item (QTableWidgetItem): The item to set colors for.
            model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
            color_column_index (int): The index of the column containing color information.
        """
        if item:
            color_item = model.item(row_index, color_column_index)
            if color_item:
                color_code = color_item.text()
                if color_code:
                    rgb_color = Colors.hex_to_rgb(color_code)
                    background_color = QColor(*rgb_color)
                    foreground_color = QColor(Qt.black)  # Set foreground color to black
                    item.setBackground(background_color)
                    item.setForeground(foreground_color)
                    item.setTextAlignment(Qt.AlignCenter)
                    
                    
    @staticmethod
    def format_date_item(date_item):
        """
        Formats a date QTableWidgetItem to display in a specific format and applies conditional coloring.

        Args:
            date_item (QTableWidgetItem): The item containing the date to format.
        """
        if date_item:
            date_str = date_item.text()
            if date_str:
                original_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                formatted_date = original_date.strftime('%d.%m.%Y')
                date_item.setText(formatted_date)
                date_item.setTextAlignment(Qt.AlignCenter)
                
                # Apply conditional coloring
                if original_date < datetime.today().date():
                    # Set the text color to red
                    date_color = "#d24848"
                    rgb_color_date = Colors.hex_to_rgb(date_color)
                    date_item.setForeground(QColor(*rgb_color_date))
                    

    @staticmethod
    def format_cadastral_item(p_model, row_index, cadastral_column_index, cadastralButton_Column_index):
        """
        Formats a cadastral QTableWidgetItem and inserts an icon if necessary.

        Args:
            p_model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
            cadastral_column_index (int): The index of the column containing cadastral numbers.
            cadastralButton_Column_index (int): The index of the column where the icon should be inserted.
        """
        Cadastral_item = p_model.item(row_index, cadastral_column_index)
        if Cadastral_item:
            cadastral_number = Cadastral_item.text()
            if cadastral_number:
                pb_ShowCadasters = QStandardItem()
                text_color1 = QColor("#FFFFFF")  # White
                pb_ShowCadasters.setForeground(QBrush(text_color1))
                pb_ShowCadasters.setSelectable(True)
                pb_ShowCadasters.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)        
                # TODO: Solve icon centering!
                icon_path = ":/images/themes/default/mActionAdd3DMap.svg"
                icon = QIcon(icon_path)
                pb_ShowCadasters.setIcon(icon)
                p_model.setItem(row_index, cadastralButton_Column_index, pb_ShowCadasters)

    @staticmethod
    def format_dok_item(p_model, row_index, dokAddress_column_index, dokButton_column_index):
        """
        Formats a dok (document) QTableWidgetItem and inserts an icon if necessary.

        Args:
            p_model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
            dokAddress_column_index (int): The index of the column containing document addresses.
            dokButton_column_index (int): The index of the column where the icon should be inserted.
        """
        dokAddress_item = p_model.itemFromIndex(p_model.index(row_index, dokAddress_column_index))
        if dokAddress_item and dokAddress_item.data(Qt.DisplayRole):
            dokLink = dokAddress_item.data(Qt.DisplayRole)
            if dokLink:
                pb_dokLink = QStandardItem()
                pb_dokLink.setData("Ava", Qt.DisplayRole)
                pb_dokLink.setTextAlignment(Qt.AlignCenter)
                # TODO: Solve icon centering!
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
                # Add a button to each row in the 'Button' column (column dokButton_column_index)
                p_model.setItem(row_index, dokButton_column_index, pb_dokLink)

    @staticmethod
    def build_mailabl_link_button(p_model, row_index, webButton_Column_index):
        """
        Builds a mailabl link button QTableWidgetItem.

        Args:
            p_model (QStandardItemModel): The model containing the data.
            row_index (int): The index of the row in the model.
            webButton_Column_index (int): The index of the column where the button should be inserted.
        """
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
        # Add the mailabl link button to the model
        p_model.setItem(row_index, webButton_Column_index, pb_openInMailabl)

