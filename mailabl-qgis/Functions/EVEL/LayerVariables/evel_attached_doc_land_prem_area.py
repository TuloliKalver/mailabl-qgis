from qgis.PyQt.QtCore import QVariant

class AttachedDocLandPremAreaFields:
    # Define field names as variables
    field_id = "ID"
    field_doc_id = "DOC_ID"
    field_el_id = "EL_ID"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"

class AttachedDocLandPremAreaAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_doc_id = "Viide ext_doc tabelisse"
    alias_el_id = "Viide water_duct tabelisse"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for ATTACHED_DOC_LAND_PREM_AREA
        field_definitions = [
            (AttachedDocLandPremAreaFields.field_id, QVariant.Int, True),
            (AttachedDocLandPremAreaFields.field_doc_id, QVariant.Int, True),
            (AttachedDocLandPremAreaFields.field_el_id, QVariant.Int, True),
            (AttachedDocLandPremAreaFields.field_added_by, QVariant.String, 30),
            (AttachedDocLandPremAreaFields.field_added_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for ATTACHED_DOC_LAND_PREM_AREA
        primary_key = ("PK_SN_ATT_DOC_LAND_PREM_AREA_ID", [AttachedDocLandPremAreaFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for ATTACHED_DOC_LAND_PREM_AREA
        foreign_keys = [
            ("FK_SN_ATT_DOC_LAND_PREM_AREA", AttachedDocLandPremAreaFields.field_doc_id, "evel.EXTERNAL_DOC(ID)"),
            ("FK_ATTACHED_DOC_EL_ID", AttachedDocLandPremAreaFields.field_el_id, "evel.LAND_PERM_AREA(ID)")
        ]
        return foreign_keys
