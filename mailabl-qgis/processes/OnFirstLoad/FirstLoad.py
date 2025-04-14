from PyQt5.QtWidgets import QLineEdit
from .CloseUnload import Unload
from .AddSetupLayers import SetupLayers
from ...config.settings import Devuser
from ...utils.messagesHelper import ModernMessageDialog
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ...app.ui_controllers import FrameHandler
from ...config.ui_directories import PathLoaderSimple
from ...config.settings import Version


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

        Startup.on_load(self)


    def closePluginWindow():

        heading = Headings().tubli
        text = HoiatusTexts().korrigeeri_sümbolit
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)  
        unload_events.closeEvent()


    def on_load(self):
        frames = [self.leftMenuContainer,
                    self.frAgreements,
                    self.swWorkSpace,
                    self.lblUserAccessDenied
                    ]
        FrameHandler.hide_multiple_frames(self, frames)

        initial_size = self.UC_Main_Frame.size()
        self.resize(initial_size.width()+5, initial_size.height()+5)

        # Hide typing password
        self.lePassword.setEchoMode(QLineEdit.Password)

        path = PathLoaderSimple.metadata()
        version_nr = Version.get_plugin_version(path)
        lblVersion = self.lblLoadVersion
        if version_nr == 'dev':
            lblVersion.setStyleSheet("color: #bc5152;")
        else:
            lblVersion.setStyleSheet("")  # Reset to default style

        lblVersion.setText(f"v.{version_nr}")
