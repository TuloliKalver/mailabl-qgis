from qgis.PyQt.QtCore import QVariant

class SNSewerValveFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_type_id = "TYPE_ID"
    field_manufacturer = "MANUFACTURER"
    field_valve_hand = "VALVE_HAND"
    field_diameter = "DIAMETER"
    field_condition_class_id = "CONDITION_CLASS_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNSewerValveAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_aqua_id = "Liik"
    alias_type_id = "Alamliik"
    alias_manufacturer = "Tootja"
    alias_valve_hand = "Käelisus"
    alias_diameter = "Diameeter"
    alias_condition_class_id = "Seisukord"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for SN_SEWER_VALVE
        field_definitions = [
            (SNSewerValveFields.field_id, QVariant.Int, True),
            (SNSewerValveFields.field_node_id, QVariant.Int, False),
            (SNSewerValveFields.field_type_aqua_id, QVariant.Int, False),
            (SNSewerValveFields.field_type_id, QVariant.Int, False),
            (SNSewerValveFields.field_manufacturer, QVariant.String, 50),
            (SNSewerValveFields.field_valve_hand, QVariant.Int, False),
            (SNSewerValveFields.field_diameter, QVariant.Double, 6),
            (SNSewerValveFields.field_condition_class_id, QVariant.Int, False),
            (SNSewerValveFields.field_creator, QVariant.String, 64),
            (SNSewerValveFields.field_creation_date, QVariant.DateTime, False),
            (SNSewerValveFields.field_updated_by, QVariant.String, 64),
            (SNSewerValveFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for SN_SEWER_VALVE
        primary_key = ("PK_SN_SEWER_VALVE", [SNSewerValveFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_VALVE
        foreign_keys = [
            ("FK_SN_SEWER_VALVE_VALVE_HAND", SNSewerValveFields.field_valve_hand, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_VALVE_CONDITION_CLASS_ID", SNSewerValveFields.field_condition_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_VALVE_TYPE_ID", SNSewerValveFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_VALVE_TYPE_AQUA_ID", SNSewerValveFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_VALVE_NODE_ID", SNSewerValveFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)")
        ]
        return foreign_keys
