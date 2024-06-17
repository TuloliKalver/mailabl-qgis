from qgis.PyQt.QtCore import QVariant

class LandPermAreaFields:
    field_id = "ID"
    field_type_id = "TYPE_ID"
    field_plan_id = "PLAN_ID"
    field_state_id = "STATE_ID"
    field_real_estate_name = "REAL_ESTATE_NAME"
    field_real_estate_nr = "REAL_ESTATE_NR"
    field_description = "DESCRIPTION"
    field_contract_date = "CONTRACT_DATE"
    field_perimeter = "PERIMETER"
    field_area_size = "AREA_SIZE"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class LandPermAreaAliases:
    alias_id = "Primaarvõti"
    alias_type_id = "Tüüp"
    alias_plan_id = "Lepingu olek"
    alias_state_id = "Lepingu olek"
    alias_real_estate_name = "Lähiaadress"
    alias_real_estate_nr = "Katastritunnus"
    alias_description = "Kaetud tehnovõrgud"
    alias_contract_date = "Sõlmimise kp"
    alias_perimeter = "Ümbermõõt (m)"
    alias_area_size = "Geomeetria"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:

    @staticmethod
    def fields():
        field_definitions = [
            (LandPermAreaFields.field_id, QVariant.Int, True),
            (LandPermAreaFields.field_type_id, QVariant.Int, False),
            (LandPermAreaFields.field_plan_id, QVariant.Int, False),
            (LandPermAreaFields.field_state_id, QVariant.Int, False),
            (LandPermAreaFields.field_real_estate_name, QVariant.String, 100),
            (LandPermAreaFields.field_real_estate_nr, QVariant.String, 14),
            (LandPermAreaFields.field_description, QVariant.String, 50),
            (LandPermAreaFields.field_contract_date, QVariant.DateTime, False),
            (LandPermAreaFields.field_perimeter, QVariant.Int, False),
            (LandPermAreaFields.field_area_size, QVariant.Int, False),
            (LandPermAreaFields.field_creator, QVariant.String, 64),
            (LandPermAreaFields.field_creation_date, QVariant.DateTime, False),
            (LandPermAreaFields.field_updated_by, QVariant.String, 50),
            (LandPermAreaFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

    @staticmethod
    def primary_key():
        primary_key = ("PK_LAND_PERM_AREA_ID", [LandPermAreaFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        foreign_keys = [
            ("FK_LAND_PERM_AREA_STATE_ID", LandPermAreaFields.field_state_id, "evel.SN_CONSTANT(ID)"),
            ("FK_LAND_PERM_AREA_PLAN_ID", LandPermAreaFields.field_plan_id, "evel.PLAN(ID)"),
            ("FK_LAND_PERM_AREA_TYPE_ID", LandPermAreaFields.field_type_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys