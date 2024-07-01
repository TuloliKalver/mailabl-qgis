from qgis.PyQt.QtCore import QVariant

class SNWaterDuctFields:
    # Defineeri välja nimed muutujatena
    field_msl = "MSLINK"
    field_identification = "IDENTIFICATION"
    field_network_id = "NETWORK_ID"
    field_nettype_id = "NETTYPE_ID"
    field_duct_type_id = "DUCT_TYPE_ID"
    field_material_id = "MATERIAL_ID"
    field_diameter_type_id = "DIAMETER_TYPE_ID"
    field_diameter_id = "DIAMETER_ID"
    field_pressure_class_id = "PRESSURE_CLASS_ID"
    field_firmness_class_id = "FIRMNESS_CLASS_ID"
    field_begin_node_id = "BEGIN_NODE_ID"
    field_end_node_id = "END_NODE_ID"
    field_begin_z_coord = "BEGIN_Z_COORD"
    field_end_z_coord = "END_Z_COORD"
    field_location_id = "LOCATION_ID"
    field_flowdirection = "FLOWDIRECTION"
    field_condition_class_id = "CONDITION_CLASS_ID"
    field_length_2d = "LENGTH_2D"
    field_length = "LENGTH"
    field_inventory_nr = "INVENTORY_NR"
    field_usage_permit_nr = "USAGE_PERMIT_NR"
    field_usage_permit_date = "USAGE_PERMIT_DATE"
    field_usage_state = "USAGE_STATE"
    field_owner_id = "OWNER_ID"
    field_lessee_id = "LESSEE_ID"
    field_note = "NOTE"
    field_plan_id = "PLAN_ID"
    field_build_year = "BUILD_YEAR"
    field_removal_year = "REMOVAL_YEAR"
    field_geom = "GEOM"
    field_location_accuracy_id = "LOCATION_ACCURACY_ID"
    field_height_accuracy_id = "HEIGHT_ACCURACY_ID"
    field_mapping_method_id = "MAPPING_METHOD_ID"
    field_pressure = "PRESSURE"
    field_address_id = "ADDRESS_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"
    field_estimated_service_life = "ESTIMATED_SERVICE_LIFE"
    field_epanet_inner_diameter = "EPANET_INNER_DIAMETER"
    field_epanet_roughness = "EPANET_ROUGHNESS"
    field_epanet_mloss = "EPANET_MLOSS"
    field_epanet_status_id = "EPANET_STATUS_ID"
    field_duct_friction_loss = "DUCT_FRICTION_LOSS"

class SNWaterDuctAliases:
    # Defineeri aliasid muutujatena
    alias_msl = "ID"
    alias_identification = "Toru tähis"
    alias_network_id = "Võrk"
    alias_nettype_id = "Võrgu tüüp"
    alias_duct_type_id = "Otstarve"
    alias_material_id = "Materjal"
    alias_diameter_type_id = "Läbimõõdu tüüp"
    alias_diameter_id = "Läbimõõt"
    alias_pressure_class_id = "Rõhuklass"
    alias_firmness_class_id = "Ringjäikus"
    alias_begin_node_id = "Algussõlm"
    alias_end_node_id = "Lõppsõlm"
    alias_begin_z_coord = "Toru kõrgus AS"
    alias_end_z_coord = "Toru kõrgus LS"
    alias_location_id = "Paiknemine"
    alias_flowdirection = "Voolusuund"
    alias_condition_class_id = "Seisukord"
    alias_length_2d = "Pikkus 2D"
    alias_length = "Pikkus 3D"
    alias_inventory_nr = "Põhavara nr"
    alias_usage_permit_nr = "Kasutusloa nr"
    alias_usage_permit_date = "Kasutusloa kp"
    alias_usage_state = "Kasutuse olek"
    alias_owner_id = "Omanik"
    alias_lessee_id = "Rentnik"
    alias_note = "Märkused"
    alias_plan_id = "Graafilised andmed"
    alias_build_year = "Ehitusaasta"
    alias_removal_year = "Kasut_eemald_aasta"
    alias_geom = "Geomeetria"
    alias_location_accuracy_id = "Asukoha täpsus"
    alias_height_accuracy_id = "Kõrguse täpsus"
    alias_mapping_method_id = "Kaardistusmeetod"
    alias_pressure = "Surve"
    alias_address_id = "Aadress ID"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"
    alias_estimated_service_life = "Tehniline eluiga"
    alias_epanet_inner_diameter = "Epanet_sise_diam"
    alias_epanet_roughness = "Epanet_karedus"
    alias_epanet_mloss = "Epanet_kadu"
    alias_epanet_status_id = "Epanet olek"
    alias_duct_friction_loss = "Hõõrdesurvekadu"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Defineeri välja määratlused evel.SN_WATER_DUCT jaoks
        field_definitions = [
            (SNWaterDuctFields.field_msl, QVariant.Int, True),
            (SNWaterDuctFields.field_identification, QVariant.String, False),
            (SNWaterDuctFields.field_network_id, QVariant.Int, False),
            (SNWaterDuctFields.field_nettype_id, QVariant.Int, False),
            (SNWaterDuctFields.field_duct_type_id, QVariant.Int, False),
            (SNWaterDuctFields.field_material_id, QVariant.Int, False),
            (SNWaterDuctFields.field_diameter_type_id, QVariant.Int, False),
            (SNWaterDuctFields.field_diameter_id, QVariant.Int, False),
            (SNWaterDuctFields.field_pressure_class_id, QVariant.Int, False),
            (SNWaterDuctFields.field_firmness_class_id, QVariant.Int, False),
            (SNWaterDuctFields.field_begin_node_id, QVariant.Int, False),
            (SNWaterDuctFields.field_end_node_id, QVariant.Int, False),
            (SNWaterDuctFields.field_begin_z_coord, QVariant.Double, False),
            (SNWaterDuctFields.field_end_z_coord, QVariant.Double, False),
            (SNWaterDuctFields.field_location_id, QVariant.Int, False),
            (SNWaterDuctFields.field_flowdirection, QVariant.Double, False),
            (SNWaterDuctFields.field_condition_class_id, QVariant.Int, False),
            (SNWaterDuctFields.field_length_2d, QVariant.Double, False),
            (SNWaterDuctFields.field_length, QVariant.Double, False),
            (SNWaterDuctFields.field_inventory_nr, QVariant.String, False),
            (SNWaterDuctFields.field_usage_permit_nr, QVariant.String, False),
            (SNWaterDuctFields.field_usage_permit_date, QVariant.DateTime, False),
            (SNWaterDuctFields.field_usage_state, QVariant.Int, False),
            (SNWaterDuctFields.field_owner_id, QVariant.Int, False),
            (SNWaterDuctFields.field_lessee_id, QVariant.Int, False),
            (SNWaterDuctFields.field_note, QVariant.String, False),
            (SNWaterDuctFields.field_plan_id, QVariant.Int, False),
            (SNWaterDuctFields.field_build_year, QVariant.Int, False),
            (SNWaterDuctFields.field_removal_year, QVariant.Int, False),
            (SNWaterDuctFields.field_geom, QVariant.String, False),
            (SNWaterDuctFields.field_location_accuracy_id, QVariant.Int, False),
            (SNWaterDuctFields.field_height_accuracy_id, QVariant.Int, False),
            (SNWaterDuctFields.field_mapping_method_id, QVariant.Int, False),
            (SNWaterDuctFields.field_pressure, QVariant.Double, False),
            (SNWaterDuctFields.field_address_id, QVariant.Int, False),
            (SNWaterDuctFields.field_creator, QVariant.String, False),
            (SNWaterDuctFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterDuctFields.field_updated_by, QVariant.String, False),
            (SNWaterDuctFields.field_update_date, QVariant.DateTime, False),
            (SNWaterDuctFields.field_estimated_service_life, QVariant.Int, False),
            (SNWaterDuctFields.field_epanet_inner_diameter, QVariant.Double, False),
            (SNWaterDuctFields.field_epanet_roughness, QVariant.Double, False),
            (SNWaterDuctFields.field_epanet_mloss, QVariant.Double, False),
            (SNWaterDuctFields.field_epanet_status_id, QVariant.Int, False),
            (SNWaterDuctFields.field_duct_friction_loss, QVariant.Double, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti evel.SN_WATER_DUCT jaoks
        primary_key = ("PK_SN_WATER_DUCT", [SNWaterDuctFields.field_msl])
        return primary_key

    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed evel.SN_WATER_DUCT jaoks
        foreign_keys = [
            ("FK_SN_WATER_DUCT_NETWORK", [SNWaterDuctFields.field_network_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_SN_CONSTANT", [SNWaterDuctFields.field_nettype_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_MATERIAL", [SNWaterDuctFields.field_material_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_DIAMETER", [SNWaterDuctFields.field_diameter_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_DIAMETER_TYPE", [SNWaterDuctFields.field_diameter_type_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_ENODE_ID", [SNWaterDuctFields.field_end_node_id], "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_WATER_DUCT_PLAN_ID", [SNWaterDuctFields.field_plan_id], "evel.PLAN(ID)"),
            ("FK_SN_WATER_DUCT_HEIGHT", [SNWaterDuctFields.field_height_accuracy_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_DUCT_TYPE", [SNWaterDuctFields.field_duct_type_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_LOCATION_ACC", [SNWaterDuctFields.field_location_accuracy_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_FIRMNESS_CLASS", [SNWaterDuctFields.field_firmness_class_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_PRESSURE_CLASS", [SNWaterDuctFields.field_pressure_class_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_MAPPING", [SNWaterDuctFields.field_mapping_method_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_BNODE_ID", [SNWaterDuctFields.field_begin_node_id], "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_WATER_DUCT_COND_CLASS", [SNWaterDuctFields.field_condition_class_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_OWNER_ID", [SNWaterDuctFields.field_owner_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_LOCATION", [SNWaterDuctFields.field_location_id], "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_DUCT_ADDRESS_ID", [SNWaterDuctFields.field_address_id], "evel.APARTMENT_DATA(ID)"),
            ("FK_SN_WATER_DUCT_LESSEE_ID", [SNWaterDuctFields.field_lessee_id], "evel.SN_CONSTANT(ID)"),
            ("FK_WATER_DUCT_USAGESTATE", [SNWaterDuctFields.field_usage_state], "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys

