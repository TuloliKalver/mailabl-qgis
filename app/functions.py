from qgis.core import (QgsFeature,
                       QgsMapLayer, QgsProject)
from PyQt5.QtCore import QVariant
from qgis.core import QgsField
from qgis.core import QgsProject, QgsFeature, edit
from .View_tools import shp_tools
from qgis.core import QgsField

class QGIS_items:
    def __init__(self):
        self.excluded_group = 'Imporditavad kinnistud'  
    
    def clear_and_populate_combo_box(self, combo_box):
        combo_box.clear()
        layer_names = self.get_sorted_layer_names()
        combo_box.addItems(layer_names)

    def get_sorted_layer_names(self):
        layers = []
        for layer_id, layer in QgsProject.instance().mapLayers().items():
            if isinstance(layer, QgsMapLayer) and layer.type() == QgsMapLayer.VectorLayer:
                layer_node = QgsProject.instance().layerTreeRoot().findLayer(layer_id)
                if layer_node is not None and layer_node.parent() is not None and layer_node.parent().name() != self.excluded_group:
                    layers.append(layer)

        # Get the names of the layers
        layer_names = [layer.name() for layer in layers]

        # Sort layer names alphabetically
        sorted_layer_names = sorted(layer_names)
        return sorted_layer_names
        



class FieldManager:
    def field_exists(self, field_name, input_layer):
        layer = QgsProject.instance().mapLayersByName(input_layer)[0]
        fields = layer.fields()
        existing_field_names = [field.name() for field in fields]
        return field_name in existing_field_names

    def new_field_int (self, new_field,input_layer):        
        if not self.field_exists(new_field, input_layer):
            field_type = QVariant.Int  # Field type (Integer in this case)

            layer = QgsProject.instance().mapLayersByName(input_layer)[0]
            provider = layer.dataProvider()

            # Add a new field to the data provider
            insert_new = QgsField(new_field, field_type)
            provider.addAttributes([insert_new])

            # Update fields to apply the changes
            layer.updateFields()
            print(f"New field '{new_field}' added.")
        else:
            print(f"Field '{new_field}' already exists. Skipping.")


#develope later for mutomations and constancy
class QGISDataTypes:

    field_type_int = QVariant.Int   # Whole numbers, e.g., 1, 42, -10
    float = 'Double'  # Floating-point numbers, e.g., 3.14, -0.001, 2.71828
    text = 'String'  # Text or string data, e.g., "Hello, World!", "QGIS", "12345"
    date = 'Date'  # Date without a time component, e.g., 2023-10-21
    time = 'Time'  # Time without a date component, e.g., 14:30:00
    datetime = 'DateTime'  # Date and time combined, e.g., 2023-10-21 14:30:00
    boolean = 'Boolean'  # True or False values
    bigInteger = 'BigInteger'  # Large whole numbers
    decimal = 'Decimal'  # Fixed-point decimal numbers
    smallint = 'SmallInt'  # Small whole numbers
    intArray = 'IntList'  # List of integers, e.g., [1, 2, 3, 4]
    doubleArray = 'DoubleList'  # List of floating-point numbers, e.g., [1.1, 2.2, 3.3]
    stringArray = 'StringList'  # List of strings, e.g., ["apple", "banana", "cherry"]


class QGIS_data_transfers:




    @staticmethod
    def save_memory_to_target_layer(input_layer_name, target_layer_name):
        # Get the target layer by name
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        target_layer = QgsProject.instance().mapLayersByName(target_layer_name)[0]

        if not target_layer:
            print(f"Target layer '{target_layer_name}' not found.")
            return

        # Get the selected features from the memory layer
        selected_features = input_layer.selectedFeatures()

        # Start editing the target layer
        target_layer.startEditing()

        # Loop through selected features and insert them into the target layer
        for feature in selected_features:
            # Create a new feature in the target layer
            new_feature = QgsFeature(target_layer.fields())

            # Set the attributes of the new feature
            new_feature.setAttributes(feature.attributes())

            # Set the geometry of the new feature
            new_feature.setGeometry(feature.geometry())

            # Add the new feature to the target layer
            target_layer.addFeature(new_feature)

        # Commit changes and stop editing
        target_layer.commitChanges()
        target_layer.updateExtents()
        graph_tools = shp_tools()
        graph_tools.activateLayer_zoomTo(target_layer)        
        


