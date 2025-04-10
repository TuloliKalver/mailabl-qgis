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
from .app.button_connector import SettingsModuleButtonConnector, PropertiesModuleButtonConnector

from .Common.app_state import PropertiesProcessStage, Processes
from .Common.ChaceHelpers import CacheUpdater

from .config.settings import SettingsDataSaveAndLoad, Version
from .config.SetupModules.SetupMainLayers import SetupCadastralLayers
from .config.QGISSettingPaths import LayerSettings, SettingsLoader
from .config.ui_directories import PathLoaderSimple
from .config.mainwidget import WidgetInfo
from .config.SetupModules.SetupProjects import SetupProjects
from .config.SetupModules.SetupConrtacts import SetupConrtacts
from .config.SetupModules.SetupEasments import SetupEasments
from .config.SetupModules.SetupUsers import SetupUsers

from .Functions.SearchEngines import ModularSearchEngine
from .Functions.Easements.EasementsToolsHandler import EasementTools
from .Functions.Folders.folders import copy_and_rename_folder
from .Functions.EVEL.evel_general import EVELTools
from .Functions.HomeTree.BuildTree import MyTreeHome
from .Functions.HomeTree.TreePropertiesSearches import FeatureInfoTool, FeatureInfoToolSearch
from .Functions.Searchpropertyfromlayer import SearchProperties

from .queries.python.users.user_info import UserSettings
from .queries.python.projects.ProjectTableGenerators.projects import Projects
from .queries.python.access_credentials import  (clear_UC_data,
                                                get_access_token, print_result,
                                                save_user_name)

from .KeelelisedMuutujad.modules import Module
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

        self.window_manager = WindowPositionHelper(self)
        self.return_pressed_manager = ReturnPressedManager(self)
        self.custom_event_filter = BlockButtonsToPreferLabelEventFilter(self)
        self.evel_tools = EVELTools()
        self.zoom_handler = ZoomForModuleData()
        self.pmbc = PropertiesModuleButtonConnector(self)
        self.smbc = SettingsModuleButtonConnector(self)

        UI = UIStateManager(self)
        loader = SHPLayerLoader(self)
        self.mse = ModularSearchEngine(self)
                
        Startup.FirstLoad(self)


        self.pmbc.button_controller()
        self.smbc.button_controller()




        self.return_pressed_manager.setup_connections_to_handle_return()
        self.custom_event_filter.set_button_focus_policy()


        self.setup_timer()
        self.set_layer_settings_labels()


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
            self.pbCancelPropertiesAction: self.exit_properties_process_flows
        }

        self.test_buttons = {
            self.pbtest_2: self.test_update_property,
        }

        for button,_ in self.test_buttons.items():
            button.setVisible(True)

        for button, function in self.properties_actions.items():
            button.clicked.connect(function)

        self.list_widgets_with_signals = {
            self.lvCounty: self.get_connected_signal,
            self.lvState: self.get_connected_signal,
            self.lvSettlement: self.get_connected_signal
        }

        for list_widget, function in self.list_widgets_with_signals.items():
            list_widget.itemSelectionChanged.connect(function)

        self.chkSelectAllSettlements.stateChanged.connect(self.on_toggle_all_with_list)
        self.chkToggleRoadSelection.stateChanged.connect(self.on_toggle_select_only_non_transport_properties)

        self.pbeasements.clicked.connect(lambda: WorkSpaceHandler.swWorkSpace_Easements(self))
        self.pbRefreshEasementTable.clicked.connect(lambda: WorkSpaceHandler.easements_reload(self))
        self.pbContracts.clicked.connect(lambda: WorkSpaceHandler.swWorkSpace_Contracts(self))
        self.pbRefresh_tblMailabl_contracts.clicked.connect(lambda: WorkSpaceHandler.contracts_reload(self))
        self.pbMapThemes.clicked.connect(lambda: WorkSpaceHandler.swWorkSpace_MapThemes_FrontPage(self))
        self.pbMapThemes.setEnabled(False)
        self.pbAddDrawings.clicked.connect(lambda: WorkSpaceHandler.swWorkSpace_AddDrawings_FrontPage(self))
        self.pbAddDrawings.setEnabled(False)
    
        self.pbSyncMailabl.clicked.connect(lambda: WorkSpaceHandler.Open_generate_mapLayer_synced_with_Mailabl_first_page(self))
        self.pbSync_start_sync.clicked.connect(self.generate_virtual_mapLayer_synced_with_Mailabl)
        
        self.pbSettings.clicked.connect(self.toggle_settings_main_view)
        self.pbHome.clicked.connect(lambda: WorkSpaceHandler.swWorkSpace_Properties(self))
        self.pbProjects.clicked.connect(lambda: WorkSpaceHandler.swWorkspace_Projects(self))
        self.pbRefresh_tblMailabl_projects.clicked.connect(self.update_tblMailabl_projects)
        self.pbGenProjectFolder.clicked.connect(self.generate_project_folder)
        self.pbGreateEVEL.setEnabled(False)

        # Logo ja kodukas
        self.pbMailabl.clicked.connect(lambda: loadWebpage.open_webpage(WebLinks().page_mailabl_home))
        self.pbUserPolicy.clicked.connect(lambda: loadWebpage.open_webpage(WebLinks().page_mailabl_terms_of_use))
        self.pbPrivacyPolicy.clicked.connect(lambda: loadWebpage.open_webpage(WebLinks().page_privacy_policy))
                
        #Setting workspace buttons and functions
        self.pbLayerSettings.clicked.connect(self.layer_setup)
        self.pbSettings_Setup_Projects.clicked.connect(lambda: SetupProjects.load_project_settings_widget(self))
        self.pbSettings_Setup_Contracts.clicked.connect(lambda: SetupConrtacts.load_contract_settings_widget(self))
        self.pbSettingsSetupEasements.clicked.connect(lambda: SetupEasments.load_easements_settings_widget(self))
        self.pbUserSettings.clicked.connect(lambda: SetupUsers.load_user_settings_widget(self))

        self.lblPhotos.setEnabled(False)
        self.lblPhtosText.setEnabled(False)
        
        self.pbSearchProjects.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.PROJECT))
        self.pbSearchContracts.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.CONTRACT))
        self.pbSearcheasements.clicked.connect(lambda: self.mse.universalSearch(module_name=Module.EASEMENT))
        
    #Adding and removing        
        #self.pbSearch_Add.clicked.connect(lambda: searchGeneral.search_cadastral_items_by_values(self))
        

        self.pbMainMenu.clicked.connect(self.handleSidebar_leftButtons)
        
        self.pbZoomProjects.clicked.connect(
            lambda: self.zoom_handler.zoom_functions[Module.PROJECT](self, module=Module.PROJECT, language="et")
        )
        
        pbEasementTools = self.pbEasementsTools
        pbEasementTools.clicked.connect(lambda: self.load_easement_widget(pbEasementTools))

        self.leSearch_Add.setEnabled(False)
        self.pbSearch_Add.setEnabled(False)
        self.pbCooseFromMap_Add.setEnabled(False)
        self.pbCompiler.clicked.connect(self.start_compielre)

        self.pbSelecPrpertiesOveral.clicked.connect(self.start_feature_info_tool)

        self.pbDisconnect.clicked.connect(self.stop_feature_info_tool)
        self.pbDisconnect.setEnabled(False)

        self.pbOpenProperty.clicked.connect(self.open_properties_item_in_mylabl)
        self.pbOpenProperty.setEnabled(False)

        self.pbCadastralSearch.clicked.connect(self.start_propertie_search)

        #TODO - this is not working yet!!!#
        self.treeView.setVisible(False)


        self.pbLogin.clicked.connect(self.save_user_data)
        self.pbCancelLogin.clicked.connect(self.remove_UC_data)

        self.pbLogOut.clicked.connect(self.log_out)
        self.pbLogOut.setVisible(False)




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

    def open_properties_item_in_mylabl(self):
        MyTreeHome.open_property()
    
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

    def start_compielre(self):
        from .processes.SyncProperties.CompyleOldPropertyModel import LayerCompilerSetup
        print("button clicked")
        LayerCompilerSetup.load_layer_compiler_widget(self)
        gc.collect()  # Force garbage collection
            
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
            ModernMessageDialog.Info_messages_modern(heading, text)
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
            ModernMessageDialog.Info_messages_modern(heading, text)
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
            ModernMessageDialog.Info_messages_modern(heading, text)
        
        self.pbGenProjectFolder.blockSignals(False)
        gc.collect()  # Force garbage collection
            
########################################################################

    def handleSidebar_leftButtons(self):
        button1 = self.pbSettings
        button10 = self.pbAddDrawings
        button11 = self.pbContracts
        button12 = self.pbMainContract
        button13 = self.pbPreContacts
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
                button10,
                button11,
                button12,
                button13,
                button14,
                button15,
                button16,
                button17,
                button18]

        original_texts = {button1: "Sätted",
                            button10: "Teostusjoonised",
                            button11: "Lepingud",
                            button12: "Teenuslepingud",
                            button13: "Liitumislepingud",
                            button14: "Kinnistud",
                            button15: "Teemakaardid",
                            button16: "Projektid",
                            button17: "Servituudid",
                            button18: "Mailabliga sünkroniseerimine"
                        }

        new_texts = {button1: "",
                    button10: "",
                    button11: "",
                    button12: "",
                    button13: "",
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

        save_user_name(self)
        res = get_access_token(self)
        res = True
        if res:
            
            user_name, user_lastname, roles_text, has_qgis_access, propeties_create = UserSettings.user_data()
            #propeties_create = True
            #has_qgis_access = True
            #user_name = "Nipi"
            #user_lastname =  " Tiri"
            #roles_text = "many_roles!!"

            #print(f"has properties rights: {propeties_create}")
            if propeties_create == False:
                self.btnMapActions.hide()

            # Get version number to check if it's "dev" mode
            path = PathLoaderSimple.metadata()
            version_nr = Version.get_plugin_version(path)
            lblVersion = self.lbVersionNumber
            if version_nr == 'dev':
                lblVersion.setStyleSheet("color: #bc5152;")
                lblVersion.setText(f"v.{version_nr}")
                if has_qgis_access == False:
                    self.lblUserAccessDenied.setVisible(True)
                    self.lblUserAccessDenied.setText(sisu.kasutaja_oigused_puuduvad)
                    self.lblUserAccessDenied.setStyleSheet("color: #bc5152;")
                    self.lblUserAccessDenied.setAlignment(Qt.AlignCenter)
                    self.pbLogin.setEnabled(False)
                    self.pbLogin.setStyleSheet("background-color: #bc5152;")
                    return  # Stop further execution
            else:
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

            self.lbNuserName.setText(user_name)
            self.lblNUserSurename.setText(user_lastname)
            self.lblUserRoles.setText(roles_text)
            self.UC_Main_Frame.setVisible(False)
            FrameHandler.show_multiple_frames(self, frames)
            self.set_start_page_based_on_toggle_and_preferred_settings()
            self.resize(1150, 700)

        else:
            heading = pealkiri.warningCritical
            text = sisu.vigane_voti
            ModernMessageDialog.Info_messages_modern(heading, text)

    def set_start_page_based_on_toggle_and_preferred_settings(self):
        index = SettingsDataSaveAndLoad.load_user_prefered_startpage_index(self)            
        # Convert index to integer, handling potential exceptions
        index_int = int(index)

            # Get the mapped functions dictionary from WidgetInfo
        mapped_functions = WidgetInfo.mapped_indexes_functions(self)
            #print(f"mapped_functions:  {mapped_functions}")
            # Check if mapped_functions is not None before iterating
        if mapped_functions is not None and index_int in mapped_functions:
            function = mapped_functions.get(index_int)
            if function:
                    #print(f"mapped index function: {function}")
                function()
            else:
                    # Handle the case where the mapped function is None
                print(f"No function mapped for index {index_int}. Setting default to page 5.")
                self.swWorkSpace.setCurrentIndex(5)
                
        else:
                # Handle the case where index is not a valid page index (e.g., set a default)
            print(f"Invalid page index: {index_int} or mapped_functions is None. Setting default to page 5.")
            self.swWorkSpace.setCurrentIndex(5)
            
    def print_UC_data(self):
        print_result(self)    

    def layer_setup(self):
        #print("started 'layer_setup'")
        lblcurrent_main_layer_label = self.lblcurrent_main_layer_label
        lblnewCadastrals_input_layer_label = self.lblnewCadastrals_input_layer_label
        lblSHPNewItems = self.lblSHPNewItems
        SetupCadastralLayers.load_layer_settings_widget(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems)
        
    def set_layer_settings_labels(self):
        #load = SettingsDataSaveAndLoad()
        lblcurrent_main_layer_label = self.lblcurrent_main_layer_label
        lblnewCadastrals_input_layer_label = self.lblnewCadastrals_input_layer_label
        lblSHPNewItems = self.lblSHPNewItems
        lblLayerProjects_Properties = self.lblLayerProjects_Properties
        lblProjectsFolder_location = self.lblProjectsFolder_location
        lblProjectsTargetFolder_location = self.lblProjectsTargetFolder_location
        lbl_preferred_project_status = self.lbl_preferred_project_status
        lbl_preferred_contract_status = self.lbl_preferred_contract_status
        lblPreferredContractsTypes_value = self.lblPreferredContractsTypes_value

        load.startup_label_loader(lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,
                                    lblSHPNewItems, lblLayerProjects_Properties, lblProjectsFolder_location,
                                    lblProjectsTargetFolder_location, lbl_preferred_project_status, 
                                    lbl_preferred_contract_status, lblPreferredContractsTypes_value)        

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
        statusValue = GetValuesFromComboBox._get_selected_status_id_from_combobox(comboBox)
        Projects.load_projects_by_status(table, statusValue)
        button.blockSingnals = False
        
    def toggle_settings_main_view(self):
        self.swWorkSpace.setCurrentIndex(4)

        
        
        lblcurrent_main_layer_label = self.lblcurrent_main_layer_label
        lblnewCadastrals_input_layer_label = self.lblnewCadastrals_input_layer_label
        lblSHPNewItems = self.lblSHPNewItems
        lblLayerProjects_Properties = self.lblLayerProjects_Properties
        lblProjectsFolder_location = self.lblProjectsFolder_location 
        lblProjectsTargetFolder_location = self.lblProjectsTargetFolder_location
        lbl_preferred_project_status = self.lbl_preferred_project_status
        lbl_user_name = self.lbNuserName
        lbl_preferred_contract_status = self.lbl_preferred_contract_status 
        lblPreferredContractsTypes_value = self.lblPreferredContractsTypes_value
        lblPreferredFolderName_structure = self.lblPreferredFolderName_structure
        prefered_folder_structure_value = SettingsDataSaveAndLoad.load_projects_prefered_folder_name_structure(self)
        lblPreferredFolderName_structure.setText(prefered_folder_structure_value)
        lblPreferredEasementsStatus = self.lblPreferredEasementsStatus
        PreferredEasementsStatus_Value = SettingsDataSaveAndLoad.load_easements_status_names(self)
        lblPreferredEasementsStatus.setText(PreferredEasementsStatus_Value)
        lblPreferredEasementsTypes_value = self.lblPreferredEasementsTypes_value
        PreferredEasementsTypes_values = SettingsDataSaveAndLoad.load_easements_type_names(self)
        lblPreferredEasementsTypes_value.setText(PreferredEasementsTypes_values)
        prefered_homepage_name_value = SettingsDataSaveAndLoad.load_user_prefered_startpage_name(self)
        if prefered_homepage_name_value == "":
            self.lblSettings_preferedHomePage.setText("Määramata")
        else:
            self.lblSettings_preferedHomePage.setText(prefered_homepage_name_value)
        
        water_layer_name = SettingsLoader.get_setting( LayerSettings.WATER_LAYER)
        sewer_layer_name = SettingsLoader.get_setting( LayerSettings.SEWER_LAYER)
        pressure_sewer_layer_name = SettingsLoader.get_setting( LayerSettings.PRESSURE_SEWER_LAYER)
        drainage_layer_name = SettingsLoader.get_setting( LayerSettings.DRAINAGE_LAYER)
        
        self.lblWaterPipesValue.setText(water_layer_name)
        self.lblSewerPipesValue.setText(sewer_layer_name)
        self.lblPrSewagePipesValue.setText(pressure_sewer_layer_name)
        self.lblDrainagePipesValue.setText(drainage_layer_name)

        SettingsDataSaveAndLoad.startup_label_loader(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,
                                                        lblSHPNewItems, lblLayerProjects_Properties,lblProjectsFolder_location, 
                                                        lblProjectsTargetFolder_location, lbl_preferred_project_status, 
                                                        lbl_preferred_contract_status, lblPreferredContractsTypes_value)

        

        widget = self.pbSettings_SliderFrame   
        WidgetAnimator.toggle_Frame_height_for_settings(self, widget)


        

#########################################################################################################################

                    #new section to be implemented into Mailabl plugin 

#########################################################################################################################

    def get_connected_signal(self):
        listWidgets = [self.lvCounty, self.lvState, self.lvSettlement]
        for widget in listWidgets:
            widget.setEnabled(False)
        element = self.sender()
        CacheUpdater.update_slected_items_cache(element)
        
        UI = UIStateManager(self)
        
        UI.flow_and_ui_controls()

        for widget in listWidgets:
            widget.setEnabled(True)


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

    @staticmethod
    def see_loaded_layers():
        stored_layers_settings = PropertiesProcessStage.loaded_layers
        print("loaded layer settings are")
        print(stored_layers_settings)
        
    def exit_properties_process_flows(self):
        WorkSpaceHandler.swWorkSpace_Properties(self)
        self.btnMapActions.setEnabled(True)
        widget = self.pbSettings_SliderFrame   
        WidgetAnimator.toggle_Frame_height_for_settings(self, widget)




    @staticmethod
    def test_update_property(self) -> bool:
        #item_id: str, notes_text: str

        
        item_id = "133842"
        notes_text = "This is a test note."
        old_name = "Õpetajate tee"
        from .queries.python.property_data import UpdateData

        UpdateData._update_archived_properies_data(item_id=item_id)




