from .AddSetupLayers import Group_layer
from .CloseUnload import closeEvent

def FirstLoad():
    #loda setup layers to project
    Group_layer().create_mailabl_setup_group_layer()

def closePluginWindow():
    closeEvent()