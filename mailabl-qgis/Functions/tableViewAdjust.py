from PyQt5.QtGui import QFontMetrics

from PyQt5.QtGui import QFontMetrics

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
