# Import required QGIS modules
from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsWkbTypes
from datetime import datetime

# Set the layer names of the "Old" and "New" layers
old_layer_name = "Test_põhi"
new_layer_name = "Test_uus"

# Get the "Old" and "New" layers from the QGIS project
old_layers = QgsProject.instance().mapLayersByName(old_layer_name)
new_layers = QgsProject.instance().mapLayersByName(new_layer_name)

# Check if the layers are found
if not old_layers:
    raise ValueError(f"No layer found with the name '{old_layer_name}'. Please check the layer name.")

if not new_layers:
    raise ValueError(f"No layer found with the name '{new_layer_name}'. Please check the layer name.")

# Select the first layer from the lists
old_layer = old_layers[0]
new_layer = new_layers[0]

# Second stage: Check the "MUUDET" field and add matching results to a new virtual layer

# Set the layer name of the "Muudetud andmetega kinnistud" layer
muudetud_layer_name = "Muudetud andmetega kinnistud"

# Remove the existing "Muudetud andmetega kinnistud" layer if it already exists
existing_muudetud_layers = QgsProject.instance().mapLayersByName(muudetud_layer_name)
for existing_muudetud_layer in existing_muudetud_layers:
    QgsProject.instance().removeMapLayer(existing_muudetud_layer)

# Create a new virtual layer named 'muudetud_kinnistud' with the same CRS as the "Old" layer
muudetud_layer = QgsVectorLayer(QgsWkbTypes.displayString(QgsWkbTypes.Polygon) + "?crs=" + old_layer.crs().authid(), muudetud_layer_name, "memory")

# Define the fields for the 'muudetud_kinnistud' layer
muudetud_fields = old_layer.fields()
muudetud_layer.startEditing()
muudetud_layer.dataProvider().addAttributes(muudetud_fields)
muudetud_layer.updateFields()

# Check if the "MUUDET" field exists in the "Old" and "New" layers
old_muu_det_field = old_layer.fields().indexFromName('MUUDET')
new_muu_det_field = new_layer.fields().indexFromName('MUUDET')

if old_muu_det_field == -1:
    raise ValueError("Field 'MUUDET' not found in the 'Old' layer.")
if new_muu_det_field == -1:
    raise ValueError("Field 'MUUDET' not found in the 'New' layer.")

# Copy the features from the "Old" layer to the 'muudetud_kinnistud' layer that have matching "MUUDET" values in the "New" layer
for new_feature in new_layer.getFeatures():
    new_muu_det_value = datetime.strptime(new_feature.attribute('MUUDET').toString('dd/MM/yyyy'), '%d/%m/%Y')
    for old_feature in old_layer.getFeatures():
        old_muu_det_value = datetime.strptime(old_feature.attribute('MUUDET').toString('dd/MM/yyyy'), '%d/%m/%Y')
        if new_feature.attribute('TUNNUS') == old_feature.attribute('TUNNUS') and new_muu_det_value > old_muu_det_value:
            muudetud_feature = QgsFeature(muudetud_fields)
            muudetud_feature.setGeometry(new_feature.geometry())
            muudetud_feature.setAttributes(new_feature.attributes())
            muudetud_layer.addFeature(muudetud_feature)

# Commit the changes and update the extent of the 'muudetud_kinnistud' layer
muudetud_layer.commitChanges()
muudetud_layer.updateExtents()

# Add the 'muudetud_kinnistud' layer to the project
QgsProject.instance().addMapLayer(muudetud_layer)

# Print the number of features in the 'muudetud_kinnistud' layer
print(f"Number of features in 'muudetud_kinnistud' layer: {muudetud_layer.featureCount()}")
