import os
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from qgis.core import (QgsFeature,
                       QgsGeometry, QgsLayerTreeGroup,
                       QgsMapLayer, QgsProject, QgsVectorLayer)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QDate
from qgis.utils import iface
from PyQt5.uic import loadUi
from ..KeelelisedMuutujad.messages import Headings
 
pealkiri = Headings()

model = QStandardItemModel()

class Directories:
    #declare catalouges and links
    #main directory
    #plugin_dir = os.path.dirname(__file__)
    # Get the parent directory of the directory containing the script
    plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    #Status bar widget folder
    widgets_folder = "widgets"
    WStatusBar = "WStatusBar.ui"
    WConfirmation = "Confirmation_list.ui"
    #widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
    WstatusBar_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, WStatusBar))

    WResults_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, WConfirmation))
    
    @staticmethod
    def print_paths():
        print(f"plugin_dir: {Directories.plugin_dir}")
        print(f"WstatusBar_path: {Directories.WstatusBar_path}")
        print(f"WResults_path: {Directories.WResults_path}")
        
    def load_ConfirmationUI():
        widget = loadUi(Directories.WResults_path)
        # Show the loaded widget
        widget.show()
        # Make the application wait for the user interaction
        result = widget.exec_()

        # Check the result after the user interaction (e.g., which button was pressed)
        if result == widget.Accepted:
            print("User pressed OK")
        else:
            print("User pressed Cancel")
            #widget.close()