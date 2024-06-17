from qgis.PyQt.QtCore import QVariant

class SNWaterDuctProgramFields:
    # Defineeri välja nimed muutujatena
    field_id = "ID"
    field_duct_id = "DUCT_ID"
    field_program_id = "PROGRAM_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"
    field_last_time = "LAST_TIME"
    field_notes = "NOTES"
    field_signed_by = "SIGNED_BY"
    field_signed_date = "SIGNED_DATE"

class SNWaterDuctProgramAliases:
    # Defineeri aliasid muutujatena
    alias_id = "Primaarvõti"
    alias_duct_id = "Toru id"
    alias_program_id = "Programmi id"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"
    alias_last_time = "Viimase hoolduse kp"
    alias_notes = "Märkused"
    alias_signed_by = "Teostaja"
    alias_signed_date = "Teostamise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Defineeri välja määratlused SN_WATER_DUCT_PROGRAM jaoks
        field_definitions = [
            (SNWaterDuctProgramFields.field_id, QVariant.Int, True),
            (SNWaterDuctProgramFields.field_duct_id, QVariant.Int, True),
            (SNWaterDuctProgramFields.field_program_id, QVariant.Int, True),
            (SNWaterDuctProgramFields.field_added_by, QVariant.String, 30),
            (SNWaterDuctProgramFields.field_added_date, QVariant.DateTime, False),
            (SNWaterDuctProgramFields.field_last_time, QVariant.DateTime, False),
            (SNWaterDuctProgramFields.field_notes, QVariant.String, 250),
            (SNWaterDuctProgramFields.field_signed_by, QVariant.String, 30),
            (SNWaterDuctProgramFields.field_signed_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti SN_WATER_DUCT_PROGRAM jaoks
        primary_key = ("PK_SN_WATER_DUCT_PROGRAM", [SNWaterDuctProgramFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed SN_WATER_DUCT_PROGRAM jaoks
        foreign_keys = [
            ("FK_SN_WATER_DUCT_PROGRAM_DUCT_ID", SNWaterDuctProgramFields.field_duct_id, "evel.SN_WATER_DUCT(MSLINK)"),
            ("FK_SN_WATER_DUCT_PROG_PROG_ID", SNWaterDuctProgramFields.field_program_id, "evel.SN_PROGRAM(ID)")
        ]
        return foreign_keys
