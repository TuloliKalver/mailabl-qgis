from qgis.PyQt.QtCore import QVariant

class SNWaterOtherNodeFields:
    # Defineeri välja nimed muutujatena
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_type_id = "TYPE_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNWaterOtherNodeAliases:
    # Defineeri aliasid muutujatena
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_aqua_id = "Liik"
    alias_type_id = "Alamliik"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class SNWaterOtherNodeFunctions:

    @staticmethod
    def sn_water_other_node_fields():
        # Defineeri välja määratlused SN_WATER_OTHER_NODE jaoks
        field_definitions = [
            (SNWaterOtherNodeFields.field_id, QVariant.Int, True),
            (SNWaterOtherNodeFields.field_node_id, QVariant.Int, False),
            (SNWaterOtherNodeFields.field_type_aqua_id, QVariant.Int, False),
            (SNWaterOtherNodeFields.field_type_id, QVariant.Int, False),
            (SNWaterOtherNodeFields.field_creator, QVariant.String, 64),
            (SNWaterOtherNodeFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterOtherNodeFields.field_updated_by, QVariant.String, 64),
            (SNWaterOtherNodeFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNWaterOtherNodeKeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti SN_WATER_OTHER_NODE jaoks
        primary_key = ("PK_SN_WOTHER_NODE", [SNWaterOtherNodeFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed SN_WATER_OTHER_NODE jaoks
        foreign_keys = [
            ("FK_SN_WOTHER_NODE_TYPE_AQUA", SNWaterOtherNodeFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WOTHER_NODE_TYPE_ID", SNWaterOtherNodeFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WOTHER_NODE_NODE_ID", SNWaterOtherNodeFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)")
        ]
        return foreign_keys
