import os
import json
from PyQt5.uic import loadUi
from qgis.core import QgsSettings

PLUGIN_DIR = os.path.dirname(__file__)
PLUGIN_DIR_MAIN = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Constants
CONF_FOLDER = "config"
CONF_WIDGETS_FOLDER = "confWidgets"
QGIS_STYLES_FOLDER = "QGIS_styles"
ICONS_FOLDER = "icons/"
WIDGETS_FOLDER = "widgets"
CONFIG_FILE = "config.json"
FUNCTIONS_FOLDER = "Functions"
EASEMENTS_FOLDER = "Easements"

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
    Flag_settings_button = True
    Flag_SliderButton_LoadData = False
    Flag_SliderButton_Properties = False    
    Flag_Running_Process = False

class OpenLink:
    def __init__(self):
        self.main = config.get('weblink', '')
        self.privacy = config.get('privacy', '')
        self.terms = config.get('terms', '')

    @staticmethod
    def weblink_by_module(module):
        print
        return f"{OpenLink().main}{module}"


class MailablWebModules:
    def __init__(self):
        self.projects = '/projects/'
        self.contracts = '/contracts/'
        self.easements = '/easements/'


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

class IconsByName:
    def __init__(self):
        self.Mailabl_icon_name = "icon_Mailabl.png"
        self.icon_digi_doc_name = "Digidoc_512.png"
        self.icon_word = 'doc.png'
        self.icon_xls = 'xls.png'
        self.icon_pdf = 'pdf-file-format.png'
        self.icon_unknown = 'unknown-type.png'
        self.icon_folder = 'folder.png'
        self.icon_show_on_map = "oui--app-gis_kaart_asukoht.svg" #ikoonide testimiseks

class FilesByNames:
    def __init__(self):
        self.Setup_ConfigUI = "ProjectSetup.ui"
        self.MaaAmet_import = "MaaAmet_Layer_backround.qml"
        self.MaaAmet_temp = "Maa_amet_temp_layer.qml"
        self.statusbar_widget = "WStatusBar.ui"
        self.layer_setup_ui = "LayerSetup.ui"
        self.projects_setup_ui = "ProjectSetup.ui"
        self.contracts_setup_ui = "ContractsSetup.ui"
        self.easements_setup_ui = "EasementsSetup.ui"
        self.easement_tools_ui = "Servituut.ui"

class Filepaths:
    @staticmethod
    def get_icon(icon_name):
        return os.path.join(PLUGIN_DIR_MAIN, ICONS_FOLDER, icon_name)

    @staticmethod
    def get_style(style_name):
        return os.path.join(PLUGIN_DIR_MAIN, QGIS_STYLES_FOLDER, style_name)

    @staticmethod
    def get_easements_tools():
        return os.path.join(PLUGIN_DIR_MAIN, FUNCTIONS_FOLDER, EASEMENTS_FOLDER, WIDGETS_FOLDER, FilesByNames().easement_tools_ui)

    @staticmethod
    def get_conf_widget(widget_name):
        return os.path.join(PLUGIN_DIR, CONF_WIDGETS_FOLDER, widget_name)
    
    @classmethod
    def get_widget(self, widget_name):
        return os.path.join(PLUGIN_DIR_MAIN, WIDGETS_FOLDER, widget_name)

    @staticmethod
    def load_ui_file(ui_file_path):
        return loadUi(ui_file_path)

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

    def target_cadastral (self):
        self.setup_label_cadastral_current = 'labels/cadastralCurrent'
        TARGET_CADASTRAL = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_label_cadastral_current}"
        return TARGET_CADASTRAL


    def input_cadastral (self):
        self.setup_label_cadastral_toBeAdded = 'labels/cadastralToBeAdded'
        INPUT_CADASTRAL = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_label_cadastral_toBeAdded}"
        return INPUT_CADASTRAL

    def projects_cadastral (self):
        self.setup_label_cadastral_current = 'labels/projects_cadastrals'
        TARGET_CADASTRAL = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_label_cadastral_current}"
        return TARGET_CADASTRAL
    
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
    
    def projects_preferred_status_ID (self):
        self.setup_projects_preferred_status = 'labels/projects_preferred_status'
        PROJECT_STATUS = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_projects_preferred_status}"
        return PROJECT_STATUS

    def projects_preferred_status_Name (self):
        self.setup_projects_preferred_status_name = 'labels/projects_preferred_status_name'
        PROJECT_STATUS_NAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_projects_preferred_status_name}"
        return PROJECT_STATUS_NAME
    
    def contracts_preferred_type_name(self):
        setup_contracts_preferred_status_name = 'labels/contracts_preferred_type_name'
        CONTRACT_TYPE_NAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{setup_contracts_preferred_status_name}"
        return CONTRACT_TYPE_NAME
    

    def contracts_preferred_status_ids(self):
            setup_contracts_preferred_status_ids = 'labels/contracts_preferred_status_ids'
            CONTRACT_STATUS_IDS = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{setup_contracts_preferred_status_ids}"
            return CONTRACT_STATUS_IDS
        
    def contracts_preferred_status_name(self):
        setup_contracts_preferred_status_ids = 'labels/contracts_preferred_status_names'
        CONTRACT_STATUS_NAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{setup_contracts_preferred_status_ids}"
        return CONTRACT_STATUS_NAME

    def easements_preferred_type_name(self):
        setup_easements_preferred_status_name = 'labels/easements_preferred_type_name'
        EASEMENTS_TYPE_NAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{setup_easements_preferred_status_name}"
        return EASEMENTS_TYPE_NAME
    

    def easements_preferred_status_ids(self):
            setup_easements_preferred_status_ids = 'labels/easements_preferred_status_ids'
            EASEMENTS_STATUS_IDS = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{setup_easements_preferred_status_ids}"
            return EASEMENTS_STATUS_IDS
        
    def easements_preferred_status_name(self):
        setup_easements_preferred_status_ids = 'labels/easements_preferred_status_names'
        EASEMENTS_STATUS_NAME = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{setup_easements_preferred_status_ids}"
        return EASEMENTS_STATUS_NAME


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

    def save_SHP_layer_setting(self,label,layer):
        settings = QgsSettings()
        #save setup target
        value = layer
        target_settings_address = SettingsDataSaveAndLoad.SHP_import_layer(self)
        settings.setValue(target_settings_address,value)
        label.setText(value)
    
    def save_target_cadastral(self, input_value, target_value):
        settings = QgsSettings()
        #print(f"save_target_cadastral 'target_value' {target_value}")
        #save setup target
        target_settings_address = SettingsDataSaveAndLoad.target_cadastral(self)
        #print(f"save_target_cadastral 'target_settings_address' {target_settings_address}")
        settings.setValue(target_settings_address, input_value)
        #save setup input
        #print(f"save_target_cadastral 'input_vlue': {input_value}")
        input_setting_address = SettingsDataSaveAndLoad.input_cadastral(self)
        #print(f"save_target_cadastral 'input_setting_address' {input_setting_address}")
        settings.setValue(input_setting_address, target_value)
        
    def save_target_projects(self, input_value):
        settings = QgsSettings()
        target_settings_address = SettingsDataSaveAndLoad.projects_cadastral(self)
        settings.setValue(target_settings_address, input_value)

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
        

    def save_FolderValues(self, lblProjectsFolder_location, lblProjectsTargetFolder_location, copy_folder, target_folder):
        settings = QgsSettings()
        copy_folder_settings_address = SettingsDataSaveAndLoad.projects_copyFolderPath(self)
        target_folder_settings_address = SettingsDataSaveAndLoad.projects_targetFolderPath(self)
        settings.setValue(copy_folder_settings_address, copy_folder)
        settings.setValue(target_folder_settings_address, target_folder)
        lblProjectsFolder_location.setText(copy_folder)
        lblProjectsTargetFolder_location.setText(target_folder)

    def save_preferred_projects_status_id(self, project_id, status_name, label):
        settings = QgsSettings()
        # Extract the integer value from the list
        project_id_int = int(project_id[0]) if project_id else None
        print(f"id_s: {project_id_int}")
        path = SettingsDataSaveAndLoad.projects_preferred_status_ID(self)
        path_name = SettingsDataSaveAndLoad.projects_preferred_status_Name(self)
        settings.setValue(path, project_id_int)
        settings.setValue(path_name, status_name)
        # Set the text of the label to the string representation of project_id_int
        label.setText(str(project_id_int))

    def save_contract_settings(self, contract_type_names, contratc_status_names, contract_status_ids):
        settings = QgsSettings()
        contract_status_ids_int = int(contract_status_ids[0]) if contract_status_ids else None
        print(f"id_s: {contract_status_ids_int}")
        print(f"contract types: {contract_type_names}")
        contrcts_status_ids_path = SettingsDataSaveAndLoad.contracts_preferred_status_ids(self)
        contracts_status_name_path = SettingsDataSaveAndLoad.contracts_preferred_status_name(self)
        contract_name_paths = SettingsDataSaveAndLoad.contracts_preferred_type_name(self)
        settings.setValue(contrcts_status_ids_path, contract_status_ids_int)
        settings.setValue(contracts_status_name_path, contratc_status_names)
        settings.setValue(contract_name_paths, contract_type_names)

    def save_easements_settings(self, easements_type_names, contratc_status_names, easements_status_ids):
        settings = QgsSettings()
        easements_status_ids_int = int(easements_status_ids[0]) if easements_status_ids else None
        print(f"id_s: {easements_status_ids_int}")
        print(f"easements types: {easements_type_names}")
        easments_status_ids_path = SettingsDataSaveAndLoad.easements_preferred_status_ids(self)
        easements_status_name_path = SettingsDataSaveAndLoad.easements_preferred_status_name(self)
        easements_name_paths = SettingsDataSaveAndLoad.easements_preferred_type_name(self)
        settings.setValue(easments_status_ids_path, easements_status_ids_int)
        settings.setValue(easements_status_name_path, contratc_status_names)
        settings.setValue(easements_name_paths, easements_type_names)


    def startup_label_loader (self,lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, 
                              lblLayerProjects_Properties, lblProjectsFolder_location, lblProjectsTargetFolder_location,
                              lbl_preferred_project_status, lbl_preferred_contract_status, lblPreferredContractsTypes_value):
        current_label_value = SettingsDataSaveAndLoad().load_target_cadastral_name()
        create_new_layer_label_value = SettingsDataSaveAndLoad.load_input_cadastral_name(self)
        SHP_layer_label_value = SettingsDataSaveAndLoad.load_SHP_inputLayer_name(self)
        projects_label_value = SettingsDataSaveAndLoad.load_projects_properties_layer_name(self)
        input_folder_value = SettingsDataSaveAndLoad.load_projcets_copy_folder_path_value(self)
        output_folder_value = SettingsDataSaveAndLoad.load_target_Folder_path_value(self)
        projects_status_name_value = SettingsDataSaveAndLoad.load_projects_status_name(self)
        contracts_type_names = SettingsDataSaveAndLoad.load_contracts_type_names(self)
        contracts_status_names = SettingsDataSaveAndLoad.load_contract_status_names(self)

        lblcurrent_main_layer_label.setText(current_label_value)
        lblnewCadastrals_input_layer_label.setText(create_new_layer_label_value)
        lblSHPNewItems.setText(SHP_layer_label_value)
        lblLayerProjects_Properties.setText(projects_label_value)
        lblProjectsFolder_location.setText(input_folder_value)
        lblProjectsTargetFolder_location.setText(output_folder_value)
        lbl_preferred_project_status.setText(projects_status_name_value)
        lblPreferredContractsTypes_value.setText(contracts_type_names)
        lbl_preferred_contract_status.setText(contracts_status_names)
        
        
    def on_save_button_clicked_cadastrals(self, input_layer_combo_box, target_layer_combo_box):
        #print("started to save")
        input_value = input_layer_combo_box.currentText()
        target_value = target_layer_combo_box.currentText()
        SettingsDataSaveAndLoad.save_target_cadastral(self,input_value, target_value)
        #print(f"Data saved {input_layer_combo_box} and {target_layer_combo_box}")
        
    def on_save_button_clicked_projects(self, cmb_layers, lblProjectsTargetFolder_location, lblProjectsFolder_location, target_value, input_value):
        #print("started to save")
        copy_folder = input_value.text()
        target_folder = target_value.text()
        project_value = cmb_layers.currentText()
        #SettingsDataSaveAndLoad.save_projects_folder_preferred_name_structure(self, input_value)
        SettingsDataSaveAndLoad.save_target_projects(self, project_value)
        SettingsDataSaveAndLoad.save_FolderValues(self,lblProjectsFolder_location, lblProjectsTargetFolder_location, copy_folder, target_folder)


    def load_projcets_copy_folder_path_value(self):
        settings_address = SettingsDataSaveAndLoad.projects_copyFolderPath(self)
        settings = QgsSettings()
        return settings.value(settings_address, '', type=str)
    
    def load_target_Folder_path_value(self):
        settings_address = SettingsDataSaveAndLoad.projects_targetFolderPath(self)
        settings = QgsSettings()
        return settings.value(settings_address, '', type=str)

    def load_projects_status_id(self):
        settings_projects_id = SettingsDataSaveAndLoad.projects_preferred_status_ID(self)
        settings = QgsSettings()
        return settings.value(settings_projects_id, '', type=str)
        
    def load_projects_status_name(self):
        settings_projects_status_name = SettingsDataSaveAndLoad.projects_preferred_status_Name(self)
        settings = QgsSettings()
        return settings.value(settings_projects_status_name, '', type=str)
    
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
    
    def load_projects_properties_layer_name(self):
        settings_address = SettingsDataSaveAndLoad.projects_cadastral(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value

    def load_contracts_type_names(self):
        settings_address = SettingsDataSaveAndLoad.contracts_preferred_type_name(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    
    def load_contract_status_ids(self):
        settings_address = SettingsDataSaveAndLoad.contracts_preferred_status_ids(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    
    def load_contract_status_names(self):
        settings_address = SettingsDataSaveAndLoad.contracts_preferred_status_name(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    
    def load_easements_type_names(self):
        settings_address = SettingsDataSaveAndLoad.easements_preferred_type_name(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    
    def load_easements_status_ids(self):
        settings_address = SettingsDataSaveAndLoad.easements_preferred_status_ids(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    
    def load_easements_status_names(self):
        settings_address = SettingsDataSaveAndLoad.easements_preferred_status_name(self)
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value


class connect_settings_to_layer:    
    def ActiveMailablPropertiesLayer_name():
        active_layer = SettingsDataSaveAndLoad().load_target_cadastral_name()
        return active_layer
        
    def Import_Layer_name():
        settings_loader = SettingsDataSaveAndLoad()
        active_layer = settings_loader.load_SHP_inputLayer_name()
        return active_layer
    

class settingPageElements():
    def __init__(self,lblcurrent_main_layer_label, lblnewCadastrals_input_layer_label, lblSHPNewItems, label_14, lblLayerProjects_Properties):
        self.lblcurrent_main_layer_label = lblcurrent_main_layer_label
        self.lblnewCadastrals_input_layer_label = lblnewCadastrals_input_layer_label
        self.lblSHPNewItems = lblSHPNewItems
        self.label_14 = label_14
        self.lblLayerProjects_Properties = lblLayerProjects_Properties
        