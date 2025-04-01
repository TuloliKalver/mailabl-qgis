from .CloseUnload import Unload
from .AddSetupLayers import SetupLayers
from ...config.settings import Devuser
from ...utils.messagesHelper import ModernMessageDialog
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts


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

        heading = Headings().tubli
        text = HoiatusTexts().korrigeeri_sümbolit
        ModernMessageDialog.Info_messages_modern(heading,text)  
        unload_events.closeEvent()