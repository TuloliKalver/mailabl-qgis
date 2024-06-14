from qgis.PyQt.QtCore import QVariant

class AttachedDocSNWaterNodeFields:
    # Define field names as variables
    field_id = "ID"
    field_doc_id = "DOC_ID"
    field_el_id = "EL_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"

class AttachedDocSNWaterNodeAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_doc_id = "Viide ext_doc tabelisse"
    alias_el_id = "Viide water_node tabelisse"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"

class LayerFunctions:

    def fields():
        # Define the field definitions for ATTACHED_DOC_SN_WATER_NODE
        field_definitions = [
            (AttachedDocSNWaterNodeFields.field_id, QVariant.Int, True),
            (AttachedDocSNWaterNodeFields.field_doc_id, QVariant.Int, True),
            (AttachedDocSNWaterNodeFields.field_el_id, QVariant.Int, True),
            (AttachedDocSNWaterNodeFields.field_added_by, QVariant.String, 30),
            (AttachedDocSNWaterNodeFields.field_added_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for ATTACHED_DOC_SN_WATER_NODE
        primary_key = ("PK_SN_ATT_DOC_SN_WNODE", [AttachedDocSNWaterNodeFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for ATTACHED_DOC_SN_WATER_NODE
        foreign_keys = [
            ("FK_SN_ATT_DOC_SN_WNODE", AttachedDocSNWaterNodeFields.field_el_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_ATT_SN_WNODE_DOC", AttachedDocSNWaterNodeFields.field_doc_id, "evel.EXTERNAL_DOC(ID)")
        ]
        return foreign_keys
