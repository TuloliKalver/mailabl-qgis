#delete_items.py

import os
from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox
from ..app.View_tools import listView_functions, tableView_functions, shp_tools
from ..config.settings import SettingsDataSaveAndLoad
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..utils.signal_utils import block_signals
from ..utils.layer_processing_utils import retrieve_and_process_layer, apply_subset_filter, no_filter



table_functions = tableView_functions()
pealkiri = Headings()

county_nimi_field = Katastriyksus.mk_nimi #'MK_NIMI'
state_nimi_field = Katastriyksus.ov_nimi #'OV_NIMI'
city_nimi_field = Katastriyksus.ay_nimi #"AY_NIMI"

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Status bar widget folder
widgets_folder = "widgets"
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))

list_functions = listView_functions()
load = SettingsDataSaveAndLoad()



class DeletingProcesses:

    def get_county_list_delete(self):
        county_field = Katastriyksus.mk_nimi
        lw_county = self.lwDelete_County_Names 
        lbl = self.lblDel_Amount     
        layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        expression = ""
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]

        if layer.isValid():
            layer.setSubsetString(expression)
            layer.triggerRepaint()
            layer.updateExtents()
            shp_tools.activateLayer_zoomTo(layer)

            county_list = retrieve_and_process_layer(
                layer_name=layer_name,
                filter_function=no_filter,
                process_function=lambda feature: feature[county_field]
            )

            list_functions.insert_values_to_listView_object(lw_county, county_list)

            item_count = shp_tools.count_items_in_layer(layer_name)
            lbl.setText(f"{item_count}")
        else:
            print(f"Layer {layer} not found")

    def process_layer_selection(self, button, layer_name, field_to_filter, filter_value,
                                process_field, list_widget, lbl, county_restriction="", state_restrictions=""):
        with block_signals(button):
            try:
                layer = QgsProject.instance().mapLayersByName(layer_name)[0]
            except IndexError:
                text = (f"Laetavate kinnistute kiht {layer_name} on puudu.\nJätkamiseks lae algandmed")
                heading = pealkiri.warningSimple
                QMessageBox.warning(None, heading, text)
                return

            data_list = retrieve_and_process_layer(
                layer_name=layer_name,
                filter_function=lambda feature: feature[field_to_filter] == filter_value,
                process_function=lambda feature: feature[process_field]
            )

            list_functions.insert_values_to_listView_object(list_widget, data_list)
            apply_subset_filter(layer, layer_name, field_to_filter, process_field,
                                county_restriction, state_restrictions)

            item_count = shp_tools.count_items_in_layer(layer_name)
            lbl.setText(f"{item_count}")

    def DeleteProcess_get_state_list(self, button, layer_name, state_field,
                                     county_field, city_field,
                                     lwDel_County_Names, lwDel_State_names,
                                     lwDel_City_Names, lbl):
        item_county = lwDel_County_Names.currentItem()
        county_restriction = item_county.text() if item_county else ""
        self.process_layer_selection(button, layer_name, county_field, county_restriction,
                                     state_field, lwDel_State_names, lbl, county_restriction)

    def DeleteProcess_get_city_list(self, button, layer_name, state_field,
                                    city_field,
                                    lwDel_State_names,
                                    lwDel_City_Names, lbl):
        item_state = lwDel_State_names.selectedItems()
        state_restrictions = [item.text() for item in item_state] if item_state else []
        for state in state_restrictions:
            self.process_layer_selection(button, layer_name, state_field, state,
                                         city_field, lwDel_City_Names, lbl, state_restrictions=state_restrictions)
            


class MapRestictionsAndListWidgetDataInserion():
    def get_state_list(self, button, layer_name, state_field,
                                     county_field, city_field,
                                     lwDel_County_Names, lwDel_State_names,
                                     lwDel_City_Names, lbl):
        item_county = lwDel_County_Names.currentItem()
        county_restriction = item_county.text() if item_county else ""
        DeletingProcesses.process_layer_selection(button, layer_name, county_field, county_restriction,
                                     state_field, lwDel_State_names, lbl, county_restriction)

    def get_city_list(self, button, layer_name, state_field,
                                    city_field,
                                    lwDel_State_names,
                                    lwDel_City_Names, lbl):
        item_state = lwDel_State_names.selectedItems()
        state_restrictions = [item.text() for item in item_state] if item_state else []
        for state in state_restrictions:
            DeletingProcesses.process_layer_selection(button, layer_name, state_field, state,
                                         city_field, lwDel_City_Names, lbl, state_restrictions=state_restrictions)