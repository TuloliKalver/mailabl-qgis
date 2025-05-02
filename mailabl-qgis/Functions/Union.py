# Import necessary libraries
from qgis.core import QgsProject
import processing
from ..config.settings import Filepaths, FilesByNames
from ..processes.OnFirstLoad.AddSetupLayers import SetupLayers, MailablGroupFolders

class  Union:
# remove existing temporary layers if they exist
    UnionLayer = 'Kitsenduse_skeem'
        
    def make_unioned_layer(input_layers):

        # Set input layer variables
        for layer_name in input_layers:
            input_layer = QgsProject.instance().mapLayersByName(layer_name)
            if input_layer: 
                input_layer = input_layer[0]
                input_layer.selectAll()
                
                # Run dissolve algorithm on input layers
                result = processing.run("native:dissolve", {
                    'INPUT': input_layer,
                    'FIELD': [], # Use an empty list to dissolve all features
                    'OUTPUT': 'memory:'
                })


        existing_layers = QgsProject.instance().mapLayersByName(Union.UnionLayer)
        print("UnionLayer:", Union.UnionLayer)
        print("existing_layers:", existing_layers)
        #print("type(existing_layers[0]):", type(existing_layers[0]))

        if existing_layers:
            # Remove the existing layer before continuing
            QgsProject.instance().removeMapLayer(existing_layers[0])
        else:
            print("Error: One or both layers failed to load.")
            # Add the buffer layer to the group layer
            group_layer_name = MailablGroupFolders().SANDBOXING

            # Get the group layer or create it if it doesn't exist
            root = QgsProject.instance().layerTreeRoot()
            group = root.findGroup(group_layer_name)


            buffer_layer = QgsProject.instance().addMapLayer(result['OUTPUT'], False)
            buffer_layer.setName(Union.UnionLayer)
            group.addLayer(buffer_layer)
            style_name = FilesByNames().Easement_unioned

            QGIS_Layer_style = Filepaths().get_style(style_name)
            
            # Apply the layer style
            buffer_layer.loadNamedStyle(QGIS_Layer_style)

            buffer_layer.triggerRepaint()




        for layer_name in input_layers:
            input_layer = QgsProject.instance().mapLayersByName(layer_name)
            if input_layer:
                QgsProject.instance().removeMapLayer(input_layer[0])
