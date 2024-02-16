from qgis.core import QgsProject, QgsLayerTreeGroup

class SetupLayers:
    def __init__(self):
                    #Remove code from Kataster_Dialog.py rows 217 and 732 and froward until Def end

    # Define names for the main and child group layers
        self.mailabl_main_group_name = 'Mailabl settings'  # Main group name
        self.import_layer_name = 'Imporditavad kinnistud'  # Name for importable properties
        self.new_properties_name = 'Uued kinnistud'  # Name for new properties
        self.changed_properties_name = 'Muutunud andmed'  # Name for changed properties
        self.archived_properties = 'Arhiveeritud kinnistud' #Holds upto 3 achived files. 
        

    # Function to create the structured layer hierarchy
    def create_mailabl_setup_group_layer(self):
        # Get the root of the layer tree
        root = QgsProject.instance().layerTreeRoot()
        # Check if the main group layer already exists
        mailabl_group = root.findGroup(self.mailabl_main_group_name)

        if mailabl_group is None:
            # If it doesn't exist, create a new main group layer named "Mailabl settings"
            mailabl_group = QgsLayerTreeGroup(self.mailabl_main_group_name)
            root.insertChildNode(-1, mailabl_group)

        # Check if the child group layers already exist
        importable_properties = mailabl_group.findGroup(self.import_layer_name)
        changed_properties = mailabl_group.findGroup(self.changed_properties_name)
        new_properties = mailabl_group.findGroup(self.new_properties_name)
        archived_properties = mailabl_group.findGroup(self.archived_properties)
        
        # Create child group layers if they don't exist
        if importable_properties is None:
            #If the name in properties group doesn't exist, create it
            importable_properties = QgsLayerTreeGroup(self.import_layer_name)
            mailabl_group.addChildNode(importable_properties)

        if changed_properties is None:
            #If the name in properties group doesn't exist, create itt
            changed_properties = QgsLayerTreeGroup(self.changed_properties_name)
            mailabl_group.addChildNode(changed_properties)

        if new_properties is None:
            #If the name in properties group doesn't exist, create it
            new_properties = QgsLayerTreeGroup(self.new_properties_name)
            mailabl_group.addChildNode(new_properties)

        if archived_properties is None:
            #If the name in properties group doesn't exist, create it
            archived_properties = QgsLayerTreeGroup(self.archived_properties)
            mailabl_group.addChildNode(archived_properties)
