# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

import re
from PyQt5.QtCore import QCoreApplication
from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from ..Functions.Contracts.Contracts import ContractsMain
from ..Functions.Easements.Easements import EasementssMain
from ..Functions.AsBuilt.ASBuilt import AsBuiltMain
from ..Functions.Coordinations.Coordinations import CoordinationsMain
from ..utils.ComboboxHelper import GetValuesFromComboBox
from ..KeelelisedMuutujad.modules import Module
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..config.SetupModules.SetupEasments import SetupEasments
from ..config.SetupModules.SetupConrtacts import SetupConrtacts
from ..config.SetupModules.SetupProjects import SetupProjects
from ..config.SetupModules.AsBuitSettings import AsBuiltDrawings
from ..config.SetupModules.SetupCoordinations import CoordinationsSetup
from .MainMenuController import SetupController, MenuModules
from ..utils.ComboboxHelper import ComboBoxHelper
from ..widgets.decisionUIs.DecisionMaker import DecisionDialogHelper
from ..app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ..queries.python.property_data import MyLablChecker, UpdateData
from ..utils.rightClickHelper import RightClickHelper


pealkiri = Headings()
combo_handler = ComboBoxHelper()


class WorkSpaceHandler:
    dialog = None  # Class-level storage

    def __init__(self, parent=None) -> None:
        WorkSpaceHandler.dialog = parent
        self.dialog = parent

    @staticmethod
    def set_dialog(dialog):
        WorkSpaceHandler.dialog = dialog

    @staticmethod
    def asBuilt_reload(_):  # Ignore incoming self
        dialog = WorkSpaceHandler.dialog
        if dialog is None:
            print("❌ No dialog stored in WorkSpaceHandler.")
            return

        button = dialog.pbRefreshTesotusTable
        table = dialog.tblAsBuilt
        cmb_types = dialog.cmbTesotusTypes
        cmb_status = dialog.cmbTeostusStatuses

        button.blockSignals(True)

        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())

        statusValue = GetValuesFromComboBox._get_selected_id_from_combobox(cmb_status)
        selected_types_ids = cmb_types.checkedItemsData()

        AsBuiltMain.load_main_AsBuilt_by_type_and_status(
            dialog,
            table=table,
            types=selected_types_ids,
            statuses=statusValue
        )

        button.blockSignals(False)


    def swWorkSpace_Coordinations(self, menu_module, module, refresh=False):
        button = self.pbCooperations
        table = self.tblMailabl_Cooperation
        statuses_combo_box = self.cmbCooperationStatuses
        types_combo_box = self.cmbCooperationTypes
        proprtiest_connect = self.pbCooperations_Connect_properties
        pbSearchCooperation  = self.pbSearchCooperation
        le_searchCooperation = self.le_searchCooperation
        pbCooperation_free = self.pbCooperation_free

        proprtiest_connect.setEnabled(False)
        pbSearchCooperation.setEnabled(False)
        le_searchCooperation.setEnabled(False)
        pbCooperation_free.setEnabled(False)

        if refresh is False:
            self.swWorkSpace.setCurrentIndex(menu_module)
            res = WorkSpaceHandler.check_if_settings_are_set(self, menu_module)
            if res is False:
                setupEasments = CoordinationsSetup(self)
                setupEasments.load_coordinations_settings_widget()
                button.setEnabled(True)
                button.blockSignals(False)
                return

            combo_handler.populate_comboBox_smart(
                comboBox=statuses_combo_box,
                button=button,
                module=module,
                context=self,
                preferred_items=False
            )

            # Add types to the combobox and set the preferred     
            combo_handler.populate_comboBox_smart(
                comboBox=types_combo_box,
                button=button,
                module=module,
                context=self,
                preferred_items=True
            )                
        selected_status = GetValuesFromComboBox._get_selected_id_from_combobox(statuses_combo_box)
        prefered_types_ids = types_combo_box.checkedItemsData()
        #print(f"selected status: {selected_status}")
        #print(f"selected types: {prefered_types_ids}")

        CoordinationsMain.load_main_Coordinations_by_type_and_status(self,
                                                             table=table,
                                                             types=prefered_types_ids,
                                                             statuses=selected_status
                                                             )


        button.blockSignals(False)


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
        RightClickHelper.ASBuilt_right_click_action()

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

    def swWorkspace_arhive_helper(self, menu_module):
        self.ledCadastralnumbers.clear() 
        self.textBrowser.clear()
        self.swWorkSpace.setCurrentIndex(menu_module)


    def archive_helper(self):
        text = self.ledCadastralnumbers.text()
        browser = self.textBrowser
        browser.clear()

        numbers = [n.strip() for n in text.split(",") if n.strip()]
        pattern = re.compile(r"^\d{5}:\d{3}:\d{4}$")

        for tunnus in numbers:
            browser.append(f"<b>➡ Töötlen</b> {tunnus}")

            if pattern.match(tunnus):
                browser.append(f"<span style='color: green;'>✅ Vorming OK</span>")

                res, id = MyLablChecker._get_propertie_ids_by_cadastral_numbers_EQUALS(item=tunnus)

                if res is True:
                    browser.append(f"<span style='color: orange;'>ℹ Kinnistu ID <b>{id}</b> EI LEITUD. Andmeid ei uuendata.</span>")
                else:
                    browser.append(f"<span style='color: teal;'>🔄 Uuendan arhiveerimisandmeid ID-le: <b>{id}</b></span>")
                    UpdateData._update_archived_properies_data(id)

            else:
                browser.append(f"<span style='color: red;'>❌ Vigane vorming: {tunnus}. Jätan vahele.</span>")

            browser.append("<hr>")  # separator line
            QCoreApplication.processEvents()

    def archive_reset(self):
        text = self.ledCadastralnumbers.text()
        browser = self.textBrowser
        browser.clear()

        numbers = [n.strip() for n in text.split(",") if n.strip()]
        pattern = re.compile(r"^\d{5}:\d{3}:\d{4}$")

        for tunnus in numbers:
            browser.append(f"<b>➡ Töötlen</b> {tunnus}")

            if pattern.match(tunnus):
                browser.append(f"<span style='color: green;'>✅ Vorming OK</span>")

                res, id = MyLablChecker._get_propertie_ids_by_cadastral_numbers_EQUALS(item=tunnus)

                if res is True:
                    browser.append(f"<span style='color: orange;'>ℹ Kinnistut {tunnus} EI LEITUD. Andmeid ei uuendata.</span>")
                else:
                    browser.append(f"<span style='color: teal;'>🔄 Eemaldan arhhiveerimise tunnused kinnistule {tunnus}</b></span>")
                    UpdateData._unarchive_property_data(id)


            else:
                    browser.append(f"<span style='color: red;'>❌ Vigane vorming: {tunnus}. Jätan vahele.</span>")

        browser.append("<hr>")  # separator line
        QCoreApplication.processEvents()


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
            