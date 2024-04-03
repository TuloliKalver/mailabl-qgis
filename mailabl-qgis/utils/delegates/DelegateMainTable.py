# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

import webbrowser
import subprocess
import requests

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from ...Functions.item_selector_tools import properties_selectors
from ...queries.python.projects_pandas import GetProjectsWhere
from ...config.settings import OpenLink
from ...queries.python.projects_pandas import TableHeaders

from ...Functions.ButtonDelegates import ContractButtonDelegate, SelectContractsOnMapElementsDelegate


class DelegatesForTables():
    @staticmethod
    def setup_delegates_standard_table(table, header_labels):
        headers = TableHeaders()
        ID_column_index = header_labels.index(headers.header_id)
        webButton_Column_index = header_labels.index(headers.header_web_link_button)
        dokAddress_column_index = header_labels.index(headers.header_documents)
        cadastralButton_Column_index = header_labels.index(headers.header_properties_icon)
        dokAddress_column_index = header_labels.index(headers.header_documents)
        dokButton_column_index = header_labels.index(headers.header_file_path)

        web_link_delegate = WebLinkDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(webButton_Column_index, web_link_delegate)

        file_delegate = FileDelegate(dokAddress_column_index, table)
        table.setItemDelegateForColumn(dokButton_column_index, file_delegate)

        show_onMap_delegate = SelectMapElementsDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)

    @staticmethod
    def setup_delegates_contract_table(table, header_labels):
        headers = TableHeaders()
        ID_column_index = header_labels.index(headers.header_id)
        webButton_Column_index = header_labels.index(headers.header_web_link_button)
        dokAddress_column_index = header_labels.index(headers.header_documents)
        cadastralButton_Column_index = header_labels.index(headers.header_properties_icon)
        dokAddress_column_index = header_labels.index(headers.header_documents)
        dokButton_column_index = header_labels.index(headers.header_file_path)

        web_link_delegate = ContractButtonDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(webButton_Column_index, web_link_delegate)

        file_delegate = FileDelegate(dokAddress_column_index, table)
        table.setItemDelegateForColumn(dokButton_column_index, file_delegate)

        show_onMap_delegate = SelectContractsOnMapElementsDelegate(ID_column_index, table)
        table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)


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