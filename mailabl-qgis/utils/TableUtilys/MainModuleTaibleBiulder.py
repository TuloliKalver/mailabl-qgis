from PyQt5.QtWidgets import QTableView
from .TableHEaderIndexMap import HeaderIndexMap, AsBuiltHeaderIndexMap
from .TableHelpers import ColumnResizer, TableUtils, TableExtractor
from ..delegates.DelegateMainTable import DelegatesForTables
from ...KeelelisedMuutujad.modules import Module


class ModuleTableBuilder:
    @staticmethod
    def setup(table, model, module, language="et", row_height=25):
        header_labels = TableExtractor._extract_headers_from_model(model)


        table.setModel(model)
        DelegatesForTables.setup_delegates_by_module(table, header_labels, module, language)

        table.verticalHeader().setDefaultSectionSize(row_height)
        table.verticalHeader().setVisible(False)
        table.setSelectionBehavior(QTableView.SelectRows)
        table.setSelectionMode(QTableView.SingleSelection)
        table.setSortingEnabled(True)



        resizer = ColumnResizer(table)
        if module == Module.ASBUILT:
            print(f"Resizing columns for {module}")
            index_map = AsBuiltHeaderIndexMap(header_labels, language=language)
            TableUtils._resize_asBuilt_columns(resizer, index_map)
            TableUtils._resize_asBuilt_icon_columns(resizer, index_map, table)
    
        else:
            index_map = HeaderIndexMap(header_labels, language=language)
            TableUtils._resize_main_columns(resizer, index_map)
            TableUtils._resize_icon_columns(resizer, index_map)
        TableUtils._hide_default_columns(table, index_map)
        TableUtils._set_icon_column_labels(model, index_map)


        table.update()