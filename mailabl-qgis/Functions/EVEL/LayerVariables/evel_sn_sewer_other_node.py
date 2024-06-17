from qgis.PyQt.QtCore import QVariant

class SNSewerOtherNodeFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_type_id = "TYPE_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNSewerOtherNodeAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_aqua_id = "Liik"
    alias_type_id = "Alamliik"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for SN_SEWER_OTHER_NODE
        field_definitions = [
            (SNSewerOtherNodeFields.field_id, QVariant.Int, True),
            (SNSewerOtherNodeFields.field_node_id, QVariant.Int, False),
            (SNSewerOtherNodeFields.field_type_aqua_id, QVariant.Int, False),
            (SNSewerOtherNodeFields.field_type_id, QVariant.Int, False),
            (SNSewerOtherNodeFields.field_creator, QVariant.String, 64),
            (SNSewerOtherNodeFields.field_creation_date, QVariant.DateTime, False),
            (SNSewerOtherNodeFields.field_updated_by, QVariant.String, 64),
            (SNSewerOtherNodeFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for SN_SEWER_OTHER_NODE
        primary_key = ("PK_SN_SOTHER_NODE", [SNSewerOtherNodeFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_OTHER_NODE
        foreign_keys = [
            ("FK_SN_SOTHER_NODE_TYPE_ID", SNSewerOtherNodeFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_OTHER_NODE_NODE_ID", SNSewerOtherNodeFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SOTHER_NODE_TYPE_AQUA", SNSewerOtherNodeFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
