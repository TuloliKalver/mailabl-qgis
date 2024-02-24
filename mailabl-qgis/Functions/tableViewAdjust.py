from PyQt5.QtGui import QFontMetrics
from PyQt5.QtGui import QIcon, QColor,  QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtWidgets import QTableView


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
        

    def resizeColumnByIndex_dynamic(self, table, column_index):
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
        
        max_item_width += self.padding
        header.resizeSection(column_index, max_item_width)
        
        delegate = CustomDelegate()
        table.setItemDelegate(delegate)
        
    def setColumnWidths(self, table, column_indexes, widths):
        
        header = table.horizontalHeader()
        for index, width in zip(column_indexes, widths):
            header.resizeSection(index, width)


class colors:
    @staticmethod
    def hex_to_rgb(hex_code):
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    
            
class CustomDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.column() == 5:  # Customize column 5
            # Customize the appearance of items in column 5
            value = index.data()
            if value:
                # Draw a custom icon for an empty value
                icon = QIcon(":/images/themes/default/propertyicons/attributes.svg")
                painter.save()
                icon.paint(painter, option.rect, Qt.AlignCenter)
                painter.restore()
                return  # Return to prevent further painting for this cell
            elif value == "":                
                icon = QIcon(":/images/themes/default/mActionDeleteAttribute.svg")
                # Change the background color and text color for the specific condition
                painter.save()
                icon.paint(painter, option.rect, Qt.AlignCenter)
                painter.restore()
                return  # Return to prevent further painting for this cell



#needs to be developed function!
    def paint_status (self, painter, option, index):
        if index.column() == 5:  # Customize column 5
            # Customize the appearance of items in column 5
            value = index.data()
            if value:
                
                return  # Return to prevent further painting for this cell
            elif value == "":
                
                icon = QIcon(":/images/themes/default/mActionDeleteAttribute.svg")
                
                # Change the background color and text color for the specific condition
                painter.save()
                icon.paint(painter, option.rect, Qt.AlignCenter)
                painter.restore()
                return  # Return to prevent further painting for this cell
                
                # Set the background color to red
             #   painter.fillRect(option.rect, QColor(255, 0, 0))  # Red background
                
                # Set the text color to white (or any color you prefer)
             #   pen = QPen(Qt.white)
             #   painter.setPen(pen)
                
                # Draw the text
             #   painter.drawText(option.rect, Qt.AlignCenter, value)
                
             #   painter.restore()
             #   return
          
        # For other cases, use the default paint behavior
        super().paint(painter, option, index)
        
class AdjustTableView:
    
    def standard_table_view(self, table_view, model):
        custom_row_height = 20  # Adjust this value as needed
        for row in range(table_view.rowCount()):
            table_view.setRowHeight(row, custom_row_height) 
        
        table_view.setSortingEnabled(True)
        # Hide the vertical header (row numbers)
        table_view.verticalHeader().setVisible(False)
        # Optional: Hide grid lines
        table_view.setShowGrid(False)
        # Automatically resize columns to fit content
        table_view.resizeColumnsToContents()
        # Block editing for all cells
        table_view.setEditTriggers(QTableView.NoEditTriggers)