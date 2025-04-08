from PyQt5.QtWidgets import QTableView
from qgis.core import QgsProject
from ...app.View_tools import shp_tools
from ...app.workspace_handler import TabHandler
from ...app.View_tools import listView_functions, shp_tools, tableView_functions
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...config.settings import SettingsDataSaveAndLoad

county_nimi_field = Katastriyksus.mk_nimi #'MK_NIMI'
state_nimi_field = Katastriyksus.ov_nimi #'OV_NIMI'
city_nimi_field = Katastriyksus.ay_nimi #"AY_NIMI"
list_functions = listView_functions()
table_functions = tableView_functions()

class AddProcessPrepareTables:
    def __init__(self, parent):
        self.ad = parent

        self.tab_widget = self.ad.tabWidget_Propertie_list
        self.viewItem_county = self.ad.listWidget_county
        self.viewItem_state = self.ad.listWidget_State
        self.viewItem_city = self.ad.listWidget_City
        self.tv_streets = self.ad.tblvResults_streets_Confirm
        self.tv_properties = self.ad.tblvResults_Confirm
        self.cb_properties = self.ad.cbChooseAllAdd_properties
        self.cb_streets = self.ad.cbChooseAllAdd__street_properties
        self.cb_streets_include = self.ad.cbOnPropertiesTab_Include_streets
        self.confirmbutton = self.ad.pbConfirm_action
        self.help_menu = self.ad.sw_HM
        self.help_menu_properties = self.ad.sw_HM_Toimingud_kinnistutega
        self.help_menu_expand = self.ad.sw_HM_Toimingud_kinnistutega_Laiendamine


    # Loads only properties that are not "streets or roads"
    def prepare_properties_list_and_Add_to_table_updated_with_selecting_items(self):
        self.update_ui()



        TabHandler.tabViewByState_NOT_NEEDED(self.tab_widget, state=True)
        input_layer_name = SettingsDataSaveAndLoad().load_SHP_inputLayer_name()
        layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        layer.blockSignals(True)
        layer.removeSelection()
        layer.blockSignals(False)

        list_functions.unload_and_hide_connectedItems([], [self.tv_streets, self.tv_properties], [], [
                                                      self.cb_properties, self.cb_streets])

        self.cb_properties.blockSignals(True)
        self.cb_streets.blockSignals(True)
        self.cb_streets_include.blockSignals(True)

        item_county = self.viewItem_county.currentItem()
        item_state = self.viewItem_state.selectedItems()
        item_city = self.viewItem_city.selectedItems()

        county_restriction = item_county.text() if item_county is not None else ""
        state_restrictions = "', '".join([item.text() for item in item_state]) if item_state else ""
        city_restrictions = "', '".join([item.text() for item in item_city]) if item_city else ""


        self.cb_properties.show()
        self.cb_streets.show()
        self.cb_streets_include.show()
        
        expression = shp_tools._builds_universal_query_based_restrictions(
            
            county_nimi_field,
            state_nimi_field,
            city_nimi_field,
            county_restriction,
            state_restrictions,
            city_restrictions
        )

        layer.setSubsetString(expression)
        layer.triggerRepaint()
        layer.updateExtents()
        layer.blockSignals(True)
        layer.selectAll()
        model_properties, model_streets, total = table_functions.generate_table_from_selected_map_items_with_roads(input_layer_name)

        self.ad.lblCount.setText(str(total))

        self.tv_streets.setModel(model_streets)
        self.tv_properties.setModel(model_properties)

        self.adjust_table_view(self.tv_streets)
        self.adjust_table_view(self.tv_properties)

        self.cb_properties.blockSignals(False)
        self.cb_streets.blockSignals(False)
        self.cb_streets_include.blockSignals(False)

        self.cb_properties.setChecked(True)
        self.cb_streets.setChecked(True)
        self.cb_streets_include.setChecked(True)

        layer.blockSignals(False)

        self.confirmbutton.show()

        # Connect the selection change signal to the slot after setting the model
        #self.tv_properties.selectionModel().selectionChanged.connect(lambda selected, deselected: list_functions.onSelectionChangeReturnChanges(selected, deselected, table=self.tv_properties))
        self.tv_properties.selectionModel().selectionChanged.connect(lambda: list_functions.getAllSelectedRowsData(table1=self.tv_properties, table2=self.tv_streets))
        self.tv_streets.selectionModel().selectionChanged.connect(lambda: list_functions.getAllSelectedRowsData(table1=self.tv_properties, table2=self.tv_streets))


    def adjust_table_view(self, table_view):
        custom_row_height = 20
        for row in range(table_view.model().rowCount()):
            table_view.setRowHeight(row, custom_row_height)

        table_view.setSortingEnabled(True)
        table_view.verticalHeader().setVisible(False)
        table_view.setShowGrid(False)
        table_view.resizeColumnsToContents()
        table_view.setEditTriggers(QTableView.NoEditTriggers)

    def update_ui(self):
        self.help_menu.setCurrentIndex(3)
        self.help_menu_properties.setCurrentIndex(0)
        self.help_menu_expand.setCurrentIndex(3)
        self.tab_widget.setCurrentIndex(0)
        self.tab_widget.show()

