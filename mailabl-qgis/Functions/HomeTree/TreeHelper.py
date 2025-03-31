import subprocess
import webbrowser  # For opening links in browser
import requests
from qgis.core import QgsSettings
from PyQt5.QtGui import QIcon, QColor, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from ...utils.ColorHelper import ColorUtils
from ...KeelelisedMuutujad.modules import Module
from ...config.settings import Filepaths, IconsByName
from ...config.iconHandler import iconHandler
from ...config.settings import MailablWebModules, OpenLink
from ...config.ui_directories import PathLoader, plugin_dir_path, UI_multiline_Statusbar


paths = PathLoader(plugin_dir_path, UI_multiline_Statusbar)

class TreeHelper:

    @staticmethod
    def set_status_color(status_item, color_code):
        if color_code:
            try:                    
                rgb_color = ColorUtils.hex_to_rgb(color_code)
                background_color = QColor(*rgb_color)
                foreground_color = QColor(Qt.black)  # Set foreground color to black
                status_item.setBackground(background_color)
                status_item.setForeground(foreground_color)
                status_item.setTextAlignment(Qt.AlignCenter)
            except Exception as e:
                print(f"Error in setting color: {e}")

    @staticmethod
    def set_clickable_webIcon(item_or_row, column=None):
        icon_path = Filepaths.get_icon(IconsByName().Mailabl_icon_name)
        icon = QIcon(icon_path)

        # Case 1: QTreeWidgetItem
        if column is not None and hasattr(item_or_row, 'setIcon'):
            item_or_row.setIcon(column, icon)
            item_or_row.setText(column, "")
            item_or_row.setFlags(item_or_row.flags() | Qt.ItemIsSelectable)

        # Case 2: QStandardItem (TreeView)
        elif isinstance(item_or_row, QStandardItem):
            item_or_row.setIcon(icon)
            item_or_row.setText("")
            item_or_row.setFlags(item_or_row.flags() | Qt.ItemIsSelectable)

    @staticmethod
    def open_in_web_brauser(source, col_or_index):
        # TreeView case (QStandardItemModel + QModelIndex)
        if isinstance(source, QStandardItemModel):
            index = col_or_index
            if index.column() == 3:
                model = source
                item = model.itemFromIndex(index)
                if item:
                    module = item.data(Qt.UserRole)
                    if module:
                        module = module.lower() + 's'
                    # Column 2 holds the ID
                    id_index = index.sibling(index.row(), 2)
                    link_id = id_index.data()
                    if not link_id:
                        return

                    web_module = MailablWebModules().get_web_link(module)
                    web_link = OpenLink.weblink_by_module(web_module)
                    link = f"{web_link}{link_id}"
                    response = requests.get(link, verify=False)
                    webbrowser.open(response.url)

        # TreeWidget case (QTreeWidgetItem)
        else:
            item = source
            column = col_or_index
            if column == 3:
                module = item.data(column, Qt.UserRole)
                if module:
                    module = module.lower() + 's'
                link_id = item.text(2)
                if not link_id:
                    return

                web_module = MailablWebModules().get_web_link(module)
                web_link = OpenLink.weblink_by_module(web_module)
                link = f"{web_link}{link_id}"
                response = requests.get(link, verify=False)
                webbrowser.open(response.url)

    @staticmethod
    def set_clickable_folderIcon(item_or_row, column=None):
        dok_path = item_or_row.data(Qt.UserRole) if isinstance(item_or_row, QStandardItem) else item_or_row.data(column, Qt.UserRole)
        
        if dok_path:
            icon_path = iconHandler.set_document_icon_based_on_item(dok_path)
            icon = QIcon(icon_path)

            if isinstance(item_or_row, QStandardItem):
                item_or_row.setIcon(icon)
                item_or_row.setFlags(item_or_row.flags() | Qt.ItemIsSelectable)
            elif column is not None and hasattr(item_or_row, 'setIcon'):
                item_or_row.setIcon(column, icon)
                item_or_row.setFlags(item_or_row.flags() | Qt.ItemIsSelectable)

    @staticmethod
    def handle_dok_clicked(item_or_model, index_or_column):
        # TreeView (QStandardItemModel + QModelIndex)
        if isinstance(item_or_model, QStandardItemModel):
            index = index_or_column
            if index.column() == 5:
                item = item_or_model.itemFromIndex(index)
                if item:
                    dok_path = item.data(Qt.UserRole)
                    if dok_path:
                        subprocess.Popen(['explorer', dok_path.replace('/', '\\')], shell=True)

        # TreeWidget
        else:
            item = item_or_model
            column = index_or_column
            if column == 5:
                dok_path = item.data(column, Qt.UserRole)
                if dok_path:
                    subprocess.Popen(['explorer', dok_path.replace('/', '\\')], shell=True)

    @staticmethod
    def open_property():
        link_id = StoreValues().return_prperties_id()
        module = Module.PROPRETIE
        web_module = MailablWebModules().get_web_link(module)
        #print(f"web_module: {web_module}")
        web_link = OpenLink.weblink_by_module(web_module)
        #print(f"web_link: {web_link}")
        link = f"{web_link}{link_id}"
        response = requests.get(link, verify=False)
        webbrowser.open(response.url)


class StoreValues:
    def __init__(self) -> None:
        self.propertyID_location = 'MailablProperty_id/stores_id'

    def return_prperties_id(self):
        settings_address = self.propertyID_location
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    

    def load_propertieID_from_memory (self):
        value = self.propertyID_location
        return value
    
    def save_propertyID(self, input_value):
        settings = QgsSettings()
        target_settings_address = self.propertyID_location
        settings.setValue(target_settings_address, input_value)

