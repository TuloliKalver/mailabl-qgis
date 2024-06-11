from qgis.PyQt.QtCore import QVariant

class SewerDuctFields:
    # Define field names as variables
    field_mslk = "MSLINK"
    field_identification = "IDENTIFICATION"
    field_network_id = "NETWORK_ID"
    field_nettype_id = "NETTYPE_ID"
    field_duct_type_id = "DUCT_TYPE_ID"
    field_material_id = "MATERIAL_ID"
    field_diameter_type_id = "DIAMETER_TYPE_ID"
    field_diameter_id = "DIAMETER_ID"
    field_form_code_id = "FORM_CODE_ID"
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
    field_estimated_service_life = "ESTIMATED_SERVICE_LIFE"
    field_geom = "GEOM"
    field_address_id = "ADDRESS_ID"
    field_location_accuracy_id = "LOCATION_ACCURACY_ID"
    field_height_accuracy_id = "HEIGHT_ACCURACY_ID"
    field_mapping_method_id = "MAPPING_METHOD_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SewerDuctAliases:
    # Define aliases as variables
    alias_mslk = "Primaarvõti"
    alias_identification = "Toru tähis"
    alias_network_id = "Võrk"
    alias_nettype_id = "Võrgu tüüp"
    alias_duct_type_id = "Otstarve"
    alias_material_id = "Torumaterjal"
    alias_diameter_type_id = "Läbimõõdu tüüp"
    alias_diameter_id = "Läbimõõt"
    alias_form_code_id = "Toru kuju"
    alias_pressure_class_id = "Rõhuklass"
    alias_firmness_class_id = "Ringjäikus"
    alias_begin_node_id = "Seos algussõlmega"
    alias_end_node_id = "Seos lõppssõlmega"
    alias_begin_z_coord = "Toru kõrgus Algussõlmes"
    alias_end_z_coord = "Toru kõrgus Lõppsõlmes"
    alias_location_id = "Paiknemine"
    alias_flowdirection = "Voolu suund"
    alias_condition_class_id = "Seisukorra info"
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
    alias_removal_year = "Kasutusest eemaldamise aasta"
    alias_estimated_service_life = "Tehniline eluiga"
    alias_geom = "Geomeetria"
    alias_address_id = "Aadress ID"
    alias_location_accuracy_id = "Asukoha täpsus"
    alias_height_accuracy_id = "Kõrguse täpsus"
    alias_mapping_method_id = "Kaardistusmeetod"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:

    def sewer_duct_fields():
        # Define the field definitions for SN_SEWER_DUCT
        field_definitions = [
            (SewerDuctFields.field_mslk, QVariant.Int, True),
            (SewerDuctFields.field_identification, QVariant.String, 20),
            (SewerDuctFields.field_network_id, QVariant.Int, False),
            (SewerDuctFields.field_nettype_id, QVariant.Int, False),
            (SewerDuctFields.field_duct_type_id, QVariant.Int, False),
            (SewerDuctFields.field_material_id, QVariant.Int, False),
            (SewerDuctFields.field_diameter_type_id, QVariant.Int, False),
            (SewerDuctFields.field_diameter_id, QVariant.Int, False),
            (SewerDuctFields.field_form_code_id, QVariant.Int, False),
            (SewerDuctFields.field_pressure_class_id, QVariant.Int, False),
            (SewerDuctFields.field_firmness_class_id, QVariant.Int, False),
            (SewerDuctFields.field_begin_node_id, QVariant.Int, False),
            (SewerDuctFields.field_end_node_id, QVariant.Int, False),
            (SewerDuctFields.field_begin_z_coord, QVariant.Double, False),
            (SewerDuctFields.field_end_z_coord, QVariant.Double, False),
            (SewerDuctFields.field_location_id, QVariant.Int, False),
            (SewerDuctFields.field_flowdirection, QVariant.Double, False),
            (SewerDuctFields.field_condition_class_id, QVariant.Int, False),
            (SewerDuctFields.field_length_2d, QVariant.Double, False),
            (SewerDuctFields.field_length, QVariant.Double, False),
            (SewerDuctFields.field_inventory_nr, QVariant.String, 20),
            (SewerDuctFields.field_usage_permit_nr, QVariant.String, 20),
            (SewerDuctFields.field_usage_permit_date, QVariant.DateTime, False),
            (SewerDuctFields.field_usage_state, QVariant.Int, False),
            (SewerDuctFields.field_owner_id, QVariant.Int, False),
            (SewerDuctFields.field_lessee_id, QVariant.Int, False),
            (SewerDuctFields.field_note, QVariant.String, 1024),
            (SewerDuctFields.field_plan_id, QVariant.Int, False),
            (SewerDuctFields.field_build_year, QVariant.Int, False),
            (SewerDuctFields.field_removal_year, QVariant.Int, False),
            (SewerDuctFields.field_estimated_service_life, QVariant.Int, False),
            (SewerDuctFields.field_geom, QVariant.String, False),
            (SewerDuctFields.field_address_id, QVariant.Int, False),
            (SewerDuctFields.field_location_accuracy_id, QVariant.Int, False),
            (SewerDuctFields.field_height_accuracy_id, QVariant.Int, False),
            (SewerDuctFields.field_mapping_method_id, QVariant.Int, False),
            (SewerDuctFields.field_creator, QVariant.String, 30),
            (SewerDuctFields.field_creation_date, QVariant.DateTime, False),
            (SewerDuctFields.field_updated_by, QVariant.String, 30),
            (SewerDuctFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_SEWER_DUCT
        primary_key = ("PK_SN_SEWER_DUCT", [SewerDuctFields.field_mslk])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_DUCT
        foreign_keys = [
            ("FK_SN_SEWER_DUCT_CONDITION_CLASS_ID", SewerDuctFields.field_condition_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_FIRMNESS_CLASS_ID", SewerDuctFields.field_firmness_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_MATERIAL_ID", SewerDuctFields.field_material_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_OWNER_ID", SewerDuctFields.field_owner_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_MAPPING_METHOD_ID", SewerDuctFields.field_mapping_method_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_NETWORK_ID", SewerDuctFields.field_network_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_DIAMETER_TYPE_ID", SewerDuctFields.field_diameter_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_DIAMETER_ID", SewerDuctFields.field_diameter_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_PRESSURE_CLASS_ID", SewerDuctFields.field_pressure_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_HEIGHT_ACC_ID", SewerDuctFields.field_height_accuracy_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_DUCT_TYPE_ID", SewerDuctFields.field_duct_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_PLAN_ID", SewerDuctFields.field_plan_id, "evel.PLAN(ID)"),
            ("FK_SN_SEWER_DUCT_LOCATION_ID", SewerDuctFields.field_location_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_END_NODE_ID", SewerDuctFields.field_end_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SEWER_DUCT_BEGIN_NODE_ID", SewerDuctFields.field_begin_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SEWER_DUCT_LOC_ACC_ID", SewerDuctFields.field_location_accuracy_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_ADDRESS_ID", SewerDuctFields.field_address_id, "evel.APARTMENT_DATA(ID)"),
            ("FK_SN_SEWER_DUCT_LESSEE_ID", SewerDuctFields.field_lessee_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_FORM_CODE_ID", SewerDuctFields.field_form_code_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_USAGE_STATE", SewerDuctFields.field_usage_state, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_DUCT_NETTYPE_ID", SewerDuctFields.field_nettype_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
