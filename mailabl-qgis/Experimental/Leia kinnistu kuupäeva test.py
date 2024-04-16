# Import required QGIS modules
from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsWkbTypes

# Set the layer name of the "Test_põhi" layer
test_pohi_layer_name = "Test_põhi"

# Get the "Test_põhi" layer from the QGIS project
test_pohi_layers = QgsProject.instance().mapLayersByName(test_pohi_layer_name)

# Check if the layer is found
if not test_pohi_layers:
    raise ValueError(f"No layer found with the name '{test_pohi_layer_name}'. Please check the layer name.")

# Select the first layer from the list
test_pohi_layer = test_pohi_layers[0]

# Get the index of the "MUUDET" field
muudet_field_index = test_pohi_layer.fields().indexFromName("MUUDET")

# Check if the "MUUDET" field exists
if muudet_field_index == -1:
    raise ValueError("Field 'MUUDET' not found in the 'Test_põhi' layer.")

# Create a new virtual layer named 'Test_uu5' with the same CRS as the "Test_põhi" layer
test_uu5_layer = QgsVectorLayer(QgsWkbTypes.displayString(QgsWkbTypes.Polygon) + "?crs=" + test_pohi_layer.crs().authid(), "Test_uu5", "memory")

# Define the fields for the 'Test_uu5' layer
test_uu5_fields = test_pohi_layer.fields()
test_uu5_layer.startEditing()
test_uu5_layer.dataProvider().addAttributes(test_uu5_fields)
test_uu5_layer.updateFields()

# Copy the features from the "Test_põhi" layer to the 'Test_uu5' layer that have "MUUDET" date as "27/09/2021"
for feature in test_pohi_layer.getFeatures():
    muudet_date = feature.attribute(muudet_field_index)
    if muudet_date.toString('dd/MM/yyyy') == '21/09/2021':
        test_uu5_feature = QgsFeature(test_uu5_fields)
        test_uu5_feature.setGeometry(feature.geometry())
        test_uu5_feature.setAttributes(feature.attributes())
        test_uu5_layer.addFeature(test_uu5_feature)

# Commit the changes and update the extent of the 'Test_uu5' layer
test_uu5_layer.commitChanges()
test_uu5_layer.updateExtents()

# Add the 'Test_uu5' layer to the project
QgsProject.instance().addMapLayer(test_uu5_layer)