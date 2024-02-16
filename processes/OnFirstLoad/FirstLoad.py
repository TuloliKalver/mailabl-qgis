from .CloseUnload import Unload
from .AddSetupLayers import SetupLayers

setup_layers = SetupLayers()
unload_events = Unload ()

class Startup:
    

    def FirstLoad(self):
    
        #loda setup layers to project
        setup_layers.create_mailabl_setup_group_layer()

        

    def closePluginWindow():
        unload_events.closeEvent()