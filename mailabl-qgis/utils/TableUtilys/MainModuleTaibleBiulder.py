from PyQt5.QtWidgets import QTableView
from .TableHEaderIndexMap import HeaderIndexMap, AsBuiltHeaderIndexMap, CoordinationsIndexMap, WorksIndexMap
from .TableHelpers import ColumnResizer, TableUtils, TableExtractor
from ..delegates.DelegateMainTable import DelegatesForTables
from ...KeelelisedMuutujad.modules import Module
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys


class ModuleTableBuilder:
    @staticmethod
    def setup(table, model, module, language="et", row_height=25):
        header_labels = TableExtractor._extract_headers_from_model(model)
        
        table.setModel(model)

        table.verticalHeader().setDefaultSectionSize(row_height)
        table.verticalHeader().setVisible(False)
        table.setSelectionBehavior(QTableView.SelectRows)
        table.setSelectionMode(QTableView.SingleSelection)
        table.setSortingEnabled(True)



        resizer = ColumnResizer(table)
        print("Setting up table")
        print(f"module: {module}")
        if module == Module.ASBUILT:
            index_map = AsBuiltHeaderIndexMap(header_labels, language=language)
            #print(f"Resizing columns for {module}")
            DelegatesForTables.setup_delegates_by_module(table, header_labels, module, language)
            TableUtils._resize_asBuilt_columns(resizer, index_map)
            TableUtils._resize_asBuilt_icon_columns(resizer, index_map, table)
    
        elif module == Module.COORDINATION:
            index_map = CoordinationsIndexMap(header_labels, language=language)
            DelegatesForTables.setup_delegates_by_module(table, header_labels, module, language)

            TableUtils._resize_coordinations_columns(resizer, index_map)
            ColumnResizer.resizeColumnByIndex(resizer, 14, status=True)
            ColumnResizer.resizeColumnByIndex(resizer, 2)
        elif module == Module.WORKS:
            DelegatesForTables.setup_delegates_by_module(table, header_labels, module, language)

            print("Resizing works columns")
            index_map = WorksIndexMap(header_labels, language=language)
            TableUtils._resize_works_columns(resizer, index_map)
        else:
            index_map = HeaderIndexMap(header_labels, language)
            DelegatesForTables.setup_delegates_by_module(table, header_labels, module, language)

            TableUtils._resize_main_columns(resizer, index_map)
            TableUtils._resize_standard_columns(resizer, index_map)
        TableUtils._hide_default_columns(table, index_map, module = module)
        TableUtils._set_icon_column_labels(model, index_map, module = module)


        table.update()