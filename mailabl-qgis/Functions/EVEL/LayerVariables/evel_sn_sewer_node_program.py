from qgis.PyQt.QtCore import QVariant

class SNSewerNodeProgramFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_program_id = "PROGRAM_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"
    field_last_time = "LAST_TIME"
    field_notes = "NOTES"
    field_signed_by = "SIGNED_BY"
    field_signed_date = "SIGNED_DATE"

class SNSewerNodeProgramAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Sõlme id"
    alias_program_id = "Programmi id"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"
    alias_last_time = "Viimase hoolduse kp"
    alias_notes = "Märkused"
    alias_signed_by = "Teostaja"
    alias_signed_date = "Teostamise kp"

class SNSewerNodeProgramFunctions:

    def sn_sewer_node_program_fields():
        # Define the field definitions for SN_SEWER_NODE_PROGRAM
        field_definitions = [
            (SNSewerNodeProgramFields.field_id, QVariant.Int, True),
            (SNSewerNodeProgramFields.field_node_id, QVariant.Int, True),
            (SNSewerNodeProgramFields.field_program_id, QVariant.Int, True),
            (SNSewerNodeProgramFields.field_added_by, QVariant.String, 30),
            (SNSewerNodeProgramFields.field_added_date, QVariant.DateTime, False),
            (SNSewerNodeProgramFields.field_last_time, QVariant.DateTime, False),
            (SNSewerNodeProgramFields.field_notes, QVariant.String, 250),
            (SNSewerNodeProgramFields.field_signed_by, QVariant.String, 30),
            (SNSewerNodeProgramFields.field_signed_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNSewerNodeProgramKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_SEWER_NODE_PROGRAM
        primary_key = ("PK_SN_SEWER_NODE_PROGRAM", [SNSewerNodeProgramFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_NODE_PROGRAM
        foreign_keys = [
            ("FK_SN_SEWER_NODE_PROGRAM_NODE_ID", SNSewerNodeProgramFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SEWER_NODE_PROG_PROG_ID", SNSewerNodeProgramFields.field_program_id, "evel.SN_PROGRAM(ID)")
        ]
        return foreign_keys
