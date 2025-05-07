# TableHelpers.py
import ast

from typing import List
from PyQt5.QtCore import Qt, QItemSelectionModel, QCoreApplication
from PyQt5.QtGui import QFontMetrics, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableView, QHeaderView, QAbstractItemView, QTableView
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from .TableHEaderIndexMap import HeaderIndexMap, AsBuiltHeaderIndexMap, CoordinationsIndexMap
from ...utils.ProgressHelper import ProgressDialogModern

class TableHelper:
    dialog = None  # Class-level variable to store the dialog reference

    @staticmethod
    def set_dialog(main_dialog):
        """Sets the main dialog reference for ButtonHelper."""
        TableHelper.dialog = main_dialog

    @staticmethod
    def get_table_by_name(table_name):
        table = TableHelper.dialog.findChild(QTableView, table_name)
        return table

    @staticmethod
    def insert_data_into_tableview(element: QTableView, data: list, headers: list, feature_ids=None):
        """
        Populate a QTableView with given data using QStandardItemModel.

        Args:
            element (QTableView): The table view widget to populate.
            data (list): A list of lists representing the table data.
            headers (list): A list of field names to be used as column headers.
        """
        TableHelper.reset_and_set_tableView(element)
        if not data:
            return

        table_model = QStandardItemModel(len(data), len(headers))

        # Set headers
        for col_idx, header in enumerate(headers):
            table_model.setHeaderData(col_idx, Qt.Horizontal, header)

        # Insert data
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                item = QStandardItem(str(value) if value is not None else "")
                item.setTextAlignment(Qt.AlignCenter)
                if col_idx == 0:
                    item.setData(feature_ids[row_idx], Qt.UserRole)
                table_model.setItem(row_idx, col_idx, item)

        element.setModel(table_model)
        element.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def reset_and_set_tableView(table: QTableView):
        """
        Clears and resets the QTableView with new data and headers.

        """
        if table.model():
            table.setModel(None)  # Remove the existing model to free memory

    @staticmethod
    def select_all_items(table: QTableView):
        """
        Selects all items in the provided QTableView.
        """
        table.selectAll()

    def deselect_all_items(table: QTableView):
        """ 
        Deselect all items in a QTableView
        """
        table.clearSelection()

    @staticmethod
    def select_all_items(table: QTableView):


        """
        Selects all items in the provided QTableView.
        """
        table.selectAll()

    @staticmethod
    def deselect_all_items(table: QTableView):
        """ 
        Deselect all items in a QTableView
        """
        table.clearSelection()


    @staticmethod
    def select_items_by_field(table: QTableView, field: str, search_value: str):
        """
        Selects rows in a QTableView where the cell in the specified field does NOT match search_value.

        Args:
            table (QTableView): The table view to work with.
            field (str): The header text (field name) to search for.
            search_value (str): The value to check for; if the cell matches this value, the row is NOT selected.
        """

        
        model = table.model()
        if model is None:
            print("Table has no model.")
            return

        # Ensure multiple row selection is enabled.
        table.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Find the column index for the given field (header text)
        target_column = -1
        for col in range(model.columnCount()):
            header_data = model.headerData(col, Qt.Horizontal)
            if header_data == field:
                target_column = col
                break

        if target_column == -1:
            print(f"Field '{field}' not found.")
            return

        selection_model = table.selectionModel()
        # Deselect any current selection first
        selection_model.clearSelection()

        mapfeatures = []
        process_interval = 50  # Process events every 100 iterations

        max_items = model.rowCount()

        progress = ProgressDialogModern(purpouse="Katastri laadimine", text="Palun oota...")
        progress.update(1, "Katastri laadimine")


        for row in range(model.rowCount()):
            index = model.index(row, target_column)
            cell_data = model.data(index)
            if cell_data is not None and cell_data.lower() == search_value.lower():
                continue
            else:
                # Otherwise, add the row to the selection and store the feature id.
                feature_id = model.item(row, 0).data(Qt.UserRole)
                mapfeatures.append(feature_id)
                selection_flags = QItemSelectionModel.Select | QItemSelectionModel.Rows
                selection_model.select(model.index(row, 0), selection_flags)
            
            # Update the progress bar for every processed row.
            progress.update(value=row+1, text1=f"Laen katastri {row}/{max_items}")

        progress.update(100,"Valmis")
        progress.close()
        return mapfeatures    

    @staticmethod
    def get_selected_feature_ids_from_table_model(table: QTableView):
        """
        Retrieves the feature IDs from the model for the currently selected rows.
        Updates a progress bar during processing.

        Args:
            table (QTableView): The table view whose selected rows will be processed.

        Returns:
            list: A list of feature IDs extracted from the selected rows.
        """
        model = table.model()
        if model is None:
            print("Table has no model.")
            return []

        selection_model = table.selectionModel()
        # Retrieves selected rows as a list of QModelIndex objects.
        selected_rows = selection_model.selectedRows()

        feature_ids = []
        max_items = len(selected_rows)
        # Initialize the progress bar with 0 as the starting value and max_items as maximum.
        progress = ProgressDialogModern(purpouse="Andmete laadimine", text="Palun oota...", maximum=max_items)
        progress.update(1, "Esimene etapp")
        process_interval = 10  # Adjust interval as needed for responsiveness
        for idx, index in enumerate(selected_rows):
            # Assumes the feature id is stored in column 0 with Qt.UserRole.
            feature_id = model.item(index.row(), 0).data(Qt.UserRole)
            feature_ids.append(feature_id)
            progress.update(
                value=idx + 1
            )            

        progress.close()
        return feature_ids



class TableDataInserter:
    def insert_data_to_tables(self, tables_with_models, total, total_label, custom_row_height=20):
        """
        Inserts data into the provided tables and applies consistent styling.

        Parameters:
        - tables_with_models: List of tuples containing (QTableView, DataModel).
        - total: Total count of items to display in the label.
        - total_label: QLabel widget to display the total count.
        - custom_row_height: Integer defining the height of each row (default is 20).
        """
        # Display the total number of items in the label
        total_label.setText(str(total))

        # Iterate over each table and its corresponding data model
        for table_view, model in tables_with_models:
            # Set the data model for the table
            table_view.setModel(model)

            # Adjust row heights based on the custom row height
            for row in range(model.rowCount()):
                table_view.setRowHeight(row, custom_row_height)

            # Enable sorting functionality in the table
            table_view.setSortingEnabled(True)

            # Hide the vertical headers (row numbers) for a cleaner look
            table_view.verticalHeader().setVisible(False)

            # Optionally hide grid lines to reduce visual clutter
            table_view.setShowGrid(False)

            # Automatically adjust column widths to fit their content
            table_view.resizeColumnsToContents()

            # Disable editing of all cells to make the tables read-only
            table_view.setEditTriggers(QTableView.NoEditTriggers)

            # Select all rows in the table (optional depending on use case)
            table_view.selectAll()

class ColumnResizer:
    def __init__(self, table_widget, max_width=250, min_width=60, padding=10):
        self.table = table_widget
        self.header = self.table.horizontalHeader()
        self.padding = padding
        self.max_width = max_width
        self.min_width = min_width

        
    def resizeColumnByIndex(self, column_index, status=False):
        model = self.table.model()
        if model is None:
            return

        max_item_width = 0
        font_metrics = QFontMetrics(self.table.font())
        for row in range(model.rowCount()):
            index = model.index(row, column_index)
            item = model.data(index)
            if item:
                item_text = str(item)
                item_width = font_metrics.width(item_text)
                max_item_width = max(max_item_width, item_width)

        # Extra space for status pill visual padding
        extra_padding = 20 if status else 0
        adjusted_width = max_item_width + self.padding + extra_padding

        adjusted_width = max(adjusted_width, self.min_width)
        adjusted_width = min(adjusted_width, self.max_width)

        self.header.resizeSection(column_index, adjusted_width)

    def setColumnWidths(self, column_indexes, widths):
        for index, width in zip(column_indexes, widths):
            self.header.resizeSection(index, width)

class TableUtils:
    @staticmethod
    def _build_index_map(header_labels: List[str], language: str = "et") -> HeaderIndexMap:
        return HeaderIndexMap(header_labels, language)

    @staticmethod
    def _hide_default_columns(table, index_map: HeaderIndexMap, language: str ="et"):
        TableHeaders_new(language)
        to_hide = [
            index_map[HeaderKeys.COLOR_NAME],
            index_map[HeaderKeys.HEADER_PARENT_ID],
            index_map[HeaderKeys.HEADER_DOCUMENTS],
        ]
        for col in to_hide:
            table.hideColumn(col)

    @staticmethod
    def _set_icon_column_labels(model, index_map: HeaderIndexMap, language: str="et"):
        TableHeaders_new(language)
        for key in [
            HeaderKeys.HEADER_PROPERTY_NUMBER,
            HeaderKeys.HEADER_FILE_PATH,
            HeaderKeys.HEADER_WEB_LINK_BUTTON,
            HeaderKeys.HEADER_PROPERTIES_ICON,
        ]:
            model.setHorizontalHeaderItem(index_map[key], QStandardItem(""))

    #/TODO this method date column need to be removed from all functions
    @staticmethod
    def _resize_main_columns(reziser, index_map: HeaderIndexMap,  language: str="et"):
        TableHeaders_new(language)
        for col in [
            index_map[HeaderKeys.HEADER_NUMBER],
            index_map[HeaderKeys.HEADER_DEADLINE],
            index_map[HeaderKeys.HEADER_RESPONSIBLE],
        ]:
            reziser.resizeColumnByIndex(col)
        reziser.resizeColumnByIndex(index_map[HeaderKeys.HEADER_STATUSES], status=True)


    @staticmethod
    def _resize_asBuilt_columns(resizer, index_map: AsBuiltHeaderIndexMap,  language: str="et"):
        TableHeaders_new(language)
        for col in [
            index_map[HeaderKeys.HEADER_DEADLINE],
            index_map[HeaderKeys.HEADER_RESPONSIBLE],
        ]:
            resizer.resizeColumnByIndex(col)
        resizer.resizeColumnByIndex(index_map[HeaderKeys.HEADER_STATUSES], status=True)




    @staticmethod
    def _resize_standard_columns(resizer, index_map: HeaderIndexMap, language: str="et"):
        TableHeaders_new(language)
        columns = [
            HeaderKeys.HEADER_ID,
            HeaderKeys.HEADER_NAME,
            HeaderKeys.HEADER_PROPERTY_NUMBER,
            HeaderKeys.HEADER_WEB_LINK_BUTTON,
            HeaderKeys.HEADER_FILE_PATH,
            HeaderKeys.HEADER_PROPERTIES_ICON,
        ]
        widths = [0, 250, 0, 10, 10, 10]
        indexes = [index_map[key] for key in columns]
        resizer.setColumnWidths(indexes, widths)

    @staticmethod
    def _resize_coordinations_columns(resizer, index_map: CoordinationsIndexMap, language: str="et"):
        TableHeaders_new(language)
        print(f"Coordinations Index Map: {index_map}")
        columns = [
            HeaderKeys.HEADER_ID,
            HeaderKeys.HEADER_NUMBER,
            HeaderKeys.HEADER_JOB_NAME,
            HeaderKeys.HEADER_PROPERTY_NUMBER,
            HeaderKeys.HEADER_WEB_LINK_BUTTON,
            HeaderKeys.HEADER_FILE_PATH,
            HeaderKeys.HEADER_PROPERTIES_ICON,
            HeaderKeys.HEADER_DEADLINE,
            HeaderKeys.HEADER_RESPONSIBLE
        ]
        widths = [0,0, 250, 0, 10, 10, 10, 0, 0]
        indexes = [index_map[key] for key in columns]
        resizer.setColumnWidths(indexes, widths)



    @staticmethod
    def _resize_asBuilt_icon_columns(resizer, index_map, table, language: str = "et"):
        passed_language = language
        #print(f"Language: {passed_language}")
        TableHeaders_new(language)

        columns = [
            HeaderKeys.HEADER_ID,
            HeaderKeys.HEADER_FLAG,
            HeaderKeys.HEADER_TYPE,
            HeaderKeys.HEADER_NAME,
            HeaderKeys.HEADER_PROPERTY_NUMBER,
            HeaderKeys.HEADER_WEB_LINK_BUTTON,
            HeaderKeys.HEADER_FILE_PATH,
            HeaderKeys.HEADER_PROPERTIES_ICON,
        ]
        widths = [0, 10, 150, 250, 0, 10, 10, 10]  # default widths

        #print(f"index_map: {index_map}")
        indexes = [index_map[key] for key in columns]
        #print(f"indexes: {indexes}")

        try:
            #print(f"Trying to find 'Dok_icon'")
            file_path_col = index_map[HeaderKeys.HEADER_FILE_PATH]
            #print(f"Found 'Dok_icon': {file_path_col}")
            dok_icon_col = index_map[HeaderKeys.HEADER_DOCUMENTS]
        except KeyError:
            #print(f"'Dok_icon' not found.")
            file_path_col = None

        if dok_icon_col is not None:
            #print(f"File path column exists at index: {dok_icon_col}")
            max_icons = 0
            for row in range(table.model().rowCount()):
                index = table.model().index(row, dok_icon_col)
                value = index.data(Qt.DisplayRole)

                if value:
                    if isinstance(value, str):
                        try:
                            value = ast.literal_eval(value)
                        except Exception:
                            value = []
                    
                    if isinstance(value, list):
                        max_icons = max(max_icons, len(value))
                    else:
                        max_icons = max(max_icons, 1)
            #print(f"Max icons: {max_icons}")
            #print(f"Value: {value}")
            icon_size = 18  # px (same as in FileDelegate)
            spacing = 4
            dynamic_width = (icon_size + spacing) * max_icons + 6
            #print(f"🛠 Calculated file column width: {dynamic_width}px")

            file_path_idx = columns.index(HeaderKeys.HEADER_FILE_PATH)
            widths[file_path_idx] = dynamic_width

        resizer.setColumnWidths(indexes, widths)




class TableExtractor:
    def __init__(self) -> None:

        pass
    @staticmethod
    def _table_header_extractor(table: QTableView) -> list[str]:
        table_headers = []
        model = table.model()
        if model is not None:
            for column in range(model.columnCount()):
                header_label = model.headerData(column, Qt.Horizontal, Qt.DisplayRole)
                table_headers.append(header_label)
        return table_headers

    @staticmethod
    def _extract_headers_from_model(model) -> list[str]:
        table_headers = []
        if model is not None:
            for column in range(model.columnCount()):
                header_label = model.headerData(column, Qt.Horizontal, Qt.DisplayRole) 
                table_headers.append(header_label)
        return table_headers
    
    @staticmethod
    def _value_from_selected_row_by_column(table, index: int) -> str: 
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
    def _values_from_selected_row_by_columns(table, indexes: list) -> str:
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
    
