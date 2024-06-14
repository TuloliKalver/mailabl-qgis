from qgis.PyQt.QtCore import QVariant

class SNSewerDuctErrorFields:
    # Define field names as variables
    field_id = "ID"
    field_duct_id = "DUCT_ID"
    field_error_id = "ERROR_ID"

class SNSewerDuctErrorAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_duct_id = "Seos toruga"
    alias_error_id = "Seos veateatega"

class LayerFunctions:

    def fields():
        # Define the field definitions for SN_SEWER_DUCT_ERROR
        field_definitions = [
            (SNSewerDuctErrorFields.field_id, QVariant.Int, True),
            (SNSewerDuctErrorFields.field_duct_id, QVariant.Int, False),
            (SNSewerDuctErrorFields.field_error_id, QVariant.Int, False)
        ]
        return field_definitions

class SNSewerDuctErrorKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_SEWER_DUCT_ERROR
        primary_key = ("PK_SN_SEWER_DUCT_ERROR", [SNSewerDuctErrorFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_DUCT_ERROR
        foreign_keys = [
            ("FK_SN_SEWER_DUCT_ERROR_ERROR_ID", SNSewerDuctErrorFields.field_error_id, "evel.SN_ERROR_REPORT(MSLINK)"),
            ("FK_SN_SEWER_DUCT_ERROR_DUCT_ID", SNSewerDuctErrorFields.field_duct_id, "evel.SN_SEWER_DUCT(MSLINK)")
        ]
        return foreign_keys
