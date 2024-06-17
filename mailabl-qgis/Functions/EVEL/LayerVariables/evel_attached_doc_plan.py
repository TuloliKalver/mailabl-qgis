from qgis.PyQt.QtCore import QVariant

class AttachedDocPlanFields:
    # Define field names as variables
    field_id = "ID"
    field_doc_id = "DOC_ID"
    field_el_id = "EL_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"

class AttachedDocPlanAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_doc_id = "Viide ext_doc tabelisse"
    alias_el_id = "Viide plan tabelisse"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for ATTACHED_DOC_PLAN
        field_definitions = [
            (AttachedDocPlanFields.field_id, QVariant.Int, True),
            (AttachedDocPlanFields.field_doc_id, QVariant.Int, True),
            (AttachedDocPlanFields.field_el_id, QVariant.Int, True),
            (AttachedDocPlanFields.field_added_by, QVariant.String, 30),
            (AttachedDocPlanFields.field_added_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for ATTACHED_DOC_PLAN
        primary_key = ("PK_SN_ATT_DOC_PLAN", [AttachedDocPlanFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for ATTACHED_DOC_PLAN
        foreign_keys = [
            ("FK_SN_ATT_DOC_PLAN", AttachedDocPlanFields.field_doc_id, "evel.EXTERNAL_DOC(ID)"),
            ("FK_ATTACHED_DOC_PLAN_EL_ID", AttachedDocPlanFields.field_el_id, "evel.PLAN(ID)")
        ]
        return foreign_keys
