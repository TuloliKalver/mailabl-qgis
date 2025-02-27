#tableViewAdjust.py

from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QTableView

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

# Example Usage:
# inserter = TableDataInserter()
# inserter.insert_data_to_tables(
#     tables_with_models=[(streets_table_view, streets_model), (properties_table_view, properties_model)],
#     total=100,
#     total_label=total_count_label
# )



class ColumnResizer:
    def __init__(self, table_widget, max_width=250, min_width=60, padding=10):
        self.header = table_widget.horizontalHeader()
        self.padding = padding
        self.max_width = max_width
        self.min_width = min_width

    def resizeColumnByIndex(self, table, column_index):
        header = table.horizontalHeader()
        model = table.model()
        if model is None:
            return
        
        max_item_width = 0
        font_metrics = QFontMetrics(table.font())
        for row in range(model.rowCount()):
            index = model.index(row, column_index)
            item = model.data(index)
            if item:
                item_text = str(item)
                item_width = font_metrics.width(item_text)
                max_item_width = max(max_item_width, item_width)
        
        # Calculate the width including padding
        adjusted_width = max_item_width + self.padding

        # Choose between max width and min width
        adjusted_width = max(adjusted_width, self.min_width)
        adjusted_width = min(adjusted_width, self.max_width)

        header.resizeSection(column_index, adjusted_width)



    def setColumnWidths(self, table, column_indexes, widths):
        header = table.horizontalHeader()
        for index, width in zip(column_indexes, widths):
            header.resizeSection(index, width)

class Colors:
    @staticmethod
    def hex_to_rgb(hex_code):
        clean_hex_code = hex_code.strip('#')
        return tuple(int(clean_hex_code[i:i+2], 16) for i in (0, 2, 4))
