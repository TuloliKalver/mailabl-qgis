from .CloseUnload import Unload
from .AddSetupLayers import SetupLayers
from ...config.settings import Devuser
from ...utils.messagesHelper import ModernMessageDialog
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts


setup_layers = SetupLayers()
unload_events = Unload ()

class Startup:
    def __init__(self):
        self.dialog=self
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


    def on_load(self):
        frames = [self.leftMenuContainer,
                    self.rightMenuContainer, 
                    self.frAgreements,
                    self.swWorkSpace,
                    self.lblUserAccessDenied
                    ]

        from ...app.ui_controllers import FrameHandler
        from ...config.ui_directories import PathLoaderSimple
        from ...config.settings import Version
        FrameHandler.hide_multiple_frames(self, frames )
        path = PathLoaderSimple.metadata()
        version_nr = Version.get_plugin_version(path)
        lblVersion = self.lblLoadVersion
        if version_nr == 'dev':
            lblVersion.setStyleSheet("color: #bc5152;")
        else:
            lblVersion.setStyleSheet("")  # Reset to default style

        lblVersion.setText(f"v.{version_nr}")
