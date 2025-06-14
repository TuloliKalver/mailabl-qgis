# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-nam
"""
/***************************************************************************
 MailablDialog
                                 A QGIS plugin
 Mailabl
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-07-04
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Kalver Tammik/Tuloli OÜ
        email                : tulolikt@gmail.com
 ***************************************************************************/

"""
import os
import gc
from PyQt5.QtCore import QTimer, Qt
from qgis.PyQt import QtWidgets, uic
from functools import partial




from .app.web import loadWebpage, WebLinks
from .app.workspace_handler import WorkSpaceHandler
from .app.ui_controllers import FrameHandler, WidgetAnimator, AlterContainers
from .app.ProrpertiesConnectorContreollr import SettingsModuleButtonConnector, PropertiesModuleButtonConnector
from .app.MainMenuController import MenuModules

from .Common.app_state import  Processes

from .config.settings import SettingsDataSaveAndLoad, Version, StartupSettingsLoader
from .config.settings_new import PluginSettings
from .config.SetupModules.SetupMainLayers import SetupCadastralLayers
from .config.ui_directories import PathLoaderSimple
from .config.mainwidget import WidgetInfo
from .config.SetupModules.SetupProjects import SetupProjects
from .config.SetupModules.SetupConrtacts import SetupConrtacts
from .config.SetupModules.SetupEasments import SetupEasments
from .config.SetupModules.SetupUsers import SetupUsers
from .config.SetupModules.AsBuitSettings import AsBuiltDrawings
from .config.SetupModules.SetupCoordinations import CoordinationsSetup
from .config.SetupModules.SetupWorks import SetupWorks

from .app.MainMenuController import SetupController

from .Functions.AsBuilt.AsBuiltTools import AsBuiltTools
from .Functions.SearchEngines import ModularSearchEngine
from .Functions.Easements.EasementsToolsHandler import EasementTools
from .Functions.Folders.folders import copy_and_rename_folder
from .Functions.EVEL.evel_general import EVELTools
from .Functions.HomeTree.BuildTree import MyTreeHome
from .Functions.HomeTree.TreePropertiesSearches import FeatureInfoTool, FeatureInfoToolSearch
from .Functions.Searchpropertyfromlayer import SearchProperties
from .Functions.WORKS.works import  start_work_capture, WorkMapHelper

from .queries.python.users.user import UserSettings
from .queries.python.projects.ProjectTableGenerators.projects import Projects
from .queries.python.access_credentials import  (clear_UC_data,
                                                get_access_token, print_result,
                                                save_user_name)

from .KeelelisedMuutujad.modules import Module, ModuleTriggerButtons
from .KeelelisedMuutujad.messages import Headings, HoiatusTexts,EdukuseTexts


from .processes.ImportProcesses.Import_shp_file import SHPLayerLoader
from .processes.OnFirstLoad.FirstLoad import Startup
from .processes.SyncProperties.syncMailablProperties import PropertiesBaseMap
from .processes.OnFirstLoad.CloseUnload import Unload


from .utils.UIWindowHelpers import WindowPositionHelper, WindowManagerMinMax
from .utils.custom_event_filter import BlockButtonsToPreferLabelEventFilter, ReturnPressedManager
from .utils.TableUtilys.TableHelpers import TableHelper
from .utils.SpatialDataHelper import ZoomForModuleData
from .utils.messagesHelper import ModernMessageDialog
from .utils.ComboboxHelper import GetValuesFromComboBox
from .utils.ButtonsHelper import ButtonHelper
from .utils.CheckBoxHelper import CheckboxHelper
from .utils.SelectionActions import SelectionActions
from .utils.UIStateManager import UIStateManager
from .utils.WidgetHelpers import WidgetAndWievHelpers, ListSelectionHandler
from .utils.MapHelpers import MapDataFlowHelper
from .utils.MapToolsHelper import MapToolsHelper
from .utils.ListHelper import  ListSelections
from .utils.MainMenuControlls import MainMenuControlls
from .utils.rightClickHelper import RightClickHelper

from .widgets.connector_widget_engine.UI_controllers import PropertiesConnector


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Mailabl_dialog_base.ui'))

###############################################################################################################
# Set plugin_dir as a class variable
plugin_dir = os.path.dirname(__file__)

################################################################################################################

#initialize

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
load = SettingsDataSaveAndLoad()

################################################################################################################

class MailablDialog(QtWidgets.QDialog, FORM_CLASS):
    
################################################################################################################

    def __init__(self, parent=None):
        """Constructor."""
        super(MailablDialog, self).__init__(parent)
                
        self.setupUi(self)


#################################################################################################################


        # Set this dialog as the main dialog for ButtonHelper
        ButtonHelper.set_dialog(self)
        ListSelectionHandler.set_dialog(self)
        TableHelper.set_dialog(self)
        MapDataFlowHelper.set_dialog(self)
        WidgetAndWievHelpers.set_dialog(self)
        CheckboxHelper.set_dialog(self)
        SelectionActions(self)
        RightClickHelper(self)

        self.setup_controller = SetupController(self)
        
        self.MainControlls = MainMenuControlls(self)

        self.window_manager = WindowPositionHelper(self)
        self.return_pressed_manager = ReturnPressedManager(self)
        self.custom_event_filter = BlockButtonsToPreferLabelEventFilter(self)
        self.evel_tools = EVELTools()
        self.zoom_handler = ZoomForModuleData()
        self.pmbc = PropertiesModuleButtonConnector(self)
        self.smbc = SettingsModuleButtonConnector(self)

        setupEasments = SetupEasments(self)
        setupContracts = SetupConrtacts(self)
        setupProjects = SetupProjects(self)
        setupAsBuiltLoader = AsBuiltDrawings(self)  # Assuming `self` is a QDialog or QWidget
        setupCoordinations = CoordinationsSetup(self)
        setupWorks = SetupWorks(self)
        setupCadastrallayers = SetupCadastralLayers(self)
        WorkSpaceHandler.set_dialog(self)


        UI = UIStateManager(self)
        loader = SHPLayerLoader(self)
        self.mse = ModularSearchEngine(self)
                
        Startup.FirstLoad(self)


        self.pmbc.button_controller()
        self.smbc.button_controller()


        self.return_pressed_manager.setup_connections_to_handle_return()
        self.custom_event_filter.set_button_focus_policy()


        self.setup_timer()



        # Install event filter on the main window
        self.installEventFilter(self.custom_event_filter)
        
        self.label_5.setVisible(False)
        self.wOlAndmed_LabelHolder.setVisible(False)
        


            
        """Setup button-action mapping and connections."""
        self.properties_actions = {
            self.pbAddElements: partial(SelectionActions.main_process_control, Processes.ADD, self.pbAddElements),
            self.btnRemoveItems: partial(SelectionActions.main_process_control, Processes.REMOVE, self.btnRemoveItems),
            self.btnRemoveItems_noImport: partial(SelectionActions.main_process_control, Processes.REMOVE, self.btnRemoveItems_noImport),
            self.pbConfirmAction: partial(SelectionActions.execute_action),
            self.pbCancelAction: SelectionActions.cancel_selection,
            self.pbLoaddShapeFile:loader.load_shp_layer,
            self.pbOpenMaAmet:partial(loadWebpage.open_maa_amet_webpage_new),            
            self.btnMapActions: UI.start_properti_flow_main,
            self.pbCancelPropertiesAction: UI.exit_properties_process_flows,
            self.pbCancelBeforeEntering: UI.exit_properties_process_flows,
        }


        for button, function in self.properties_actions.items():
            button.clicked.connect(function)



##############################TESTING AREA##############################################################
 


        self.frSyncAndRenew.setVisible(True)
#############################TESTING AREA################################################################




######################################################################


        self.chkSelectAllSettlements.stateChanged.connect(self.on_toggle_all_with_list)
        self.chkToggleRoadSelection.stateChanged.connect(self.on_toggle_select_only_non_transport_properties)


        self.pbRefreshEasementTable.clicked.connect(lambda: WorkSpaceHandler.easements_reload(self))
        self.pbRefresh_tblMailabl_contracts.clicked.connect(lambda: WorkSpaceHandler.contracts_reload(self))
        self.pbRefreshTesotusTable.clicked.connect(lambda: WorkSpaceHandler.asBuilt_reload(self))
        self.pbRefresh_tblMailabl_Cooperation.clicked.connect(lambda: WorkSpaceHandler.swWorkSpace_Coordinations(self, menu_module=MenuModules.COORDINATIONS, module=Module.COORDINATION, refresh=True))
        self.pbRefreshWorksTable.clicked.connect(lambda: WorkSpaceHandler.swWorkSpace_Works(self, menu_module=MenuModules.WORKS, module=Module.WORKS, refresh=True))

        self.pbMapThemes.setEnabled(False)

        self.pbArhciveHelperStart.clicked.connect(lambda: WorkSpaceHandler.archive_helper(self))
        self.pbArchivValueReset.clicked.connect(lambda: WorkSpaceHandler.archive_reset(self))

    
        self.pbSyncMailabl.clicked.connect(lambda: WorkSpaceHandler.Open_generate_mapLayer_synced_with_Mailabl_first_page(self))
        self.pbSync_start_sync.clicked.connect(self.generate_virtual_mapLayer_synced_with_Mailabl)
        
        self.pbSettings.clicked.connect(self.toggle_settings_main_view)
        self.pbRefresh_tblMailabl_projects.clicked.connect(self.update_tblMailabl_projects)
        self.pbGenProjectFolder.clicked.connect(self.generate_project_folder)
        

        # Logo ja kodukas
        self.pbMailabl.clicked.connect(lambda: loadWebpage.open_webpage(WebLinks().page_mailabl_home))

        self.pbUserPolicy.clicked.connect(lambda: loadWebpage.open_webpage(WebLinks().page_mailabl_terms_of_use))
        self.pbPrivacyPolicy.clicked.connect(lambda: loadWebpage.open_webpage(WebLinks().page_privacy_policy))
                
        #Setting workspace buttons and functions
        self.pbLayerSettings.clicked.connect(self.layer_setup)
        self.pbSettings_Setup_Projects.clicked.connect(lambda: setupProjects.load_project_settings_widget())
        self.pbSettings_Setup_Contracts.clicked.connect(lambda: setupContracts.load_contract_settings_widget())
        self.pbSettingsSetupEasements.clicked.connect(lambda:setupEasments.load_easements_settings_widget())
        self.pbUserSettings.clicked.connect(lambda: SetupUsers.load_user_settings_widget(self))
        self.pbTeostusSettings.clicked.connect(lambda: setupAsBuiltLoader.load_construction_drawings_setup_widget())
        self.pbCoordinationsSettings.clicked.connect(lambda: setupCoordinations.load_coordinations_settings_widget())
        self.pbWorksSettings.clicked.connect(lambda: setupWorks.load_works_settings_widget())

        
        self.pbSearchProjects.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.PROJECT))
        self.pbSearchContracts.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.CONTRACT))
        self.pbSearcheasements.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.EASEMENT))
        self.pbSearchTesotus.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.ASBUILT))
        self.pbWorksSearch.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.WORKS))

        self.pbMainMenu.clicked.connect(self.handleSidebar_leftButtons)
        
        self.pbZoomProjects.clicked.connect(
            lambda: self.zoom_handler.zoom_functions[Module.PROJECT](self, module=Module.PROJECT, language="et")
        )
        
        pbEasementTools = self.pbEasementsTools
        pbEasementTools.clicked.connect(lambda: self.load_easement_widget(pbEasementTools))

        self.leSearch_Add.setEnabled(False)
        self.pbSearch_Add.setEnabled(False)
        self.pbCooseFromMap_Add.setEnabled(False)
        #self.pbCompiler.clicked.connect(self.start_compielre)

        self.pbSelecPrpertiesOveral.clicked.connect(self.start_feature_info_tool)

        self.pbDisconnect.clicked.connect(self.stop_feature_info_tool)
        self.pbDisconnect.setEnabled(False)

        self.pbOpenProperty.clicked.connect(lambda: MyTreeHome.open_property(self))
        self.pbOpenProperty.setEnabled(False)

        self.pbCadastralSearch.clicked.connect(self.start_propertie_search)

        #TODO - this is not working yet!!!#
        self.treeView.setVisible(False)


        self.pbLogin.clicked.connect(self.save_user_data)
        self.pbCancelLogin.clicked.connect(self.remove_UC_data)

        self.pbLogOut.clicked.connect(self.log_out)
        self.pbLogOut.setVisible(False)

        self.pbWorksTools_2.clicked.connect(lambda: start_work_capture(self))
        #self.Works_Testing.clicked.connect(WorkMapHelper.update_fature_statuses)
        self.Works_Testing.clicked.connect(WorkMapHelper.update_map_based_on_open_task_in_mylabl)



    def start_propertie_search(self):
        gc.collect()  # Force garbage collection
        engine = SearchProperties(self)
        label = self.isSelectedCadaster
        result = engine.search_for_item(label=label)
        if result is None:
            return
        else:
            address = self.lblAddress_value
            purpose = self.lblPurpose_value
            area = self.lblArea_value
            created_at = self.CreatedAt_value
            updated_at = self.UpdatedAt_value
            treeWidget = self.treeWidget
            lblRegistryNr = self.RegistryNr_value
            lblCadastralNr = self.CadasterNr_value
            open_cadastral_button = self.pbOpenProperty
            tool_feature = FeatureInfoToolSearch(
                window=self,
                lblCadastralNr=lblCadastralNr,
                lblRegistry= lblRegistryNr,
                address=address,
                purpose=purpose,
                area=area,
                created_at=created_at,
                updated_at=updated_at,
                treeWidget=treeWidget,
                property_button=open_cadastral_button
            )

            tool_feature.for_search_results()

    
    def load_propertieID_from_memory (self):
        value = self.propertyID_location
        return value

    def setup_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(10000)  # 10 seconds timeout
        self.timer.timeout.connect(self.stop_feature_info_tool_timed)

    def start_feature_info_tool(self):        
        self.pbSelecPrpertiesOveral.setEnabled(False)
        label = self.isSelectedCadaster
        address = self.lblAddress_value 
        purpose = self.lblPurpose_value 
        area = self.lblArea_value  
        created_at = self.CreatedAt_value  
        updated_at = self.UpdatedAt_value  
        treeWidget = self.treeWidget
        lblRegistryNr = self.RegistryNr_value
        lblCadastralNr = self.CadasterNr_value
        pbOProperty = self.pbOpenProperty
        treeView = self.treeView
        global feature_tool  # Use global variable to keep reference
        
        self.window_manager_minmax = WindowManagerMinMax(self)
        self.window_manager_minmax._minimize_window()
        feature_tool = FeatureInfoTool(
            label=label,
            lblCadastralNr=lblCadastralNr,
            lblRegistry= lblRegistryNr,
            address=address,
            purpose=purpose,
            area=area,
            created_at=created_at,
            updated_at=updated_at,
            treeWidget=treeWidget,
            reset_timer=lambda: self.reset_timer(),
            main_window = self,
            pbOProperty= pbOProperty,
            treeView=treeView
        )
        self.pbDisconnect.setEnabled(True)
        self.timer.start()

    def stop_feature_info_tool(self):
        global feature_tool  # Use global variable to keep reference
        if feature_tool:
            feature_tool.disconnect_signal()
            print("disconnecting with button")
            self.pbDisconnect.setEnabled(False)
            self.pbSelecPrpertiesOveral.setEnabled(True)
        self.timer.stop()
        gc.collect()  # Force garbage collection
            
    def stop_feature_info_tool_timed(self):
        global feature_tool  # Use global variable to keep reference
        if feature_tool:
            feature_tool.disconnect_signal_timed()
            print("disconnecting with timer")
            self.pbDisconnect.setEnabled(False)
            self.pbSelecPrpertiesOveral.setEnabled(True)
        self.timer.stop()
        gc.collect()  # Force garbage collection
            
    def reset_timer(self):
        self.timer.start()

    #def start_compielre(self):
    #    from .processes.SyncProperties.CompyleOldPropertyModel import LayerCompilerSetup
    #    print("button clicked")
    #    LayerCompilerSetup.load_layer_compiler_widget(self)
    #    gc.collect()  # Force garbage collection
            
    def log_out(self):
        Unload.log_out(self)

    def load_easement_widget(self, button):
        button.setEnabled(False)
        # Create an instance of EasementTools and pass tweasementView
        self.easement_tools = EasementTools(self.tweasementView)
        # Connect the widgetClosed signal to a method in your main class
        table = self.tweasementView
        selection_model = table.selectionModel()
        if selection_model.hasSelection():
            self.showMinimized()
            self.easement_tools.widgetClosed.connect(lambda: self.on_easement_widget_closed(button))
            # Call the load_widget method of the EasementTools instance
            self.easement_tools.load_widget()
        else:
            text = HoiatusTexts().andmed_valimata
            heading = Headings().warningSimple
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
            self.showNormal()
            button.setEnabled(True)
            return
    
    def on_easement_widget_closed(self, button):
        button.setEnabled(True)
        self.showNormal()

    def load_properties_connector(self, module, table, button):
        button_contracts = self.pbContracts_Connect_properties
        button_projects = self.pbProjects_Connect_properties
        button_easements = self.pbEasementsConnectProperties
        button_easements.setEnabled(False)
        buttons = [button_contracts, button_easements, button_projects]
        for single_button in buttons:
            single_button.setEnabled(False)

        #button.setEnabled(False)
        selection_model = table.selectionModel()
        if selection_model.hasSelection():
            self.showMinimized()
            # Create an instance of PropertiesConnector with the table instance
            self.properties_connector = PropertiesConnector(table)
            # Connect the widgetClosed signal to a method in your main class
            self.properties_connector.ConnectorWidgetClosed.connect(lambda: self.on_properties_connector_widget_closed(button))
            # Load the properties connector widget UI
            self.properties_connector.load_propertiesconnector_widget_ui(module)
            gc.collect()  # Force garbage collection
            
        else:
            text = HoiatusTexts().andmed_valimata
            heading = Headings().warningSimple
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
            for single_button in buttons:
                single_button.setEnabled(True)
            button.setEnabled(True)
            gc.collect()  # Force garbage collection
            return

    def on_properties_connector_widget_closed(self, button):
        button_contracts = self.pbContracts_Connect_properties
        button_projects = self.pbProjects_Connect_properties
        button_easements = self.pbEasementsConnectProperties
        buttons = [button_contracts, button_easements, button_projects]
        for single_button in buttons:
            single_button.setEnabled(True)
        button.setEnabled(True)
        #print("Closed properties loader window")
        self.showNormal()
        gc.collect()  # Force garbage collection
            
    def generate_project_folder(self):
        self.pbGenProjectFolder.blockSignals(True)
        table = self.tblMailabl_projects
        selection_model = table.selectionModel()

        if selection_model.hasSelection():
            copy_and_rename_folder(table)
        
        else:
            text = HoiatusTexts().projekt_valimata
            heading = Headings().warningSimple
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
        
        self.pbGenProjectFolder.blockSignals(False)
        gc.collect()  # Force garbage collection
            
########################################################################

    def handleSidebar_leftButtons(self):
        button1 = self.pbSettings
        button2 = self.pbCooperations
        button10 = self.pbAddDrawings
        button11 = self.pbContracts
        button14 = self.pbHome
        button15 = self.pbMapThemes
        button16 = self.pbProjects
        button17 = self.pbeasements
        button18 = self.pbSyncMailabl
        left_menu = self.leftMenuContainer
        container = self.leftMenuContainer
        container_width = container.width()
        #print(container_width)
        
        buttons = [button1,
                   button2, 
                button10,
                button11,
                button14,
                button15,
                button16,
                button17,
                button18]

        original_texts = {button1: "Sätted",
                           button2: "Kooskõlastused",
                            button10: "Teostusjoonised",
                            button11: "Lepingud",
                            button14: "Kinnistud",
                            button15: "Teemakaardid",
                            button16: "Projektid",
                            button17: "Servituudid",
                            button18: "Mailabliga sünkroniseerimine"
                        }

        new_texts = {button1: "",
                     button2: "",
                    button10: "",
                    button11: "",
                    button14: "",
                    button15: "",
                    button16: "",
                    button17: "",
                    button18: ""
                        }
        #Chose a random button to measure text lenght
        length = len(button18.text())
        AlterContainers.toggle_left_menu(self, length, buttons, original_texts, new_texts, left_menu, container, container_width)


    #creditentials handling
    def remove_UC_data(self):
        clear_UC_data()

    def activate_line_edit(self):
        # Activate the QLineEdit for user input
        lePassword = self.lePassword
        lePassword.setFocus()
        lePassword.setCursorPosition(0)  # Set cursor position at the beginning

    def save_user_data(self):

        frames = [self.leftMenuContainer,
                self.frAgreements,
                self.swWorkSpace,
                self.lblUserAccessDenied
                ]
        if self.cbDevMode.isChecked():
            # Get version number to check if it's "dev" mode
            path = PathLoaderSimple.metadata()
            version_nr = Version.get_plugin_version(path)
            lblVersion = self.lbVersionNumber
            if version_nr == 'dev':

                lblVersion.setStyleSheet("color: #bc5152;")
                lblVersion.setText(f"v.{version_nr}")        
                self.UC_Main_Frame.setVisible(False)
                FrameHandler.show_multiple_frames(self, frames)
                self.set_start_page_based_on_toggle_and_preferred_settings()
                self.resize(1000, 650)
                return  # Stop further execution            
        
        else:    
            save_user_name(self)
            res = get_access_token(self)
            if res:
            
                user_name, user_lastname, roles_text, has_qgis_access, propeties_create, abilities = UserSettings.user_data()


                #TODO - the moddule rights checker needs to be developed more precice to better understand what is allowed!!!
                #print(f"allowed modules: {allowed_modules}")
                #ModuleTriggerButtons.apply_button_access_control(abilities, dialog=self)
                
                #print(f"has properties rights: {propeties_create}")
                if propeties_create == False:
                    self.btnMapActions.hide()
                    self.pbArchiveHelper.hide()
                # Get version number to check if it's "dev" mode
                path = PathLoaderSimple.metadata()
                version_nr = Version.get_plugin_version(path)
                lblVersion = self.lbVersionNumber
                if version_nr == 'dev':
                    self.test_buttons = {
                            self.pbtest_2: self.view_all_plugin_settings,
                            self.pushButton: self.reset_new_settings
                        }
                    self.pbtest_2.setText("Vaata settinguid")
                    self.pushButton.setText("kustuta settingud")

                    for button,_ in self.test_buttons.items():
                        button.setVisible(True)

                    for button, function in self.test_buttons.items():
                        button.clicked.connect(function)

                    lblVersion.setStyleSheet("color: #bc5152;")
                    lblVersion.setText(f"v.{version_nr}")
                    if has_qgis_access == False:
                        self.lblUserAccessDenied.setVisible(True)
                        self.lblUserAccessDenied.setText(sisu.kasutaja_oigused_puuduvad)
                        self.lblUserAccessDenied.setStyleSheet("color: #bc5152;")
                        self.lblUserAccessDenied.setAlignment(Qt.AlignCenter)
                        self.pbLogin.setEnabled(False)
                        self.pbLogin.setStyleSheet("background-color: #bc5152;")


                        #Manage development items
                        self.pbGreateEVEL.setEnabled(True)
                        self.pbMailabl.setVisible(False)
                        self.label_5.setVisible(False)
                        self.lblPhotosValue.setEnabled(False)
                        self.lblPhtosText.setEnabled(False)


                        return  # Stop further execution
                else:
                    asBuiltTools = AsBuiltTools(self, self.tblAsBuilt)
                    self.test_buttons = {
                            self.pbtest_2: self.view_all_plugin_settings,
                            self.pushButton: self.reset_new_settings,
                        }
                    for button,_ in self.test_buttons.items():
                        button.setVisible(False)

                    lblVersion.setStyleSheet("")  # Reset to default style
                    lblVersion.setText(f"v.{version_nr}")
                    if has_qgis_access == False:
                        self.lblUserAccessDenied.setVisible(True)
                        self.lblUserAccessDenied.setText(sisu.kasutaja_oigused_puuduvad)
                        self.lblUserAccessDenied.setStyleSheet("color: #bc5152;")
                        self.lblUserAccessDenied.setAlignment(Qt.AlignCenter)
                        self.pbLogin.setEnabled(False)
                        self.pbLogin.setStyleSheet("background-color: #bc5152;")
                        return  # Stop further execution

                self.lbNuserNameValue.setText(user_name)
                self.lblNUserSurenameValue.setText(user_lastname)
                self.lblUserRolesValue.setText(roles_text)
                self.UC_Main_Frame.setVisible(False)
                FrameHandler.show_multiple_frames(self, frames)
                self.set_start_page_based_on_toggle_and_preferred_settings()
                self.resize(1000, 650)

            else:
                heading = pealkiri.warningCritical
                text = sisu.vigane_voti
                ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)

    def set_start_page_based_on_toggle_and_preferred_settings(self):
        
        index = SettingsDataSaveAndLoad.load_user_prefered_startpage_index(self)
        #print(f"start page index: {index}")        
        if index == "Määramata":
            index = "6"
        # Convert index to integer, handling potential exceptions
        index_int = int(index)

        # Get the mapped functions dictionary from WidgetInfo
        mapped_functions = WidgetInfo.mapped_indexes_functions(self)

        if mapped_functions is not None and index_int in mapped_functions:
            function = mapped_functions.get(index_int)
            if function:
                    #print(f"mapped index function: {function}")
                function()
            else:
                    # Handle the case where the mapped function is None
                #print(f"No function mapped for index {index_int}. Setting default to page 5.")
                self.swWorkSpace.setCurrentIndex(5)
                
        else:
                # Handle the case where index is not a valid page index (e.g., set a default)
            #print(f"Invalid page index: {index_int} or mapped_functions is None. Setting default to page 5.")
            self.swWorkSpace.setCurrentIndex(5)
            
    def print_UC_data(self):
        print_result(self)    

    def layer_setup(self):
        #print("started 'layer_setup'")

        SetupCadastralLayers.load_layer_settings_widget(self)
        

    def generate_virtual_mapLayer_synced_with_Mailabl(self):
        # Create an instance of YourClas
        lblFor_Sync_GreatLayerName = self.leText_For_Sync_GreateLayerName
        frSync_Cadastrals_Main = self.frSync_Cadastrals_Main
        county_list_widget = self.lwSync_County_Names
        state_list_widget = self.lwSync_State_Names
        city_list_widget = self.lwSync_City_Names
        pBar_County_list = self.pBar_Sync_County
        pBar_State_list = self.pBar_State_list 
        pBar_City_list = self.pBar_City_list
        pBar_City_items = self.pBar_CityItems
        lblSync_General = self.lblSync_General
        lblSync_General_aditional = self.lblSync_General_aditional
        lblFor_pBar_County_list = self.lblFor_pBar_Sync_County
        lblFor_pBar_State_list = self.lblFor_pBar_State_list 
        lblFor_pBar_City_list = self.lblFor_pBar_City_list
        lblFor_pBar_City_items = self.lblFor_pBar_CityItems
        Sync_Cadastrals = self.Sync_Cadastrals
        frSync_Overview_Main = self.frSync_Overview_Main
        frSync_Tools = self.frSync_Tools
        a = self.a
        b= self.b
        c = self.c
        d = self.d
        
        self.your_instance = PropertiesBaseMap(lblFor_Sync_GreatLayerName, frSync_Cadastrals_Main, county_list_widget,
                state_list_widget, city_list_widget, pBar_County_list, pBar_State_list,
                pBar_City_list, pBar_City_items, lblSync_General, lblSync_General_aditional,
                lblFor_pBar_County_list, lblFor_pBar_State_list, lblFor_pBar_City_list,
                lblFor_pBar_City_items, Sync_Cadastrals, frSync_Overview_Main, frSync_Tools, a, b, c, d)
        # Connect the button click signal to the prepare_items_for_base_map method
        self.your_instance.prepare_items_for_base_map()

#TODO -  move to projects list!        
    def update_tblMailabl_projects(self):
        button = self.pbRefresh_tblMailabl_projects
        button.blockSingnals = True
        table = self.tblMailabl_projects
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
        comboBox = self.cmbProjectStatuses
        statusValue = GetValuesFromComboBox._get_selected_id_from_combobox(comboBox)
        Projects.load_projects_by_status(table, statusValue)
        button.blockSingnals = False
        
    def toggle_settings_main_view(self):
        self.swWorkSpace.setCurrentIndex(4)
        loader = StartupSettingsLoader(self)
        loader.startup_label_loader()
        widget = self.pbSettings_SliderFrame   
        self.setup_controller.check_all_modules()
        WidgetAnimator.toggle_Frame_height_for_settings(self, widget)


        

#########################################################################################################################

                    #new section to be implemented into Mailabl plugin 

#########################################################################################################################


    def on_toggle_all_with_list(self, state):
        checkbox = self.sender()
        widget_name = checkbox.property("target_widget")
        widget = getattr(self, widget_name, None)
        if widget is not None:
            if state == Qt.Checked:
                ListSelections.select_all_items(widget)
            else:
                ListSelections.deselect_all_items(widget)

    def on_toggle_all_with_Table(self, state):
        checkbox = self.sender()
        widget_name = checkbox.property("target_widget")
        widget = getattr(self, widget_name, None)
        if widget is not None:
            if state == Qt.Checked:
                TableHelper.select_all_items(widget)
            else:
                TableHelper.deselect_all_items(widget)

    def on_toggle_select_only_non_transport_properties(self, state):
        checkbox = self.sender()
        widget_name = checkbox.property("target_widget")
        widget = getattr(self, widget_name, None)
        search_field = 'siht1'
        search_value = 'TRANSPORDIMAA'
        if widget is not None:
            if state == Qt.Checked:
                feature_ids = TableHelper.select_items_by_field(table=widget, field=search_field, search_value=search_value)
                MapToolsHelper.select_features_by_ids(feature_ids=feature_ids, zoom_to=True)
                checkbox.setText("Vali kõik")
            else:
                TableHelper.select_all_items(widget)
                feature_ids = TableHelper.get_selected_feature_ids_from_table_model(widget)
                MapToolsHelper.select_features_by_ids(feature_ids=feature_ids, zoom_to=True)
                checkbox.setText("Eemalda tranpordimaa valikust")



################################Test AREA ##########################



    def test_decision_tool(self):
        from .Functions.layer_generator import LayerManager
        from qgis.core import  QgsProject

        GroupName = "test_group"
        GroupSubName = "sub_test_group"
        LayerName = "Ala2"
        layer = QgsProject.instance().mapLayersByName(LayerName)[0]
 
        LayerManager.get_or_create_subgroup_NEEDS_IMLEMENTATION(main_group_name=GroupName, sub_group_name=GroupSubName, layer=layer)
        

    @staticmethod
    def test_property_archiving(self) -> bool:
        print("testing property archiving")
        from .Functions.GeopakagegeHandler import GeopakagegeHandler
        GeopakagegeHandler.testing()

    def test_gpkg_layer_deleting(self): 
        from qgis.core import  QgsProject
        
        from .utils.ArchiveLayerHandler import GPKGHelpers
        archive_layer_name = "Minu_arhiiv"
        layer = QgsProject.instance().mapLayersByName('Kalver_test')[0]
        layer_uri, gpkg_path = GPKGHelpers.get_layer_uri(layer, archive_layer_name)
        GPKGHelpers.delete_layer_from_gpkg(gpkg_path=gpkg_path, layer_name=archive_layer_name)         

    @staticmethod
    def test_update_property(self) -> bool:
        #item_id: str, notes_text: str
        
        item_id = "134858"
        notes_text = "This is a test note."
        old_name = "Põllu"


        from .queries.python.property_data import UpdateData

        UpdateData._update_archived_properies_data(item_id=item_id, recovery_name=old_name)

    @staticmethod
    def testing_max_fids(self) -> bool:
        
        from .utils.fidOperationsHelper import fidOperations
        from qgis.core import  QgsProject,  QgsFeatureRequest


        from .utils.LayerFeaturehepers import LayerFeatureHelpers


        target_layer = QgsProject.instance().mapLayersByName("Minu_arhiiv")[0]
        input_layer = QgsProject.instance().mapLayersByName("Kalver_test")[0]
        
        

        
        feature_id = 14357
        request = QgsFeatureRequest().setFilterFid(feature_id)
        feature = next(input_layer.getFeatures(request), None)
        

        target_fields = target_layer.fields()

        new_attrs = LayerFeatureHelpers._map_attributes_by_name(feature, target_fields)
        

        target_layer.startEditing()



        fid_index = target_fields.indexOf("fid")

        max_fid = fidOperations._get_layers_next_ids(target_layer=target_layer)

        new_attrs[fid_index] = max_fid

        feature.setAttributes(new_attrs)

        if target_layer.isEditable():
            target_layer.addFeatures([feature])
            target_layer.commitChanges()

    def view_all_plugin_settings(self):
        PluginSettings.print_all_mailabl_settings()

    def reset_new_settings(self):
        from .config.settings_new import SettingsBuilder
        SettingsBuilder.reset_initialization_flag()

