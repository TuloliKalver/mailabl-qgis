from qgis.PyQt.QtCore import QVariant

class SNWaterValveFields:
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_type_id = "TYPE_ID"
    field_manufacturer = "MANUFACTURER"
    field_valve_hand = "VALVE_HAND"
    field_diameter = "DIAMETER"
    field_diameter2 = "DIAMETER2"
    field_condition_class_id = "CONDITION_CLASS_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNWaterValveAliases:
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_aqua_id = "Liik"
    alias_type_id = "Alamliik"
    alias_manufacturer = "Tootja"
    alias_valve_hand = "Käelisus"
    alias_diameter = "Diameeter 1"
    alias_diameter2 = "Diameeter 2"
    alias_condition_class_id = "Seisukord"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Uuendaja"
    alias_update_date = "Uuendamise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        field_definitions = [
            (SNWaterValveFields.field_id, QVariant.Int, True),
            (SNWaterValveFields.field_node_id, QVariant.Int, False),
            (SNWaterValveFields.field_type_aqua_id, QVariant.Int, False),
            (SNWaterValveFields.field_type_id, QVariant.Int, False),
            (SNWaterValveFields.field_manufacturer, QVariant.String, 50),
            (SNWaterValveFields.field_valve_hand, QVariant.Int, False),
            (SNWaterValveFields.field_diameter, QVariant.Double, False),
            (SNWaterValveFields.field_diameter2, QVariant.Double, False),
            (SNWaterValveFields.field_condition_class_id, QVariant.Int, False),
            (SNWaterValveFields.field_creator, QVariant.String, 64),
            (SNWaterValveFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterValveFields.field_updated_by, QVariant.String, 64),
            (SNWaterValveFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        primary_key = ("PK_SN_WATER_VALVE", [SNWaterValveFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        foreign_keys = [
            ("FK_SN_WATER_VALVE_NODE_ID", SNWaterValveFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_WVTYPEID", SNWaterValveFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_VALVE_CONDITION_CLASS_ID", SNWaterValveFields.field_condition_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WVALVE_TYPE_AQUA", SNWaterValveFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)"),
            ("FK_WATER_VALVE_HAND", SNWaterValveFields.field_valve_hand, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
