import processing
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject

# remove existing temporary layers if they exist
existing_layers = QgsProject.instance().mapLayersByName('Ajutine_K') + QgsProject.instance().mapLayersByName('Ajutine_KS')+ QgsProject.instance().mapLayersByName('Tartulõika')
for layer in existing_layers:
    QgsProject.instance().removeMapLayer(layer)

# buffer Kanalitorud layer
layer1 = QgsProject.instance().mapLayersByName('Kanalitorud')[0]
selected_features1 = layer1.selectedFeatures() # get selected features
result1 = processing.run("native:buffer", {
    'INPUT': QgsProcessingFeatureSourceDefinition(layer1.source(), True), # use the selected features as input
    'DISTANCE': 5,
    'SEGMENTS': 5,
    'END_CAP_STYLE': 0,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2,
    'DISSOLVE': False,
    'OUTPUT': 'memory:', # use 'memory:' to output to memory or a file path to output to a file
    'FEATURES': selected_features1 # pass the selected features as an argument
})

buffer_layer1 = result1['OUTPUT']
buffer_layer1.setName('Ajutine_K')
QgsProject.instance().addMapLayer(buffer_layer1)


# buffer Survekanalitorud layer
layer2 = QgsProject.instance().mapLayersByName('Survekanalitorud')[0]
selected_features2 = layer2.selectedFeatures() # get selected features
result2 = processing.run("native:buffer", {
    'INPUT': QgsProcessingFeatureSourceDefinition(layer2.source(), True), # use the selected features as input
    'DISTANCE': 5,
    'SEGMENTS': 5,
    'END_CAP_STYLE': 0,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2,
    'DISSOLVE': False,
    'OUTPUT': 'memory:', # use 'memory:' to output to memory or a file path to output to a file
    'FEATURES': selected_features2 # pass the selected features as an argument
})

buffer_layer2 = result2['OUTPUT']
buffer_layer2.setName('Ajutine_KS')
QgsProject.instance().addMapLayer(buffer_layer2)


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
buffer_layer3.setName('Tartulõika')
QgsProject.instance().addMapLayer(buffer_layer3)