from qgis.PyQt.QtCore import QVariant

class CustomerFields:
    # Define field names as variables
    field_id = "ID"
    field_customer_number = "CUSTOMER_NUMBER"
    field_customer_name = "CUSTOMER_NAME"
    field_type_id = "TYPE_ID"
    field_state_id = "STATE_ID"
    field_address_id = "ADDRESS_ID"
    field_language = "LANGUAGE"
    field_vat_code = "VAT_CODE"
    field_phone = "PHONE"
    field_phone2 = "PHONE2"
    field_customer_email = "CUSTOMER_EMAIL"
    field_deleted = "DELETED"
    field_notes = "NOTES"
    field_invoicing_address_id = "INVOICING_ADDRESS_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"
    field_identification = "IDENTIFICATION"

class CustomerAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_customer_number = "Kliendi number"
    alias_customer_name = "Kliendi nimi"
    alias_type_id = "Kliendi tüüp"
    alias_state_id = "Kliendi olek"
    alias_address_id = "Kliendi aadress"
    alias_language = "Kliendi keel"
    alias_vat_code = "KMKR nr"
    alias_phone = "Telefon 1"
    alias_phone2 = "Telefon 2"
    alias_customer_email = "E-post"
    alias_deleted = "Kustutatud"
    alias_notes = "Märkused"
    alias_invoicing_address_id = "Arve aadress"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise aeg"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise aeg"
    alias_identification = "Isiku ärireg kood"

class LayerFunctions:

    def fields():
        # Define the field definitions for CUSTOMER
        field_definitions = [
            (CustomerFields.field_id, QVariant.Int, True),
            (CustomerFields.field_customer_number, QVariant.Int, False),
            (CustomerFields.field_customer_name, QVariant.String, 64),
            (CustomerFields.field_type_id, QVariant.Int, False),
            (CustomerFields.field_state_id, QVariant.Int, False),
            (CustomerFields.field_address_id, QVariant.Int, False),
            (CustomerFields.field_language, QVariant.String, 15),
            (CustomerFields.field_vat_code, QVariant.String, 64),
            (CustomerFields.field_phone, QVariant.String, 50),
            (CustomerFields.field_phone2, QVariant.String, 64),
            (CustomerFields.field_customer_email, QVariant.String, 128),
            (CustomerFields.field_deleted, QVariant.Bool, False),
            (CustomerFields.field_notes, QVariant.String, 256),
            (CustomerFields.field_invoicing_address_id, QVariant.Int, False),
            (CustomerFields.field_creator, QVariant.String, 64),
            (CustomerFields.field_creation_date, QVariant.DateTime, False),
            (CustomerFields.field_updated_by, QVariant.String, 64),
            (CustomerFields.field_update_date, QVariant.DateTime, False),
            (CustomerFields.field_identification, QVariant.String, 11)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for CUSTOMER
        primary_key = ("PK_CUSTOMER", [CustomerFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for CUSTOMER
        foreign_keys = [
            ("FK_CUSTOMER_APARTMENT_DATA_02", CustomerFields.field_invoicing_address_id, "evel.APARTMENT_DATA(ID)"),
            ("FK_CUSTOMER_STATE_ID", CustomerFields.field_state_id, "evel.SN_CONSTANT(ID)"),
            ("FK_CUSTOMER_TYPE_ID", CustomerFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_CUSTOMER_APARTMENT_DATA", CustomerFields.field_address_id, "evel.APARTMENT_DATA(ID)")
        ]
        return foreign_keys
