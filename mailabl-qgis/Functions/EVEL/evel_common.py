from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFields,
    QgsField,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer
)
from ..layer_generator import GroupActions


class EvelLayerNames:
    EASEMENT = "evel_Servituut"
    WATER = "evel_Vesi"
    SEWAGE = "evel_Kanal"
    SERVICES = "evel_Töökäsud"

class EvelGroupLayers:
    EVEL_MAIN = 'EVEL_Mudel'
    EASEMENT = 'Servituut'
    SERVICES = 'Töökäsud'



    @staticmethod
    def create_EVEL_group_layer(sub_group_layer_name=None):
        from qgis.core import QgsProject
        # Get the main group layer name and sub-group layer name
        main_group_layer_name = EvelGroupLayers.EVEL_MAIN
        # Get the root of the layer tree
        root = QgsProject.instance().layerTreeRoot()
        # Find or create the main group layer and insert it at the top
        main_group = root.findGroup(main_group_layer_name)
        if main_group is None:
            main_group = root.insertGroup(0, main_group_layer_name)
        # Find or create the sub-group layer within the main group
        if sub_group_layer_name is None:
            return
        sub_group = main_group.findGroup(sub_group_layer_name)
        if sub_group is None:
            main_group.addGroup(sub_group_layer_name)
    
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
    def generate_EVEL_model_layer(checkbox, group_name, layer_name, style_name):
        if checkbox.isChecked():
            EvelGroupLayers.create_EVEL_group_layer(sub_group_layer_name=group_name)
            
            

            from .LayerVariables.evel_easements import LayerFunctions
            field_definitions = LayerFunctions.easment_fields()
            # Get the project's CRS
            project_crs = QgsProject.instance().crs()
            # Create the layer with the specified fields
            layer = EVEL_Creator.create_layer_with_fields(layer_name, project_crs, field_definitions)
            # Check if a layer with the same name already exists
            EVEL_Creator.remove_layer_by_name(layer_name)
            GroupActions.add_layer_to_group(layer, group_name, style_name=style_name)
        else:
            EVEL_Creator.remove_layer_by_name(layer_name)
            EVEL_Creator.remove_empty_group_by_name(group_name)


    @staticmethod
    def remove_layer_by_name(layer_name):
        # Checkbox is unchecked, remove the easement layer if it exists
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