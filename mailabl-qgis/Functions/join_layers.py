# Import necessary libraries
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject
import processing
from ..config.QGISSettingPaths import LayerSettings, SettingsLoader
from .intersect import TempIntersectLayerName

join_layer_name = "Ajutine ühendatud kiht"

class JoinLayers:
    @staticmethod
    def join_all_layers():
        # Get the list of working layers
        working_layers = TempIntersectLayerName.intersect_layers

        # Check if "ükskiht" layer exists and remove it if present
        existing_layer = QgsProject.instance().mapLayersByName(join_layer_name)
        if existing_layer:
            QgsProject.instance().removeMapLayer(existing_layer[0])

        # Iterate over all pairs of layers
        for i in range(len(working_layers)):
            for j in range(i + 1, len(working_layers)):
                layer_name_1 = working_layers[i]
                layer_name_2 = working_layers[j]
                # Set input layer variables
                layer1_candidates = QgsProject.instance().mapLayersByName(working_layers[i])
                layer2_candidates = QgsProject.instance().mapLayersByName(working_layers[j])

                if not layer1_candidates:
                    print(f"Error: Layer '{working_layers[i]}' not found.")
                    continue
                if not layer2_candidates:
                    print(f"Error: Layer '{working_layers[j]}' not found.")
                    continue

                layer1 = layer1_candidates[0]
                layer2 = layer2_candidates[0]

                # Check if layers were loaded successfully
                if not layer1.isValid():
                    print(f"Error: Layer '{working_layers[i]}' is not valid.")
                    return
                if not layer2.isValid():
                    print(f"Error: Layer '{working_layers[j]}' is not valid.")
                    return

                layer1.selectAll()
                layer2.selectAll()

                # Run union algorithm on input layers
                result = processing.run("native:union", {
                    'INPUT': QgsProcessingFeatureSourceDefinition(layer1.source(), True),
                    'OVERLAY': QgsProcessingFeatureSourceDefinition(layer2.source(), True),
                    'OUTPUT': 'memory:'
                })

                # Create output layer and add it to the map
                output_layer = result['OUTPUT']
                output_layer.setName(join_layer_name)
                QgsProject.instance().addMapLayer(output_layer)
