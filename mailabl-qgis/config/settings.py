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
    main = config.get('weblink', '')
    privacy = config.get('privacy', '')
    terms = config.get('terms', '')

    @staticmethod
    def web_link_single_projects():
        return f'{OpenLink.main}/projects/'

    @staticmethod
    def weblink_single_contract():
        return f'{OpenLink.main}/contracts/'

    @staticmethod
    def weblink_privacy():
        return OpenLink.privacy

    @staticmethod
    def weblink_terms_of_use():
        return OpenLink.terms

class GraphQLSettings:
    @staticmethod
    def graphql_endpoint():
        return config.get('graphql_endpoint', '')

class IconsByName:
    def __init__(self):
        self.Mailabl_icon_name = "icon_Mailabl.png"
        self.icon_digi_doc_name = "Digidoc_512.png"
        self.icon_show_on_map = "oui--app-gis_kaart_asukoht.svg" #ikoonide testimiseks

class FilesByNames:
    def __init__(self):
        self.Setup_ConfigUI = "ProjectSetup.ui"
        self.MaaAmet_import = "MaaAmet_Layer_backround.qml"
        self.MaaAmet_temp = "Maa_amet_temp_layer.qml"
        self.statusbar_widget = "WStatusBar.ui"
        self.layer_setup_ui = "LayerSetup.ui"
        self.projects_setup_ui = "ProjectSetup.ui"

class Filepaths:
    @staticmethod
    def get_icon(icon_name):
        return os.path.join(PLUGIN_DIR_MAIN, ICONS_FOLDER, icon_name)

    @staticmethod
    def get_style(style_name):
        return os.path.join(PLUGIN_DIR_MAIN, QGIS_STYLES_FOLDER, style_name)

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
        self.setup_label_cadastral_current = 'labels/projects_copyFolder'
        COPYFOLDER = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_label_cadastral_current}"
        return COPYFOLDER

    def projects_targetFolderPath (self):
        self.setup_label_cadastral_current = 'labels/projects_targetFolder'
        TARGETFOLDER = f"{SettingsDataSaveAndLoad.setup_main_path(self)}{self.setup_label_cadastral_current}"
        return TARGETFOLDER
    
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

    def save_FolderValues(self, copy_folder, target_folder):
        settings = QgsSettings()
        copy_folder_settings_address = SettingsDataSaveAndLoad.projects_copyFolderPath(self)
        target_folder_settings_address = SettingsDataSaveAndLoad.projects_targetFolderPath(self)
        settings.setValue(copy_folder_settings_address, copy_folder)
        settings.setValue(target_folder_settings_address, target_folder)
        

        
    def startup_label_loader (self,lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, lblLayerProjects_Properties):
        current_label_value = SettingsDataSaveAndLoad().load_target_cadastral_name()
        create_new_layer_label_value = SettingsDataSaveAndLoad.load_input_cadastral_name(self)
        SHP_layer_label_value = SettingsDataSaveAndLoad.load_SHP_inputLayer_name(self)
        projects_label_value = SettingsDataSaveAndLoad.load_projects_properties_layer_name(self)
        lblcurrent_main_layer_label.setText(current_label_value)
        lblnewCadastrals_input_layer_label.setText(create_new_layer_label_value)
        lblSHPNewItems.setText(SHP_layer_label_value)
        lblLayerProjects_Properties.setText(projects_label_value)
        
    
        
    def on_save_button_clicked_cadastrals(self, input_layer_combo_box, target_layer_combo_box):
        #print("started to save")
        input_value = input_layer_combo_box.currentText()
        target_value = target_layer_combo_box.currentText()
        SettingsDataSaveAndLoad.save_target_cadastral(self,input_value, target_value)
        #print(f"Data saved {input_layer_combo_box} and {target_layer_combo_box}")
        
    def on_save_button_clicked_projects(self, cmb_layers, lblProjectsTargetFolder_location, lblProjectsFolder_location):
        #print("started to save")
        copy_folder = lblProjectsFolder_location.Text()
        Target_folder = lblProjectsTargetFolder_location.Text()
        project_value = cmb_layers.currentText()
        SettingsDataSaveAndLoad.save_target_projects(self, project_value)
        SettingsDataSaveAndLoad.save_FolderValues(self, copy_folder, Target_folder)
        
        
        
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
        