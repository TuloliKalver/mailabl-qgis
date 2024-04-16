# Import necessary QGIS modules
from qgis.core import QgsProject, QgsVectorLayer

# Specify the layer names
tulem_layer_name = 'Tulem'
muudetavad_kinnistud_layer_name = 'Muudetavad kinnistud'

# Get the layers by name from the project
tulem_layer = QgsProject.instance().mapLayersByName(tulem_layer_name)[0]
muudetavad_kinnistud_layer = QgsProject.instance().mapLayersByName(muudetavad_kinnistud_layer_name)[0]

# Create a dictionary to store the Tunnus-field value mapping
tunnus_mapping = {}

# Iterate over features in the "Muudetavad kinnistud" layer and store Tunnus-field values
for feature in muudetavad_kinnistud_layer.getFeatures():
    tunnus = feature['TUNNUS']
    tunnus_mapping[tunnus] = feature

# Start an editing session on the "Tulem" layer
tulem_layer.startEditing()

# Initialize a counter for updated features
updated_features_count = 0

# Iterate over features in the "Tulem" layer and update values using the mapping
for feature in tulem_layer.getFeatures():
    tunnus = feature['TUNNUS']
    if tunnus in tunnus_mapping:
        tunnus_feature = tunnus_mapping[tunnus]
        # Update each field value in the feature
        for field in tunnus_feature.fields():
            field_name = field.name()
            feature[field_name] = tunnus_feature[field_name]
        # Update the feature in the "Tulem" layer
        tulem_layer.updateFeature(feature)
        updated_features_count += 1

# Commit the changes and stop the editing session
tulem_layer.commitChanges()

# Print the number of updated features
print(f"Number of updated features: {updated_features_count}")
