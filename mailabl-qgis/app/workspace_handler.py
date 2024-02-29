from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from .ui_controllers import WidgetAnimator
from .list_handler import ExpandProcessListsFunctions
from ..config.settings import SettingsDataSaveAndLoad
from PyQt5.QtWidgets import QMessageBox
from ..Functions.delete_items import Delete_Main_Process
from ..Functions.Contracts.contractsItems import ContractsMain
from ..widgets.helper import place
from ..queries.python.Statuses.statusManager import Statuses,insertStatusToComboBox

from qgis.core import QgsProject
from qgis.utils import iface

    
class WorkSpaceHandler:
    @staticmethod
    def swWorkSpace_Home(self):
        #print("started 'swWorkspace_Home'")
        self.swWorkSpace.setCurrentIndex(5)
        self.sw_HM.setCurrentIndex(0)
    
    @staticmethod    
    def swWorkspace_Projects(self):
        self.swWorkSpace.setCurrentIndex(7)
        self.sw_HM.setCurrentIndex(8) 
        button = self.pbProjects
        button.blockSignals(True)
        table = self.tblMailabl_projects
        statusModule = Statuses()
        module = statusModule.module_projects
        comboBox = self.cmbProjectStatuses
        #QTimer.singleShot(500, lambda: Projects.load_Mailabl_projects_list(self, table))
        insertStatusToComboBox.add_statuses_to_listview(self, comboBox, module )
        statusValue = insertStatusToComboBox.get_selected_status_id(comboBox)
        Projects.load_Mailabl_projects_list(table, statusValue)
        button.blockSignals(False)
    
    @staticmethod
    def swWorkSpace_Contracts_FrontPage(self):
        push_button = self.pbContracts
        push_button.blockSignals(True)
        widget = self.pbContracts_SliderFrame
        WidgetAnimator.toggle_Frame_height_for_settings(self, widget)
        self.sw_HM.setCurrentIndex(1)
        self.swWorkSpace.setCurrentIndex(2)
        table = self.ContractView
        ContractsMain.main_contracts(self, table)
        push_button.blockSignals(False)
    
    @staticmethod
    def swWorkSpace_Substitutes_FrontPage(self):
        self.swWorkSpace.setCurrentIndex(0)
        self.sw_HM.setCurrentIndex(5)
    
    @staticmethod
    def swWorkSpace_MapThemes_FrontPage(self):
        self.swWorkSpace.setCurrentIndex(6)
        self.sw_HM.setCurrentIndex(6)

    @staticmethod
    def swWorkSpace_AddDrawings_FrontPage(self):
        self.swWorkSpace.setCurrentIndex(6)
        self.sw_HM.setCurrentIndex(2)

    @staticmethod        
    def swWorkSpace_Refresh(self):
        label = self.CadastralMovesMainLabel
        heading = "Andmete värskendamine"
        label.setText(heading)
        self.swWorkSpace.setCurrentIndex(1)  # Värskenda olemasolevaid katastri andmeid
        self.swCadastral_sub_processes.setCurrentIndex(3)
        self.sw_HM.setCurrentIndex(3)
        self.sw_HM_Toimingud_kinnistutega.setCurrentIndex(0)
        self.sw_HM_Toimingud_kinnistutega_Laiendamine.setCurrentIndex(0)

    @staticmethod
    def swWorkSpace_Expand(self):
        label = self.CadastralMovesMainLabel
        label.setText("Kinnistute lisamine")
        self.swWorkSpace.setCurrentIndex(1)
        self.swCadastral_sub_processes.setCurrentIndex(0)
        self.sw_HM.setCurrentIndex(3)
        self.sw_HM_Toimingud_kinnistutega.setCurrentIndex(0)
        self.sw_HM_Toimingud_kinnistutega_Laiendamine.setCurrentIndex(0)
        self.pbDone_State.hide()
        self.cbChooseAll_States.hide()
        self.cbChooseAll_Cities.hide()
        self.cbChooseAllAdd_properties.hide()
        self.pbDoneCity.hide()
        self.pbConfirm_action.hide()

        self.listWidget_State.clear()
        self.listWidget_City.clear()
        self.listWidget_county.clear()
        tab_widget = self.tabWidget_Propertie_list
        TabHandler.tabViewByState(tab_widget,True)
        tab_widget.setCurrentIndex(0)
        tab_widget.hide()
        ExpandProcessListsFunctions.get_county_list(self)
    
    @staticmethod
    def swDeleteworkspace(self):
        shp_layer_name = SettingsDataSaveAndLoad.load_SHP_inputLayer_name(self)
        Shp_layer = QgsProject.instance().mapLayersByName(shp_layer_name)[0]
        if Shp_layer:
            QgsProject.instance().layerTreeRoot().findLayer(Shp_layer.id()).setItemVisibilityChecked(False)
        active_cadastral_layer = SettingsDataSaveAndLoad.load_target_cadastral_name(self)
        if active_cadastral_layer:
            layer = QgsProject.instance().mapLayersByName(active_cadastral_layer)[0]
            iface.setActiveLayer(layer)
        else:
            text =("Midagi läks valesti")
            heading = "Hoiatus"
            QMessageBox.warning(self, heading, text)       

        label = self.CadastralMovesMainLabel
        heading = "Kinnistute eemaldamine"
        label.setText(heading)
        self.swWorkSpace.setCurrentIndex(1)  # Eemalda kinnistuid
        self.swCadastral_sub_processes.setCurrentIndex(1)
        self.sw_HM.setCurrentIndex(3)
        self.sw_HM_Toimingud_kinnistutega.setCurrentIndex(1)
        Delete_Main_Process.Delete_process_view_on_load(self)

    @staticmethod
    def Open_generate_mapLayer_synced_with_Mailabl_first_page(self):
        label = self.CadastralMovesMainLabel
        heading = "Sünkroniseeri QGIS Mailabli kinnistutega"
        label.setText(heading)
        lblFor_Sync_GreatLayerName = self.leText_For_Sync_GreateLayerName
        background_gray = "background-color: rgb(52, 59, 71)"
        lblFor_Sync_GreatLayerName.setStyleSheet(background_gray)
        pBar_County_list = self.pBar_Sync_County
        pBar_State_list = self.pBar_State_list 
        pBar_City_list = self.pBar_City_list
        pbar_City_items = self.pBar_CityItems
        
        progress_bars = [pBar_County_list, pBar_State_list, pBar_City_list, pbar_City_items]
        for progress_bar in progress_bars:
            progress_bar.hide()
        self.Sync_Del_bottom.setVisible(False)
        self.frSync_Cadastrals_Main.hide()
        self.frSync_Overview_Main.hide()
        self.frSync_Tools.show()
        
        self.swWorkSpace.setCurrentIndex(1)
        self.swCadastral_sub_processes.setCurrentIndex(2)
        self.sw_HM.setCurrentIndex(3)
        self.sw_HM_Toimingud_kinnistutega.setCurrentIndex(3)   
        
    @staticmethod
    def show_help_update (self):
        self.sw_HM.setCurrentIndex(7)
        self.sw_HM_Andmete_laadimine.setCurrentIndex(0)
        self.swWorkSpace.setCurrentIndex(1)
        self.swCadastral_sub_processes.setCurrentIndex(4)
        
class TabHandler:
    @staticmethod
    def tabViewByState(tab_widget, state: bool):
        if state is True:
            # Assuming tab_widget is your QTabWidget object and index is the index of the tab you want to hide
            tab_widget.setTabEnabled(0, True)
            tab_widget.setTabEnabled(1, True)            
            tab_widget.setTabEnabled(2, False)
            tab_widget.setCurrentIndex(0)

        if state is False:
            print("close")
            tab_widget.setTabEnabled(0, False)
            tab_widget.setTabEnabled(1, False)
            tab_widget.setTabEnabled(2, True)
            tab_widget.setCurrentIndex(2)
        