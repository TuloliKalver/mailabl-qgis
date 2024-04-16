# Import required QGIS modules
from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsWkbTypes

# Set the layer names of the "Test_põhi" and "Test_uus" layers
test_pohi_layer_name = "Test_põhi"
test_uus_layer_name = "Test_uus"

# Get the "Test_põhi" and "Test_uus" layers from the QGIS project
test_pohi_layers = QgsProject.instance().mapLayersByName(test_pohi_layer_name)
test_uus_layers = QgsProject.instance().mapLayersByName(test_uus_layer_name)

# Check if the layers are found
if not test_pohi_layers:
    raise ValueError(f"No layer found with the name '{test_pohi_layer_name}'. Please check the layer name.")

if not test_uus_layers:
    raise ValueError(f"No layer found with the name '{test_uus_layer_name}'. Please check the layer name.")

# Select the first layer from the lists
test_pohi_layer = test_pohi_layers[0]
test_uus_layer = test_uus_layers[0]

# Get the index of the "TUNNUS" field in the "Test_põhi" layer
tunnus_field_index = test_pohi_layer.fields().indexFromName('TUNNUS')

# Check if the "TUNNUS" field exists in the "Test_põhi" layer
if tunnus_field_index == -1:
    raise ValueError("Field 'TUNNUS' not found in the 'Test_põhi' layer.")

# Get the index of the "MUUDET" field in the "Test_põhi" and "Test_uus" layers
muudet_pohi_field_index = test_pohi_layer.fields().indexFromName('MUUDET')
muudet_uus_field_index = test_uus_layer.fields().indexFromName('MUUDET')

# Check if the "MUUDET" field exists in the "Test_põhi" and "Test_uus" layers
if muudet_pohi_field_index == -1:
    raise ValueError("Field 'MUUDET' not found in the 'Test_põhi' layer.")

if muudet_uus_field_index == -1:
    raise ValueError("Field 'MUUDET' not found in the 'Test_uus' layer.")

# Create a new virtual layer named 'Uuendatud andmed' with the same CRS as the "Test_põhi" layer
uuendatud_andmed_layer = QgsVectorLayer(QgsWkbTypes.displayString(QgsWkbTypes.Polygon) + "?crs=" + test_pohi_layer.crs().authid(), "Uuendatud andmed", "memory")

# Define the fields for the 'Uuendatud andmed' layer
uuendatud_andmed_fields = test_pohi_layer.fields()
uuendatud_andmed_layer.startEditing()
uuendatud_andmed_layer.dataProvider().addAttributes(uuendatud_andmed_fields)
uuendatud_andmed_layer.updateFields()

# Copy the features from the "Test_põhi" and "Test_uus" layers to the 'Uuendat
