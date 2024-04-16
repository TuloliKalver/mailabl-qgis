# Import required QGIS modules
from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsWkbTypes

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

# Get the field index of the 'TUNNUS' field in the "Old" layer
TUNNUS = old_layer.fields().indexFromName('TUNNUS')

# Get all unique values of 'TUNNUS' from the "New" layer
new_values = set()
for feature in new_layer.getFeatures():
    new_values.add(feature.attribute(TUNNUS))

# Create a new virtual layer named 'uued' with the same CRS as the "Old" layer
uued_layer = QgsVectorLayer(QgsWkbTypes.displayString(QgsWkbTypes.Polygon) + "?crs=" + old_layer.crs().authid(), "uued", "memory")

# Define the fields for the 'uued' layer
fields = old_layer.fields()
uued_layer.startEditing()
uued_layer.dataProvider().addAttributes(fields)
uued_layer.updateFields()

# Copy the features from the "New" layer to the 'uued' layer that are not present in the "Old" layer
for feature in new_layer.getFeatures():
    if feature.attribute(TUNNUS) not in new_values:
        uued_feature = QgsFeature(fields)
        uued_feature.setGeometry(feature.geometry())
        uued_feature.setAttributes(feature.attributes())
        uued_layer.addFeature(uued_feature)

# Commit the changes and update the extent of the 'uued' layer
uued_layer.commitChanges()
uued_layer.updateExtents()

# Add the 'uued' layer to the project
QgsProject.instance().addMapLayer(uued_layer)


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

# Copy the features from the "Old" layer to the 'muudetud_kinnistud' layer that have matching "MUUDET" values in the "New" layer
for old_feature in old_layer.getFeatures():
    old_muu_det_value = old_feature.attribute('MUUDET')
    for new_feature in new_layer.getFeatures():
        if new_feature.attribute('TUNNUS') == old_feature.attribute('TUNNUS') and new_feature.attribute('MUUDET') == old_muu_det_value:
            muudetud_feature = QgsFeature(muudetud_fields)
            muudetud_feature.setGeometry(old_feature.geometry())
            muudetud_feature.setAttributes(old_feature.attributes())
            muudetud_layer.addFeature(muudetud_feature)

# Commit the changes and update the extent of the 'muudetud_kinnistud' layer
muudetud_layer.commitChanges()
muudetud_layer.updateExtents()

# Add the 'muudetud_kinnistud' layer to the project
QgsProject.instance().addMapLayer(muudetud_layer)
