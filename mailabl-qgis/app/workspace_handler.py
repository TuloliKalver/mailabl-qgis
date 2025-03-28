# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
from PyQt5.QtCore import QObject
from qgis.core import QgsProject
from qgis.utils import iface
from PyQt5.QtWidgets import QMessageBox

from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from .list_handler import ExpandProcessListsFunctions
from ..config.settings import SettingsDataSaveAndLoad
from ..Functions.DeletProcessUIActions import DeletProcessUIActions
from ..Functions.Contracts.Contracts import ContractsMain
from ..Functions.Easements.Easements import EasementssMain
from ..queries.python.Statuses.statusManager import InsertStatusToComboBox
from ..KeelelisedMuutujad.modules import Modules
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..queries.python.Types_Tags.type_tag_manager import InsertTypesToComboBox

 
pealkiri = Headings()

class MyClassWithIndexes():
    def __init__(self):
        self.cadastralmoves = 1
        self.easements = 0
        self.contracts = 2
        self.help = 3
        self.settings = 4
        self.homepage = 5
        self.proerties = 6
        self.projects = 7
        self.removeproperties = 8

    def swWorkSpace(self, index):
        # This is a placeholder method to demonstrate how you might use the MyClassWithIndexes().
        print(f"Switching to workspace index: {index}")
        # Implement your actual workspace switching logic here

class WorkSpaceHandler:
    
    def swWorkSpace_Home(self):
        #ToggleHandler.handle_toggle(state)
        print("started 'swWorkspace_Home'")
        self.swWorkSpace.setCurrentIndex(MyClassWithIndexes().homepage)
        self.sw_HM.setCurrentIndex(0)

    def swWorkSpace_Properties(self):
        print("started 'swWorkspace_Properties'")
        self.swWorkSpace.setCurrentIndex(MyClassWithIndexes().proerties)
        self.sw_HM.setCurrentIndex(0)

    def swWorkspace_Projects(self):
        self.swWorkSpace.setCurrentIndex(MyClassWithIndexes().projects)
        self.sw_HM.setCurrentIndex(8) 
        button = self.pbProjects
        button.blockSignals(True)
        table = self.tblMailabl_projects
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        self.le_searchProjects.clear()

        module = Modules.MODULE_PROJECTS
        comboBox = self.cmbProjectStatuses
        #QTimer.singleShot(500, lambda: Projects.load_Mailabl_projects_list(self, table))
        status_id = SettingsDataSaveAndLoad.load_projects_status_id(self)
        InsertStatusToComboBox.add_statuses_to_combobox_and_set_preferes_status(self, comboBox, module, status_id)
        
        statusValue = InsertStatusToComboBox.get_selected_status_id(comboBox)
        
        Projects.load_projects_by_status(table, statusValue)
        button.blockSignals(False)
    
    def swWorkSpace_Contracts_FrontPage(self):
        push_button = self.pbContracts
        refresh_button = self.pbRefresh_tblMailabl_contracts
        push_button.blockSignals(True)
        refresh_button.blockSignals(True)
        #widget = self.pbContracts_SliderFrame
        #WidgetAnimator.toggle_Frame_height_for_settings(self, widget)
        self.sw_HM.setCurrentIndex(1)
        self.swWorkSpace.setCurrentIndex(MyClassWithIndexes().contracts)
        table = self.ContractView
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        module = Modules.MODULE_CONTRACTS
        combo_box = self.cmbcontractStatuses
        types_combo_box = self.cmbcontractTypes_checkable
        #QTimer.singleShot(500, lambda: Projects.load_Mailabl_projects_list(self, table))
        prefered_statuses = SettingsDataSaveAndLoad.load_contract_status_ids(self)
        InsertStatusToComboBox.add_statuses_to_combobox_and_set_preferes_status(self, combo_box, module, prefered_statuses)
  
        prefered_types = SettingsDataSaveAndLoad.load_contracts_type_names(self)    
        InsertTypesToComboBox.add_elementTypes_to_listview(self, types_combo_box, prefered_types, module)
        selected_types_ids = types_combo_box.checkedItemsData()
        
        statusValue = InsertStatusToComboBox.get_selected_status_id(combo_box)
        # Insert the results to TableView 
        ContractsMain.load_main_contracts_by_type_and_status(self, table, selected_types_ids, statusValue)
                
        push_button.blockSignals(False)
        refresh_button.blockSignals(False)

    def contracts_reload(self):
        refresh_button = self.pbRefresh_tblMailabl_contracts
        refresh_button.blockSignals(True)
        table = self.ContractView
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        comboBox = self.cmbcontractStatuses
        types_combo_box = self.cmbcontractTypes_checkable
        selected_types_ids = types_combo_box.checkedItemsData()
        statusValue = InsertStatusToComboBox.get_selected_status_id(comboBox)  
        ContractsMain.load_main_contracts_by_type_and_status(self, table, selected_types_ids, statusValue)
        refresh_button.blockSignals(False)

    def swWorkSpace_easements_frontpage(self):
        button = self.pbeasements
        button.blockSignals(True)
        self.swWorkSpace.setCurrentIndex(MyClassWithIndexes().easements)
        self.sw_HM.setCurrentIndex(5)
        table = self.tweasementView
        # Assuming 'table' is your QTableView object
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        module = Modules.MODULE_EASEMENTS
        combo_box = self.cmbeasementStatuses
        types_combo_box = self.cmbeasementTypesCheckable
        prefered_statuses = SettingsDataSaveAndLoad.load_easements_status_ids(self)
        if prefered_statuses == '' or None:
            heading = Headings().warningSimple
            text = "Jätkamiseks seadista eelistatud staatus"
            QMessageBox.warning(None, heading, text)
            button.blockSignals(False)
            return
        else:
            InsertStatusToComboBox.add_statuses_to_combobox_and_set_preferes_status(self, combo_box, module, prefered_statuses)
        prefered_types = SettingsDataSaveAndLoad.load_easements_type_names(self)
        if prefered_types == '' or None:
            heading = Headings().warningSimple
            text = "Jätkamiseks seadista eelistatud kitsenduste liigid"
            QMessageBox.warning(None, heading, text)
            button.blockSignals(False)
            return
        else:
            InsertTypesToComboBox.add_elementTypes_to_listview(self, types_combo_box, prefered_types, module)
            
        prefered_types_ids = types_combo_box.checkedItemsData()
        statusValue = InsertStatusToComboBox.get_selected_status_id(combo_box)
        EasementssMain.load_main_asements_by_type_and_status(self, table, prefered_types_ids, statusValue)
        button.blockSignals(False)

    def easements_reload(self):
        button = self.pbeasements
        button.blockSignals(True)
        self.swWorkSpace.setCurrentIndex(MyClassWithIndexes().easements)
        self.sw_HM.setCurrentIndex(5)
        table = self.tweasementView
        # Assuming 'table' is your QTableView object
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        combo_box = self.cmbeasementStatuses
        types_combo_box = self.cmbeasementTypesCheckable
        selected_types_ids = types_combo_box.checkedItemsData()
        statusValue = InsertStatusToComboBox.get_selected_status_id(combo_box)
        EasementssMain.load_main_asements_by_type_and_status(self, table, selected_types_ids, statusValue)
        button.blockSignals(False)
        
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

        active_cadastral_layer = SettingsDataSaveAndLoad().load_target_cadastral_name()
        if active_cadastral_layer:
            layer = QgsProject.instance().mapLayersByName(active_cadastral_layer)[0]
            iface.setActiveLayer(layer)
        else:
            text = HoiatusTexts().error
            heading = pealkiri.warningSimple
            QMessageBox.warning(self, heading, text)       

        label = self.CadastralMovesMainLabel
        heading = "Kinnistute eemaldamine"
        label.setText(heading)
        self.swWorkSpace.setCurrentIndex(1)  # Eemalda kinnistuid
        self.swCadastral_sub_processes.setCurrentIndex(1)
        self.sw_HM.setCurrentIndex(3)
        self.sw_HM_Toimingud_kinnistutega.setCurrentIndex(1)
        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.setCurrentIndex(0)
        DeletProcessUIActions.Delete_process_view_on_load(self)

    @staticmethod
    def Open_generate_mapLayer_synced_with_Mailabl_first_page(self):
        label = self.CadastralMovesMainLabel
        heading = "Sünkroniseerimine"
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
            #print("close")
            tab_widget.setTabEnabled(0, False)
            tab_widget.setTabEnabled(1, False)
            tab_widget.setTabEnabled(2, True)
            tab_widget.setCurrentIndex(2)

class ToggleHandler(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main = main_window
        

    def handle_toggle(self, state):
        if state:
            print("started False toggle setup")
            self.main.ToggleStatus.setText("Olen üldjuhendiga tuttav")
            self.main.teWelcomeContent.setVisible(True)
            self.main.setLayout(self.main.layout1)
            WorkSpaceHandler().swWorkSpace_Home(self.main)
            print("started 'swWorkspace_home'")
        else:
            print("started True toggle setup")
            self.main.ToggleStatus.setText("Nita kirjelduset")
            self.main.teWelcomeContent.setVisible(False)
            self.main.setLayout(self.main.layout2)
            WorkSpaceHandler().swWorkSpace_Properties(self.main, state)
            print("started 'swWorkspace_Proerties'")
        print(f"Toggle switch is {'ON' if state else 'OFF'}")
