import processing
from qgis.core import QgsProcessingFeatureSourceDefinition


# Set input and reference layer names
input_layer = 'Survekanalitorud'
reference_layer = 'Tartu_S'

# Set distance in meters
distance = 5

# Run select within distance algorithm
result = processing.run("native:selectwithindistance", {
    'INPUT': input_layer,
    'REFERENCE': QgsProcessingFeatureSourceDefinition(reference_layer),
    'DISTANCE': distance,
    'METHOD': 0, # Use planar distance
})

# Get selected features
selected_features = result['OUTPUT']

# Print number of selected features
print(f"{len(selected_features)} features selected within {distance}m of {reference_layer}")
