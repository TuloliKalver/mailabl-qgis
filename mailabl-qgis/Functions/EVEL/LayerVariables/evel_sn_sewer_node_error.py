from qgis.PyQt.QtCore import QVariant

class SNSewerNodeErrorFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_error_id = "ERROR_ID"

class SNSewerNodeErrorAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Seos sõlmega"
    alias_error_id = "Seos veateatega"

class SNSewerNodeErrorFunctions:

    def sn_sewer_node_error_fields():
        # Define the field definitions for SN_SEWER_NODE_ERROR
        field_definitions = [
            (SNSewerNodeErrorFields.field_id, QVariant.Int, True),
            (SNSewerNodeErrorFields.field_node_id, QVariant.Int, True),
            (SNSewerNodeErrorFields.field_error_id, QVariant.Int, True)
        ]
        return field_definitions

class SNSewerNodeErrorKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_SEWER_NODE_ERROR
        primary_key = ("PK_SN_SEWER_NODE_ERROR", [SNSewerNodeErrorFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_NODE_ERROR
        foreign_keys = [
            ("FK_SN_SEWER_NODE_ERROR_NODE_ID", SNSewerNodeErrorFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SEWER_NODE_ERROR_ERROR_ID", SNSewerNodeErrorFields.field_error_id, "evel.SN_ERROR_REPORT(MSLINK)")
        ]
        return foreign_keys
