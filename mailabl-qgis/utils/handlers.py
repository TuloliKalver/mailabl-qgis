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


