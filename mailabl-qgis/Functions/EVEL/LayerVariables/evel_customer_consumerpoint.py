from qgis.PyQt.QtCore import QVariant

class CustomerConsumerPointFields:
    # Define field names as variables
    field_id = "ID"
    field_cp_id = "CP_ID"
    field_customer_id = "CUSTOMER_ID"
    field_customer_role = "CUSTOMER_ROLE"

class CustomerConsumerPointAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_cp_id = "Seos tarbimispunktiga"
    alias_customer_id = "Seos kliendiga"
    alias_customer_role = "Kliendi ja tarbimispunkti suhe"

class LayerFunctions:

    def fields():
        # Define the field definitions for CUSTOMER_CONSUMERPOINT
        field_definitions = [
            (CustomerConsumerPointFields.field_id, QVariant.Int, True),
            (CustomerConsumerPointFields.field_cp_id, QVariant.Int, True),
            (CustomerConsumerPointFields.field_customer_id, QVariant.Int, True),
            (CustomerConsumerPointFields.field_customer_role, QVariant.Int, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for CUSTOMER_CONSUMERPOINT
        primary_key = ("PK_CUSTOMER_CONSUMERPOINT_ID", [CustomerConsumerPointFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for CUSTOMER_CONSUMERPOINT
        foreign_keys = [
            ("FK_C_CP_CP_ID", CustomerConsumerPointFields.field_cp_id, "evel.CONSUMER_POINT(ID)"),
            ("FK_CUSTOMER_CONSUMERPOINT_CUSTOMER_ID", CustomerConsumerPointFields.field_customer_id, "evel.CUSTOMER(ID)"),
            ("FK_CUSTOMER_CONSUMERPOINT_CUSTOMER_ROLE", CustomerConsumerPointFields.field_customer_role, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
