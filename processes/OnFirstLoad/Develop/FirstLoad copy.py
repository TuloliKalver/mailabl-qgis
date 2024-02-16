from ...OnFirstLoad.Develop.CloseUnload_copy import Unload
from ...OnFirstLoad.Develop.AddSetupLayers_copy import SetupLayers

setup_layers = SetupLayers()
unload_events = Unload ()

class Startup:
    

    def FirstLoad():
    
        #loda setup layers to project
        setup_layers.create_mailabl_setup_group_layer()

    def closePluginWindow():
        unload_events.closeEvent()