from qgis.core import QgsProject, QgsLayerTreeGroup
from ...KeelelisedMuutujad.FolderHelper import MailablGroupLayers


class SetupLayers:
    def __init__(self):
        self.main_group = MailablGroupLayers.MAILABL_MAIN #'Mailabl settings'  # Main group name
        
    # Function to create the structured layer hierarchy
    def create_mailabl_setup_group_layer(self):
        # Get the root of the layer tree
        root = QgsProject.instance().layerTreeRoot()

        # Check if the main group layer already exists
        mailabl_group = root.findGroup(self.main_group)

        if mailabl_group is None:
            # If it doesn't exist, create a new main group layer named "Mailabl settings"
            mailabl_group = QgsLayerTreeGroup(self.main_group)
            root.insertChildNode(-1, mailabl_group)


        groups = MailablGroupLayers.GropupLayers
        for group in groups:

            group_layer = mailabl_group.findGroup(group)
                    # Create child group layers if they don't exist
            if group_layer is None:
                # If the importable properties group doesn't exist, create it
                group_layer = QgsLayerTreeGroup(group)
                mailabl_group.addChildNode(group_layer)