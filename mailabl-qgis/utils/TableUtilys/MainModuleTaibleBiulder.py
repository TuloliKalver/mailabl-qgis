from PyQt5.QtWidgets import QTableView
from .TableHEaderIndexMap import HeaderIndexMap
from .TableHelpers import ColumnResizer, TableUtils, TableExtractor
from ..delegates.DelegateMainTable import DelegatesForTables



class ModuleTableBuilder:
    @staticmethod
    def setup(table, model, module, language="et", row_height=25):
        header_labels = TableExtractor._extract_headers_from_model(model)
        index_map = HeaderIndexMap(header_labels, language=language)

        table.setModel(model)
        DelegatesForTables.setup_delegates_by_module(table, header_labels, module, language)

        table.verticalHeader().setDefaultSectionSize(row_height)
        table.verticalHeader().setVisible(False)
        table.setSelectionBehavior(QTableView.SelectRows)
        table.setSelectionMode(QTableView.SingleSelection)
        table.setSortingEnabled(True)

        TableUtils._hide_default_columns(table, index_map)
        TableUtils._set_icon_column_labels(model, index_map)

        resizer = ColumnResizer(table)
        TableUtils._resize_main_columns(resizer, index_map)
        TableUtils._resize_icon_columns(resizer, index_map)

        table.update()