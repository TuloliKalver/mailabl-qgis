# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
from qgis.core import QgsProject
from qgis.utils import iface

from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from .list_handler import ExpandProcessListsFunctions_NOT_NEEDED
from ..config.settings import SettingsDataSaveAndLoad
from ..Functions.DeletProcessUIActions import DeletProcessUIActions
from ..Functions.Contracts.Contracts import ContractsMain
from ..Functions.Easements.Easements import EasementssMain
from ..utils.ComboboxHelper import GetValuesFromComboBox
from ..KeelelisedMuutujad.modules import Module
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts

from ..utils.ComboboxHelper import ComboBoxHelper
from ..utils.messagesHelper import ModernMessageDialog


pealkiri = Headings()
combo_handler = ComboBoxHelper()

class CenterMainSliderIndexes():
    EASEMENTS = 0
    CADASTRALMOVES = 1
    CONTRACTS = 2
    HELP = 3
    SETTINGS = 4
    HOMEPAGE = 5
    PROPERTIES = 6
    PROJECTS = 7
    REMOVEPROPERTIES = 8
    PROPERTIES_OPERATIONS = 9

    def swWorkSpace(self, index):
        # This is a placeholder method to demonstrate how you might use the MyClassWithIndexes().
        print(f"Switching to workspace index: {index}")
        # Implement your actual workspace switching logic here

class WorkSpaceHandler:
    
    def swWorkSpace_Home(self):
        print("started 'swWorkspace_Home'")
        self.swWorkSpace.setCurrentIndex(CenterMainSliderIndexes.HOMEPAGE)
        self.sw_HM.setCurrentIndex(0)

    def swWorkSpace_Properties(self):
        print("started 'swWorkspace_Properties'")
        self.swWorkSpace.setCurrentIndex(CenterMainSliderIndexes.PROPERTIES)
        self.sw_HM.setCurrentIndex(0)

    def swWorkspace_Projects(self):
        module = Module.PROJECT
        self.swWorkSpace.setCurrentIndex(CenterMainSliderIndexes.PROJECTS)
        self.sw_HM.setCurrentIndex(8) 
        button = self.pbProjects
        button.blockSignals(True)
        table = self.tblMailabl_projects
        model = table.model()
        if model:
            model.clear()
        self.le_searchProjects.clear()

        combo_handler = ComboBoxHelper()

        combo_box = self.cmbProjectStatuses
        selected_status = combo_handler.populate_comboBox_smart(
            comboBox=combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=False
        )
         
        Projects.load_projects_by_status(table, selected_status)
        button.blockSignals(False)
    
    def swWorkSpace_Contracts(self):
        module = Module.CONTRACT
        button = self.pbContracts
        refresh_button = self.pbRefresh_tblMailabl_contracts
        button.blockSignals(True)
        refresh_button.blockSignals(True)
        self.sw_HM.setCurrentIndex(1)
        self.swWorkSpace.setCurrentIndex(CenterMainSliderIndexes.CONTRACTS)
        table = self.ContractView
        model = table.model()
        if model:
            model.clear()

        combo_handler = ComboBoxHelper()
        # Add statuses to the combobox and set the preferred status
        combo_box = self.cmbcontractStatuses
        selected_status = combo_handler.populate_comboBox_smart(
            comboBox=combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=False
        )

        # Add types to the combobox and set the preferred     
        types_combo_box = self.cmbcontractTypes_checkable
        combo_handler.populate_comboBox_smart(
            comboBox=types_combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=True
        )
        
        selected_type_ids = types_combo_box.checkedItemsData()
        
        ContractsMain.load_main_contracts_by_type_and_status(self,
                                                             table=table,
                                                             types=selected_type_ids,
                                                             statuses=selected_status
                                                             )
                
        button.blockSignals(False)
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
        statusValue = GetValuesFromComboBox._get_selected_status_id_from_combobox(comboBox)  
        ContractsMain.load_main_contracts_by_type_and_status(self, table, selected_types_ids, statusValue)
        refresh_button.blockSignals(False)

    def swWorkSpace_Easements(self):
        module = Module.EASEMENT
        button = self.pbeasements
        button.blockSignals(True)
        self.swWorkSpace.setCurrentIndex(CenterMainSliderIndexes.EASEMENTS)
        self.sw_HM.setCurrentIndex(5)
        table = self.tweasementView
        # Assuming 'table' is your QTableView object
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())

        statuses_combo_box = self.cmbeasementStatuses
        selected_status = combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=False
        )

        types_combo_box = self.cmbeasementTypesCheckable
        combo_handler.populate_comboBox_smart(
            comboBox=types_combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=True
        )

        prefered_types_ids = types_combo_box.checkedItemsData()
        EasementssMain.load_main_asements_by_type_and_status(self, table, prefered_types_ids, selected_status)
        button.blockSignals(False)

    def easements_reload(self):
        button = self.pbeasements
        button.blockSignals(True)
        self.swWorkSpace.setCurrentIndex(CenterMainSliderIndexes.EASEMENTS)
        self.sw_HM.setCurrentIndex(5)
        table = self.tweasementView
        # Assuming 'table' is your QTableView object
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        combo_box = self.cmbeasementStatuses
        types_combo_box = self.cmbeasementTypesCheckable
        selected_types_ids = types_combo_box.checkedItemsData()
        statusValue = GetValuesFromComboBox._get_selected_status_id_from_combobox(combo_box)
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
    def tabViewByState_NOT_NEEDED(tab_widget, state: bool):
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

