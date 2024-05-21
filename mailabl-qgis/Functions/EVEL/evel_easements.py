from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFields,
    QgsField,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
)
from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsProject
from PyQt5.QtCore import QDateTime
from .evel_general import EvelGroupLayers, EvelLayerNames
from ..layer_generator import GroupActions

class EasemensFields:
    # Define field names as variables
    field_id = "ID"
    field_type_id = "TYPE_ID"
    field_plan_id = "PLAN_ID"
    field_state_id = "STATE_ID"
    field_real_estate_name = "REAL_ESTATE_NAME"
    field_real_estate_nr = "REAL_ESTATE_NR"
    field_description = "DESCRIPTION"
    field_contract_date = "CONTRACT_DATE"
    field_perimeter = "PERIMETER"
    field_area_size = "AREA_SIZE"
    field_geom = "GEOM"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"
    
class EasementAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_type_id = "Tüüp (LAND_PERM_TYPE)"
    alias_plan_id = "Lepingu olek (LAND_PERM_STATE) (Tegemisel, sõlmitud)"
    alias_state_id = "Lepingu olek (LAND_PERM_STATE) (Tegemisel, sõlmitud)"
    alias_real_estate_name = "Lähiaadress"
    alias_real_estate_nr = "Katastritunnus"
    alias_description = "Kaetud tehnovõrgud (Kirjeldus (Vesi, Kanal))"
    alias_contract_date = "Sõlmimise kp"
    alias_perimeter = "Ümbermõõt (m)"
    alias_area_size = "Geomeetria"
    alias_geom = "Geomeetria"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kpMuutmise kp"

class LayerFunctions:
    def generate_EVEL_easement():

        easement_group = EvelGroupLayers.EASEMENT
        EvelGroupLayers.create_EVEL_group_layer(sub_group_layer_name=easement_group)
        
        # Define the layer's attributes based on EVEL easements schema
        fields = QgsFields()
        fields.append(QgsField(EasemensFields().field_id, QVariant.Int))
        fields.append(QgsField(EasemensFields().field_type_id, QVariant.Int))
        fields.append(QgsField(EasemensFields().field_plan_id, QVariant.Int))
        fields.append(QgsField(EasemensFields().field_state_id, QVariant.Int))
        fields.append(QgsField(EasemensFields().field_real_estate_name, QVariant.String, len=100))
        fields.append(QgsField(EasemensFields().field_real_estate_nr, QVariant.String, len=14))
        fields.append(QgsField(EasemensFields().field_description, QVariant.String, len=50))
        fields.append(QgsField(EasemensFields().field_contract_date, QVariant.DateTime))
        fields.append(QgsField(EasemensFields().field_perimeter, QVariant.Int))
        fields.append(QgsField(EasemensFields().field_area_size, QVariant.Int))
        fields.append(QgsField(EasemensFields().field_creator, QVariant.String, len=64))
        fields.append(QgsField(EasemensFields().field_creation_date, QVariant.DateTime))
        fields.append(QgsField(EasemensFields().field_updated_by, QVariant.String, len=50))
        fields.append(QgsField(EasemensFields().field_update_date, QVariant.DateTime))
        # Get the project's CRS
        project_crs = QgsProject.instance().crs()

        # Create the vector layer
        layer = QgsVectorLayer(f"Polygon?crs={project_crs.authid()}", EvelLayerNames().EASEMENT, "memory")

        
        # Assign the fields to the layer's data provider
        provider = layer.dataProvider()
        provider.addAttributes(fields)
        layer.updateFields()
        
        # Check if a layer with the same name already exists
        existing_layers = QgsProject.instance().mapLayersByName(EvelLayerNames().EASEMENT)
        if existing_layers:
            # Remove the existing layer before continuing
            QgsProject.instance().removeMapLayer(existing_layers[0])
            
        from ...config.settings import FilesByNames
        style_name = FilesByNames().easement_evelLayer
        GroupActions.add_layer_to_group(layer, easement_group, style_name=style_name)

    @staticmethod
    def test_add_easement(layer, cadastral_name, cadastral_nr):
        # Get field names from EasemensFields class
        field_names = EasemensFields()

        # Create a new feature
        feature = QgsFeature()
        
        # Set attribute values based on the field names
        feature.setAttribute(field_names.field_type_id, None)  # Set as needed
        feature.setAttribute(field_names.field_plan_id, 301)  # Example value
        feature.setAttribute(field_names.field_state_id, 301)
        feature.setAttribute(field_names.field_real_estate_name, cadastral_name)
        feature.setAttribute(field_names.field_real_estate_nr, cadastral_nr)
        feature.setAttribute(field_names.field_description, "")
        feature.setAttribute(field_names.field_contract_date, "")  # Example value
        feature.setAttribute(field_names.field_perimeter, 100)
        feature.setAttribute(field_names.field_area_size, 500)
        feature.setAttribute(field_names.field_creator, "")
        feature.setAttribute(field_names.field_creation_date, QDateTime.currentDateTime())
        feature.setAttribute(field_names.field_updated_by, "")
        feature.setAttribute(field_names.field_update_date, QDateTime.currentDateTime())

        # Add the feature to the layer
        layer.startEditing()
        layer.addFeature(feature)
        layer.commitChanges()
