# Import necessary libraries
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject
import processing

# Check if "ükskiht" layer exists and remove it if present
if QgsProject.instance().mapLayersByName('ükskiht'):
    QgsProject.instance().removeMapLayer(QgsProject.instance().mapLayersByName('ükskiht')[0])


# Set input layer variables
layer1 = QgsProject.instance().mapLayersByName('Ajutine_K_I')[0]
layer1.selectAll()
layer2 = QgsProject.instance().mapLayersByName('Ajutine_KS_I')[0]
layer2.selectAll()

# Check if layers were loaded successfully
if not layer1.isValid() or not layer2.isValid():
    print("Error: One or both layers failed to load.")
else:
    # Run union algorithm on input layers
    result = processing.run("native:union", {'INPUT': QgsProcessingFeatureSourceDefinition(layer1.source(), True),
                                             'OVERLAY': QgsProcessingFeatureSourceDefinition(layer2.source(), True),
                                             'OUTPUT': 'memory:'})

    # Create output layer and add it to the map
    output_layer = result['OUTPUT']
    output_layer.setName('ükskiht')
    QgsProject.instance().addMapLayer(output_layer)

QgsProject.instance().removeMapLayer(layer1)
QgsProject.instance().removeMapLayer(layer2)