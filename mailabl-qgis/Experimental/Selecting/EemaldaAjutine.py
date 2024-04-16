# Import necessary modules
from qgis.core import QgsProject

# Get the current project
project = QgsProject.instance()

# Get a list of all layers in the project
layers = project.mapLayers()

# Iterate through the layers
for layer_id, layer in layers.items():
    # Check if the layer name matches "Tartu_S"
    if layer.name() == "Tartu_S":
        # Remove the layer from the project
        project.removeMapLayer(layer_id)
