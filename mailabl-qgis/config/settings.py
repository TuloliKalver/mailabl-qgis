import os
import json
from PyQt5.uic import loadUi
from qgis.core import QgsSettings
from qgis.core import (QgsFeature, QgsGeometry, QgsLayerTreeGroup, QgsMapLayer,
                       QgsProject, QgsSettings, QgsVectorLayer)


PLUGIN_DIR = os.path.dirname(__file__)
CONF_FOLDER = "config"
CONF_WIDGETS_FOLDER = "confWidgets"


main_path = '/Mailabl/Setting/'
setup_label_cadastral_current = '/Mailabl/Setting/labels/cadastralCurrent'
setup_label_cadastral_toBeAdded = '/Mailabl/Setting/labels/cadastralToBeAdded'
setup_label_cadastrals_for_importing ='/Mailabl/Settings/lables/SHP_Layer'
Mailabl_Projects_layer_address = 'Mailabl/labels/Mailabl_Projects_layer'



with open(f'{PLUGIN_DIR}/config.json', "r") as json_content:
    config = json.load(json_content)

class version:
    @staticmethod
    def get_plugin_version(metadata_file):
        with open(metadata_file, 'r') as f:
            for line in f:
                if line.strip().startswith("version="):
                    return line.strip().split('=')[1]

class flags:
    active_properties_layer_flag = False
    Flag_settings_button = True
    Flag_SliderButton_LoadData = False
    Flag_SliderButton_Properties = False    
    Flag_Running_Process = False


class OpenLink:
    main = config['weblink']
    
    def weblink_single_projects():
        link = f'{OpenLink.main}/projects/'
        return link

    def weblink_single_contract():
        link = f'{OpenLink.main}/contracts/'
        return link



class GraphQLSettings:
    def graphql_endpoint():
        return config['graphql_endpoint']

class IconsByName:
    def __init__(self):
        icon_digiDoc_name = "Digidoc_512.png"
        icon_mailabl_name= "icon.png"


class Filepaths:
    Mailabl_icon_name = "icon.png"
    pluginDir_updated = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def __init__(self):
        # Main directory
        self.PLUGIN_DIR = os.path.dirname(__file__)
        self.pluginDir_updated = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.Setup_ConfigUI = "ProjectSetup.ui"
        self.MaaAmet_import = "MaaAmet_Layer_backround.qml"
        self.MaaAmet_temp = "Maa_amet_temp_layer.qml"
        

    @staticmethod
    def Mailabl_icon():
        icon_filename = Filepaths.Mailabl_icon_name  # Access the attribute directly from the class
        plugin_dir = Filepaths.pluginDir_updated
        icon_path = os.path.join(plugin_dir, icon_filename)
        #print(icon_path)
        return icon_path

    def digiDoc_icon(self):
        icon_filename="Digidoc_512.png"
        icon_path = os.path.join(PLUGIN_DIR, icon_filename)
        #print(icon_path)
        return icon_path

    #style setup folder
    
    def File_maaAmet_style(self):
        style_folder = "QGIS_styles" 
        style_path = os.path.join(self.pluginDir_updated,style_folder, self.MaaAmet_import)
        #print (f"From settings: {style_path}")
        return style_path

    def File_MaaAmet_temporary_style(self):
        style_folder = "QGIS_styles" 
        style_path = os.path.join(self.pluginDir_updated,style_folder, self.MaaAmet_temp)
        #print (f"From settings: {style_path}")
        return style_path


    def Status_bar_loader_properties(self):
    #Status bar widget folder
        WIDGETS_FOLDER = "widgets"  
        WIDGETS_PATH = os.path.join(PLUGIN_DIR,WIDGETS_FOLDER, "WStatusBar.ui")
        return WIDGETS_PATH

#Open Dialog to settup layers
    def Config_LayerSettings_Widget(self):
        CONF_WIDGETS_FOLDER = "confWidgets"
        FILE = "LayerSetup.ui"
        CONF_WIDGETS_PATH = os.path.join(PLUGIN_DIR, CONF_WIDGETS_FOLDER, FILE)
        return CONF_WIDGETS_PATH
    
    def Config_ProjectSettings_Widget(self):       
        CONF_WIDGETS_FOLDER = "confWidgets"
        FILE = "ProjectSetup.ui"
        CONF_WIDGETS_PATH = os.path.join(PLUGIN_DIR, CONF_WIDGETS_FOLDER, FILE)
        return CONF_WIDGETS_PATH
    
    
    
    # Load the custom progress widget from the .ui file
    def load_layer_settings_widget(self):
        #print("started")
        ui_file_path = self.Config_LayerSettings_Widget()
        #print(ui_file_path)
        progress_widget = loadUi(ui_file_path)
        #print(progress_widget)
        progress_widget.show()
        #print("ended")

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
        SHP_CADASTRAL = f"{main_path}{settings_SHP_layer_name}"
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

        
    def startup_label_loader (self,lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, lblLayerProjects_Properties):
        current_label_value = SettingsDataSaveAndLoad.load_target_cadastral_name(self)
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
        
    def on_save_button_clicked_projects(self, cmb_layers):
        #print("started to save")
        project_value = cmb_layers.currentText()
        SettingsDataSaveAndLoad.save_target_projects(self, project_value)
        
        
        
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
        settings_loader = SettingsDataSaveAndLoad()
        active_layer = settings_loader.load_target_cadastral_name()
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
        