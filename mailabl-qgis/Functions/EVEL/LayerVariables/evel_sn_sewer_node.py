from qgis.PyQt.QtCore import QVariant

class SNSewerNodeFields:
    # Define field names as variables
    field_mslk = "MSLINK"
    field_identification = "IDENTIFICATION"
    field_network_id = "NETWORK_ID"
    field_nettype_id = "NETTYPE_ID"
    field_z_coord1 = "Z_COORD1"
    field_z_coord2 = "Z_COORD2"
    field_z_coord3 = "Z_COORD3"
    field_open_state = "OPEN_STATE"
    field_state_info = "STATE_INFO"
    field_condition_class_id = "CONDITION_CLASS_ID"
    field_inventory_nr = "INVENTORY_NR"
    field_usage_permit_nr = "USAGE_PERMIT_NR"
    field_usage_permit_date = "USAGE_PERMIT_DATE"
    field_usage_state = "USAGE_STATE"
    field_owner_id = "OWNER_ID"
    field_lessee_id = "LESSEE_ID"
    field_address_id = "ADDRESS_ID"
    field_note = "NOTE"
    field_plan_id = "PLAN_ID"
    field_build_year = "BUILD_YEAR"
    field_removal_year = "REMOVAL_YEAR"
    field_geom = "GEOM"
    field_location_accuracy_id = "LOCATION_ACCURACY_ID"
    field_height_accuracy_id = "HEIGHT_ACCURACY_ID"
    field_mapping_method_id = "MAPPING_METHOD_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"
    field_pnt_rotation = "PNT_ROTATION"
    field_pnt_scale = "PNT_SCALE"
    field_internal_node_id = "INTERNAL_NODE_ID"
    field_eic_code = "EIC_CODE"
    field_pressure = "PRESSURE"

class SNSewerNodeAliases:
    # Define aliases as variables
    alias_mslk = "Primaarvõti"
    alias_identification = "Tähis"
    alias_network_id = "Võrk"
    alias_nettype_id = "Võrgutüüp"
    alias_z_coord1 = "Elemendi kõrgus (m)"
    alias_z_coord2 = "Põhja kõrgus (m)"
    alias_z_coord3 = "Maapinna kõrgus (m)"
    alias_open_state = "Olek"
    alias_state_info = "Oleku info"
    alias_condition_class_id = "Seisukord"
    alias_inventory_nr = "Põhivara nr"
    alias_usage_permit_nr = "Kasutusloa nr"
    alias_usage_permit_date = "Kasutusloa kp"
    alias_usage_state = "Kasutuse olek"
    alias_owner_id = "Omanik"
    alias_lessee_id = "Rentnik"
    alias_address_id = "Aadress"
    alias_note = "Märkused"
    alias_plan_id = "Graafilised andmed"
    alias_build_year = "Ehitusaasta"
    alias_removal_year = "Kasut_eemald_aasta"
    alias_geom = "Geomeetria"
    alias_location_accuracy_id = "Asukoha täpsus"
    alias_height_accuracy_id = "Kõrguse täpsus"
    alias_mapping_method_id = "Kaardistusmeetod"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"
    alias_pnt_rotation = "Sõlme pöördenurk"
    alias_pnt_scale = "Sõlme skaala"
    alias_internal_node_id = "Sõlmede ühendamiseks"
    alias_eic_code = "EIC kood"
    alias_pressure = "Surve"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for SN_SEWER_NODE
        field_definitions = [
            (SNSewerNodeFields.field_mslk, QVariant.Int, True),
            (SNSewerNodeFields.field_identification, QVariant.String, 50),
            (SNSewerNodeFields.field_network_id, QVariant.Int, False),
            (SNSewerNodeFields.field_nettype_id, QVariant.Int, False),
            (SNSewerNodeFields.field_z_coord1, QVariant.Double, 20, 6),
            (SNSewerNodeFields.field_z_coord2, QVariant.Double, 20, 6),
            (SNSewerNodeFields.field_z_coord3, QVariant.Double, 20, 6),
            (SNSewerNodeFields.field_open_state, QVariant.Int, False),
            (SNSewerNodeFields.field_state_info, QVariant.Int, False),
            (SNSewerNodeFields.field_condition_class_id, QVariant.Int, False),
            (SNSewerNodeFields.field_inventory_nr, QVariant.String, 20),
            (SNSewerNodeFields.field_usage_permit_nr, QVariant.String, 20),
            (SNSewerNodeFields.field_usage_permit_date, QVariant.DateTime, False),
            (SNSewerNodeFields.field_usage_state, QVariant.Int, False),
            (SNSewerNodeFields.field_owner_id, QVariant.Int, False),
            (SNSewerNodeFields.field_lessee_id, QVariant.Int, False),
            (SNSewerNodeFields.field_address_id, QVariant.Int, False),
            (SNSewerNodeFields.field_note, QVariant.String, 1024),
            (SNSewerNodeFields.field_plan_id, QVariant.Int, False),
            (SNSewerNodeFields.field_build_year, QVariant.Double, 4),
            (SNSewerNodeFields.field_removal_year, QVariant.Double, 4),
            (SNSewerNodeFields.field_geom, QVariant.Point, False),
            (SNSewerNodeFields.field_location_accuracy_id, QVariant.Int, False),
            (SNSewerNodeFields.field_height_accuracy_id, QVariant.Int, False),
            (SNSewerNodeFields.field_mapping_method_id, QVariant.Int, False),
            (SNSewerNodeFields.field_creator, QVariant.String, 30),
            (SNSewerNodeFields.field_creation_date, QVariant.DateTime, False),
            (SNSewerNodeFields.field_updated_by, QVariant.String, 30),
            (SNSewerNodeFields.field_update_date, QVariant.DateTime, False),
            (SNSewerNodeFields.field_pnt_rotation, QVariant.Int, False),
            (SNSewerNodeFields.field_pnt_scale, QVariant.Int, False),
            (SNSewerNodeFields.field_internal_node_id, QVariant.Int, False),
            (SNSewerNodeFields.field_eic_code, QVariant.String, 50),
            (SNSewerNodeFields.field_pressure, QVariant.Double, 1)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for SN_SEWER_NODE
        primary_key = ("PK_SN_SEWER_NODE_MSLINK", [SNSewerNodeFields.field_mslk])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_NODE
        foreign_keys = [
            ("FK_SN_SEWER_NODE_PLAN_ID", SNSewerNodeFields.field_plan_id, "evel.PLAN(ID)"),
            ("FK_SN_SEWER_NODE_MAPPING_METHOD_ID", SNSewerNodeFields.field_mapping_method_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_HEIGHT_ACCURACY_ID", SNSewerNodeFields.field_height_accuracy_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_CONDITION_CLASS_ID", SNSewerNodeFields.field_condition_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_STATE_INFO", SNSewerNodeFields.field_state_info, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_OWNER_ID", SNSewerNodeFields.field_owner_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_OPEN_STATE", SNSewerNodeFields.field_open_state, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_LOCATION_ACCURACY_ID", SNSewerNodeFields.field_location_accuracy_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_LESSEE_ID", SNSewerNodeFields.field_lessee_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_USAGE_STATE", SNSewerNodeFields.field_usage_state, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_ADDRESS_ID", SNSewerNodeFields.field_address_id, "evel.APARTMENT_DATA(ID)"),
            ("FK_SN_SEWER_NODE_NETTYPE_ID", SNSewerNodeFields.field_nettype_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_NODE_NETWORK_ID", SNSewerNodeFields.field_network_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
