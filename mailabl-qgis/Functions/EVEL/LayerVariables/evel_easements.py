from qgis.PyQt.QtCore import QVariant

class EasemensFields:
    # Define field names as variables
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
    field_geom = "GEOM"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class EasementAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_type_id = "Tüüp (LAND_PERM_TYPE)"
    alias_plan_id = "Lepingu olek (LAND_PERM_STATE) (Tegemisel, sõlmitud)"
    alias_state_id = "Lepingu olek (LAND_PERM_STATE) (Tegemisel, sõlmitud)"
    alias_real_estate_name = "Lähiaadress"
    alias_real_estate_nr = "Katastritunnus"
    alias_description = "Kaetud tehnovõrgud (Kirjeldus (Vesi, Kanal))"
    alias_contract_date = "Sõlmimise kp"
    alias_perimeter = "Ümbermõõt (m)"
    alias_area_size = "Pindala"
    alias_geom = "Geomeetria"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kpMuutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for EVEL easements
        field_definitions = [
                (EasemensFields.field_id, QVariant.Int, None),
                (EasemensFields.field_type_id, QVariant.Int, None),
                (EasemensFields.field_plan_id, QVariant.Int, None),
                (EasemensFields.field_state_id, QVariant.Int, None),
                (EasemensFields.field_real_estate_name, QVariant.String, 100),
                (EasemensFields.field_real_estate_nr, QVariant.String, 14),
                (EasemensFields.field_description, QVariant.String, 50),
                (EasemensFields.field_contract_date, QVariant.DateTime, None),
                (EasemensFields.field_perimeter, QVariant.Int, None),
                (EasemensFields.field_area_size, QVariant.Int, None),
                (EasemensFields.field_creator, QVariant.String, 64),
                (EasemensFields.field_creation_date, QVariant.DateTime, None),
                (EasemensFields.field_updated_by, QVariant.String, 50),
                (EasemensFields.field_update_date, QVariant.DateTime, None)
            ]
        return field_definitions