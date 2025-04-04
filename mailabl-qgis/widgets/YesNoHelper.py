import os
from PyQt5.QtGui import QStandardItemModel
from PyQt5.uic import loadUi
from ..KeelelisedMuutujad.messages import Headings

 
pealkiri = Headings()

model = QStandardItemModel()

class Directories:

        
    def load_ConfirmationUI():
        from ..config.settings import Filepaths, FilesByNames
        widget_name = Filepaths._get_widget_name(FilesByNames().WConfirmation)
        widget = Filepaths.load_ui_file(widget_name)
        
        widget.show()
        # Make the application wait for the user interaction
        result = widget.exec_()

        # Check the result after the user interaction (e.g., which button was pressed)
        if result == widget.Accepted:
            print("User pressed OK")
        else:
            print("User pressed Cancel")
            #widget.close()