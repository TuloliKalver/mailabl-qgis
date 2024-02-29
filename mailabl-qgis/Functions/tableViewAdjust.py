from PyQt5.QtGui import QFontMetrics

class ColumnResizer:
    def __init__(self, table_widget):
        self.header = table_widget.horizontalHeader()
        self.padding = 10  # Adjust the padding value as needed
        self.max_width = 225  # Maximum width for a column

    def resizeColumnByIndex(self, table, column_index):
        header = table.horizontalHeader()
        model = table.model()
        if not model:
            return
        
        max_item_width = 0
        for row in range(model.rowCount()):
            index = model.index(row, column_index)
            item = model.data(index)
            if item:
                item_text = str(item)
                item_width = QFontMetrics(table.font()).width(item_text)
                max_item_width = max(max_item_width, item_width)
        
        # Limit the maximum width to 150 pixels
        max_item_width = min(max_item_width, self.max_width)
        
        max_item_width += self.padding
        header.resizeSection(column_index, max_item_width)
        

    def setColumnWidths(self, table, column_indexes, widths):
        header = table.horizontalHeader()
        for index, width in zip(column_indexes, widths):
            header.resizeSection(index, width)

class Colors:
    @staticmethod
    def hex_to_rgb(hex_code):
        clean_hex_code = hex_code.strip('#')
        return tuple(int(clean_hex_code[i:i+2], 16) for i in (0, 2, 4))
