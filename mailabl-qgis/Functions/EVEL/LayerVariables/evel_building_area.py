from qgis.PyQt.QtCore import QVariant

class BuildingAreaFields:
    field_id = "ID"
    field_network_id = "NETWORK_ID"
    field_plan_id = "PLAN_ID"
    field_type_area_id = "TYPE_AREA_ID"
    field_type_id = "TYPE_ID"
    field_usage_state = "USAGE_STATE"
    field_name = "NAME"
    field_description = "DESCRIPTION"
    field_owner_id = "OWNER_ID"
    field_condition_class = "CONDITION_CLASS"
    field_build_year = "BUILD_YEAR"
    field_area_size = "AREA_SIZE"
    field_perimeter = "PERIMETER"
    field_location_id = "LOCATION_ID"
    field_geom = "GEOM"
    field_location_accuracy_id = "LOCATION_ACCURACY_ID"
    field_height_accuracy_id = "HEIGHT_ACCURACY_ID"
    field_mapping_method_id = "MAPPING_METHOD_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class BuildingAreaAliases:
    alias_id = "Primaarvõti"
    alias_network_id = "Võrk"
    alias_plan_id = "Graafilised andmed"
    alias_type_area_id = "Liik"
    alias_type_id = "Alamliik"
    alias_usage_state = "Kasutuse olek"
    alias_name = "Nimetus"
    alias_description = "Kirjeldus"
    alias_owner_id = "Omanik"
    alias_condition_class = "Seisukorra info"
    alias_build_year = "Ehitusaasta"
    alias_area_size = "Pindala"
    alias_perimeter = "Ümbermõõt"
    alias_location_id = "Paiknemine"
    alias_geom = "Geomeetria"
    alias_location_accuracy_id = "Asukoha täpsus"
    alias_height_accuracy_id = "Kõrguse täpsus"
    alias_mapping_method_id = "Kaardistusmeetod"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        field_definitions = [
            (BuildingAreaFields.field_id, QVariant.Int, True),
            (BuildingAreaFields.field_network_id, QVariant.Int, False),
            (BuildingAreaFields.field_plan_id, QVariant.Int, False),
            (BuildingAreaFields.field_type_area_id, QVariant.Int, False),
            (BuildingAreaFields.field_type_id, QVariant.Int, False),
            (BuildingAreaFields.field_usage_state, QVariant.Int, False),
            (BuildingAreaFields.field_name, QVariant.String, 80),
            (BuildingAreaFields.field_description, QVariant.String, 50),
            (BuildingAreaFields.field_owner_id, QVariant.Int, False),
            (BuildingAreaFields.field_condition_class, QVariant.Int, False),
            (BuildingAreaFields.field_build_year, QVariant.Double, False),
            (BuildingAreaFields.field_area_size, QVariant.Int, False),
            (BuildingAreaFields.field_perimeter, QVariant.Int, False),
            (BuildingAreaFields.field_location_id, QVariant.Int, False),
            (BuildingAreaFields.field_geom, QVariant.Polygon, False),
            (BuildingAreaFields.field_location_accuracy_id, QVariant.Int, False),
            (BuildingAreaFields.field_height_accuracy_id, QVariant.Int, False),
            (BuildingAreaFields.field_mapping_method_id, QVariant.Int, False),
            (BuildingAreaFields.field_creator, QVariant.String, 64),
            (BuildingAreaFields.field_creation_date, QVariant.DateTime, False),
            (BuildingAreaFields.field_updated_by, QVariant.String, 50),
            (BuildingAreaFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        primary_key = ("PK_ID", [BuildingAreaFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        foreign_keys = [
            ("FK_BUILDING_AREA_HEIGHT_ACCURACY_ID", BuildingAreaFields.field_height_accuracy_id, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_OWNER_ID", BuildingAreaFields.field_owner_id, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_CONDITION_CLASS_ID", BuildingAreaFields.field_condition_class, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_TYPE_ID", BuildingAreaFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_MAPPING_METHOD_ID", BuildingAreaFields.field_mapping_method_id, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_PLAN_ID", BuildingAreaFields.field_plan_id, "evel.PLAN(ID)"),
            ("FK_BUILDING_AREA_NETWORK_ID", BuildingAreaFields.field_network_id, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_LOCATION_ID", BuildingAreaFields.field_location_id, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_TYPE_AREA_ID", BuildingAreaFields.field_type_area_id, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_USAGE_STATE_ID", BuildingAreaFields.field_usage_state, "evel.SN_CONSTANT(ID)"),
            ("FK_BUILDING_AREA_LOCATION_ACCURACY_ID", BuildingAreaFields.field_location_accuracy_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
