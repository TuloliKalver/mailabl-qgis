from qgis.PyQt.QtCore import QVariant

#Liitumispunkt!
class DemarcationPointFields:
    # Define field names as variables
    field_id = "ID"
    field_network_id = "NETWORK_ID" #SN constant väärtused!!!
    field_consumer_point_id = "CONSUMER_POINT_ID"
    field_plan_id = "PLAN_ID" #kas see on siis faili ID!
    field_real_estate_nr = "REAL_ESTATE_NR"
    field_description = "DESCRIPTION"
    field_geom = "GEOM"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class DemarcationPointAliases:
    # Define aliases as variables in Estonian
    alias_id = "Primaarvõti"
    alias_network_id = "Võrgu ID"
    alias_consumer_point_id = "Tarbijapunkti ID"
    alias_plan_id = "Plaani ID" #Graafiline seos!???? loe dokumentatsioonist 
    alias_real_estate_nr = "Katastritunnus"
    alias_description = "Kirjeldus"
    alias_geom = "Geomeetria"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kuupäev"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kuupäev"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for DEMARCATION_POINT
        field_definitions = [
            (DemarcationPointFields.field_id, QVariant.Int, None),
            (DemarcationPointFields.field_network_id, QVariant.Int, None),
            (DemarcationPointFields.field_consumer_point_id, QVariant.Int, None),
            (DemarcationPointFields.field_plan_id, QVariant.Int, None),
            (DemarcationPointFields.field_real_estate_nr, QVariant.String, 14),
            (DemarcationPointFields.field_description, QVariant.String, 80),
            (DemarcationPointFields.field_geom, QVariant.String, None),  # Geometry type
            (DemarcationPointFields.field_creator, QVariant.String, 64),
            (DemarcationPointFields.field_creation_date, QVariant.DateTime, None),
            (DemarcationPointFields.field_updated_by, QVariant.String, 50),
            (DemarcationPointFields.field_update_date, QVariant.DateTime, None)
        ]
        return field_definitions
