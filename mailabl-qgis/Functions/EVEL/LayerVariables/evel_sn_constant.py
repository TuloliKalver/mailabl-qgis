from qgis.PyQt.QtCore import QVariant
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFields,
    QgsField,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer,
    QgsFeature
)
import os
import sys
import importlib
from ....KeelelisedMuutujad.EVEL_lang_module import EvelGroupLayersNames, UICheckboxes, CheckBoxMappings

class SNConstantFields:
    field_id = "ID"
    field_groupname = "GROUPNAME"
    field_txt = "TXT"
    field_parent_group = "PARENT_GROUP"
    field_description = "DESCRIPRION"
    field_orderno = "ORDERNO"

class SNConstantAliases:
    alias_id = "Primaarvõti"
    alias_groupname = "Grupp"
    alias_txt = "Liigid"
    alias_parent_group = "A grupp"
    alias_description = "Kirjeldus"
    alias_orderno = "Järjekorra nr"

class LayerFunctions:
    @staticmethod
    def fields():
        field_definitions = [
            (SNConstantFields.field_id, QVariant.Int, True),
            (SNConstantFields.field_groupname, QVariant.String, 50),
            (SNConstantFields.field_txt, QVariant.String, 60),
            (SNConstantFields.field_parent_group, QVariant.String, 50),
            (SNConstantFields.field_description, QVariant.String, 50),
            (SNConstantFields.field_orderno, QVariant.Int, False)
        ]
        return field_definitions

class KeyDefinitions:
    @staticmethod
    def primary_key():
        primary_key = ("PK_SN_CONSTANT", [SNConstantFields.field_id])
        return primary_key
    
class Values:
    variables = [
        {"ID": 0, "GROUPNAME": 'BUILDING_AREA_LOCATION', "TXT": 'Maa-alune', "PARENT_GROUP": None, "DESCRIPTION": 'Rajatise paiknemine', "ORDERNO": None},
        {"ID": 1, "GROUPNAME": 'BUILDING_AREA_LOCATION', "TXT": 'Maapealne', "PARENT_GROUP": None, "DESCRIPTION": None, "ORDERNO": None},
        {"ID": 2, "GROUPNAME": 'BUILDING_AREA_TYPE', "TXT": 'Reovee eelpuhastid', "PARENT_GROUP": None, "DESCRIPTION": 'Rajatise tüüp', "ORDERNO": None},
    ]

class GroupActions:
    @staticmethod
    def add_layer_to_group(layer, group_name, style_name=None):
        print(f"group_name: {group_name}")
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        group = root.findGroup(group_name)
        if not group:
            print("group_name not found")
            group = root.addGroup(group_name)
        group.insertLayer(0, layer)
        
        # Apply style if provided
        if style_name:
            layer.loadNamedStyle(style_name)
            layer.triggerRepaint()

class EVEL_SnCreator:
    @staticmethod
    def create_layer_with_fields(layer_name, crs, field_definitions):
        fields = QgsFields()
        for field_def in field_definitions:
            field = QgsField(field_def[0], QVariant.String if field_def[1] == 10 else QVariant.Int, '', field_def[2])
            fields.append(field)
        layer = QgsVectorLayer(f"NoGeometry?crs={crs.authid()}", layer_name, 'memory')
        layer.dataProvider().addAttributes(fields)
        layer.updateFields()
        QgsProject.instance().addMapLayer(layer)
        return layer


    @staticmethod
    def remove_layer_by_name(layer_name):
        project = QgsProject.instance()
        layers = project.mapLayersByName(layer_name)
        if layers:
            project.removeMapLayer(layers[0])
        else:
            print("no layers found in: remove_layer_by_name")

    @staticmethod
    def remove_empty_group_by_name(group_name):
        root = QgsProject.instance().layerTreeRoot()
        group = EVEL_SnCreator.find_group_by_name(root, group_name)
        if group and not group.findLayers():
            parent = group.parent()
            parent.removeChildNode(group)

    @staticmethod
    def find_group_by_name(node, name):
        for child in node.children():
            if isinstance(child, QgsLayerTreeGroup) and child.name() == name:
                return child
            elif isinstance(child, QgsLayerTreeGroup):
                result = EVEL_SnCreator.find_group_by_name(child, name)
                if result:
                    return result
        return None

    @staticmethod
    def get_field_definitions(file_name):
        if file_name.endswith('.py'):
            file_name = file_name[:-3]

        current_directory = os.path.dirname(__file__)
        layer_variables_directory = os.path.join(current_directory, 'LayerVariables')
        if layer_variables_directory not in sys.path:
            sys.path.insert(0, layer_variables_directory)

        module_path = file_name
        module = importlib.import_module(module_path)
        field_definitions = module.LayerFunctions.fields()
        return field_definitions

    @staticmethod
    def generate_sn_layer(group_name, layer_name, style_name=None):
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        from ....processes.OnFirstLoad.AddSetupLayers import SetupLayers
        setup_layer_name = SetupLayers().mailabl_main_group_name

        settings_group = root.findGroup(setup_layer_name)
        if settings_group is None:
            settings_group = root.addGroup(setup_layer_name)

        main_group = settings_group.findGroup(EvelGroupLayersNames.EVEL_MAIN)
        if main_group is None:
            main_group = settings_group.addGroup(EvelGroupLayersNames.EVEL_MAIN)

        group_layer = main_group.findGroup(group_name)
        if group_layer is None:
            group_layer = main_group.addGroup(group_name)

        project_crs = project.crs()

        field_definitions = LayerFunctions.fields()
        print(f"field_definitions: {field_definitions}")
        layer = EVEL_SnCreator.create_layer_with_fields(layer_name, project_crs, field_definitions)
        
        #EVEL_SnCreator.remove_layer_by_name(layer_name)
        
        GroupActions.add_layer_to_group(layer, group_name, style_name)

        EVEL_SnCreator.insert_values_to_layer(layer_name, Values.variables)

    @staticmethod
    def insert_values_to_layer(layer_name, values):
        print(f"layer_name: {layer_name}")
        #project = QgsProject.instance()
        #layers = project.mapLayersByName(layer_name)
        #print(f"layers: {layers}")
        #layer = layers[0]
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        print(f"Layer: {layer}")
        if layer:
            layer.startEditing()
            for value in values:
                feature = QgsFeature()
                feature.setFields(layer.fields())
                
                # Assuming 'value' is a dictionary from Values.variables
                attributes = [
                    value.get("ID"),
                    value.get("GROUPNAME"),
                    value.get("TXT"),
                    value.get("PARENT_GROUP"),
                    value.get("DESCRIPTION"),
                    value.get("ORDERNO"),
                ]
                
                # Ensure attributes match the field count
                #while len(attributes) < len(layer.fields()):
                #    attributes.append(None)
                
                feature.setAttributes(attributes)
                layer.addFeature(feature)
            print(f"Features added")
            layer.commitChanges()
        else:
            print("no layers found in: insert_values_to_layer(layer_name, values)")
   
class SnPublicFunctions:
    def generate_SN_layer(checkbox):

        checkbox_name = UICheckboxes.get_checkbox_display_name(checkbox.objectName())
        group_name = CheckBoxMappings.get_group_name(checkbox.objectName())
        layer_name = CheckBoxMappings.get_layer_name(checkbox.objectName())
        style_name = CheckBoxMappings.get_style_filename(checkbox.objectName())

        print(f"Checkbox Name: {checkbox_name}")
        print(f"Group Name: {group_name}")
        print(f"Layer Name: {layer_name}")
        print(f"Style Name: {style_name}")

        if checkbox.isChecked():
            EVEL_SnCreator.generate_sn_layer(group_name, layer_name, style_name)
        else:
            EVEL_SnCreator.remove_layer_by_name(layer_name)
            EVEL_SnCreator.remove_empty_group_by_name(group_name)


