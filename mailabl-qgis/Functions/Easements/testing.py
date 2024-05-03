# Related Third-Party Imports
import re
from qgis.utils import iface
from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

import re
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import SettingsDataSaveAndLoad
from .EasementsItems import queryHandling
from ...queries.python.DataLoading_classes import GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder
from ...queries.python.update_relations.update_project_properties import map_selectors
from ...config.settings import Filepaths, Flags, SettingsDataSaveAndLoad, FilesByNames
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ..propertie_layer.properties_layer_data import PropertiesLayerFunctions

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()


class EasementTools:
    def __init__(self, tweasementView):
        self.tweasementView = tweasementView
        self.widget_EasmentTools = None
        self.on_selection_changed_lambda_easements = None
        self.select_tool = None
        self.is_select_tool_activated = False  # Track whether select tool was activated
        self.is_table_generated = False  # Track whether table was generated

    def load_widget(self):
        if self.widget_EasmentTools is None:
            # Create a new instance of the widget if it doesn't exist
            table = self.tweasementView
            selection_model = table.selectionModel()
            if selection_model.hasSelection():
                ui_file_path = Filepaths.get_easements_tools()
                self.widget_EasmentTools = loadUi(ui_file_path)
                save_button = self.widget_EasmentTools.pbSave
                cancel_button = self.widget_EasmentTools.pbCancel
                select_button = self.widget_EasmentTools.pbValiKinnistu

                self.widget_EasmentTools.show()
                WidgetTools.load_selected_item_name(self, table, self.widget_EasmentTools)

                self.widget_EasmentTools.dPuhvriSuurus.valueChanged.connect(lambda: WidgetTools.dialer(self.widget_EasmentTools))
                self.widget_EasmentTools.dPuhvriSuurus.setValue(20)

                if self.select_tool is None:
                    WidgetTools.loadselectedProperties(self, self.widget_EasmentTools)
                clear_table = self.widget_EasmentTools.pbClearCadastrals
                
            
                select_button.clicked.connect(lambda: WidgetTools.activate_layer_and_use_selectTool(self, self.widget_EasmentTools))
                #WidgetTools.activate_layer_and_use_selectTool_on_first_load(self, self.widget_EasmentTools)


                save_button.clicked.connect(lambda: self.on_save_button_clicked(self.widget_EasmentTools))
                cancel_button.clicked.connect(lambda: self.on_cancel_button_clicked(self.widget_EasmentTools))
                    # Activate select tool and generate table if needed

                # Connect closeEvent method to handle window close event
                self.widget_EasmentTools.closeEvent = self.closeEvent

            else:
                text = HoiatusTexts().andmed_valimata
                heading = Headings().warningSimple
                QMessageBox.information(self.tweasementView, heading, text)
                return
        else:
            # If an instance already exists, simply show it
            self.cleanup()
            self.widget_EasmentTools.show()

    def on_save_button_clicked(self, widget):
        if widget is not None:
            text = "Olen alles arenduses. \n mitte midagi ei salvestatud"
            heading = pealkiri.tubli
            self.cleanup()
            QMessageBox.information(widget, heading, text)
            # Additional logic if needed
            
            widget.accept()  # Close the dialog

    def closeEvent(self, event):
        self.cleanup()
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.informationSimple
        QMessageBox.information(self.widget_EasmentTools, heading, text)
        event.accept()  # Allow the window to close

    def on_cancel_button_clicked(self, widget):
        if widget is not None:
            # Handle logic when the cancel button is clicked

            self.cleanup()
            text = sisu.kasutaja_peatas_protsessi
            heading = pealkiri.informationSimple
            QMessageBox.information(widget, heading, text)
            widget.reject()  # Close the dialog

    def cleanup(self):
        # Reset or disable functionalities based on their activation state
        if self.is_select_tool_activated:
            # Deactivate select tool
            self.deactivate_select_tool()
            self.is_select_tool_activated = False
        if self.is_table_generated:
            # Clear table
            # Perform cleanup actions
            self.is_table_generated = False

        if self.widget_EasmentTools is not None:
            # Get the model set on the table view and clear it
            model = self.widget_EasmentTools.tvProperties.model()
            if model is not None:
                model.clear()

            # Reset the flag
            Flags.active_properties_layer_flag = False

            # Delete the widget instance
            self.widget_EasmentTools.deleteLater()


    def deactivate_select_tool(self):
        # Deactivate selection tool
        if self.select_tool:
            iface.mapCanvas().setMapTool(None)
            self.select_tool = None

class WidgetTools:
    def load_selected_item_name(self, table, widget):
        label = widget.lSelectedEasment

        table_headers = queryHandling()
        # Get the selected row index
        selected_row_index = table.selectionModel().currentIndex().row()
        # Get the model associated with the table
        model = table.model()
        value_name = table_headers.header_name
        value_number = table_headers.header_number

    
        # Find the column index by header name, skipping empty headers
        column_index_name = None
        column_index_number = None

        for column in range(model.columnCount()):
            header_data = model.headerData(column, QtCore.Qt.Horizontal)
            if header_data:
                if header_data == value_name:
                    column_index_name = column
                elif header_data == value_number:
                    column_index_number = column

        if column_index_name is not None and column_index_number is not None:
            # Get the value in the selected row and specified column
            name = model.data(model.index(selected_row_index, column_index_name))
            number = model.data(model.index(selected_row_index, column_index_number))

            # Check if either name or number is missing
            if name is not None and number is not None:
                # Concatenate name and number into a single text string
                text = f"{number} - {number}"
            elif name is not None:
                # Only name is available
                text = name
            elif number is not None:
                # Only number is available
                text = number
            else:
                # Both name and number are missing
                text = sisu.puudulikud_andmed

            label.setText(text)


    @staticmethod
    def dialer(widget):
        value = widget.dPuhvriSuurus.value() / 10 # divide by 10 to convert to the desired units  
        puhver = round(value * 2) / 2 # round up to nearest 0.5 increment
        widget.label.setText(f'Puhver: {puhver:.1f}m')


    @staticmethod
    def loadselectedProperties(self, widget):
        pbClearTable = widget.pbClearCadastrals
        table_view = widget.tvProperties
        
        flag = Flags.active_properties_layer_flag
        flag = True    
        Flags.active_properties_layer_flag = flag
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if not isinstance(active_layer, QgsMapLayer):
            #print(f"Ei leidnud kinnistute kihti '{layer}'")
            return
        iface.setActiveLayer(active_layer)

        if active_layer and active_layer.selectedFeatureCount() > 0:
            # Show the widget when there are selected features
            PropertiesLayerFunctions.generate_table_from_selected_map_items(self,table_view, active_layer_name)
            table_view.update()
            widget.showNormal()

            
    def activate_layer_and_use_selectTool(self, widget):
        global on_selection_changed_lambda_easements

        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        
        if not isinstance(active_layer, QgsMapLayer):
            heading = Headings().warningSimple
            text = HoiatusTexts().puudulik_kinnistute_seadistus
            QMessageBox.warning(self, heading, text)
            return
        
        iface.setActiveLayer(active_layer)
        self.select_tool = iface.actionSelect().trigger()
        self.is_select_tool_activated = True

        if active_layer and active_layer.selectedFeatureCount() > 0:
            table_view = widget.tvProperties
            help = PropertiesLayerFunctions()
            help.generate_table_from_selected_map_items(table_view, active_layer_name)
            table_view.update()
            
            #if not widget.isVisible():
            #    widget.showNormal()

        flag = Flags.active_properties_layer_flag
        print(f"flag is: {flag}")
        flag = True    
        Flags.active_properties_layer_flag = flag
        print(f"flag afther reser: {flag}")

        if flag:
            on_selection_changed_lambda_easements = lambda: WidgetTools.on_selection_changed(widget)
            widget.showMinimized()
            active_layer.selectionChanged.connect(on_selection_changed_lambda_easements)
        else:
            print("Flag is false")

    @staticmethod
    def on_selection_changed(widget):
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
#        print("on_selection_changed")
        if Flags.active_properties_layer_flag:
            # If the flag is true, execute the function
#            print("Flag is true in selection change")
#            print(f"And active_properties_layer flag is {Flags.active_properties_layer_flag}")
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]

            if active_layer and active_layer.selectedFeatureCount() > 0:
                # Show the widget when there are selected features
                table_view = widget.tvProperties

                help = PropertiesLayerFunctions()
                help.generate_table_from_selected_map_items(table_view, active_layer_name)
                table_view.update()
                widget.showNormal()

        else:
            # If the flag is false, do nothing
            print("Flag is false")