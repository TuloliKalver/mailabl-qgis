from .CloseUnload import Unload
from .AddSetupLayers import SetupLayers
from ...config.settings import Devuser
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import SettingsDataSaveAndLoad
from ...KeelelisedMuutujad.messages import Headings, HoiatusTextsAuto, HoiatusTexts


setup_layers = SetupLayers()
unload_events = Unload ()

class Startup:
    

    def FirstLoad(self):
    
        #loda setup layers to project
        setup_layers.create_mailabl_setup_group_layer()

        username = Devuser.dev_username()
        access = Devuser.dev_access()

        if username:
            self.leUsername.setText(username)
        else:
            self.leUsername.setText('')
        if access:
            self.lePassword.setText(access)
        else:
            self.lePassword.setText('')

    def closePluginWindow():
        QMessageBox.information(None, Headings().tubli, HoiatusTexts().korrigeeri_sümbolit)        
        unload_events.closeEvent()