# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from ..Functions.Contracts.Contracts import ContractsMain
from ..Functions.Easements.Easements import EasementssMain
from ..Functions.AsBuilt.ASBuilt import AsBuiltMain
from ..utils.ComboboxHelper import GetValuesFromComboBox
from ..KeelelisedMuutujad.modules import Module
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..config.SetupModules.SetupEasments import SetupEasments
from ..config.SetupModules.SetupConrtacts import SetupConrtacts
from ..config.SetupModules.SetupProjects import SetupProjects
from ..config.SetupModules.AsBuitSettings import AsBuiltDrawings
from .MainMenuController import SetupController, MenuModules
from ..utils.ComboboxHelper import ComboBoxHelper
from ..widgets.decisionUIs.DecisionMaker import DecisionDialogHelper
from ..app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame



pealkiri = Headings()
combo_handler = ComboBoxHelper()


class WorkSpaceHandler:


    def swWorkSpace_Controller(self, menu_module, module):
        #menu_module controlls menu and flows between modules
        #Module is to load the data from the
        button = self.pbAddDrawings
        table = self.tblAsBuilt

        self.swWorkSpace.setCurrentIndex(menu_module)
        res = WorkSpaceHandler.check_if_settings_are_set(self, menu_module)
        if res is False:
            setupEasments = AsBuiltDrawings(self)
            setupEasments.load_construction_drawings_setup_widget()
            button.setEnabled(True)
            button.blockSignals(False)
            return


        # Add statuses to the combobox and set the preferred status
        statuses_combo_box = self.cmbTeostusStatuses
        combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=False
        )

        # Add types to the combobox and set the preferred     
        types_combo_box = self.cmbTesotusTypes
        combo_handler.populate_comboBox_smart(
            comboBox=types_combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=True
        )                

        selected_status = GetValuesFromComboBox._get_selected_id_from_combobox(statuses_combo_box)
        prefered_types_ids = types_combo_box.checkedItemsData()

        AsBuiltMain.load_main_AsBuilt_by_type_and_status(self,
                                                             table=table,
                                                             types=prefered_types_ids,
                                                             statuses=selected_status
                                                             )
                
        button.blockSignals(False)
        

    def asBuilt_reload(self):
        button = self.pbRefreshTesotusTable
        button.blockSignals(True)
        
        table = self.tblAsBuilt       # Assuming 'table' is your QTableView object
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        cmb_status = self.cmbTeostusStatuses
        statusValue = GetValuesFromComboBox._get_selected_id_from_combobox(cmb_status)

        cmb_types = self.cmbTesotusTypes
        selected_types_ids = cmb_types.checkedItemsData()
        
        AsBuiltMain.load_main_AsBuilt_by_type_and_status(self,
                                                             table=table,
                                                             types=selected_types_ids,
                                                             statuses=statusValue
                                                             )
                
        button.blockSignals(False)

    def asBuilt_search(self):
        button = self.pbSearchTesotus
        button.blockSignals(True)
        search_text = self.le_searchTesotus.text().strip()
        table = self.tblAsBuilt
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())

        AsBuiltMain.load_asBuilt_by_query(self, table, search_text)

        button.blockSignals(False)





    @staticmethod
    def swWorkSpace_MapThemes_FrontPage(self):
        self.swWorkSpace.setCurrentIndex(6)

    def swWorkSpace_Home(self):
        print("started 'swWorkspace_Home'")
        self.swWorkSpace.setCurrentIndex(MenuModules.HOMEPAGE)
        
    def swWorkSpace_Properties(self):
        print("started 'swWorkspace_Properties'")
        self.swWorkSpace.setCurrentIndex(MenuModules.PROPERTIES)
        

    def swWorkspace_Projects(self):
        module = Module.PROJECT
        menu_module = MenuModules.PROJECTS
        button = self.pbProjects
        button.blockSignals(True)
        self.swWorkSpace.setCurrentIndex(menu_module)
        res = WorkSpaceHandler.check_if_settings_are_set(self,menu_module)
        if res is False:
            setup = SetupProjects(self)
            setup.load_project_settings_widget()
            button.setEnabled(True)
            button.blockSignals(False)
            return
    
        table = self.tblMailabl_projects
        model = table.model()
        if model:
            model.clear()
        self.le_searchProjects.clear()

        combo_handler = ComboBoxHelper()

        statuses_combo_box = self.cmbProjectStatuses
        combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            button=button,
            module=module,
            context=self,
            preferred_items=False
        )

        selected_status = GetValuesFromComboBox._get_selected_id_from_combobox(statuses_combo_box)


        Projects.load_projects_by_status(table, selected_status)
        button.blockSignals(False)
    
    def swWorkSpace_Contracts(self):
        module = Module.CONTRACT
        menu_module = MenuModules.CONTRACTS
        self.swWorkSpace.setCurrentIndex(menu_module)
        button = self.pbContracts

        res = WorkSpaceHandler.check_if_settings_are_set(self,menu_module)
        if res is False:
            setup = SetupConrtacts(self)
            setup.load_contract_settings_widget()
            button.setEnabled(True)
            button.blockSignals(False)
            return

        refresh_button = self.pbRefresh_tblMailabl_contracts
        button.blockSignals(True)
        refresh_button.blockSignals(True)

        table = self.ContractView
        model = table.model()
        if model:
            model.clear()

        combo_handler = ComboBoxHelper()
        # Add statuses to the combobox and set the preferred status
        statuses_combo_box = self.cmbcontractStatuses
        selected_status = combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
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
        
        selected_status = GetValuesFromComboBox._get_selected_id_from_combobox(statuses_combo_box)
        prefered_types_ids = types_combo_box.checkedItemsData()


        ContractsMain.load_main_contracts_by_type_and_status(self,
                                                             table=table,
                                                             types=prefered_types_ids,
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
        statusValue = GetValuesFromComboBox._get_selected_id_from_combobox(comboBox)  
        ContractsMain.load_main_contracts_by_type_and_status(self, table, selected_types_ids, statusValue)
        refresh_button.blockSignals(False)

    def swWorkSpace_Easements(self):
        module = Module.EASEMENT
        button = self.pbeasements
        button.blockSignals(True)
        menu_module = MenuModules.EASEMENTS
        self.swWorkSpace.setCurrentIndex(menu_module)
        res = WorkSpaceHandler.check_if_settings_are_set(self,menu_module)
        if res is False:
            setupEasments = SetupEasments(self)
            setupEasments.load_easements_settings_widget()
            button.setEnabled(True)
            button.blockSignals(False)
            return

        table = self.tweasementView
        # Assuming 'table' is your QTableView object
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())

        statuses_combo_box = self.cmbeasementStatuses
        combo_handler.populate_comboBox_smart(
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

        selected_status = GetValuesFromComboBox._get_selected_id_from_combobox(statuses_combo_box)
        prefered_types_ids = types_combo_box.checkedItemsData()

        EasementssMain.load_main_easements_by_type_and_status(self, table, prefered_types_ids, selected_status)
        button.blockSignals(False)

    def easements_reload(self):
        button = self.pbeasements
        button.blockSignals(True)
        self.swWorkSpace.setCurrentIndex(MenuModules.EASEMENTS)
        
        table = self.tweasementView
        # Assuming 'table' is your QTableView object
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        combo_box = self.cmbeasementStatuses
        types_combo_box = self.cmbeasementTypesCheckable
        selected_types_ids = types_combo_box.checkedItemsData()
        statusValue = GetValuesFromComboBox._get_selected_id_from_combobox(combo_box)
        EasementssMain.load_main_easements_by_type_and_status(self, table, selected_types_ids, statusValue)
        button.blockSignals(False)


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
        self.swCadastral_sub_processes.setCurrentIndex(0)

        
    def check_if_settings_are_set(self, menu_module):
        controller = SetupController(self)
        res, labels = controller.has_undefined_labels(menu_module)
        if res is False:    
            buttons={"keep": "Edasi",}
            ret = DecisionDialogHelper.ask_user(
                title=Headings.inFO_SIMPLE,
                message="Puuduvad alg seaded,\nteeme kohe seadistuse",
                options=buttons,
                parent=self,
                type= AnimatedGradientBorderFrame.WARNING
                    )
            #TODO afther dev is fone!
            #res = True

            if ret is False:
                settings_module = MenuModules.SETTINGS
                self.swWorkSpace.setCurrentIndex(settings_module)
                controller.check_all_modules()
                return False 
            else:
                pass
        else:
            print("✅ Setup looks good.")
            return True
            