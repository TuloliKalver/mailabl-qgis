# Import required QGIS modules
from qgis.core import  QgsVectorLayer, QgsProject
from PyQt5.QtCore import QDate


# Set the layer name of the "Test_uus" layer
input_layer_name = "Test_põhi"
update_layer_name = "SHP_KATASTRIYKSUS_283"
new_layer_name = "Muudetavad kinnistud"

# Get the "Test_uus" layer from the QGIS project
update_layer = QgsProject.instance().mapLayersByName(update_layer_name)
# Get the "Test_põhi" layer from the QGIS project
input_layer = QgsProject.instance().mapLayersByName(input_layer_name)

# Check if the layer is found
if not update_layer:
    raise ValueError(f"No layer found with the name '{update_layer_name}'. Please check the layer name.")
if not input_layer:
    raise ValueError(f"No layer found with the name '{input_layer_name}'. Please check the layer name.")

# Find the latest date from the "MUUDET" field
latest_date = None

for feature in input_layer[0].getFeatures():
    muudet_date = feature.attribute("MUUDET")
    if muudet_date:
        muudet_date = QDate.fromString(muudet_date.toString("yyyy-MM-dd"), "yyyy-MM-dd")
        if not latest_date or muudet_date > latest_date:
            latest_date = muudet_date

# Print the latest date in the desired format
latest_date_str = latest_date.toString("yyyy-MM-dd")
print("Viimane kuupäev:", latest_date_str)

# Copy the features from the update layer with the latest date to a list
filtered_features = []
loetud_count = 0  # Initialize the count for filtered features

for feature in update_layer[0].getFeatures():
    muudet_date = feature.attribute("MUUDET")
    if muudet_date and muudet_date.toString("yyyy-MM-dd") >= latest_date_str:
        filtered_features.append(feature)
        loetud_count += 1  # Increment the count for filtered features

# Create a new layer with the same CRS as the input layer
new_layer = QgsVectorLayer("Polygon?crs=" + update_layer[0].crs().authid(), new_layer_name, "memory")

# Add the fields from the original layer to the new layer
new_layer_data_provider = new_layer.dataProvider()
fields = update_layer[0].fields()
new_layer_data_provider.addAttributes(fields)
new_layer.updateFields()

# Add the filtered features to the new layer
new_layer.startEditing()

for feature in filtered_features:
    new_layer.addFeature(feature)

new_layer.commitChanges()
new_layer.updateExtents()

# Add the new layer to the project
QgsProject.instance().addMapLayer(new_layer)

# Print the filtered features count
print("Loetud arv:", loetud_count)

# Select the features in the new layer
ids = [feature.id() for feature in new_layer.getFeatures()]
new_layer.selectByIds(ids)
