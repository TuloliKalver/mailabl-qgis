from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFields,
    QgsField,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer
)
from ..layer_generator import GroupActions
from ...KeelelisedMuutujad.EVEL_lang_module import EvelGroupLayersNames, EvelLayerNames
from ...config.settings import FilesByNames

class EvelGroupLayers:
    EVEL_MAIN = 'EVEL_Mudel'
    EASEMENT = 'Servituut'
    SERVICES = 'Töökäsud'

    @staticmethod
    def create_EVEL_group_layer(sub_group_layer_name=None):
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
    def generate_EVEL_model_layer(checkbox):
        group_name = EvelGroupLayersNames.__dict__.get(checkbox.objectName())
        layer_name = EvelLayerNames.__dict__.get(checkbox.objectName())
        style_name = CheckboxStyles.get_style_filename(checkbox.objectName())  # Corrected method name

        if checkbox.isChecked():
            EVEL_Creator.generate_EVEL_group_layer_and_model_layer(group_name, layer_name, style_name)
        else:
            EVEL_Creator.remove_layer_by_name(layer_name)
            EVEL_Creator.remove_empty_group_by_name(group_name)
            
    @staticmethod
    def generate_EVEL_group_layer_and_model_layer(group_name, layer_name, style_name):
        # Check if the group layer exists, if not, create it
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        main_group = root.findGroup(EvelGroupLayers.EVEL_MAIN)
        if main_group is None:
            main_group = root.insertGroup(0, EvelGroupLayers.EVEL_MAIN)
        
        group_layer = main_group.findGroup(group_name)
        if group_layer is None:
            group_layer = main_group.addGroup(group_name)

        # Create the model layer within the group layer
        project_crs = project.crs()
        field_definitions = []  # Define your fields here or pass as a parameter
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


class CheckboxStyles:
    # Define QML style filenames for each checkbox based on their objectName()
    STYLES = {
        'cbWater': "water_evelLayer.qml",
        'cbSewage': "sewage_evelLayer.qml",
        'cbRainwater': "rainwater_evelLayer.qml",
        'cbPumpstation': "pumpstation_evelLayer.qml",
        'cbSewTreatment': "sew_treatment_evelLayer.qml",
        'cbConnectionPoints': "connection_points_evelLayer.qml",
        'cbEasements': "easements_evelLayer.qml",
        'cbServices': "services_evelLayer.qml",
        'cbSNConstant': "sn_constant_evelLayer.qml",
        # Add new checkboxes here with their corresponding .qml style filenames
        'cbDevice': "device_evelLayer.qml",
        'cbContract': "contract_evelLayer.qml",
        'cbCustomer': "customer_evelLayer.qml",
        'cbExternalDoc': "external_doc_evelLayer.qml",
        'cbApartment': "apartment_evelLayer.qml",
        'cbFlowMeter': "flow_meter_evelLayer.qml",
        'cbDemarcationPoint': "demarcation_point_evelLayer.qml",
        'cbFirePlug': "fire_plug_evelLayer.qml",
        'cbManhole': "manhole_evelLayer.qml",
        'cbPressureStation': "pressure_station_evelLayer.qml",
        'cbValve': "valve_evelLayer.qml",
        'cbTank': "tank_evelLayer.qml",
        'cbProperties': "properties_evelLayer.qml",
        'cbProgram': "program_evelLayer.qml",
        'cbOperation': "operation_evelLayer.qml",
        'cbError': "error_evelLayer.qml",
    }

    @staticmethod
    def get_style_filename(checkbox_name):
        # Return the QML style filename based on the checkbox name
        return CheckboxStyles.STYLES.get(checkbox_name, None)