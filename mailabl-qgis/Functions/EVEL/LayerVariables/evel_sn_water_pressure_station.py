from qgis.PyQt.QtCore import QVariant

class SNWaterPressureStationFields:
    # Defineeri välja nimed muutujatena
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_type_id = "TYPE_ID"
    field_pressure_increase = "PRESSURE_INCREASE"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"
    field_hydrophore = "HYDROPHORE"
    field_hydrophore_capacity = "HYDROPHORE_CAPACITY"

class SNWaterPressureStationAliases:
    # Defineeri aliasid muutujatena
    alias_id = "Identifikaator"
    alias_node_id = "Viide sõlmele"
    alias_type_aqua_id = "Liik"
    alias_type_id = "Alamliik"
    alias_pressure_increase = "Surve muutus (bar)"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"
    alias_hydrophore = "Hüdrofoori olemasolu"
    alias_hydrophore_capacity = "Hüdrofoori maht (m3)"

class SNWaterPressureStationFunctions:

    @staticmethod
    def sn_water_pressure_station_fields():
        # Defineeri välja määratlused SN_WATER_PRESSURE_STATION jaoks
        field_definitions = [
            (SNWaterPressureStationFields.field_id, QVariant.Int, True),
            (SNWaterPressureStationFields.field_node_id, QVariant.Int, False),
            (SNWaterPressureStationFields.field_type_aqua_id, QVariant.Int, False),
            (SNWaterPressureStationFields.field_type_id, QVariant.Int, False),
            (SNWaterPressureStationFields.field_pressure_increase, QVariant.Int, False),
            (SNWaterPressureStationFields.field_creator, QVariant.String, 64),
            (SNWaterPressureStationFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterPressureStationFields.field_updated_by, QVariant.String, 64),
            (SNWaterPressureStationFields.field_update_date, QVariant.DateTime, False),
            (SNWaterPressureStationFields.field_hydrophore, QVariant.Double, False),
            (SNWaterPressureStationFields.field_hydrophore_capacity, QVariant.Double, False)
        ]
        return field_definitions

class SNWaterPressureStationKeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti SN_WATER_PRESSURE_STATION jaoks
        primary_key = ("PK_SN_PRESSURE_STATION", [SNWaterPressureStationFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed SN_WATER_PRESSURE_STATION jaoks
        foreign_keys = [
            ("FK_SN_PRES_STATION_NODE_ID", SNWaterPressureStationFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_PRESSURE_STATION_TYPE_ID", SNWaterPressureStationFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WATER_PRESSURE_STATION_TYPE_AQUA_ID", SNWaterPressureStationFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
