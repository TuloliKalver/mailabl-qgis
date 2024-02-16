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


#declare catalouges and links
#main directory
#plugin_dir = os.path.dirname(__file__)
# Get the parent directory of the directory containing the script
plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))
#ui_file_path = f"C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\kataster\app\widgets\WStatusBar.ui"

class progressBar_loader:
    
    def progress_bar_load(total):

        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
        progress_widget.show()


class messages:
    __init__(self)
        pass


    def update_progress_widget(count, progress_points, progress_widget, progress_bar):
        progress_bar.setValue(count)
        if count in progress_points:
            
            # paigal seisev teavitus kõige peal "Laadimine võtab mõned minutid!"
            # esmane label "Kas sa täna kohvi oled juba joonud?"
            messages = {
                progress_points[0]: "Kas sa täna kohvi oled juba joonud?",
                progress_points[1]: "Nüüd siruta varbaid",
                progress_points[2]: "Natuke minna - jõuad veel mõned kükid ka teha"
            }
            progress_widget.label_2.setText(messages[count])
            
            
        #use of content 
        total_rows = shapefile_layer.featureCount() #Can be any number or calculation
        progress_points = [total_rows // 4, total_rows // 2, total_rows * 3 // 4]


        #Start afther this point 
        count += 1
        #use class and import method 
        update_progress_widget(count, progress_points, progress_widget, progress_bar)
        #use always this to prevent satatusbar from hanging
        QCoreApplication.processEvents()
    
    
