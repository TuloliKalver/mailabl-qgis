import processing
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject

# remove existing temporary layers if they exist
class TempBufferLayerNames:
    sewer_temp_name = 'Ajutine_K'
    prSewer_temp_name = 'Ajutine_KS'


existing_layers =  QgsProject.instance().mapLayersByName('Tartulõika')
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
