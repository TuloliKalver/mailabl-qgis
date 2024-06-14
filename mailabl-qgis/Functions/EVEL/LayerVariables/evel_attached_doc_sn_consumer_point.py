from qgis.PyQt.QtCore import QVariant

class AttachedDocSNConsumerPointFields:
    # Define field names as variables
    field_id = "ID"
    field_doc_id = "DOC_ID"
    field_el_id = "EL_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"

class AttachedDocSNConsumerPointAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_doc_id = "Viide ext_doc tabelisse"
    alias_el_id = "Viide water_duct tabelisse"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"

class LayerFunctions:

    def fields():
        # Define the field definitions for ATTACHED_DOC_SN_CONSUMER_POINT
        field_definitions = [
            (AttachedDocSNConsumerPointFields.field_id, QVariant.Int, True),
            (AttachedDocSNConsumerPointFields.field_doc_id, QVariant.Int, True),
            (AttachedDocSNConsumerPointFields.field_el_id, QVariant.Int, True),
            (AttachedDocSNConsumerPointFields.field_added_by, QVariant.String, 30),
            (AttachedDocSNConsumerPointFields.field_added_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for ATTACHED_DOC_SN_CONSUMER_POINT
        primary_key = ("PK_SN_ATT_DOC_SN_CONSUMER_POINT", [AttachedDocSNConsumerPointFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for ATTACHED_DOC_SN_CONSUMER_POINT
        foreign_keys = [
            ("FK_ATTACHED_DOC_SN_CONSUMER_POINT_EL_ID", AttachedDocSNConsumerPointFields.field_el_id, "evel.CONSUMER_POINT(ID)"),
            ("FK_ATTACHED_DOC_SN_CONSUMER_POINT_DOC_ID", AttachedDocSNConsumerPointFields.field_doc_id, "evel.EXTERNAL_DOC(ID)")
        ]
        return foreign_keys
