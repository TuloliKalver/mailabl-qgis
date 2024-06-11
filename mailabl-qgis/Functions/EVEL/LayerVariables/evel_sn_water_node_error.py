from qgis.PyQt.QtCore import QVariant

class SNWaterNodeErrorFields:
    # Defineeri välja nimed muutujatena
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_error_id = "ERROR_ID"

class SNWaterNodeErrorAliases:
    # Defineeri aliasid muutujatena
    alias_id = "Primaarvõti"
    alias_node_id = "Seos sõlmega"
    alias_error_id = "Seos veateatega"

class SNWaterNodeErrorFunctions:

    @staticmethod
    def sn_water_node_error_fields():
        # Defineeri välja määratlused SN_WATER_NODE_ERROR jaoks
        field_definitions = [
            (SNWaterNodeErrorFields.field_id, QVariant.Int, True),
            (SNWaterNodeErrorFields.field_node_id, QVariant.Int, True),
            (SNWaterNodeErrorFields.field_error_id, QVariant.Int, True)
        ]
        return field_definitions

class SNWaterNodeErrorKeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti SN_WATER_NODE_ERROR jaoks
        primary_key = ("PK_SN_WATER_NODE_ERROR", [SNWaterNodeErrorFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed SN_WATER_NODE_ERROR jaoks
        foreign_keys = [
            ("FK_SN_WATER_NODE_ERROR_NODE_ID", SNWaterNodeErrorFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_WATER_NODE_ERROR_ERROR_ID", SNWaterNodeErrorFields.field_error_id, "evel.SN_ERROR_REPORT(MSLINK)")
        ]
        return foreign_keys
