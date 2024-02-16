from .AddSetupLayers import create_mailabl_setup_group_layer
from .CloseUnload import closeEvent

def FirstLoad():
    #loda setup layers to project
    create_mailabl_setup_group_layer()

def closePluginWindow():
    closeEvent()