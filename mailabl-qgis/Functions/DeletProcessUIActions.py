#DeleteProcessUIActions.py

from ..utils.UIDeleteTables import UIDeleteTables
from ..utils.UIDeleteButtonsManager import UIDeleteButtonsManager
from ..utils.UIDeleteCheckboxes import UIDeleteCheckboxes
from ..utils.UIDeleteFrames import UIDeleteFrames
from ..utils.UIDeleteListViews import UIDeleteListViews
from ..Functions.delete_items import DeletingProcesses
from ..utils.UIDeleteCheckboxes import UIDeleteCheckboxes
from ..utils.TableUtilys.TableHelpers import TableDataInserter
#from ..Functions.RemoveProperties.RemoveSelectedProperties import DeleteActions
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from PyQt5.QtWidgets import QMessageBox
from ..config.settings import SettingsDataSaveAndLoad
from ..app.View_tools import  shp_tools, tableView_functions
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from qgis.core import QgsProject

table_functions = tableView_functions()

county_nimi_field = Katastriyksus.mk_nimi #'MK_NIMI'
state_nimi_field = Katastriyksus.ov_nimi #'OV_NIMI'
city_nimi_field = Katastriyksus.ay_nimi #"AY_NIMI"

def get_selected_item_text(item):
    return item.text() if item else ""


class DeletProcessUIActions():

    def Delete_process_view_on_load(self):
        UIDeleteButtonsManager.buttons_on_load(self)
        UIDeleteCheckboxes.checkboxes_on_load(self)
        UIDeleteTables.tables_on_load(self)
        UIDeleteFrames.frames_on_load(self)
        UIDeleteListViews.clear_all_views(self)
        UIDeleteListViews.selection_model_views_on_load(self)
        DeletingProcesses.get_county_list_delete(self)


    def Delete_process_view_on_countyListView_click(self):
        UIDeleteButtonsManager.buttons_on_load(self)
        UIDeleteCheckboxes.checkboxes_on_load(self)
        UIDeleteTables.tables_on_load(self)
        UIDeleteFrames.frames_on_load(self)
        UIDeleteListViews.clear_after_county(self)

    #County views
    def Delete_process_view_after_county(self):
        UIDeleteButtonsManager.buttons_show_after_county(self)
        UIDeleteCheckboxes.checkboxes_on_after_county(self)
        UIDeleteFrames.frames_on_load(self)


    def Delete_process_view_after_unsuccessful_county(self):
        UIDeleteButtonsManager.buttons_on_load(self)
        UIDeleteCheckboxes.checkboxes_on_load(self)
        UIDeleteFrames.frames_on_load(self)

    #state views
    def Delete_process_view_after_state(self):
        UIDeleteButtonsManager.buttons_show_after_state(self)
        UIDeleteCheckboxes.checkboxes_on_after_state(self)
        UIDeleteFrames.frames_on_load(self)
        UIDeleteTables.tables_on_load(self)


    def Delete_process_view_after_unsuccessful_state(self):
        UIDeleteButtonsManager.buttons_show_after_county(self)
        UIDeleteCheckboxes.checkboxes_on_after_county(self)
        UIDeleteFrames.frames_on_load(self)

    #city views
    def Delete_process_view_after_city(self):
        UIDeleteButtonsManager.buttons_show_after_city(self)
        UIDeleteCheckboxes.checkboxes_on_after_city(self)
        UIDeleteFrames.frames_after_city(self)
        UIDeleteTables.table_after_city(self)

    def Delete_process_view_after_unsuccessful_city(self):
        UIDeleteButtonsManager.buttons_show_after_state(self)
        UIDeleteCheckboxes.checkboxes_on_after_state(self)
        UIDeleteFrames.frames_on_load(self)
        UIDeleteTables.table_after_unsuccessful_city(self)


class DeleteProcessHandlers:

    def __init__(self, ui):
        self.button_del_county = getattr(ui, 'pbDel_County', None)
        self.button_del_state = getattr(ui, 'pbDel_State', None)
        self.button_del_city = getattr(ui, 'pbDel_City', None)
        self.lwDel_County_Names = getattr(ui, 'lwDelete_County_Names', None)
        self.lwDel_State_names = getattr(ui, 'lwDelete_State_Names', None)
        self.lwDel_City_Names = getattr(ui, 'lwDelete_Cities_Names', None)
        self.label_del_amount = getattr(ui, 'lblDel_Amount', None)
        self.tbl_delete_streets = getattr(ui, 'tbl_Delete_streets', None)
        self.tbl_delete_properties = getattr(ui, 'tbl_Delete_properties', None)
        self.tabw_delete_list = getattr(ui, 'tabW_Delete_list', None)

    def Delete_reset_stage(self):
        DeletProcessUIActions.Delete_process_view_on_countyListView_click(self)

    def Delete_reset_to_stage_state(self):
        DeletProcessUIActions.Delete_process_view_after_state(self)
        if self.button_del_city:
            self.button_del_city.hide()
        if self.lwDel_City_Names:
            self.lwDel_City_Names.clear()

    def delete_process_after_county(self):
        if not self.lwDel_County_Names or not self.lwDel_County_Names.selectedItems():
            DeletProcessUIActions.Delete_process_view_after_unsuccessful_county(self)
            QMessageBox.warning(None, Headings().warningSimple, HoiatusTexts().maakond_valimata)
        else:
            DeletProcessUIActions.Delete_process_view_after_county(self)
            activ_cadastral_layer = SettingsDataSaveAndLoad().load_target_cadastral_name()
            DeletingProcesses().DeleteProcess_get_state_list(
                self.button_del_county, activ_cadastral_layer, state_nimi_field, county_nimi_field, city_nimi_field,
                self.lwDel_County_Names, self.lwDel_State_names, self.lwDel_City_Names, self.label_del_amount)

    def delete_process_after_state(self):
        if not self.lwDel_State_names or not self.lwDel_State_names.selectedItems():
            DeletProcessUIActions.Delete_process_view_after_unsuccessful_state(self)
            QMessageBox.warning(None, Headings().warningSimple, HoiatusTexts().omavalitsus_valimata)
        else:
            DeletProcessUIActions.Delete_process_view_after_state(self)
            activ_cadastral_layer = SettingsDataSaveAndLoad().load_target_cadastral_name()
            DeletingProcesses().DeleteProcess_get_city_list(
                self.button_del_state, activ_cadastral_layer, state_nimi_field, city_nimi_field,
                self.lwDel_State_names, self.lwDel_City_Names, self.label_del_amount)

    def delete_process_after_city(self):
        from ..app.workspace_handler import TabHandler
        TabHandler.tabViewByState(self.tabw_delete_list, state=True)
        if not self.lwDel_State_names or not self.lwDel_State_names.selectedItems():
            DeletProcessUIActions.Delete_process_view_after_unsuccessful_city(self)
            QMessageBox.warning(None, Headings().warningSimple, HoiatusTexts().omavalitsus_valimata)
        else:
            DeletProcessUIActions.Delete_process_view_after_city(self)
            layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
            layer = QgsProject.instance().mapLayersByName(layer_name)[0]
            layer.removeSelection()

            county_restriction = get_selected_item_text(self.lwDel_County_Names.currentItem())
            state_restrictions = ", ".join(get_selected_item_text(item) for item in self.lwDel_State_names.selectedItems())
            city_restrictions = ", ".join(get_selected_item_text(item) for item in self.lwDel_City_Names.selectedItems())

            self.tabw_delete_list.setCurrentIndex(0)
            self.tabw_delete_list.show()

            expression = shp_tools.universal_map_simplifier(
                layer_name, county_nimi_field, state_nimi_field, city_nimi_field,
                county_restriction, state_restrictions, city_restrictions
            )

            layer.setSubsetString(expression)
            layer.triggerRepaint()
            layer.updateExtents()
            layer.selectAll()
            shp_tools.activateLayer_zoomTo(layer)

            properties_model, streets_model, total = table_functions.generate_table_from_selected_map_items_with_roads(layer_name)
            inserter = TableDataInserter()
            inserter.insert_data_to_tables(
                tables_with_models=[(self.tbl_delete_streets, streets_model), (self.tbl_delete_properties, properties_model)],
                total=total, total_label=self.label_del_amount
            )

        UIDeleteCheckboxes.checkboxes_on_after_city(self)

    def DeleteProcess_check_validity_in_Mylabl(self):
        DeleteActions.delete_selected_items_from_mylabl(self)
