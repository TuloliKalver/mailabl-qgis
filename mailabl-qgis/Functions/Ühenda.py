# Import necessary libraries
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject
import processing

# remove existing temporary layers if they exist
existing_layers = QgsProject.instance().mapLayersByName('evv_servituudid')
for layer in existing_layers:
    QgsProject.instance().removeMapLayer(layer)

# Set input layer variables
layer1 = QgsProject.instance().mapLayersByName('ükskiht')[0]
layer1.selectAll()

# Check if layers were loaded successfully
if not layer1.isValid():
    print("Error: One or both layers failed to load.")
else:
    # Run dissolve algorithm on input layers
    result = processing.run("native:dissolve", {
        'INPUT': layer1,
        'FIELD': [], # Use an empty list to dissolve all features
        'OUTPUT': 'memory:'
    })['OUTPUT']
    result.setName("evv_servituudid")
    QgsProject.instance().addMapLayer(result)

# Remove the original layer from the project
QgsProject.instance().removeMapLayer(layer1)
