# Seosetabel veateate ja dokumentide vahel

from qgis.PyQt.QtCore import QVariant

class AttachedDocSNErrorReportFields:
    # Define field names as variables
    field_id = "ID"
    field_doc_id = "DOC_ID"
    field_el_id = "EL_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"

class AttachedDocSNErrorReportAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_doc_id = "Viide ext_doc tabelisse"
    alias_el_id = "Viide error_report tabelisse"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"

class LayerFunctions:

    def fields():
        # Define the field definitions for ATTACHED_DOC_SN_ERROR_REPORT
        field_definitions = [
            (AttachedDocSNErrorReportFields.field_id, QVariant.Int, True),
            (AttachedDocSNErrorReportFields.field_doc_id, QVariant.Int, True),
            (AttachedDocSNErrorReportFields.field_el_id, QVariant.Int, True),
            (AttachedDocSNErrorReportFields.field_added_by, QVariant.String, 30),
            (AttachedDocSNErrorReportFields.field_added_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for ATTACHED_DOC_SN_ERROR_REPORT
        primary_key = ("PK_SN_ATT_DOC__ERROR_REPORT", [AttachedDocSNErrorReportFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for ATTACHED_DOC_SN_ERROR_REPORT
        foreign_keys = [
            ("FK_SN_ATT_SN_ERROR_REPORT", AttachedDocSNErrorReportFields.field_doc_id, "evel.EXTERNAL_DOC(ID)"),
            ("FK_ATTACHED_DOC_SN_ERROR_REPORT_EL_ID", AttachedDocSNErrorReportFields.field_el_id, "evel.SN_ERROR_REPORT(MSLINK)")
        ]
        return foreign_keys
