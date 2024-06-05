
from qgis.core import QgsSettings

MAIN_PATH = '/Mailabl/Setting/'

class LayerSettings:
    CADASTRAL_CURRENT = 'labels/cadastralCurrent'
    CADASTRAL_TO_BE_ADDED = 'labels/cadastralToBeAdded'
    PROJECTS_CADASTRALS = 'labels/projects_cadastrals'
    WATER_LAYER = 'labels/water_layer'
    SEWER_LAYER = 'labels/sewer_layer'
    PRESSURE_SEWER_LAYER = 'labels/pressure_sewer_layer'
    RAINWATER_LAYER = 'labels/rainwater_layer'
    DRAINAGE_LAYER = 'labels/drainage_layer'
    PUMPINGSTATION_LAYER = 'labels/pumpingstation_layer'

class ProjectSettings:
    PROJECTS_COPY_FOLDER_PATH = 'labels/projects_copyFolder'
    PROJECTS_TARGET_FOLDER_PATH = 'labels/projects_targetFolder'
    PROJECTS_FOLDER_PREFERRED_NAME_STRUCTURE = 'labels/projects_preferred_projects_name_structure'
    PROJECTS_PREFERRED_STATUS_ID = 'labels/projects_preferred_status'
    PROJECTS_PREFERRED_STATUS_NAME = 'labels/projects_preferred_status_name'

class ContractsSettings:
    CONTRACTS_TYPE_NAME = 'labels/contracts_preferred_type_name'
    CONTRACTS_STATUS_IDS = 'labels/contracts_preferred_status_ids'
    CONTRACTS_STATUS_NAME = 'labels/contracts_preferred_status_names'

class EasementsSettings:
    EASEMENTS_TYPE_NAME = 'labels/easements_preferred_type_name'
    EASEMENTS_STATUS_IDS = 'labels/easements_preferred_status_ids'
    EASEMENTS_STATUS_NAME = 'labels/easements_preferred_status_names'


class UserSettings:
    USER_NAME = 'labels/user_name'
    USER_LASTNAME = 'labels/user_lastname'
    USER_ROLES = 'labels/user_roles'
    USER_PREFERRED_PAGE = 'labels/user_preferred_homepage'

class SettingsLoader:
    def __init__(self):
        self.settings = QgsSettings()
 
    def save_setting(setting_name, value):
        #print(f"setting name: {setting_name}")
        #print(f"setting value: {value}")
        
        if setting_name:
            settings = QgsSettings()
            #print("next step")
            setting_address = MAIN_PATH + setting_name
            #print(f"Setting addrss: {setting_address} + {value}")
            settings.setValue(setting_address, value)
        else:    
            print("no next step")

    def get_setting(setting_name):
        # Check if the setting exists
        print(f"setting name: {setting_name}")
        if setting_name:
            setting_address = MAIN_PATH + setting_name
            print(f"Setting addrss: {setting_address}")
            settings = QgsSettings()
            value = settings.value(setting_address, '', type=str)
            return value
        
        else:    
            print("no next step")
