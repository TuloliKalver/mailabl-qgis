import processing
from qgis.core import QgsVectorLayer, QgsProcessingFeatureSourceDefinition, QgsProject

# remove existing intersection layer if it exists
existing_layer = QgsProject.instance().mapLayersByName('Ajutine_K_I') + QgsProject.instance().mapLayersByName('Ajutine_KS_I')
if existing_layer:
    QgsProject.instance().removeMapLayer(existing_layer[0])

# get the Tartulõika overlay layer and select all features
overlay_layer = QgsProject.instance().mapLayersByName('Tartulõika')[0]
overlay_layer.selectAll()

# select all features in Ajutine_KS layer
ajutine_ks_layer = QgsProject.instance().mapLayersByName('Ajutine_KS')[0]
ajutine_ks_layer.selectAll()

# intersect Ajutine_KS layer with Tartulõika overlay layer
result_ks = processing.run("native:intersection", {
    'INPUT': QgsProcessingFeatureSourceDefinition(ajutine_ks_layer.source(), True),
    'OVERLAY': QgsProcessingFeatureSourceDefinition(overlay_layer.source(), True),
    'INPUT_FIELDS': ["mslink"],
    'OVERLAY_FIELDS': ["TUNNUS"],
    'OVERLAY_FIELDS_PREFIX': '',
    'OUTPUT': 'memory:',
    'OUTPUT_FIELDS': 'keep_all'
})

# intersect Ajutine_K layer with Tartulõika overlay layer
ajutine_k_layer = QgsProject.instance().mapLayersByName('Ajutine_K')[0]
ajutine_k_layer.selectAll()

result_k = processing.run("native:intersection", {
    'INPUT': QgsProcessingFeatureSourceDefinition(ajutine_k_layer.source(), True),
    'OVERLAY': QgsProcessingFeatureSourceDefinition(overlay_layer.source(), True),
    'INPUT_FIELDS': ["mslink"],
    'OVERLAY_FIELDS': ["TUNNUS"],
    'OVERLAY_FIELDS_PREFIX': '',
    'OUTPUT': 'memory:',
    'OUTPUT_FIELDS': 'keep_all'
})

# add intersected layers to the project
intersection_ks_layer = result_ks['OUTPUT']
intersection_ks_layer.setName('Ajutine_KS_I')
QgsProject.instance().addMapLayer(intersection_ks_layer)

intersection_k_layer = result_k['OUTPUT']
intersection_k_layer.setName('Ajutine_K_I')
QgsProject.instance().addMapLayer(intersection_k_layer)

QgsProject.instance().removeMapLayer(overlay_layer)
QgsProject.instance().removeMapLayer(ajutine_ks_layer)
QgsProject.instance().removeMapLayer(ajutine_k_layer)