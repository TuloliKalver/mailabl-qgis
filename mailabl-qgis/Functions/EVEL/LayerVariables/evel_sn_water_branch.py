from qgis.PyQt.QtCore import QVariant

class SNWaterBranchFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_type_id = "TYPE_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNWaterBranchAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_aqua_id = "Liik"
    alias_type_id = "Alamliik"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class SNWaterBranchFunctions:

    def sn_water_branch_fields():
        # Define the field definitions for SN_WATER_BRANCH
        field_definitions = [
            (SNWaterBranchFields.field_id, QVariant.Int, True),
            (SNWaterBranchFields.field_node_id, QVariant.Int, False),
            (SNWaterBranchFields.field_type_aqua_id, QVariant.Int, False),
            (SNWaterBranchFields.field_type_id, QVariant.Int, False),
            (SNWaterBranchFields.field_creator, QVariant.String, 64),
            (SNWaterBranchFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterBranchFields.field_updated_by, QVariant.String, 64),
            (SNWaterBranchFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNWaterBranchKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_WATER_BRANCH
        primary_key = ("PK_SN_WATER_BRANCH", [SNWaterBranchFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_WATER_BRANCH
        foreign_keys = [
            ("FK_SN_WATER_BRANCH_NODE_ID", SNWaterBranchFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_TYPE_ID", SNWaterBranchFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WBRANCH_TYPE_AQUA", SNWaterBranchFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
