
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
    