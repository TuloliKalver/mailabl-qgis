import processing
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject

# remove existing temporary layers if they exist
existing_layers = QgsProject.instance().mapLayersByName('Tartu_S')
for layer in existing_layers:
    QgsProject.instance().removeMapLayer(layer)


#Kinistute eraldamine
layer3 = QgsProject.instance().mapLayersByName('Tartu')[0]
selected_features3 = layer3.selectedFeatures() # get selected features
result3 = processing.run("native:buffer", {
    'INPUT': QgsProcessingFeatureSourceDefinition(layer3.source(), True), # use the selected features as input
    'DISTANCE': 0,
    'SEGMENTS': 5,
    'END_CAP_STYLE': 0,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2,
    'DISSOLVE': False,
    'OUTPUT': 'memory:', # use 'memory:' to output to memory or a file path to output to a file
    'FEATURES': selected_features3 # pass the selected features as an argument
})

buffer_layer3 = result3['OUTPUT']
buffer_layer3.setName('Tartu_S')
QgsProject.instance().addMapLayer(buffer_layer3)