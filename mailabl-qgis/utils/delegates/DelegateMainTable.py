# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

from ...queries.python.projects_pandas import TableHeaders
from ...Functions.ButtonDelegates import  ModuleButtonDelegate, SelectByModuleElementsOnMapDelegate, FileDelegate


class DelegatesForTables():
    @staticmethod
    def setup_delegates_by_module(table, header_labels, module):
        headers = TableHeaders()
        ID_column_index = header_labels.index(headers.header_id)
        webButton_Column_index = header_labels.index(headers.header_web_link_button)
        dokAddress_column_index = header_labels.index(headers.header_documents)
        cadastralButton_Column_index = header_labels.index(headers.header_properties_icon)
        dokAddress_column_index = header_labels.index(headers.header_documents)
        dokButton_column_index = header_labels.index(headers.header_file_path)

        web_link_delegate = ModuleButtonDelegate(ID_column_index, table, module)
        table.setItemDelegateForColumn(webButton_Column_index, web_link_delegate)

        file_delegate = FileDelegate(dokAddress_column_index, table)
        table.setItemDelegateForColumn(dokButton_column_index, file_delegate)

        show_onMap_delegate = SelectByModuleElementsOnMapDelegate(ID_column_index, table, module)
        table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)
