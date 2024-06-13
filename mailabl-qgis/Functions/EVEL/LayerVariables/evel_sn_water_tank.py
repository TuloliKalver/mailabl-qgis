from qgis.PyQt.QtCore import QVariant

class SNWaterTankFields:
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_capacity = "CAPACITY"
    field_bottom_height = "BOTTOM_HEIGHT"
    field_water_lower_level = "WATER_LOWER_LEVEL"
    field_water_upper_level = "WATER_UPPER_LEVEL"
    field_parcel_nr = "PARCEL_NR"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNWaterTankAliases:
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_aqua_id = "Liik"
    alias_capacity = "Maht m3"
    alias_bottom_height = "Põhja kõrgus"
    alias_water_lower_level = "Minimaalne tase"
    alias_water_upper_level = "Maksimaalne tase"
    alias_parcel_nr = "Katastri tunnus"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class SNWaterTankFunctions:

    @staticmethod
    def sn_water_tank_fields():
        field_definitions = [
            (SNWaterTankFields.field_id, QVariant.Int, True),
            (SNWaterTankFields.field_node_id, QVariant.Int, False),
            (SNWaterTankFields.field_type_aqua_id, QVariant.Int, False),
            (SNWaterTankFields.field_capacity, QVariant.Double, False),
            (SNWaterTankFields.field_bottom_height, QVariant.Double, False),
            (SNWaterTankFields.field_water_lower_level, QVariant.Double, False),
            (SNWaterTankFields.field_water_upper_level, QVariant.Double, False),
            (SNWaterTankFields.field_parcel_nr, QVariant.String, 14),
            (SNWaterTankFields.field_creator, QVariant.String, 64),
            (SNWaterTankFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterTankFields.field_updated_by, QVariant.String, 64),
            (SNWaterTankFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNWaterTankKeyDefinitions:

    @staticmethod
    def primary_key():
        primary_key = ("PK_SN_WATER_TANK", [SNWaterTankFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        foreign_keys = [
            ("FK_SN_WATER_TANK_NODE_ID", SNWaterTankFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_WTANK_TYPE_AQUA_ID", SNWaterTankFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
