from qgis.PyQt.QtCore import QVariant

class SNSewerValveStateLogFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_state = "STATE"
    field_state_info = "STATE_INFO"
    field_duration = "DURATION"
    field_changed_by = "CHANGED_BY"
    field_change_date = "CHANGE_DATE"

class SNSewerValveStateLogAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Sõlme id"
    alias_state = "Olek"
    alias_state_info = "Oleku info"
    alias_duration = "Kestus"
    alias_changed_by = "Muutja"
    alias_change_date = "Muutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for SN_SEWER_VALVE_STATE_LOG
        field_definitions = [
            (SNSewerValveStateLogFields.field_id, QVariant.Int, True),
            (SNSewerValveStateLogFields.field_node_id, QVariant.Int, False),
            (SNSewerValveStateLogFields.field_state, QVariant.Int, False),
            (SNSewerValveStateLogFields.field_state_info, QVariant.Int, False),
            (SNSewerValveStateLogFields.field_duration, QVariant.Double, 11, 2, False),
            (SNSewerValveStateLogFields.field_changed_by, QVariant.String, 50),
            (SNSewerValveStateLogFields.field_change_date, QVariant.DateTime, True)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for SN_SEWER_VALVE_STATE_LOG
        primary_key = ("PK_SN_SEWER_VALVE_STATE_LOG", [SNSewerValveStateLogFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_VALVE_STATE_LOG
        foreign_keys = [
            ("FK_SN_SEWER_VALVE_STATE_LOG_STATE_INFO", SNSewerValveStateLogFields.field_state_info, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_VALVE_STATE_LOG_NODE_ID", SNSewerValveStateLogFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SEWER_VALVE_STATE_LOG_STATE", SNSewerValveStateLogFields.field_state, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
