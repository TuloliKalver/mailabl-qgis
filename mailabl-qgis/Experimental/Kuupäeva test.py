# Import required QGIS modules
from qgis.core import QgsField, QgsVectorLayer, QgsProject
from PyQt5.QtCore import QDate

# Set the layer name of the "Test_põhi" layer
input_layer_name = "Test_põhi"
update_layer_name = "Test_uus"
new_layer_name = "Test_select_tool"

# Get the "Test_põhi" layer from the QGIS project
input_layers = QgsProject.instance().mapLayersByName(input_layer_name)
update_layers = QgsProject.instance().mapLayersByName(update_layer_name)

# Check if the layer is found
if not update_layers:
    raise ValueError(f"No layer found with the name '{update_layer_name}'. Please check the layer name.")
if not input_layers:
    raise ValueError(f"No layer found with the name '{input_layer_name}'. Please check the layer name.")

# Access the specific layer from the list
input_layer = input_layers[0]
update_layer = update_layers[0]

# Find the latest date from the "MUUDET" field
latest_date = None

for feature in input_layer.getFeatures():
    muudet_date = feature.attribute("MUUDET")
    if muudet_date:
        muudet_date = QDate.fromString(muudet_date, "dd/MM/yyyy")
        if not latest_date or muudet_date > latest_date:
            latest_date = muudet_date

# Print the latest date in the desired format
latest_date_str = latest_date.toString("dd/MM/yyyy")
print("Viimane kuupäev:", latest_date_str)

# Step 2: Select features with a date equal to or greater than the latest date
selection_expression = "\"MUUDET\" >= '{}'".format(latest_date.toString("yyyy-MM-dd"))
input_layer.selectByExpression(selection_expression, QgsVectorLayer.SetSelection)

# Step 3: Print the count of selected feature results
selected_features = input_layer.selectedFeatures()
print("Valitud objektide arv:", len(selected_features))
