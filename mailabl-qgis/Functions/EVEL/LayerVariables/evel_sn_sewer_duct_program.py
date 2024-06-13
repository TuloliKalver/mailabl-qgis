from qgis.PyQt.QtCore import QVariant

class SNSewerDuctPrograFields:
    # Define field names as variables
    field_id = "ID"
    field_duct_id = "DUCT_ID"
    field_program_id = "PROGRAM_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"
    field_last_time = "LAST_TIME"
    field_notes = "NOTES"
    field_signed_by = "SIGNED_BY"
    field_signed_date = "SIGNED_DATE"

class SNSewerDuctPrograAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_duct_id = "Toru id"
    alias_program_id = "Programmi id"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"
    alias_last_time = "Viimase hoolduse kp"
    alias_notes = "Märkused"
    alias_signed_by = "Teostaja"
    alias_signed_date = "Teostamise kp"

class SNSewerDuctPrograFunctions:

    def sn_sewer_duct_progra_fields():
        # Define the field definitions for SN_SEWER_DUCT_PROGRA
        field_definitions = [
            (SNSewerDuctPrograFields.field_id, QVariant.Int, True),
            (SNSewerDuctPrograFields.field_duct_id, QVariant.Int, True),
            (SNSewerDuctPrograFields.field_program_id, QVariant.Int, True),
            (SNSewerDuctPrograFields.field_added_by, QVariant.String, 30),
            (SNSewerDuctPrograFields.field_added_date, QVariant.DateTime, False),
            (SNSewerDuctPrograFields.field_last_time, QVariant.DateTime, False),
            (SNSewerDuctPrograFields.field_notes, QVariant.String, 50),
            (SNSewerDuctPrograFields.field_signed_by, QVariant.String, 30),
            (SNSewerDuctPrograFields.field_signed_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNSewerDuctPrograKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_SEWER_DUCT_PROGRA
        primary_key = ("PK_SN_SEWER_DUCT_PROGRAM", [SNSewerDuctPrograFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_DUCT_PROGRA
        foreign_keys = [
            ("FK_SN_SEWER_DUCT_PROGRAM_DUCT_ID", SNSewerDuctPrograFields.field_duct_id, "evel.SN_SEWER_DUCT(MSLINK)"),
            ("FK_SN_SEWER_DUCT_PROG_PROG_ID", SNSewerDuctPrograFields.field_program_id, "evel.SN_PROGRAM(ID)")
        ]
        return foreign_keys
