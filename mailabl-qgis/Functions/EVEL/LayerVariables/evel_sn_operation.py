from qgis.PyQt.QtCore import QVariant

class SNOperationFields:
    # Define field names as variables
    field_mslinlk = "MSLINK"
    field_workgroup = "WORKGROUP"
    field_workno = "WORKNO"
    field_foreman = "FOREMAN"
    field_error_id = "ERROR_ID"
    field_operation_id = "OPERATION_ID"
    field_repair_cost = "REPAIR_COST"
    field_material_cost = "MATERIAL_COST"
    field_notes = "NOTES"
    field_begin_date = "BEGIN_DATE"
    field_end_date = "END_DATE"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"

class SNOperationAliases:
    # Define aliases as variables
    alias_mslinlk = "Primaarvõti"
    alias_workgroup = "Teostaja"
    alias_workno = "Töö number"
    alias_foreman = "Vastutaja"
    alias_error_id = "Seos veateatesse"
    alias_operation_id = "Tegevus"
    alias_repair_cost = "Tööde maksumus"
    alias_material_cost = "Materjali maksumus"
    alias_notes = "Märkused"
    alias_begin_date = "Töö alustamise aeg"
    alias_end_date = "Töö lõpetamise aeg"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"

class SNOperationFunctions:

    def sn_operation_fields():
        # Define the field definitions for SN_OPERATION
        field_definitions = [
            (SNOperationFields.field_mslinlk, QVariant.Int, True),
            (SNOperationFields.field_workgroup, QVariant.String, 100),
            (SNOperationFields.field_workno, QVariant.String, 20),
            (SNOperationFields.field_foreman, QVariant.String, 30),
            (SNOperationFields.field_error_id, QVariant.Int, False),
            (SNOperationFields.field_operation_id, QVariant.Int, False),
            (SNOperationFields.field_repair_cost, QVariant.Double, False),
            (SNOperationFields.field_material_cost, QVariant.Double, False),
            (SNOperationFields.field_notes, QVariant.String, 250),
            (SNOperationFields.field_begin_date, QVariant.DateTime, False),
            (SNOperationFields.field_end_date, QVariant.DateTime, False),
            (SNOperationFields.field_creator, QVariant.String, 64),
            (SNOperationFields.field_creation_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNOperationKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_OPERATION
        primary_key = ("PK_SN_OPERATION", [SNOperationFields.field_mslinlk])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_OPERATION
        foreign_keys = [
            ("FK_SN_OPERATION_SN_ERROR_REPORT", SNOperationFields.field_error_id, "evel.SN_ERROR_REPORT(MSLINK)"),
            ("FK_SN_OPERATION_OPERATION_ID", SNOperationFields.field_operation_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
