import re
from qgis.utils import iface
from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtCore import pyqtSlot
from qgis.gui import QgsMapToolPan
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic, QtSvg
from PyQt5 import QtCore

from ...config.settings import SettingsDataSaveAndLoad
from .EasementsItems import queryHandling
from ...queries.python.DataLoading_classes import GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder
from ...queries.python.update_relations.update_project_properties import map_selectors
from ...config.settings import Filepaths, Flags, SettingsDataSaveAndLoad, FilesByNames
from ...processes.infomessages.messages import Headings, HoiatusTexts, EdukuseTexts
from ..propertie_layer.properties_layer_data import PropertiesLayerFunctions

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()

on_selection_changed_lambda_easements = None


class EasementTools:
    def __init__(self, tweasementView):
        self.tweasementView = tweasementView
        self.widget_EasmentTools = None
        self.is_select_tool_activated = False
        self.select_tool = None
        self.select_tool_connection = None

        # Connect button click signal outside the load_widget method

    def load_widget(self):
        global on_selection_changed_lambda_easements
        on_selection_changed_lambda_easements = None
        if self.widget_EasmentTools is None:
            # Create a new instance of the widget if it doesn't exist
            table = self.tweasementView
            selection_model = table.selectionModel()
            if selection_model.hasSelection():
                ui_file_path = Filepaths.get_easements_tools()
                self.widget_EasmentTools = loadUi(ui_file_path)
                save_button = self.widget_EasmentTools.pbSave
                cancel_button = self.widget_EasmentTools.pbCancel
 

                # Connect button click signals
                self.connect_button_click_signal()



                self.widget_EasmentTools.show()
                WidgetTools.load_selected_item_name(table, self.widget_EasmentTools)

                self.widget_EasmentTools.dPuhvriSuurus.valueChanged.connect(
                    lambda: WidgetTools.dialer(self.widget_EasmentTools))
                self.widget_EasmentTools.dPuhvriSuurus.setValue(20)

                if self.select_tool is None:
                    WidgetTools.loadselectedProperties(self, self.widget_EasmentTools)
            
            
                clear_table = self.widget_EasmentTools.pbClearCadastrals


                save_button.clicked.connect(lambda: self.on_save_button_clicked())
                cancel_button.clicked.connect(lambda: self.on_cancel_button_clicked())
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

    def connect_button_click_signal(self):
        if self.widget_EasmentTools:
            # Connect the button click signal only if the widget exists
            select_button = self.widget_EasmentTools.pbValiKinnistu
            if not self.select_tool_connection:
                self.select_tool_connection = select_button.clicked.connect(
                    lambda: WidgetTools.activate_layer_and_use_selectTool(self, self.widget_EasmentTools)
                )

    def closeEvent(self, event):
        self.cleanup()
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.informationSimple
        QMessageBox.information(self.widget_EasmentTools, heading, text)
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        active_layer.selectionChanged.disconnect(on_selection_changed_lambda_easements)            
        
        Flags.active_properties_layer_flag = False
        self.widget_EasmentTools.close()
        event.accept()  # Allow the window to close

    def clear_table(self):
        if self.widget_EasmentTools is not None:
            model = self.widget_EasmentTools.tvProperties.model()
            if model is not None:
                model.clear()

    def activate_select_tool(self):
        # Add logic to activate select tool
        pass

    def on_save_button_clicked(self):
        if self.widget_EasmentTools is not None:
            text = "Olen alles arenduses. \n mitte midagi ei salvestatud"
            heading = pealkiri.tubli
            self.cleanup()
            QMessageBox.information(self.widget_EasmentTools, heading, text)
            active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
            active_layer.selectionChanged.disconnect(on_selection_changed_lambda_easements)            
            
            Flags.active_properties_layer_flag = False
            self.widget_EasmentTools.accept()



    def on_cancel_button_clicked(self):
        if self.widget_EasmentTools is not None:
            self.cleanup()
            text = sisu.kasutaja_peatas_protsessi
            heading = pealkiri.informationSimple
            QMessageBox.information(self.widget_EasmentTools, heading, text)
            active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
            active_layer.selectionChanged.disconnect(on_selection_changed_lambda_easements)            
            
            Flags.active_properties_layer_flag = False
            self.widget_EasmentTools.reject()
            


    def cleanup(self):
        if self.is_select_tool_activated:
            # Deactivate select tool
            self.deactivate_select_tool()
            self.is_select_tool_activated = False
            
            
    def deactivate_select_tool(self):
        # Deactivate selection tool
        if self.select_tool:
            iface.mapCanvas().setMapTool(QgsMapToolPan(iface.mapCanvas()))
            self.select_tool = None


class WidgetTools:

    @staticmethod
    def dialer(widget):
        value = widget.dPuhvriSuurus.value() / 10  # divide by 10 to convert to the desired units
        puhver = round(value * 2) / 2  # round up to nearest 0.5 increment
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
            return
        iface.setActiveLayer(active_layer)

        if active_layer and active_layer.selectedFeatureCount() > 0:
            # Show the widget when there are selected features
            PropertiesLayerFunctions.generate_table_from_selected_map_items(self, table_view, active_layer_name)
            table_view.update()
            widget.showNormal()
        pass

    def activate_layer_and_use_selectTool(self, widget):
        #print("started with activated layer")
        global on_selection_changed_lambda_easements
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if not isinstance(active_layer, QgsMapLayer):
            return

        iface.setActiveLayer(active_layer)
        iface.actionSelect().trigger()
        #print("start selecting stuff")
        #Hide the main window
        flag = Flags.active_properties_layer_flag
        #print(f"Flag status befor if statement {flag}")
        
        if active_layer and active_layer.selectedFeatureCount() > 0:
            # Show the widget when there are selected features
            table_view = widget.tvProperties

            help = PropertiesLayerFunctions()
            help.generate_table_from_selected_map_items(table_view, active_layer_name)
            table_view.update()
            widget.showNormal()

        flag = Flags.active_properties_layer_flag
        if flag:
            
            print(f"value of lambda_esaments before connecting: {on_selection_changed_lambda_easements}")
            on_selection_changed_lambda_easements = lambda: WidgetTools.on_selection_changed(widget)
            active_layer.selectionChanged.connect(on_selection_changed_lambda_easements)
            print(f"value of lambda_esaments: {on_selection_changed_lambda_easements}")
            widget.showMinimized()  # Assuming widget is defined somewhere     
            
        else:
            print("Flag is false")


    @staticmethod
    def on_selection_changed(widget):
            
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        if Flags.active_properties_layer_flag:
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
            if active_layer and active_layer.selectedFeatureCount() > 0:
                table_view = widget.tvProperties
                help = PropertiesLayerFunctions()
                help.generate_table_from_selected_map_items(table_view, active_layer_name)
                table_view.update()
                widget.showNormal()
        else:
            # If the flag is false, do nothing
            print("Flag is false")

    @staticmethod
    def load_selected_item_name(table, widget):
        label = widget.lSelectedEasment

        table_headers = queryHandling()
        selected_row_index = table.selectionModel().currentIndex().row()
        model = table.model()
        value_name = table_headers.header_name
        value_number = table_headers.header_number

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
            name = model.data(model.index(selected_row_index, column_index_name))
            number = model.data(model.index(selected_row_index, column_index_number))

            if name is not None and number is not None:
                text = f"{number} - {number}"
            elif name is not None:
                text = name
            elif number is not None:
                text = number
            else:
                text = sisu.puudulikud_andmed

            label.setText(text)

    @staticmethod
    def generate_table(self, widget):
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if not isinstance(active_layer, QgsMapLayer):
            return

        iface.setActiveLayer(active_layer)

        if active_layer and active_layer.selectedFeatureCount() > 0:
            table_view = widget.tvProperties
            help = PropertiesLayerFunctions()
            help.generate_table_from_selected_map_items(table_view, active_layer_name)
            table_view.update()
