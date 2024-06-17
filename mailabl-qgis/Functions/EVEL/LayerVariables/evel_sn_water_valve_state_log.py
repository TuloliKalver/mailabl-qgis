from qgis.PyQt.QtCore import QVariant

class SNWaterValveStateLogFields:
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_state = "STATE"
    field_duration = "DURATION"
    field_state_info = "STATE_INFO"
    field_changed_by = "CHANGED_BY"
    field_change_date = "CHANGE_DATE"

class SNWaterValveStateLogAliases:
    alias_id = "Primaarvõti"
    alias_node_id = "Sõlme id"
    alias_state = "Olek"
    alias_duration = "Kestus"
    alias_state_info = "Oleku info"
    alias_changed_by = "Muutja"
    alias_change_date = "Muutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        field_definitions = [
            (SNWaterValveStateLogFields.field_id, QVariant.Int, True),
            (SNWaterValveStateLogFields.field_node_id, QVariant.Int, False),
            (SNWaterValveStateLogFields.field_state, QVariant.Int, False),
            (SNWaterValveStateLogFields.field_duration, QVariant.Double, False),
            (SNWaterValveStateLogFields.field_state_info, QVariant.Int, False),
            (SNWaterValveStateLogFields.field_changed_by, QVariant.String, 50),
            (SNWaterValveStateLogFields.field_change_date, QVariant.DateTime, True)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        primary_key = ("PK_SN_WATER_VALVE_STATE_LOG", [SNWaterValveStateLogFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        foreign_keys = [
            ("FK_SN_WATER_VALVE_STATE_LOG_ST", SNWaterValveStateLogFields.field_state, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WAT_VAL_LOG_STATE_INFO", SNWaterValveStateLogFields.field_state_info, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_VALVE_LOG_NODE_ID", SNWaterValveStateLogFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)")
        ]
        return foreign_keys
