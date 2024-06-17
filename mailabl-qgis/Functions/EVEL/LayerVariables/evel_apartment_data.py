from qgis.PyQt.QtCore import QVariant

class ApartmentDataFields:
    # Define field names as variables
    field_id = "ID"
    field_adr_id = "ADR_ID"

class ApartmentDataAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_adr_id = "Aadress id"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for APARTMENT_DATA
        field_definitions = [
            (ApartmentDataFields.field_id, QVariant.Int, True),
            (ApartmentDataFields.field_adr_id, QVariant.Int, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for APARTMENT_DATA
        primary_key = ("PK_ADDRESS_ID", [ApartmentDataFields.field_id])
        return primary_key
