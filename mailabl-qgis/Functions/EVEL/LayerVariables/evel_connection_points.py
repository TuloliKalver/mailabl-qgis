from qgis.PyQt.QtCore import QVariant

class ConsumerPointFields:
    # Define field names as variables
    field_id = "ID"
    field_cp_id = "CP_ID"
    field_customer_id = "CUSTOMER_ID"
    field_customer_role = "CUSTOMER_ROLE"

class ConsumerPointAliases:
    # Define aliases as variables
    alias_id = "Primary Key"
    alias_cp_id = "Consumer Point ID"
    alias_customer_id = "Customer ID"
    alias_customer_role = "Customer Role"

class ConnectionPointsLayerFunctions:

    def fields():
        # Define the field definitions for CUSTOMER_CONSUMERPOINT
        field_definitions = [
            (ConsumerPointFields.field_id, QVariant.Int, None),
            (ConsumerPointFields.field_cp_id, QVariant.Int, None),
            (ConsumerPointFields.field_customer_id, QVariant.Int, None),
            (ConsumerPointFields.field_customer_role, QVariant.Int, None)
        ]
        return field_definitions
