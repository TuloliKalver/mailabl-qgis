from qgis.PyQt.QtCore import QVariant

class SNSewerPumpingStationFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_material_id = "MATERIAL_ID"
    field_role_id = "ROLE_ID"
    field_name = "NAME"
    field_productivity = "PRODUCTIVITY"
    field_pressure_increase = "PRESSURE_INCREASE"
    field_power_consumption = "POWER_CONSUMPTION"
    field_el_max_current = "EL_MAX_CURRENT"
    field_control_id = "CONTROL_ID"
    field_parcel_nr = "PARCEL_NR"
    field_address_id = "ADDRESS_ID"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNSewerPumpingStationAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Seos sõlmega"
    alias_type_aqua_id = "Tüüp"
    alias_material_id = "Materjal"
    alias_role_id = "Roll"
    alias_name = "Tähis/Nimi"
    alias_productivity = "Maksimaalne tootlikkus Q (l/s)"
    alias_pressure_increase = "Surve muutus (bar)"
    alias_power_consumption = "Pumpla tarbitav elektrikoguvõimsus (kW)"
    alias_el_max_current = "Pumpla peakaitse läbilaskevõime (A)"
    alias_control_id = "Juhitavus"
    alias_parcel_nr = "Katastri tunnus"
    alias_address_id = "Seos aadressiga"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class SNSewerPumpingStationFunctions:

    def sn_sewer_pumping_station_fields():
        # Define the field definitions for SN_SEWER_PUMPING_STATION
        field_definitions = [
            (SNSewerPumpingStationFields.field_id, QVariant.Int, True),
            (SNSewerPumpingStationFields.field_node_id, QVariant.Int, False),
            (SNSewerPumpingStationFields.field_type_aqua_id, QVariant.Int, False),
            (SNSewerPumpingStationFields.field_material_id, QVariant.Int, False),
            (SNSewerPumpingStationFields.field_role_id, QVariant.Int, False),
            (SNSewerPumpingStationFields.field_name, QVariant.String, 50),
            (SNSewerPumpingStationFields.field_productivity, QVariant.Double, 6),
            (SNSewerPumpingStationFields.field_pressure_increase, QVariant.Int, False),
            (SNSewerPumpingStationFields.field_power_consumption, QVariant.Double, 10, 2),
            (SNSewerPumpingStationFields.field_el_max_current, QVariant.Double, 10, 2),
            (SNSewerPumpingStationFields.field_control_id, QVariant.Int, False),
            (SNSewerPumpingStationFields.field_parcel_nr, QVariant.String, 14),
            (SNSewerPumpingStationFields.field_address_id, QVariant.Int, False),
            (SNSewerPumpingStationFields.field_creator, QVariant.String, 64),
            (SNSewerPumpingStationFields.field_creation_date, QVariant.DateTime, False),
            (SNSewerPumpingStationFields.field_updated_by, QVariant.String, 64),
            (SNSewerPumpingStationFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNSewerPumpingStationKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_SEWER_PUMPING_STATION
        primary_key = ("PK_SN_PUMPING_STATION", [SNSewerPumpingStationFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_PUMPING_STATION
        foreign_keys = [
            ("FK_SN_SEWER_PUMPING_STATION_ADDRESS_ID", SNSewerPumpingStationFields.field_address_id, "evel.APARTMENT_DATA(ID)"),
            ("FK_SN_SEWER_PUMPING_STATION_ROLE_ID", SNSewerPumpingStationFields.field_role_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_PUMPING_STATION_TYPE_AQUA_ID", SNSewerPumpingStationFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_PUMPING_STATION_NODE_ID", SNSewerPumpingStationFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SEWER_PUMPING_STATION_CONTROL_ID", SNSewerPumpingStationFields.field_control_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_PUMPING_STATION_TYPE_ID", SNSewerPumpingStationFields.field_material_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
