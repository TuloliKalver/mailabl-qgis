import processing
from qgis.core import (
    QgsProcessingFeatureSource,
    QgsVectorLayer,
    QgsProject,
)

# Set input and reference layer names
input_layer = 'Kanalitorud'
reference_layer = 'Tartu_8796c4ac_c205_464e_bfd0_41fecfc47f00 Tartu'

# Get input and reference layers
input_layer_obj = QgsProject.instance().mapLayer(input_layer)
reference_layer_obj = QgsProject.instance().mapLayer(reference_layer)

# Check if any features are selected on the reference layer
if reference_layer_obj.selectedFeatureCount() > 0:
    # Get the selected features from the reference layer
    reference_selection = reference_layer_obj.selectedFeatures()

    # Set distance in meters
    distance = 5

    # Create QgsProcessingFeatureSource object from reference layer and its selected features
    reference_source = QgsProcessingFeatureSource(reference_layer_obj.source(), subset=reference_selection)

    # Run select within distance algorithm
    result = processing.run("native:selectbylocation", {
        'INPUT': input_layer_obj,
        'PREDICATE': [0, 3],  # Use intersect and within predicates
        'INTERSECT': reference_source,  # Use selected features from reference layer
        'METHOD': 0,  # Use planar distance
        'DISTANCE': distance,
    })

    # Get selected features
    selected_features = result['OUTPUT']

    # Get the current selection in the input layer
    current_selection = set(input_layer_obj.selectedFeatureIds())

    # Add the selected features to the current selection
    new_selection = current_selection.union(set(feat.id() for feat in selected_features))
    input_layer_obj.selectByIds(list(new_selection))

   
else:
    print("No features selected on reference layer. Skipping selection within distance step.")
