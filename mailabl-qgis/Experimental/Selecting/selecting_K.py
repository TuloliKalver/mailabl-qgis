import processing
from qgis.core import QgsProcessingFeatureSourceDefinition

#input_layer = 'Kanalitorud'
#reference_layer = 'Tartu_S'

def select_elements_from_layer(layers, reference_layer):
# Set input and reference layer names

    for layer in layers:
        # Set distance in meters
        distance = 5

        # Run select within distance algorithm
        result = processing.run("native:selectwithindistance", {
            'INPUT': layer,
            'REFERENCE': QgsProcessingFeatureSourceDefinition(reference_layer),
            'DISTANCE': distance,
            'METHOD': 0, # Use planar distance
        })

        # Get selected features
        selected_features = result['OUTPUT']

        # Print number of selected features
        print(f"{len(selected_features)} features selected within {distance}m of {reference_layer}")
