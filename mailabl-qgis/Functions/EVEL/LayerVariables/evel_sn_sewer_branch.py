from qgis.PyQt.QtCore import QVariant

class SNSewerBranchFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_type_id = "TYPE_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNSewerBranchAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Viide sõlmele"
    alias_type_aqua_id = "Liik (SW_BRANCH_TYPE)"
    alias_type_id = "Alamliik (SW_BRANCH_TYPE_SUB)"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for SN_SEWER_BRANCH
        field_definitions = [
            (SNSewerBranchFields.field_id, QVariant.Int, True),
            (SNSewerBranchFields.field_node_id, QVariant.Int, False),
            (SNSewerBranchFields.field_type_aqua_id, QVariant.Int, False),
            (SNSewerBranchFields.field_type_id, QVariant.Int, False),
            (SNSewerBranchFields.field_creator, QVariant.String, 64),
            (SNSewerBranchFields.field_creation_date, QVariant.DateTime, False),
            (SNSewerBranchFields.field_updated_by, QVariant.String, 64),
            (SNSewerBranchFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for SN_SEWER_BRANCH
        primary_key = ("PK_SN_SEWER_BRANCH", [SNSewerBranchFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_BRANCH
        foreign_keys = [
            ("FK_SN_SEWER_BRANCH_TYPE_AQUA_ID", SNSewerBranchFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_BRANCH_TYPE_ID", SNSewerBranchFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_BRANCH_NODE_ID", SNSewerBranchFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)")
        ]
        return foreign_keys
