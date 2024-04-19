# Import necessary libraries
from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject
import processing
from ..config.QGISSettingPaths import LayerSettings, SettingsLoader
from .intersect import TempIntersectLayerName

class JoinLayers:
    join_layer_name = "Joined_layer"  # Define join layer name here

    @staticmethod
    def join_all_layers(intersect_layer_names, num_intersect_layers, join_layer_name):
        # Get all intersect layers

        if num_intersect_layers == 1:
            # Rename the single intersect layer
            if len(intersect_layer_names) == 1:  # Check if only one item is left in the list
                intersect_layer = QgsProject.instance().mapLayersByName(intersect_layer_names[0])
                if intersect_layer:
                    intersect_layer = intersect_layer[0]
                    intersect_layer.setName(join_layer_name)
                    return
            else:
                print("Expected one intersect layer, but found more or none.")
                return

        # Join and rename multiple intersect layers
        processed_layers = set()  # Define as a set
        join_num = 1
        while num_intersect_layers > 1:
            # Select two intersect layers to join
            if len(intersect_layer_names) >= 2:
                layer1_name = intersect_layer_names.pop(0)
                layer1 = QgsProject.instance().mapLayersByName(layer1_name)[0]
                layer1.selectAll()
                
                print("layer1_name")
                print(layer1_name)
                layer2_name = intersect_layer_names.pop(0)
                layer2 = QgsProject.instance().mapLayersByName(layer2_name)[0]
                layer2.selectAll()
                print("layer2_name")
                print(layer2_name)
            else:
                break  # Break out of the loop if there are not enough layers to pop

            # Run union algorithm on input layers    
            result = processing.run(
                        "native:union", 
                        {
                        'INPUT': QgsProcessingFeatureSourceDefinition(layer1.source(), True),
                        'OVERLAY': QgsProcessingFeatureSourceDefinition(layer2.source(), True),
                        'OUTPUT': 'memory:'
                        }
                        )


            # Create output layer and add it to the map
            output_layer = result['OUTPUT']
            output_layer_name = f"{join_layer_name}_{join_num}"
            output_layer.setName(output_layer_name)
            QgsProject.instance().addMapLayer(output_layer)

            processed_layers.add((layer1_name, layer2_name))  # Add processed layers to the set
            print("processed_layers")
            print(processed_layers)
            num_intersect_layers -= 1
            join_num += 1

        for layer_names in processed_layers:
            print("layer_names")
            print(layer_names)
            # Remove buffer and intersect layers from the project
            for layer_name in layer_names:
                layers = QgsProject.instance().mapLayersByName(layer_name)
                if layers:
                    layer = layers[0]  # Get the first layer if found
                    QgsProject.instance().removeMapLayer(layer)
                else:
                    print(f"Layer '{layer_name}' not found.")
                    return        # Refresh the map canvas
        iface.mapCanvas().refresh()
