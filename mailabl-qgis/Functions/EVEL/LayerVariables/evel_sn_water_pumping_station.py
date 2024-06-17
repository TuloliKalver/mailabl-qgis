from qgis.PyQt.QtCore import QVariant

class SNWaterPumpingStationFields:
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_material_id = "MATERIAL_ID"
    field_role_id = "ROLE_ID"
    field_productivity = "PRODUCTIVITY"
    field_pressure_increase = "PRESSURE_INCREASE"
    field_p_reg_code = "P_REG_CODE"
    field_p_pasport_nr = "P_PASPORT_NR"
    field_p_depth = "P_DEPTH"
    field_water_type_id = "WATER_TYPE_ID"
    field_water_source_id = "WATER_SOURCE_ID"
    field_wipeout_date = "WIPEOUT_DATE"
    field_renewal_date = "RENEWAL_DATE"
    field_is_controlled = "IS_CONTROLLED"
    field_is_signalisation = "IS_SIGNALISATION"
    field_protection_zone = "PROTECTION_ZONE"
    field_mantle_diam = "MANTLE_DIAM"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNWaterPumpingStationAliases:
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_material_id = "Materjal"
    alias_role_id = "Roll"
    alias_productivity = "Tootlikkus (l/s)"
    alias_pressure_increase = "Surve tõus (atm)"
    alias_p_reg_code = "Registri kood"
    alias_p_pasport_nr = "Passi number"
    alias_p_depth = "Puurkaevu sügavus (m)"
    alias_water_type_id = "Veeliik"
    alias_water_source_id = "Veeallikas"
    alias_wipeout_date = "Likvideerimise aasta"
    alias_renewal_date = "Renoveerimise aasta"
    alias_is_controlled = "Kaugjuhitav?"
    alias_is_signalisation = "Signalisatsiooni olemasolu"
    alias_protection_zone = "Sanitaarkaitse ulatus (m)"
    alias_mantle_diam = "Mantli diameeter (mm)"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        field_definitions = [
            (SNWaterPumpingStationFields.field_id, QVariant.Int, True),
            (SNWaterPumpingStationFields.field_node_id, QVariant.Int, False),
            (SNWaterPumpingStationFields.field_material_id, QVariant.Int, False),
            (SNWaterPumpingStationFields.field_role_id, QVariant.Int, False),
            (SNWaterPumpingStationFields.field_productivity, QVariant.Double, False),
            (SNWaterPumpingStationFields.field_pressure_increase, QVariant.Double, False),
            (SNWaterPumpingStationFields.field_p_reg_code, QVariant.String, 20),
            (SNWaterPumpingStationFields.field_p_pasport_nr, QVariant.String, 50),
            (SNWaterPumpingStationFields.field_p_depth, QVariant.Double, False),
            (SNWaterPumpingStationFields.field_water_type_id, QVariant.Int, False),
            (SNWaterPumpingStationFields.field_water_source_id, QVariant.Int, False),
            (SNWaterPumpingStationFields.field_wipeout_date, QVariant.DateTime, False),
            (SNWaterPumpingStationFields.field_renewal_date, QVariant.DateTime, False),
            (SNWaterPumpingStationFields.field_is_controlled, QVariant.Bool, False),
            (SNWaterPumpingStationFields.field_is_signalisation, QVariant.Bool, False),
            (SNWaterPumpingStationFields.field_protection_zone, QVariant.Double, False),
            (SNWaterPumpingStationFields.field_mantle_diam, QVariant.Double, False),
            (SNWaterPumpingStationFields.field_creator, QVariant.String, 64),
            (SNWaterPumpingStationFields.field_creation_date, QVariant.DateTime, False),
            (SNWaterPumpingStationFields.field_updated_by, QVariant.String, 64),
            (SNWaterPumpingStationFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        primary_key = ("PK_SN_WATER_PSTATION_ID", [SNWaterPumpingStationFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        foreign_keys = [
            ("FK_SN_W_PUMPING_STATION_NODE_ID", SNWaterPumpingStationFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_WPUMPING_STATION_MATERIAL_ID", SNWaterPumpingStationFields.field_material_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WPUMPING_STATION_ROLE_ID", SNWaterPumpingStationFields.field_role_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WPUMPING_STATION_WATER_TYPE_ID", SNWaterPumpingStationFields.field_water_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_WPUMPING_STATION_WATER_SOURCE_ID", SNWaterPumpingStationFields.field_water_source_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
