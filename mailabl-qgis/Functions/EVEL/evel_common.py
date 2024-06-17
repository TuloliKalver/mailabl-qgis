import importlib
import sys
import os

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFields,
    QgsField,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer
)
from ..layer_generator import GroupActions
from ...KeelelisedMuutujad.EVEL_lang_module import EvelGroupLayersNames, EvelLayerNames, UICheckboxes, CheckBoxMappings
from ...config.settings import FilesByNames
from ...processes.OnFirstLoad.AddSetupLayers import SetupLayers



class EVEL_Creator:
    @staticmethod
    def create_layer_with_fields(layer_name, layer_crs, field_definitions):
        # Define the layer's attributes based on the provided field definitions
        fields = QgsFields()
        for field_name, field_type, field_length in field_definitions:
            if field_length:
                fields.append(QgsField(field_name, field_type, len=field_length))
            else:
                fields.append(QgsField(field_name, field_type))
        
        # Create the vector layer
        layer = QgsVectorLayer(f"Polygon?crs={layer_crs.authid()}", layer_name, "memory")

        # Assign the fields to the layer's data provider
        provider = layer.dataProvider()
        provider.addAttributes(fields)
        layer.updateFields()

        return layer

    @staticmethod

    def generate_EVEL_model_layer(checkbox):
        checkbox_name = UICheckboxes.get_checkbox_display_name(checkbox.objectName())
        group_name = CheckBoxMappings.get_group_name(checkbox.objectName())
        layer_name = CheckBoxMappings.get_layer_name(checkbox.objectName())
        layer_variables_filename = CheckBoxMappings.get_file_name(checkbox.objectName())
        style_name = CheckBoxMappings.get_style_filename(checkbox.objectName())

             # Insert print statements to debug the variables
        print(f"Checkbox Name: {checkbox_name}")
        print(f"Group Name: {group_name}")
        print(f"Layer Name: {layer_name}")
        print(f"layer_variables_filename: {layer_variables_filename}")
        print(f"Style Name: {style_name}")

        if checkbox.isChecked():
            EVEL_Creator.generate_EVEL_group_layer_and_model_layer(group_name, layer_name,  layer_variables_filename, style_name,)
        else:
            EVEL_Creator.remove_layer_by_name(layer_name)
            EVEL_Creator.remove_empty_group_by_name(group_name)
            
    @staticmethod
    def generate_EVEL_group_layer_and_model_layer(group_name, layer_name,  file_name, style_name=None,):
        # Check if the group layer exists, if not, create it
        project = QgsProject.instance()
        root = project.layerTreeRoot()
    # Use the provided setup_layer_name variable to find or create the "Settings" group
        setup_layer_name = SetupLayers().mailabl_main_group_name
        settings_group = EVELGroupGenerator.get_or_create_group(root, setup_layer_name)
        
        # Ensure "EVEL_MAIN" group exists under "Settings", if not, create it
        main_group = settings_group.findGroup(EvelGroupLayersNames.EVEL_MAIN)
        if main_group is None:
            main_group = settings_group.addGroup(EvelGroupLayersNames.EVEL_MAIN)
        
        # Find or create the group named by group_name under "EVEL_MAIN" group
        group_layer = main_group.findGroup(group_name)
        if group_layer is None:
            group_layer = main_group.addGroup(group_name)


        # Create the model layer within the group layer
        project_crs = project.crs()

        field_definitions = EVEL_Creator.get_field_definitions(file_name)  # Define your fields here or pass as a parameter
        layer = EVEL_Creator.create_layer_with_fields(layer_name, project_crs, field_definitions)
        
        # Check if a layer with the same name already exists
        EVEL_Creator.remove_layer_by_name(layer_name)
        
        # Add layer to the group layer and apply style
        GroupActions.add_layer_to_group(layer, group_name, style_name)

    @staticmethod
    def remove_layer_by_name(layer_name):
        # Checkbox is unchecked, remove the layer if it exists
        existing_layers = QgsProject.instance().mapLayersByName(layer_name)
        if existing_layers:
            QgsProject.instance().removeMapLayer(existing_layers[0])

    @staticmethod
    def remove_empty_group_by_name(group_name):
        root = QgsProject.instance().layerTreeRoot()
        group = EVEL_Creator.find_group_by_name(root, group_name)
        if group and not group.findLayers():
            parent = group.parent()
            parent.removeChildNode(group)

    @staticmethod
    def find_group_by_name(node, name):
        for child in node.children():
            if isinstance(child, QgsLayerTreeGroup) and child.name() == name:
                return child
            elif isinstance(child, QgsLayerTreeGroup):
                result = EVEL_Creator.find_group_by_name(child, name)
                if result:
                    return result
        return None


    @staticmethod
    def get_field_definitions(file_name):
        # Remove .py extension if present
        if file_name.endswith('.py'):
            file_name = file_name[:-3]

        # Add the LayerVariables directory to sys.path
        current_directory = os.path.dirname(__file__)
        layer_variables_directory = os.path.join(current_directory, 'LayerVariables')
        if layer_variables_directory not in sys.path:
            sys.path.insert(0, layer_variables_directory)

        # Construct the module path
        module_path = file_name
        
        # Import the module dynamically
        module = importlib.import_module(module_path)
        
        # Access the LayerFunctions class and call the fields method
        field_definitions = module.LayerFunctions.fields()
        
        return field_definitions
        
    



class EVELGroupGenerator:
    # Function to get or create a group by name
    def get_or_create_group(parent, group_name):
        group = parent.findGroup(group_name)
        if group is None:
            group = parent.addGroup(group_name)
        return group


class EVELCancel:
    @staticmethod
    def remove_group_and_contents(group_name):
        root = QgsProject.instance().layerTreeRoot()
        group = EVELCancel.find_group_by_name(root, group_name)
        if group:
            EVELCancel.remove_all_children(group)
            parent = group.parent()
            parent.removeChildNode(group)

    @staticmethod
    def remove_all_children(group):
        for child in group.children():
            if isinstance(child, QgsLayerTreeLayer):
                QgsProject.instance().removeMapLayer(child.layerId())
            elif isinstance(child, QgsLayerTreeGroup):
                EVELCancel.remove_all_children(child)
                group.removeChildNode(child)

    @staticmethod
    def find_group_by_name(node, name):
        for child in node.children():
            if isinstance(child, QgsLayerTreeGroup) and child.name() == name:
                return child
            elif isinstance(child, QgsLayerTreeGroup):
                result = EVELCancel.find_group_by_name(child, name)
                if result:
                    return result
        return None

