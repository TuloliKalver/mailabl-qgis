from qgis.PyQt.QtCore import QVariant

class SNWaterNodeFields:
    # Defineeri välja nimed muutujatena
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
    field_pnt_rotation = "PNT_ROTATION"
    field_pnt_scale = "PNT_SCALE"
    field_internal_node_id = "INTERNAL_NODE_ID"
    field_eic_code = "EIC_CODE"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"
    field_node_friction_loss = "NODE_FRICTION_LOSS"

class SNWaterNodeAliases:
    # Defineeri aliasid muutujatena
    alias_mslk = "Primaarvõti"
    alias_identification = "Tähis"
    alias_network_id = "Võrk"
    alias_nettype_id = "Võrgu tüüp"
    alias_z_coord1 = "Elemendi kõrgus (m)"
    alias_z_coord2 = "Põhja kõrgus (m)"
    alias_z_coord3 = "Maapinna Kõrgus"
    alias_open_state = "Olek (a/s)"
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
    alias_pnt_rotation = "Sõlme pöördenurk"
    alias_pnt_scale = "Sõlme skaala"
    alias_internal_node_id = "Eritüübiliste sõlmede ühendamiseks"
    alias_eic_code = "EIC kood"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"
    alias_node_friction_loss = "Kohtsurvekadu"

class SNWaterNodeFunctions:

    @staticmethod
    def sn_water_node_fields():
        # Defineeri välja määratlused SN_WATER_NODE jaoks
        field_definitions = [
            (SNWaterNodeFields.field_mslk, QVariant.Int, True),
            (SNWaterNodeFields.field_identification, QVariant.String, 50),
            (SNWaterNodeFields.field_network_id, QVariant.Int, False),
            (SNWaterNodeFields.field_nettype_id, QVariant.Int, False),
            (SNWaterNodeFields.field_z_coord1, QVariant.Double, False),
            (SNWaterNodeFields.field_z_coord2, QVariant.Double, False),
            (SNWaterNodeFields.field_z_coord3, QVariant.Double, False),
            (SNWaterNodeFields.field_open_state, QVariant.Int, False),
            (SNWaterNodeFields.field_state_info, QVariant.Int, False),
            (SNWaterNodeFields.field_condition_class_id, QVariant.Int, False),
            (SNWaterNodeFields.field_inventory_nr, QVariant.String, 20),
            (SNWaterNodeFields.field_usage_permit_nr, QVariant.String, 20),
            (SNWaterNodeFields.field_usage_permit_date, QVariant.DateTime, False),
            (SNWaterNodeFields.field_usage_state, QVariant.Int, False),
            (SNWaterNodeFields.field_owner_id, QVariant.Int, False),
            (SNWaterNodeFields.field_lessee_id, QVariant.Int, False),
            (SNWaterNodeFields.field_address_id, QVariant.Int, False),
            (SNWaterNodeFields.field_note, QVariant.String, 1024),
            (SNWaterNodeFields.field_plan_id, QVariant.Int, False),
            (SNWaterNodeFields.field_build_year, QVariant.Double, False),
            (SNWaterNodeFields.field_removal_year, QVariant.Double, False),
            (SNWaterNodeFields.field_geom, QVariant.String, False),  # Assuming geometry is stored as string
            (SNWaterNodeFields.field_location_accuracy_id, QVariant.Int, False),
            (SNWaterNodeFields.field_height_accuracy_id, QVariant.Int, False),
            (SNWaterNodeFields.field_mapping_method_id, QVariant.Int, False),
            (SNWaterNodeFields.field_pnt_rotation, QVariant.Int, False),
            (SNWaterNodeFields.field_pnt_scale, QVariant.Int, False),
            (SNWaterNodeFields.field_internal_node_id, QVariant.Int, False),
            (SNWaterNodeFields.field_eic_code, QVariant.String, 50),
            (SNWaterNodeFields.field_creator, QVariant.String, 30),
            (SNWaterNodeFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterNodeFields.field_updated_by, QVariant.String, 30),
            (SNWaterNodeFields.field_update_date, QVariant.DateTime, False),
            (SNWaterNodeFields.field_node_friction_loss, QVariant.Double, False)
        ]
        return field_definitions

class SNWaterNodeKeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti SN_WATER_NODE jaoks
        primary_key = ("PK_SN_WATER_NODE", [SNWaterNodeFields.field_mslk])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed SN_WATER_NODE jaoks
        foreign_keys = [
            ("FK_SN_WATER_NODE_NETTYPE_ID", SNWaterNodeFields.field_nettype_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_VALVE_STATE_INFO", SNWaterNodeFields.field_state_info, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_NODE_LESSEE_ID", SNWaterNodeFields.field_lessee_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WNODE_OWNER", SNWaterNodeFields.field_owner_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_NODE_STATE", SNWaterNodeFields.field_open_state, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_NODE_PLAN_ID", SNWaterNodeFields.field_plan_id, "evel.PLAN(ID)"),
            ("FK_WNODE_USAGESTATE_ID", SNWaterNodeFields.field_usage_state, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_NODE_NETWORK_ID", SNWaterNodeFields.field_network_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_NODE_CONDITION_CLASS", SNWaterNodeFields.field_condition_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WNODE_MAPPING", SNWaterNodeFields.field_mapping_method_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_NODE_ADDRESS_ID", SNWaterNodeFields.field_address_id, "evel.APARTMENT_DATA(ID)"),
            ("FK_SN_WNODE_LOCATION", SNWaterNodeFields.field_location_accuracy_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WNODE_HEIGHT", SNWaterNodeFields.field_height_accuracy_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
