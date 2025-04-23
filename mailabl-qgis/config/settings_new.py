from qgis.core import QgsSettings
from ..KeelelisedMuutujad.modules import Module


class PluginSettings:
    BASE_PATH = '/Mailabl/Setting/'

    OPTION_STATUS = "status"
    OPTION_TYPE = "type"
    OPTION_LAYER = "layer"

    CONTEXT_PREFERRED = "preferred"
    CONTEXT_FOLDER = "folder"

    SUB_CONTEXT_NAME = "names"
    SUB_CONTEXT_IDs = "ids"
    SUB_CONTEXT_PATH = "path"

    WATER = "water"
    SEWER = "sewer"
    PRESSURE_SEWER = "pressureSewer"
    DRAINAGE = "drainage"

    #Sample name logicks 
    #/Mailabl/Setting/labels/specification/preferred/status/names
    #/Mailabl/Setting/labels/specification/preferred/status/ids
    #/Mailabl/Setting/labels/specification/preferred/type/names
    #/Mailabl/Setting/labels/specification/preferred/type/ids

    @staticmethod
    def save_setting(module: str, context: str,  value: str,  subcontext: str=None, key_type: str=None,):
        key = SettingsBuilder.build_key(module, context, subcontext, key_type)
        QgsSettings().setValue(key, value)

    @staticmethod
    def load_setting(module: str, context: str, subcontext: str = None, key_type: str =None, text_fomated=False) -> str:
        key = SettingsBuilder.build_key(module, context, subcontext, key_type)
        settings_list = QgsSettings().value(key, '', type=str)
        #print(f"load settings settings list: {settings_list}")
        if text_fomated == True:
            string = ""
            if settings_list == "Määramata":
                return settings_list
            for item in settings_list:
                string += f"{item}, "
            settings_list = string.rstrip(", ")
        return settings_list 
    
    @staticmethod
    def clear_setting(module):
        for option_type in [PluginSettings.OPTION_TYPE_STATUS, PluginSettings.OPTION_TYPE]:
            key = PluginSettings.settings_address(module, option_type)
            QgsSettings().remove(key)


    @staticmethod
    def print_all_mailabl_settings():
        """
        Debug utility: prints all QgsSettings keys and values under 'Mailabl/Setting/'.
        Useful for checking what has been stored for the plugin.
        """
        settings = QgsSettings()
        base_prefix = "Mailabl/Setting/"

        print("🔍 All Mailabl plugin settings:")
        for key in settings.allKeys():
            #print(f"Looking for base_perfix: {base_prefix}")
            #print(f"Key looking into!: {key}")
            if key.startswith(base_prefix):
                value = settings.value(key)
                print(f"  {key} = {value}")



class SettingsBuilder:
    BASE_PATH = f"{PluginSettings.BASE_PATH}labels"
    INIT_FLAG_KEY = f"{PluginSettings.BASE_PATH}initialized"

    modules = Module.all_modules
    contexts = [PluginSettings.CONTEXT_PREFERRED, PluginSettings.CONTEXT_FOLDER]

    # For nested contexts like "preferred" → we want both status and type (names/ids)
    subcontexts = {
        PluginSettings.CONTEXT_PREFERRED: [PluginSettings.OPTION_STATUS, 
                                           PluginSettings.OPTION_TYPE,
                                           PluginSettings.OPTION_LAYER]
    }

    keys = {
        PluginSettings.OPTION_STATUS: [PluginSettings.SUB_CONTEXT_NAME, PluginSettings.SUB_CONTEXT_IDs],
        PluginSettings.OPTION_TYPE: [PluginSettings.SUB_CONTEXT_NAME, PluginSettings.SUB_CONTEXT_IDs],
        PluginSettings.OPTION_LAYER: [PluginSettings.WATER, PluginSettings.SEWER, PluginSettings.PRESSURE_SEWER, PluginSettings.DRAINAGE],
        PluginSettings.CONTEXT_FOLDER: [PluginSettings.SUB_CONTEXT_PATH]
    }

    @staticmethod
    def build_key(module=None, context=None, subcontext=None, key_type=None):
        """
        Build structured setting key for Mailabl plugin.
        Format: /Mailabl/Setting/labels/<module>/<context>/<subcontext>/<key>
        """
        base = SettingsBuilder.BASE_PATH
        parts = [module, context, subcontext, key_type]
        return f"{base}/{'/'.join(p for p in parts if p)}"

    @staticmethod
    def initialize_settings():
        """
        Initialize default settings only once. Skipped if already done.
        """
        settings = QgsSettings()
        if settings.value(SettingsBuilder.INIT_FLAG_KEY, False, type=bool):
            print("⚠️ Settings already initialized.")
            return

        print("🛠️ Initializing structured Mailabl settings...")

        for module in SettingsBuilder.modules:
            for context in SettingsBuilder.contexts:
                if context in SettingsBuilder.subcontexts:
                    for subcontext in SettingsBuilder.subcontexts[context]:
                        for key_type in SettingsBuilder.keys[subcontext]:
                            key = SettingsBuilder.build_key(module, context, subcontext, key_type)
                            settings.setValue(key, "Määramata")
                            print(f"🟢 Created: {key}")
                else:
                    for key_type in SettingsBuilder.keys.get(context, []):
                        key = SettingsBuilder.build_key(module, context, None, key_type)
                        settings.setValue(key, "Määramata")
                        print(f"🟢 Created: {key}")

        settings.setValue(SettingsBuilder.INIT_FLAG_KEY, True)
        print("✅ Initialization complete. Flag set.")

    @staticmethod
    def reset_initialization_flag():
        settings = QgsSettings()

        # Delete the init flag
        settings.remove(SettingsBuilder.INIT_FLAG_KEY)
        print("🔁 Initialization flag cleared.")

        # Optionally: clear all structured setting keys we created
        print("🧹 Removing all structured plugin keys...")
        for module in SettingsBuilder.modules:
            for context in SettingsBuilder.contexts:
                if context in SettingsBuilder.subcontexts:
                    for subcontext in SettingsBuilder.subcontexts[context]:
                        for key_type in SettingsBuilder.keys[subcontext]:
                            key = SettingsBuilder.build_key(module, context, subcontext, key_type)
                            settings.remove(key)
                            print(f"❌ Removed: {key}")
                else:
                    for key_type in SettingsBuilder.keys.get(context, []):
                        key = SettingsBuilder.build_key(module, context, None, key_type)
                        settings.remove(key)
                        print(f"❌ Removed: {key}")

        print("✅ All Mailabl structured settings have been reset.")