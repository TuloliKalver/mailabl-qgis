import os
import json
from PyQt5.uic import loadUi
from qgis.core import QgsSettings
from ..KeelelisedMuutujad.modules import Module
from ..config.QGISSettingPaths import SettingsLoader, LayerSettings
from .settings_new import PluginSettings, SettingsBuilder



PLUGIN_DIR = os.path.dirname(__file__)
PLUGIN_DIR_MAIN = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Constants
CONF_FOLDER = "config"
CONF_WIDGETS_FOLDER = "confWidgets"
QGIS_STYLES_FOLDER = "QGIS_styles"
ICONS_FOLDER = "icons/"
WIDGETS_FOLDER = "widgets"

WIDGET_MODULAR_FOLDER = "connector_widget_engine"
CONFIG_FILE = "config.json"
FUNCTIONS_FOLDER = "Functions"
EASEMENTS_FOLDER = "Easements"
EVEL_FOLDER = "EVEL"
DECISIONS_FOLDER = "decisionUIs"


# Load configuration
with open(os.path.join(PLUGIN_DIR, CONFIG_FILE), "r") as json_content:
    config = json.load(json_content)

class Version:
    @staticmethod
    def get_plugin_version(metadata_file):
        with open(metadata_file, 'r') as f:
            for line in f:
                if line.strip().startswith("version="):
                    return line.strip().split('=')[1]

class Flags:
    active_properties_layer_flag = False
    
    Flag_SliderButton_LoadData = False
    Flag_SliderButton_Properties = False    
    Flag_Running_Process = False

class OpenLink:
    def __init__(self):
        self.main = config.get('weblink', '')
        self.privacy = config.get('privacy', '')
        self.terms = config.get('terms', '')

    @staticmethod
    def weblink_by_module(module_path: str) -> str:
        """
        Build a full link like: https://example.com/projects/
        Usage:
            OpenLink.weblink_by_module(MailablWebModules.PROJECTS)
        """
        return f"{OpenLink().main}{module_path}"
    @staticmethod
    def get_module_link(module_name):
        #print(f"Module Name in web links: {module_name}")
        web_links_by_module = {
            Module.PROJECT: Module.PROJECT,
            Module.CONTRACT: Module.CONTRACT,
            Module.EASEMENT: Module.EASEMENT,
            Module.TASK: Module.TASK,
            Module.LETTER: Module.LETTER,
            Module.COORDINATION: Module.COORDINATION,
            Module.ORDINANCE: Module.ORDINANCE,
            Module.SUBMISSION: Module.SUBMISSION,
            Module.PROPERTIE: Module.PROPERTIE,
            Module.ASBUILT: Module.TASK,
            Module.WORKS: Module.TASK
        }
        return web_links_by_module.get(module_name, "")


class MailablWebModules:
#/TODO: rebuild link services to Delegate based services as in other views

    #TODO: Trash this class!!! 

    # ✅ Class-level constants (recommended for future use)
    PROJECTS = '/projects/'
    CONTRACTS = '/contracts/'
    EASEMENTS = '/easements/'
    TASKS = '/tasks/'
    LETTERS = '/letters/'
    COORDINATIONS = '/coordinations/'
    ORDINANCES = '/ordinances/'
    SUBMISSIONS = '/submissions/'
    PROPERTIES = '/properties/'
    
#/TODO: rebuild link services to Delegate based services as in other views
    def get_web_link(self, module_name):
        print(f"Module Name in web links: {module_name}")
        web_links_by_module = {
            Module.PROJECT: MailablWebModules.PROJECTS,
            Module.CONTRACT: MailablWebModules.CONTRACTS,
            Module.EASEMENT: MailablWebModules.EASEMENTS,
            Module.TASK: MailablWebModules.TASKS,
            Module.LETTER: MailablWebModules.LETTERS,
            Module.COORDINATION: MailablWebModules.COORDINATIONS,
            Module.ORDINANCE: MailablWebModules.ORDINANCES,
            Module.SUBMISSION: MailablWebModules.SUBMISSIONS,
            Module.PROPERTIE: MailablWebModules.PROPERTIES,
            Module.ASBUILT:MailablWebModules.TASKS,
            Module.WORKS: MailablWebModules.TASKS
        }


        if module_name not in web_links_by_module:
            raise ValueError(f"Invalid module name: {module_name}")
        return web_links_by_module[module_name]
    
    
    @staticmethod
    def weblink_privacy():
        return OpenLink().privacy

    @staticmethod
    def weblink_terms_of_use():
        return OpenLink().terms

class GraphQLSettings:
    @staticmethod
    def graphql_endpoint():
        return config.get('graphql_endpoint', '')

class Devuser:
    def dev_username():
        return config.get('username', '')
     
    def dev_access():
        return config.get('word', '')


class IconsByName:
    def __init__(self):
        self.Mailabl_icon_name = "icon_Mailabl.png"
        self.icon_digi_doc_name = "Digidoc_512.png"
        self.icon_word = 'docx.png'
        self.icon_xls = 'xlsx.png'
        self.icon_pdf = 'pdf-file-format.png'
        self.icon_unknown = 'unknown-type.png'
        self.icon_folder = 'folder.png'
        self.icon_show_on_map = "oui--app-gis_kaart_asukoht.svg" #ikoonide testimiseks
        self.no_files = "plus.png"
        self.icon_autocad = "cad.png"
        self.icon_dgn = "sheet.png"
        self.icon_text = 'txt.png'
        self.icon_image = "jpg.png"
        self.icon_video = "mov.png"
        self.icon_archive = "zip.png"
        self.icon_html =  "html.png"
        self.icon_gis = "3gis.png"
        self.edit_data = "note.png"
        self.folder_empty_add = "folder_empty_add.png"
        self.folder_add = "folder_add.png"
        self.pin_add = "pin_add.png"
        

class FilesByNames:
    TEOSTUS_SETUP = "TeostusJOONISED.UI"
    DecisionMaker_UI = "DecicionMakerUI.ui"
    asBuitTools_UI = "asBuiltTools.ui"
    COORDINATIONS_UI = "CoordinationsSetup.ui"
   
    

    def __init__(self):

        self.MaaAmet_import = "Properties_backgrund.qml"
        self.Archived_layer = "Archived_properties.qml"
        self.MaaAmet_temp = "Maa_amet_temp_layer.qml"
        self.Easement_style = "Easement_Properties.qml"
        self.Easement_Water = "Easement_W.qml"
        self.Easement_Road = "Easement_Road.qml"
        self.Easement_sewage = "Easement_Sew.qml"
        self.Easement_prSewage = "Easement_PrSew.qml"
        self.Easement_Drainage = "Easement_Drainage.qml"
        self.Easement_unioned = "UnionedEasement.qml"
        self.Easement_evelLayer = "Servituut.qml"
        #Need to be separated into diferent classes!
        self.statusbar_widget = "WStatusBar.ui"



        self.layer_setup_ui = "LayerSetup.ui"
        self.projects_setup_ui = "ProjectSetup.ui"
        self.contracts_setup_ui = "ContractsSetup.ui"
        self.easements_setup_ui = "EasementsSetup.ui"
        self.user_setup_ui = "UserSetup.ui"
        self.Setup_ConfigUI = "ProjectSetup.ui"
        self.works_setup_ui = "worksSetup.ui"

        self.layer_compiler = "layer_compiler.ui"
        self.easement_tools_ui = "Servituut.ui"
        self.add_properties_to_module_ui = "Properties_connector_new.ui"
        self.EVEL_tools_ui = "EVEL.ui"

        self.WConfirmation = "Confirmation_list.ui"
        self.info_message_ui = "infoMessages.ui"
        self.Projects_UI = "Projects.ui"
        self.Contracts_UI = "Contracts.ui"
        self.Easements_UI = "Easements.ui"
        self.User_UI = "Users.ui"
        self.Properties_UI = "Properties.ui"

        self.error_message_ui = "errorMessage.ui"  #planned
        self.warning_message_ui = "warningMessage.ui"  #planned
        self.success_message_ui = "successMessage.ui"   #planned
        self.loading_message_ui = "loadingMessage.ui"   #planned

class Filepaths:
    @staticmethod
    def get_icon(icon_name):
        return os.path.join(PLUGIN_DIR_MAIN, ICONS_FOLDER, icon_name)
   
   #arrange this method for EVEL model!!!
    '''
    @staticmethod
    def get_style_evel(style_name):
        style_path = os.path.join(PLUGIN_DIR_MAIN, FUNCTIONS_FOLDER, EVEL_FOLDER, QGIS_STYLES_FOLDER)
        
        # Check for style_name directly in the main QGIS_STYLES_FOLDER
        file_path = os.path.join(style_path, style_name)
        if os.path.exists(file_path):
            return file_path
        
        # If style_name is not found directly, search in subdirectories
        for dirpath, dirnames, filenames in os.walk(style_path):
            for dirname in dirnames:
                subdir_path = os.path.join(dirpath, dirname)
                file_path = os.path.join(subdir_path, style_name)
                if os.path.exists(file_path):
                    return file_path
        
        # Return None if style_name is not found in QGIS_STYLES_FOLDER or its subfolders
        return None
    '''

    @staticmethod
    def get_style(style_name):
        return os.path.join(PLUGIN_DIR_MAIN, QGIS_STYLES_FOLDER, style_name)

    @staticmethod
    def get_easements_tools():
        return os.path.join(PLUGIN_DIR_MAIN, FUNCTIONS_FOLDER, EASEMENTS_FOLDER, WIDGETS_FOLDER, FilesByNames().easement_tools_ui)
    
    def get_EVEL_tools():
        return os.path.join(PLUGIN_DIR_MAIN, FUNCTIONS_FOLDER, EVEL_FOLDER, WIDGETS_FOLDER, FilesByNames().EVEL_tools_ui)

    @staticmethod
    def get_conf_widget(widget_name):
        return os.path.join(PLUGIN_DIR, CONF_WIDGETS_FOLDER, widget_name)
    
    @classmethod
    def _get_widget_name(self, widget_name):
        return os.path.join(PLUGIN_DIR_MAIN, WIDGETS_FOLDER, widget_name)

    @classmethod
    def get_decision_widget(cls, widget_name):
        return os.path.join(PLUGIN_DIR_MAIN, WIDGETS_FOLDER, DECISIONS_FOLDER, widget_name)
    
    @staticmethod
    def load_ui_file(ui_file_path):
        return loadUi(ui_file_path)


class QGISSavedMAilablSettings:
    def __init__(self):
        self.main_path = '/Mailabl/Setting/'
        self.setup_label_cadastral_current = '/Mailabl/Setting/labels/cadastralCurrent'
        self.setup_label_cadastral_toBeAdded = '/Mailabl/Setting/labels/cadastralToBeAdded'
        self.setup_label_cadastrals_for_importing ='/Mailabl/Settings/lables/SHP_Layer'
        

#Handles storing and displaying data in labels on other places
class DataSettings:
    def __init__(self):
        self.main_path = '/Mailabl/Setting/'
        self.setup_label_cadastral_current = '/Mailabl/Setting/labels/cadastralCurrent'
        self.setup_label_cadastral_toBeAdded = '/Mailabl/Setting/labels/cadastralToBeAdded'
        self.setup_label_cadastrals_for_importing ='/Mailabl/Settings/lables/SHP_Layer'
        
    def get_target_cadastral_current(self):
        settings = QgsSettings()
        return settings.value(self.setup_label_cadastral_current, '', type=str)

    def get_target_cadastral_toBeAdded(self):
        settings = QgsSettings()
        return settings.value(self.setup_label_cadastral_toBeAdded, '', type=str)

    def get_label_value(self, address):
        settings = QgsSettings()
        value = settings.value(address, '', type=str)
        return value

    def clear_layer_settings(self):
        settings = QgsSettings()
        settings.remove(self.setup_label_cadastral_current)
        settings.remove(self.setup_label_cadastral_toBeAdded)
        
class SettingsDataSaveAndLoad:
    def setup_main_path (self):
        self.main_path = '/Mailabl/Setting/'          
        return self.main_path
    
    def SHP_import_layer (self):
        settings_SHP_layer_name = 'labels/SHP_import'
        SHP_CADASTRAL = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{settings_SHP_layer_name}"
        #print(f"SHP_layer {SHP_CADASTRAL}")
        return SHP_CADASTRAL
    
    def Archived_layers(self):
        archived_layers = 'labels/archivedLayers'
        ARCHIVED_LAYER = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{archived_layers}"
        return ARCHIVED_LAYER



    def input_cadastral (self):
        self.setup_label_cadastral_toBeAdded = 'labels/cadastralToBeAdded'
        INPUT_CADASTRAL = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_label_cadastral_toBeAdded}"
        return INPUT_CADASTRAL

    
    def projects_copyFolderPath (self):
        self.setuup_folder_input = 'labels/projects_copyFolder'
        COPYFOLDER = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setuup_folder_input}"
        return COPYFOLDER

    def projects_targetFolderPath(self):
        self.setup_folder_output = 'labels/projects_targetFolder'
        TARGETFOLDER = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_folder_output}"
        return TARGETFOLDER
    
    def projects_Folder_preferred_name_structure(self):
        preferred_projects_name_structure = 'labels/projects_preferred_projects_name_structure'
        FOLDER_NAME_STRUCTURE = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{preferred_projects_name_structure}"
        return FOLDER_NAME_STRUCTURE
    

    def user_name (self):
        user_name = 'labels/user_name'
        USER_FIRSTNAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{user_name}"
        return USER_FIRSTNAME

    def user_lastname (self):
        user_lastname = 'labels/user_lastname'
        USER_LASTNAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{user_lastname}"
        return USER_LASTNAME

    def user_roles (self):
        user_roles = 'labels/user_roles'
        USER_ROLES = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{user_roles}"
        return USER_ROLES

    def user_prefered_startpage_name (self):
        user_pr_page_name = 'labels/user_preferred_homepage'
        USER_PREFERRED_PAGE_NAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{user_pr_page_name}"
        return USER_PREFERRED_PAGE_NAME

    def user_prefered_startpage_index (self):
        user_pr_page_index = 'labels/user_preferred_homepage_index'
        USER_PREFERRED_PAGE_INDEX = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{user_pr_page_index}"
        return USER_PREFERRED_PAGE_INDEX


    def target_cadastral (self):
        self.setup_label_cadastral_current = 'labels/cadastralCurrent'
        TARGET_CADASTRAL = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_label_cadastral_current}"
        return TARGET_CADASTRAL

    def _save_SHP_layer_setting(self,label,layer):
        settings = QgsSettings()
        #save setup target
        value = layer
        target_settings_address = SettingsDataSaveAndLoad.SHP_import_layer(self)
        settings.setValue(target_settings_address, value)
        label.setText(value)

    def save_archived_layers(self, layers, label=None,):
        settings = QgsSettings()
        archived_layers_address = SettingsDataSaveAndLoad.Archived_layers(self)
        settings.setValue(archived_layers_address, layers)
        if label is not None:
            label.setText(layers)
    
    def save_target_cadastral(self, input_value ):#, target_value):
        settings = QgsSettings()
        target_settings_address = SettingsDataSaveAndLoad.target_cadastral(self)
        settings.setValue(target_settings_address, input_value)
        #input_setting_address = SettingsDataSaveAndLoad.input_cadastral(self)
        #settings.setValue(input_setting_address, target_value)
        


    def save_projects_folder_preferred_name_structure(self, input_value):
        settings = QgsSettings()
        preferred_folder_name_adress = SettingsDataSaveAndLoad.projects_Folder_preferred_name_structure(self)
        settings.setValue(preferred_folder_name_adress, input_value)

    def save_user_values(self, user_name, user_lastname, roles):
        settings = QgsSettings()
        
        user_name_address = SettingsDataSaveAndLoad.user_name(self)
        user_lastname_address = SettingsDataSaveAndLoad.user_lastname(self)
        user_roles_address = SettingsDataSaveAndLoad.user_roles(self)
        settings.setValue(user_name_address, user_name)
        settings.setValue(user_lastname_address, user_lastname)
        settings.setValue(user_roles_address, roles)

    def save_user_prefered_startpage(self, user_page_index, user_page_name):
        settings = QgsSettings()
        user_page_name_setting = SettingsDataSaveAndLoad.user_prefered_startpage_name(self)
        user_page_index_setting = SettingsDataSaveAndLoad.user_prefered_startpage_index(self)
        settings.setValue(user_page_index_setting, user_page_index)
        settings.setValue(user_page_name_setting, user_page_name)

    def save_FolderValues(self, lblProjectsFolderValue, lblProjectsTargetFolderValue, copy_folder, target_folder):

        settings = QgsSettings()
        copy_folder_settings_address = SettingsDataSaveAndLoad.projects_copyFolderPath(self)
        target_folder_settings_address = SettingsDataSaveAndLoad.projects_targetFolderPath(self)
        settings.setValue(copy_folder_settings_address, copy_folder)
        settings.setValue(target_folder_settings_address, target_folder)
        lblProjectsFolderValue.setText(copy_folder)
        lblProjectsTargetFolderValue.setText(target_folder)



        

    def load_projcets_copy_folder_path_value(self):
        settings_address = SettingsDataSaveAndLoad.projects_copyFolderPath(self)
        settings = QgsSettings()
        return settings.value(settings_address, '', type=str)
    
    def load_target_Folder_path_value(self):
        settings_address = SettingsDataSaveAndLoad.projects_targetFolderPath(self)
        settings = QgsSettings()
        return settings.value(settings_address, '', type=str)


    def load_projects_prefered_folder_name_structure(self):
        settings_projects_preferred_folder_name = SettingsDataSaveAndLoad.projects_Folder_preferred_name_structure(self)
        settings = QgsSettings()
        return settings.value(settings_projects_preferred_folder_name, '', type=str)
    
    def load_user_name(self):
        user_name = SettingsDataSaveAndLoad.user_name(self)
        settings = QgsSettings()
        return settings.value(user_name, '', type=str)

    def load_user_lastname(self):
        user_lastname = SettingsDataSaveAndLoad.user_lastname(self)
        settings = QgsSettings()
        return settings.value(user_lastname, '', type=str)

    def load_user_roles(self):
        user_roles = SettingsDataSaveAndLoad.user_roles(self)
        settings = QgsSettings()
        return settings.value(user_roles, '', type=str)
    
    def load_user_prefered_startpage_index(self):
        prefered_startpage_index = SettingsDataSaveAndLoad.user_prefered_startpage_index(self)
        settings = QgsSettings()
        return settings.value(prefered_startpage_index, '', type=str)
        

    def load_user_prefered_startpage_name(self):
        prefered_startpage_name = SettingsDataSaveAndLoad.user_prefered_startpage_name(self)
        settings = QgsSettings()
        return settings.value(prefered_startpage_name, '', type=str)
    

    def load_target_cadastral_name(self):
        settings_address = SettingsDataSaveAndLoad.target_cadastral(self)
        settings = QgsSettings()
        return settings.value(settings_address, '', type=str)
    
    def load_input_cadastral_name(self):
        settings_address = SettingsDataSaveAndLoad.input_cadastral(self)
        settings = QgsSettings()
        return settings.value(settings_address, '', type=str)
    
    def load_SHP_inputLayer_name(self):
        settings_address = SettingsDataSaveAndLoad.SHP_import_layer(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    



class StoredLayers:    
    def users_properties_layer_name():
        active_layer = SettingsDataSaveAndLoad().load_target_cadastral_name()
        return active_layer
        
    def import_layer_name():
        settings_loader = SettingsDataSaveAndLoad()
        active_layer = settings_loader.load_SHP_inputLayer_name()
        return active_layer
    


class StartupSettingsLoader:
    def __init__(cls, dialog):
        cls.dialog = dialog    
    def startup_label_loader(self):

        SettingsBuilder.initialize_settings()

        StartupSettingsLoader.load_drawings_settings(self)

        StartupSettingsLoader.load_coordination_settings(self)

        prefEasementTypeName = PluginSettings.load_setting(module = Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_NAME, 
            text_fomated=True
        )


        prefContractTypeName = PluginSettings.load_setting(module = Module.CONTRACT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            text_fomated=True
        )

        self.dialog.lblPreferredEasementsTypesValue.setText(prefEasementTypeName)
        self.dialog.lblPreferredContractsTypesValue.setText(prefContractTypeName)

        prefEasementStatusName = PluginSettings.load_setting(module = Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME
        )

        prefProjectStatusName = PluginSettings.load_setting(module = Module.PROJECT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME
        )

        prefContractsStatusName = PluginSettings.load_setting(module = Module.CONTRACT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME
        )
        prefAsbuiltStatusName = PluginSettings.load_setting(module = Module.TASK,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME
        )

        self.dialog.lblPreferredProjectStatusValue.setText(prefProjectStatusName)
        self.dialog.lblPreferredContractStatusValue.setText(prefContractsStatusName)
        self.dialog.lblPreferredEasementsStatusValue.setText(prefEasementStatusName)


        water_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.WATER        )

        sewer_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.SEWER
        )


        pressure_sewer_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.PRESSURE_SEWER
        )
        
        drainage_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.DRAINAGE
        )
        self.dialog.lblWaterPipesValue.setText(water_layer_name)
        self.dialog.lblSewerPipesValue.setText(sewer_layer_name)
        self.dialog.lblPrSewagePipesValue.setText(pressure_sewer_layer_name)
        self.dialog.lblDrainagePipesValue.setText(drainage_layer_name)


        projects_label_value = PluginSettings.load_setting(
            module=Module.PROJECT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.PROJECTS_LAYER,
        )


        self.dialog.lblLayerProjectsValue.setText(projects_label_value)

        current_label_value = SettingsDataSaveAndLoad().load_target_cadastral_name()
        self.dialog.lblMainLayerValue.setText(current_label_value)

        StartupSettingsLoader.load_works_settings(self)


        prefered_folder_structure_value = SettingsDataSaveAndLoad.load_projects_prefered_folder_name_structure(self)
        
        SHP_layer_label_value = SettingsDataSaveAndLoad.load_SHP_inputLayer_name(self)

        input_folder_value = SettingsDataSaveAndLoad.load_projcets_copy_folder_path_value(self)
        output_folder_value = SettingsDataSaveAndLoad.load_target_Folder_path_value(self)
 
        prefered_homepage_name_value = SettingsDataSaveAndLoad.load_user_prefered_startpage_name(self)

        if prefered_homepage_name_value == "":
            self.dialog.lblSPreferedHomeValue.setText("Määramata")
        else:
            self.dialog.lblSPreferedHomeValue.setText(prefered_homepage_name_value)

        self.dialog.lblPreferredFolderNameValue.setText(prefered_folder_structure_value)

        self.dialog.lblSHPLayerValue.setText(SHP_layer_label_value)

        self.dialog.lblProjectsFolderValue.setText(input_folder_value)
        self.dialog.lblProjectsTargetFolderValue.setText(output_folder_value)

        self.dialog.lblLayerProjectsBaseValue.setText("Määramata*")
        self.dialog.lblLayerProjectsBaseValue.setEnabled(False)


    def load_works_settings(self):
        module = Module.WORKS

        works_layer_name = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.WORKS_LAYER
        )

        status_name = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            )
        
        types_names = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            text_fomated=True
        )

        if works_layer_name == "":
            self.dialog.lblWorksLayerValue.setText("Määramata")
        else:
            self.dialog.lblWorksLayerValue.setText(works_layer_name)

        if status_name == "":
            self.dialog.lblworksPreferredStatusesValue.setText("Määramata")
        else:
            self.dialog.lblworksPreferredStatusesValue.setText(status_name)

        if types_names == "":
            self.dialog.lblWorksActionsValue.setText("Määramata")
        else:
            self.dialog.lblWorksActionsValue.setText(types_names)




    def load_drawings_settings(self):
        module = Module.ASBUILT

        status_name = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            )

        AsbuiltLayer = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.ASBUILT_LAYER
        )

        types_names = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            text_fomated=True
        )


        folder = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.CONTEXT_FOLDER,
        )

        value = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.CONTEXT_FOLDER,
            key_type=PluginSettings.CHECKBOXVALUE,
        )

        if value == "true":
            value = True
        else:
            value = False

        self.dialog.cbPartOfProject.setChecked(value)

        self.dialog.lblTeostusPreferredStatusesValue.setText(status_name)
        self.dialog.lblTeostusMapLayerValue.setText(AsbuiltLayer)
       
        self.dialog.lblTesotusActionsValue.setText(types_names)
        self.dialog.lblTeostusFolderNameValue.setText(folder)
        

    def load_coordination_settings(self):
        module = Module.COORDINATION

        status_name = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            )

        CooperationsLayer = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.ASBUILT_LAYER
        )

        types_names = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            text_fomated=True
        )

        self.dialog.lblCoordinationsActionsValue.setText(types_names)
        self.dialog.lblCoordinationsPreferredStatusesValue.setText(status_name)
        self.dialog.lblCoordinationsMapLayerValue.setText(CooperationsLayer)