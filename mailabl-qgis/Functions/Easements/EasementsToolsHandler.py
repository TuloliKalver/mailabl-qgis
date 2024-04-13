# Related Third-Party Imports
import re
from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtWidgets import QMessageBox, QFrame
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

from ...config.settings import Filepaths, SettingsDataSaveAndLoad, FilesByNames
from ...processes.infomessages.messages import Headings, HoiatusTexts, EdukuseTexts

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()

class EasementTools:
    def load_widget(self):
        ui_file_path = Filepaths.get_easements_tools()
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel
        
        widget.show()
                # Access the variables through the instance
        save_button.clicked.connect(lambda: EasementTools.on_save_button_clicked(self, widget))
        cancel_button.clicked.connect(lambda: EasementTools.on_cancel_button_clicked(self, widget))

    def on_save_button_clicked(self, widget):
        text = "Olen alles arenduses. \n mitte midagi ei salvestatud"
        heading = pealkiri.tubli
        QMessageBox.information(widget, heading, text)
        # Additional logic if needed
        widget.accept()  # Close the dialog

    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.informationSimple
        QMessageBox.information(widget, heading, text)
        widget.reject()  # Close the dialog        