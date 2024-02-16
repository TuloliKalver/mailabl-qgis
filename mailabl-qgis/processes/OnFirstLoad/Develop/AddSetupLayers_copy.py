from qgis.core import QgsProject, QgsLayerTreeGroup


# Define names for the main and child group layers
mailabl_main_group_name = 'Mailabl settings'  # Main group name
import_layer_name = 'Imporditavad kinnistud'  # Name for importable properties
new_properties_name = 'Uued kinnistud'  # Name for new properties
changed_properties_name = 'Muutunud andmed'  # Name for changed properties



class SetupLayers:


    # Function to create the structured layer hierarchy
    def create_mailabl_setup_group_layer():
        # Get the root of the layer tree
        root = QgsProject.instance().layerTreeRoot()

        # Check if the main group layer already exists
        mailabl_group = root.findGroup(mailabl_main_group_name)

        if mailabl_group is None:
            # If it doesn't exist, create a new main group layer named "Mailabl settings"
            mailabl_group = QgsLayerTreeGroup(mailabl_main_group_name)
            root.insertChildNode(-1, mailabl_group)

        # Check if the child group layers already exist
        importable_properties = mailabl_group.findGroup(import_layer_name)
        changed_properties = mailabl_group.findGroup(changed_properties_name)
        new_properties = mailabl_group.findGroup(new_properties_name)

        # Create child group layers if they don't exist
        if importable_properties is None:
            # If the importable properties group doesn't exist, create it
            importable_properties = QgsLayerTreeGroup(import_layer_name)
            mailabl_group.addChildNode(importable_properties)

        if changed_properties is None:
            # If the changed properties group doesn't exist, create it
            changed_properties = QgsLayerTreeGroup(changed_properties_name)
            mailabl_group.addChildNode(changed_properties)

        if new_properties is None:
            # If the new properties group doesn't exist, create it
            new_properties = QgsLayerTreeGroup(new_properties_name)
            mailabl_group.addChildNode(new_properties)
