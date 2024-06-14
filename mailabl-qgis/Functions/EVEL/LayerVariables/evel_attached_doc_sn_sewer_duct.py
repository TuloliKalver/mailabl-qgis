# Seosetabel kanalisatsioonitorude ja dokumentide vahel

from qgis.PyQt.QtCore import QVariant

class AttachedDocSNSewerDuctFields:
    # Define field names as variables
    field_id = "ID"
    field_doc_id = "DOC_ID"
    field_el_id = "EL_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"

class AttachedDocSNSewerDuctAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_doc_id = "Viide ext_doc tabelisse"
    alias_el_id = "Viide sewer_duct tabelisse"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"

class LayerFunctions:

    def fields():
        # Define the field definitions for ATTACHED_DOC_SN_SEWER_DUCT
        field_definitions = [
            (AttachedDocSNSewerDuctFields.field_id, QVariant.Int, True),
            (AttachedDocSNSewerDuctFields.field_doc_id, QVariant.Int, True),
            (AttachedDocSNSewerDuctFields.field_el_id, QVariant.Int, True),
            (AttachedDocSNSewerDuctFields.field_added_by, QVariant.String, 30),
            (AttachedDocSNSewerDuctFields.field_added_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for ATTACHED_DOC_SN_SEWER_DUCT
        primary_key = ("PK_SN_ATT_DOC_SN_SEWER_DUCT", [AttachedDocSNSewerDuctFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for ATTACHED_DOC_SN_SEWER_DUCT
        foreign_keys = [
            ("FK_SN_ATT_SN_SEWER_DUCT", AttachedDocSNSewerDuctFields.field_doc_id, "evel.EXTERNAL_DOC(ID)"),
            ("FK_ATTACHED_DOC_SN_SEWER_DUCT_EL_ID", AttachedDocSNSewerDuctFields.field_el_id, "evel.SN_SEWER_DUCT(MSLINK)")
        ]
        return foreign_keys
