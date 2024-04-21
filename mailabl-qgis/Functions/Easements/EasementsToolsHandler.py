


import re
from PyQt5.QtCore import Qt

import processing

from qgis.utils import iface
from qgis.core import QgsMapLayer, QgsProject, QgsProcessingFeatureSourceDefinition

from qgis.gui import QgsMapToolPan
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore

from .EasementsItems import queryHandling
from .resticon import WaterWorks, GetRuledRestriction
from ..Union import Union
from ..propertie_layer.properties_layer_data import PropertiesLayerFunctions
from ..item_selector_tools import UseQGISNative
from ...processes.OnFirstLoad.AddSetupLayers import SetupLayers
from ...config.settings import SettingsDataSaveAndLoad
from ...config.QGISSettingPaths import LayerSettings, SettingsLoader
from ...config.settings import Filepaths, Flags, SettingsDataSaveAndLoad, FilesByNames
from ...processes.infomessages.messages import Headings, HoiatusTexts, EdukuseTexts
from ..intersect import Intersect, TempIntersectLayerName
from ..join_layers import JoinLayers

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()

on_selection_changed_lambda_easements = None

goup_layer_name = ''

class EasementTools:
    def __init__(self, tweasementView):
        self.tweasementView = tweasementView
        self.widget_EasmentTools = None
        self.is_select_tool_activated = False
        self.select_tool = None
        self.select_tool_connection = None
        self.Buffer_tool_connection = None


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
                #buffer_properties_button = self.widget_EasmentTools.pbCreateProperties
                clear_buffer_button = self.widget_EasmentTools.pbClearCadastrals

                
                properties_table = self.widget_EasmentTools.tvProperties
                pbGen_easement = self.widget_EasmentTools.pbKoostaServituut
                # Connect button click signals

                active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
                self.connect_button_click_signal(active_layer_name)

                self.widget_EasmentTools.show()
                self.widget_EasmentTools.tabWidget.hide()

                                # Get the checkboxes and their associated texts and functions
                self.checkboxes_info = EasementTools.get_checkbox_info(self.widget_EasmentTools)

                # Update checkbox texts and connect them to functions
                EasementTools.update_checkboxes(self.checkboxes_info)
                
                WidgetTools.load_selected_item_name(table, self.widget_EasmentTools)

                self.widget_EasmentTools.dPuhvriSuurus.valueChanged.connect(
                    lambda: WidgetTools.activ_dialer(self.widget_EasmentTools))
                self.widget_EasmentTools.dPuhvriSuurus.setValue(20)
                
                if self.select_tool is None:
                    WidgetTools.loadselectedProperties(self, self.widget_EasmentTools)


                pbGen_easement.clicked.connect(lambda: GenerateEasement.generate_easement())            
                
                clear_buffer_button.clicked.connect(lambda: MapCleaners.clearPuhver2m(properties_table))
                #style_name = FilesByNames().Easement_style         
                #buffer_properties_button.clicked.connect(lambda: BufferTools.generate_buffer_around_selected_item(self.widget_EasmentTools, TempBufferLayerNames.buffer_layer_name, active_layer_name, style_name))
                save_button.clicked.connect(lambda: self.on_save_button_clicked(self.checkboxes_info))
                cancel_button.clicked.connect(lambda: self.on_cancel_button_clicked(self.checkboxes_info))
                
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

    def connect_button_click_signal(self, active_layer_name):
        if self.widget_EasmentTools:
            # Connect the button click signal only if the widget exists
            select_button = self.widget_EasmentTools.pbValiKinnistu
            if not self.select_tool_connection:
                self.select_tool_connection = select_button.clicked.connect(
                    lambda: WidgetTools.activate_layer_and_use_selectTool(self, self.widget_EasmentTools)
                )

    @staticmethod
    def get_checkbox_info(widget):
        water_checkbox = getattr(widget, 'cbV', None)
        sewer_checkbox = getattr(widget, 'cbK', None)
        prSewer_checkbox = getattr(widget, 'cbKSK', None)
        drainage_checkbox = getattr(widget, 'cbD', None)
        sewagePumping_checkbox = getattr(widget, 'cbsewagePupming', None)
        SewageDump_checkbox = getattr(widget, 'cbSewageDump', None) #Purgimissõlm
        sewagePlant_checkbox = getattr(widget, 'cbsewagePlant', None)
        WaterStation_checkbox = getattr(widget, 'cbWaterStation', None)
        Rainwater_checkbox = getattr(widget, 'cbSK', None)
        RainPump_checkbox = getattr(widget, 'cbRainPump', None)

      # Define texts for checkboxes
        checkbox_texts = {
            water_checkbox: WaterWorks().survetorustik_1,
            sewer_checkbox: WaterWorks().vabavoolsed_torustikud_1,
            prSewer_checkbox: WaterWorks().survetorustik_1,
            drainage_checkbox: WaterWorks().vabavoolsed_torustikud_1,
            sewagePumping_checkbox: WaterWorks().pumpla_1,
            SewageDump_checkbox: WaterWorks().purgimissõlm,
            sewagePlant_checkbox: WaterWorks().purgimissõlm,
            WaterStation_checkbox: WaterWorks().purgimissõlm,
            Rainwater_checkbox: WaterWorks().vabavoolsed_torustikud_1,
            RainPump_checkbox: WaterWorks().pumpla_1
        }

        # Define lambdas to connect checkboxes to functions (to be implemented)
        checkbox_functions = {
            water_checkbox: lambda: cbMapSelectors.selectWater_pipes(widget, water_checkbox),
            sewer_checkbox: lambda: cbMapSelectors.selectSewer_pipes(widget, sewer_checkbox),
            prSewer_checkbox: lambda: cbMapSelectors.selectprSewer_pipes(widget, prSewer_checkbox),
            drainage_checkbox: lambda: cbMapSelectors.selectDrainage_pipes(widget, drainage_checkbox),
            sewagePumping_checkbox: None ,
            SewageDump_checkbox: None,
            sewagePlant_checkbox: None,
            WaterStation_checkbox: None,
            Rainwater_checkbox: None,
            RainPump_checkbox: None,
        }

        # Create checkboxes_info dictionary
        checkboxes_info = {}
        for checkbox, text in checkbox_texts.items():
            if checkbox:
                checkboxes_info[checkbox] = (text, checkbox_functions.get(checkbox))

        return checkboxes_info

    @staticmethod
    def uncheck_checkboxes(widget, checkboxes_info):
        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                checkbox.setChecked(False)

    @staticmethod
    def update_checkboxes(checkboxes_info):
        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                current_text = checkbox.text()
                if connect_function is not None:
                    checkbox.setStyleSheet("color: #c5c5d2")  # Set text background color and text color
                    #checkbox.setText(f"{current_text}")
                    checkbox.setEnabled(True)
                    checkbox.clicked.connect(connect_function)
                else:
                    checkbox.setText(f"{current_text}* ({text}m)")
                    checkbox.setEnabled(False)
                    checkbox.setStyleSheet("color: #8a95a5")
                    
    def closeEvent(self, event):
        self.cleanup()
        self.Buffer_cleanup()
        if on_selection_changed_lambda_easements:
            active_layer_name = SettingsLoader.get_setting(LayerSettings.CADASTRAL_CURRENT)
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
            active_layer.selectionChanged.disconnect(on_selection_changed_lambda_easements)

        Flags.active_properties_layer_flag = False
        self.widget_EasmentTools.close()
        self.uncheck_checkboxes(self.widget_EasmentTools, self.checkboxes_info)  # Uncheck checkboxes
        event.accept()  # Allow the window to close

    def clear_table(self):
        if self.widget_EasmentTools is not None:
            model = self.widget_EasmentTools.tvProperties.model()
            if model is not None:
                model.clear()

    def on_save_button_clicked(self, checkboxes_info):
        self.Buffer_cleanup()
        if self.widget_EasmentTools is not None:
            text = "Olen alles arenduses. \n mitte midagi ei salvestatud"
            heading = pealkiri.tubli
            self.cleanup()
            self.uncheck_checkboxes(self.widget_EasmentTools, checkboxes_info)  # Uncheck checkboxes
            QMessageBox.information(self.widget_EasmentTools, heading, text)
            if on_selection_changed_lambda_easements:
                active_layer_name = SettingsLoader.get_setting(LayerSettings.CADASTRAL_CURRENT)
                active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
                active_layer.selectionChanged.disconnect(on_selection_changed_lambda_easements)
                self.widget_EasmentTools.pbCreateProperties.disconnect(BufferTools.generate_buffer_around_selected_item)
            Flags.active_properties_layer_flag = False
            
            self.widget_EasmentTools.accept()
            
    def on_cancel_button_clicked(self, checkboxes_info):
        self.Buffer_cleanup()
        if self.widget_EasmentTools is not None:
            self.cleanup()
            text = sisu.kasutaja_peatas_protsessi
            heading = pealkiri.informationSimple
            QMessageBox.information(self.widget_EasmentTools, heading, text)
            if on_selection_changed_lambda_easements:
                active_layer_name = SettingsLoader.get_setting(LayerSettings.CADASTRAL_CURRENT)
                active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
                active_layer.selectionChanged.disconnect(on_selection_changed_lambda_easements)

            Flags.active_properties_layer_flag = False
            self.widget_EasmentTools.reject()
            self.uncheck_checkboxes(self.widget_EasmentTools, checkboxes_info)  # Uncheck checkboxes
            
    def cleanup(self):
        if self.is_select_tool_activated:
            # Deactivate select tool
            self.deactivate_select_tool()
            self.is_select_tool_activated = False
        

    def Buffer_cleanup(self):
        layer_name = SettingsLoader.get_setting(LayerSettings.CADASTRAL_CURRENT)        
        all_fuffers = TempBufferLayerNames.buffer_layers
        for temp_layer_name in all_fuffers:
            MapCleaners.clear_selection_and_delete_temp_layer(layer_name,temp_layer_name)
        
        layer_name = Union().UnionLayer
        layer = QgsProject.instance().mapLayersByName(layer_name)
        if layer:
            layer = layer[0].id()  # Get the first layer if found
            QgsProject.instance().removeMapLayer(layer)
        else:
            # print(f"layer '{layer_name}' not found.")
            pass
        
        WorkLayers = WorkingLayers.list_of_workinglayers()
        for layer_name in WorkLayers:    
            layer = QgsProject.instance().mapLayersByName(layer_name)
            if layer:
                layer = layer[0]
                layer.removeSelection()
            
        
        


    def deactivate_select_tool(self):
        # Deactivate selection tool
        if self.select_tool:
            iface.mapCanvas().setMapTool(QgsMapToolPan(iface.mapCanvas()))
            self.select_tool = None


class WidgetTools:

    @staticmethod
    def activ_dialer(widget):
        WidgetTools.dialer(widget)
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        style_name = FilesByNames().Easement_style
        BufferTools.generate_buffer_around_selected_item(widget,TempBufferLayerNames.buffer_layer_name, active_layer_name, style_name)

    def dialer(widget):
        value = widget.dPuhvriSuurus.value() / 10  # divide by 10 to convert to the desired units
        puhver = round(value * 2) / 2  # round up to nearest 0.5 increment
        widget.label.setText(f'Puhver: {puhver:.1f}m')

        
    @staticmethod
    def loadselectedProperties(self, widget):
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
            active_layer_name = SettingsLoader.get_setting(LayerSettings.CADASTRAL_CURRENT)
            style_name = FilesByNames().Easement_style
            BufferTools.generate_buffer_around_selected_item(widget, TempBufferLayerNames.buffer_layer_name, active_layer_name, style_name)

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
            style_name = FilesByNames().Easement_style
            BufferTools.generate_buffer_around_selected_item(widget, TempBufferLayerNames.buffer_layer_name, active_layer_name, style_name)
            table_view.update()
            widget.showNormal()


        flag = Flags.active_properties_layer_flag
        if flag:
            
          # print(f"value of lambda_esaments before connecting: {on_selection_changed_lambda_easements}")
            on_selection_changed_lambda_easements = lambda: WidgetTools.on_selection_changed(widget)
            active_layer.selectionChanged.connect(on_selection_changed_lambda_easements)
          # print(f"value of lambda_esaments: {on_selection_changed_lambda_easements}")
            widget.showMinimized()  # Assuming widget is defined somewhere     
            
        else:
            # print("Flag is false")
            pass

    @staticmethod
    def on_selection_changed(widget):
            
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        if Flags.active_properties_layer_flag:
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
            if active_layer and active_layer.selectedFeatureCount() > 0:
                table_view = widget.tvProperties
                help = PropertiesLayerFunctions()
                help.generate_table_from_selected_map_items(table_view, active_layer_name)
                style_name = FilesByNames().Easement_style
                BufferTools.generate_buffer_around_selected_item(widget, TempBufferLayerNames.buffer_layer_name, active_layer_name, style_name)

                table_view.update()
                widget.showNormal()
        else:
            # If the flag is false, do nothing
            # print("Flag is false")
            pass

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

            if name !='' and number !='':
                text = f"{number} {name}"
            
            
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


class TempBufferLayerNames:
    water_temp_name = 'Ajutine_V'
    sewer_temp_name = 'Ajutine_K'
    prSewer_temp_name = 'Ajutine_KS'
    drainage_temp_name = 'Ajudine_D'
    buffer_layer_name = 'puhver_kinnistu'
    buffer_layers = [water_temp_name, sewer_temp_name,prSewer_temp_name, drainage_temp_name, buffer_layer_name]
    
class WorkingLayers:
    water_layer_name = SettingsLoader.get_setting(LayerSettings.WATER_LAYER)        
    sewer_layer_name = SettingsLoader.get_setting(LayerSettings.SEWER_LAYER)        
    prSewer_layer_name = SettingsLoader.get_setting(LayerSettings.PRESSURE_SEWER_LAYER)        
    drainage_layer_name = SettingsLoader.get_setting(LayerSettings.DRAINAGE_LAYER)        

    @staticmethod
    def list_of_workinglayers():
        a = WorkingLayers
        list_of_working_layers = [a.water_layer_name, a.sewer_layer_name, a.prSewer_layer_name, a.drainage_layer_name]
        return list_of_working_layers    

class BufferTools:    
    def generate_buffer_around_selected_item(widget, tempp_buffer_layer, layer_name, style_name, checkbox=None, insert_distance = None):
        #print(f"in generator. tempp_buffer_layer: {tempp_buffer_layer}, layer_name: {layer_name}")
        active_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        
        if active_layer:
            #print("yess")
            # Check if there are any selected features
            if active_layer.selectedFeatureCount() > 0:
                #print("yess 2")
                # Get the selected features
                selected_features = active_layer.selectedFeatures()
                
                # Determine the distance for buffering
                if insert_distance is not None:
                # Convert comma to period if necessary
                   distance = insert_distance.replace(',', '.')

                else:
                    # Calculate distance based on widget value
                    puhver = widget.dPuhvriSuurus.value() / 10
                    distance = round(puhver * 2) / 2

                result = processing.run("native:buffer", {
                    'INPUT': QgsProcessingFeatureSourceDefinition(active_layer.source(), True),
                    'DISTANCE': distance,
                    'SEGMENTS': 5,
                    'OUTPUT': 'memory:',
                    'FEATURES': selected_features,
                    'DISSOLVE': False,
                    'END_CAP_STYLE': 0,
                    'JOIN_STYLE': 0,
                    'MITER_LIMIT': 2,
                })
                
                # Load the QGIS layer style

                QGIS_Layer_style = Filepaths().get_style(style_name)

                # Get the group layer name
                group_layer_name = SetupLayers().tools_layer_name

                # Get the group layer or create it if it doesn't exist
                root = QgsProject.instance().layerTreeRoot()
                group = root.findGroup(group_layer_name)
                if group is None:
                    group = root.addGroup(group_layer_name)

                # Check if a layer with the same name already exists
                existing_layers = QgsProject.instance().mapLayersByName(tempp_buffer_layer)
                if existing_layers:
                    # Remove the existing layer before continuing
                    QgsProject.instance().removeMapLayer(existing_layers[0])
                    
                # Add the buffer layer to the group layer
                buffer_layer = QgsProject.instance().addMapLayer(result['OUTPUT'], False)
                buffer_layer.setName(tempp_buffer_layer)
                group.addLayer(buffer_layer)
                
                # Apply the layer style
                buffer_layer.loadNamedStyle(QGIS_Layer_style)
                buffer_layer.triggerRepaint()



            else:
                QMessageBox.information(None, Headings().informationSimple, HoiatusTexts().kihil_kinnistu_valik)
                if checkbox is not None:
                    checkbox.setChecked(False)
                
        else:
            QMessageBox.warning(None, Headings().warningCritical, HoiatusTexts().puudulik_kinnistute_seadistus)
            if checkbox is not None:
                    checkbox.setChecked(False)
                
class cbMapSelectors:    

    def selectWater_pipes(widget, checkbox):
        print(f"ccheckbox: {checkbox}")
        water_layer_name = SettingsLoader.get_setting(LayerSettings.WATER_LAYER)
                
        temp_layer_name = TempBufferLayerNames.water_temp_name
        properties_buffer = TempBufferLayerNames.buffer_layer_name
        
        depth = widget.lblHV.text()
        inner_diameter = widget.lblDeV.text()

        if checkbox.isChecked():
            selected_features = UseQGISNative.select_elements_from_layer(water_layer_name, properties_buffer, widget)
            #diameters, begin_z_coords = UseQGISNative.get_diameter_and_Z(selected_features)

            #print("diameters")
            #print(diameters)

            #print("z_coordinat")
            #print(begin_z_coords)

            style_name = FilesByNames().Easement_Water

            distance = GetRuledRestriction.check_waterworks_rule(inner_diameter, depth)
            print(f"Applicable restriction: {distance}")

            checkbox.setText(f"Torud ({distance}m)")
            #distance = WaterWorks.vabavoolsed_torustikud_1
            BufferTools.generate_buffer_around_selected_item(widget, temp_layer_name, water_layer_name, style_name, checkbox, distance)
        if not checkbox.isChecked():
            MapCleaners.clear_selection_and_delete_temp_layer(water_layer_name, temp_layer_name)
    
    def selectSewer_pipes(widget, checkbox):
        print(f"ccheckbox: {checkbox}")
        sewer_layer_name = SettingsLoader.get_setting(LayerSettings.SEWER_LAYER)        
        temp_layer_name = TempBufferLayerNames.sewer_temp_name
        properties_buffer = TempBufferLayerNames.buffer_layer_name

        depth = widget.lblHK.text()
        inner_diameter = widget.lblDeK.text()

        distance = GetRuledRestriction.check_waterworks_rule(inner_diameter, depth)
        print(f"Applicable restriction: {distance}")

        checkbox.setText(f"Torud ({distance}m)")


        if checkbox.isChecked():
            UseQGISNative.select_elements_from_layer(sewer_layer_name, properties_buffer, widget)
            style_name = FilesByNames().Easement_sewage
            distance = GetRuledRestriction.check_waterworks_rule(inner_diameter, depth)
            print(f"Applicable restriction: {distance}")

            #distance = WaterWorks.vabavoolsed_torustikud_1
            BufferTools.generate_buffer_around_selected_item(widget, temp_layer_name, sewer_layer_name, style_name, checkbox, distance)
        if not checkbox.isChecked():
            MapCleaners.clear_selection_and_delete_temp_layer(sewer_layer_name, temp_layer_name)
    
    def selectprSewer_pipes(widget, checkbox):
        print(f"ccheckbox: {checkbox}")
        prSerer_layer_name = SettingsLoader.get_setting(LayerSettings.PRESSURE_SEWER_LAYER)        
        temp_layer_name = TempBufferLayerNames.prSewer_temp_name
        properties_buffer = TempBufferLayerNames.buffer_layer_name

        depth = widget.lblHK.text()
        inner_diameter = widget.lblDeK.text()

        distance = GetRuledRestriction.check_waterworks_rule(inner_diameter, depth)
        print(f"Applicable restriction: {distance}")

        checkbox.setText(f"Surve torud ({distance}m)")


        if checkbox.isChecked():
            UseQGISNative.select_elements_from_layer(prSerer_layer_name, properties_buffer, widget)
            style_name = FilesByNames().Easement_prSewage
            #distance = WaterWorks.survetorustik_1
            BufferTools.generate_buffer_around_selected_item(widget, temp_layer_name, prSerer_layer_name, style_name, checkbox, distance)
        if not checkbox.isChecked():
            MapCleaners.clear_selection_and_delete_temp_layer(prSerer_layer_name, temp_layer_name)
    

    def selectDrainage_pipes(widget, checkbox):
        print(f"ccheckbox: {checkbox}")
        drainage_layer_name = SettingsLoader.get_setting(LayerSettings.DRAINAGE_LAYER)        
        temp_layer_name = TempBufferLayerNames.drainage_temp_name
        properties_buffer = TempBufferLayerNames.buffer_layer_name
    
        depth = widget.lblHK.text()
        inner_diameter = widget.lblDeK.text()

        distance = GetRuledRestriction.check_waterworks_rule(inner_diameter, depth)
        print(f"Applicable restriction: {distance}")

        checkbox.setText(f"Drenaaž ({distance}m)")


        if checkbox.isChecked():
            UseQGISNative.select_elements_from_layer(drainage_layer_name, properties_buffer, widget)
            style_name = FilesByNames().Easement_Drainage
            #distance = WaterWorks.vabavoolsed_torustikud_1
            BufferTools.generate_buffer_around_selected_item(widget, temp_layer_name, drainage_layer_name, style_name, checkbox, distance)
        if not checkbox.isChecked():
            MapCleaners.clear_selection_and_delete_temp_layer(drainage_layer_name, temp_layer_name)

        

class MapCleaners:
    @staticmethod
    def clear_selection_and_delete_temp_layer(layer_name, temp_layer_name):
      # print(f"temp_layer_name: {temp_layer_name}")
        # Clear the selection when checkbox is unchecked
        layer = QgsProject.instance().mapLayersByName(layer_name)
        if layer:
            layer = layer[0]
            layer.removeSelection()
        else:
            # print(f"layer '{layer_name}' not found.")
            pass
        # Delete the temporary layer
        temp_layer = QgsProject.instance().mapLayersByName(temp_layer_name)
        if temp_layer:
            temp_layer = temp_layer[0]
            QgsProject.instance().removeMapLayer(temp_layer.id())
        else:
            # print(f"Temporary layer '{temp_layer_name}' not found.")
            pass
        iface.mapCanvas().refresh()


    def clearPuhver2m(table):
        layer_name = SettingsLoader.get_setting(LayerSettings.CADASTRAL_CURRENT)
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        if layer:
            layer.removeSelection()
        else:
            # print('No ei ole ju enam olemas!')
            pass
        temp_layer_name = TempBufferLayerNames.buffer_layer_name
        MapCleaners.clear_selection_and_delete_temp_layer(layer_name, temp_layer_name)
        # Clear the model from rows
        model = table.model()
        rowCount = model.rowCount()
        model.removeRows(0, rowCount)
        iface.mapCanvas().refresh()


class GenerateEasement:
    @staticmethod
    def generate_easement():
        print("started Intersection")
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()

        # Slice the lists to include only the first four items
        buffer_layers = TempBufferLayerNames.buffer_layers[:4]
        intersect_layers = TempIntersectLayerName.intersect_layers[:4]
        

        # Create a dictionary to map buffer layers to intersect layers
        layer_mapping = dict(zip(buffer_layers, intersect_layers))
        #print("mapped layers:")
        #print(layer_mapping)
        # Iterate through the buffer layers and perform operations for each
        
        for buffer_layer in buffer_layers:
            intersect_layer = layer_mapping.get(buffer_layer)

            if intersect_layer:  # Check if intersect layer exists
                Intersect.intersect_two_layers(buffer_layer, active_layer_name, intersect_layer)
        
        intersect_layers = QgsProject.instance().mapLayers().values()
        intersect_layer_names = [layer.name() for layer in intersect_layers if layer.name().startswith("Ajutine_intersect_")]
        #print("intersect_layer_names:")
        #print(intersect_layer_names)
        if not intersect_layer_names:
            #print("No intersect layers found.")
            return
        # Check if join layer exists and remove it if present
        existing_layers = QgsProject.instance().mapLayersByName(JoinLayers.join_layer_name)
        if existing_layers:
            for layer in existing_layers:
                if layer:
                    layer = layer[0].id()  # Get the first layer if found
                    QgsProject.instance().removeMapLayer(layer)
                else:
                    #print(f"layer '{layer}' not found.")
                    pass

 
        # Check the number of intersect layers found
        num_intersect_layers = len(intersect_layer_names)
        #print("num_intersect_layers:")
        #print(num_intersect_layers)
        join_layer_name = "Joined_layer"
        while num_intersect_layers >= 1:
            JoinLayers.join_all_layers(intersect_layer_names, num_intersect_layers, join_layer_name)
                # Decrement the number of intersect layers
            num_intersect_layers -= 1
        # Remove buffer and intersect layers from the project
        
        for layer_name in buffer_layers + TempIntersectLayerName.intersect_layers:
            layer = QgsProject.instance().mapLayersByName(layer_name)
            if layer:
                layer = layer[0].id()  # Get the first layer if found
                QgsProject.instance().removeMapLayer(layer)
            else:
                # print(f"layer '{layer_name}' not found.")
                pass

        joined_layers = QgsProject.instance().mapLayers().values()
        joined_layer_names = [layer.name() for layer in joined_layers if layer.name().startswith("Joined_layer")]
        num_join_layers = len(joined_layer_names)
        #print("num_join_layers")
        #print(num_join_layers)
        final_layer_name = "Final_joined"

        while num_join_layers >= 1:
            #print("num_join_layers in loop")
            #print(num_join_layers)
            JoinLayers.join_all_layers(joined_layer_names, num_join_layers, final_layer_name)
                # Decrement the number of intersect layers
            num_join_layers -= 1
        
        joined_layers = QgsProject.instance().mapLayers().values()
        joined_layer_name = [layer.name() for layer in joined_layers if layer.name().startswith(final_layer_name)]
        print(f"joined_layer_name: {joined_layer_name}")        
        Union.make_unioned_layer(joined_layer_name)

        working_layers = WorkingLayers.list_of_workinglayers() 
        working_layers.append(active_layer_name)
        
        for layer_name in working_layers:          
            layer = QgsProject.instance().mapLayersByName(layer_name)
            if layer:
                layer = layer[0]
                layer.removeSelection()
            else:
                # print(f"layer '{layer_name}' not found.")
                pass

        properties_buffer = TempBufferLayerNames.buffer_layer_name    
        layer = QgsProject.instance().mapLayersByName(properties_buffer)
        if layer:
            layer = layer[0].id()  # Get the first layer if found
            QgsProject.instance().removeMapLayer(layer)
        else:
            # print(f"layer '{layer_name}' not found.")
            pass
