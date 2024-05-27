from PyQt5.QtWidgets import QScrollArea, QWidget, QScrollBar, QVBoxLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt

class Scrollers:
    def size_fit_test(self):
        # Assuming SettingsPageMainFrame is an instance of QWidget
        frame = self.SettingsPageMainFrame  # QWidget frame with Frame inside as content 
        main_layout = self.frame_32
        # Assuming verticalScrollBar is an instance of QScrollBar
        Scroller = self.verticalScrollBar # QScrollBar 

        # Ensure both widgets are properly initialized and accessible
        if frame is None or Scroller is None:
            print("Error: Widgets not properly initialized.")
            return

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBar(Scroller)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(frame)

        # Add the scroll area to a layout in your main window
        # For example, if you have a QVBoxLayout named main_layout:
        main_layout.addWidget(scroll_area)

class CheckBoxes:

    @staticmethod
    def uncheck_checkboxes(widget, checkboxes_info):
        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                checkbox.setChecked(False)

    @staticmethod
    def update_checkboxes(checkboxes_info, table):
        if table:
            model = table.model()
           

        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                current_text = checkbox.text()
                if connect_function is not None:
                    if model is None:
                        checkbox.setEnabled(False)
                    elif model is not  None:
                        item_count = model.rowCount()
                        if item_count == 0:
                            checkbox.setEnabled(False)
                        else:
                            checkbox.setEnabled(True)
                            checkbox.clicked.connect(connect_function)
                else:
                    checkbox.setText(f"{current_text}* ({text}m)")
                    checkbox.setEnabled(False)


