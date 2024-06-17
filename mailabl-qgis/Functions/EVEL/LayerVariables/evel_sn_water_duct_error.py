from qgis.PyQt.QtCore import QVariant

class SNWaterDuctErrorFields:
    # Define field names as variables
    field_id = "ID"
    field_duct_id = "DUCT_ID"
    field_error_id = "ERROR_ID"

class SNWaterDuctErrorAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_duct_id = "Seos toruga"
    alias_error_id = "Seos veateatega"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for SN_WATER_DUCT_ERROR
        field_definitions = [
            (SNWaterDuctErrorFields.field_id, QVariant.Int, True),
            (SNWaterDuctErrorFields.field_duct_id, QVariant.Int, True),
            (SNWaterDuctErrorFields.field_error_id, QVariant.Int, True)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for SN_WATER_DUCT_ERROR
        primary_key = ("PK_SN_WATER_DUCT_ERROR", [SNWaterDuctErrorFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Define the foreign keys for SN_WATER_DUCT_ERROR
        foreign_keys = [
            ("FK_SN_WATER_DUCT_ERROR_DUCT_ID", SNWaterDuctErrorFields.field_duct_id, "evel.SN_WATER_DUCT(MSLINK)"),
            ("FK_SN_WATER_DUCT_ERROR_ERROR_ID", SNWaterDuctErrorFields.field_error_id, "evel.SN_ERROR_REPORT(MSLINK)")
        ]
        return foreign_keys
