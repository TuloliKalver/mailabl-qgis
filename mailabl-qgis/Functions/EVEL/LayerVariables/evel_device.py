from qgis.PyQt.QtCore import QVariant

class DeviceFields:
    # Define field names as variables
    field_id = "ID"
    field_identification = "IDENTIFICATION"
    field_type_id = "TYPE_ID"
    field_network_id = "NETWORK_ID"
    field_manhole_id = "MANHOLE_ID"
    field_sw_pumping_station_id = "SW_PUMPING_STATION_ID"
    field_productivity = "PRODUCTIVITY"
    field_unit = "UNIT"
    field_manufacturer = "MANUFACTURER"
    field_mark = "MARK"
    field_install_date = "INSTALL_DATE"
    field_power_w = "POWER_W"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class DeviceAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_identification = "Seadme tähis/nr"
    alias_type_id = "Seadme liik"
    alias_network_id = "Võrk"
    alias_manhole_id = "Seos mõõtekaevuga"
    alias_sw_pumping_station_id = "Seos reoveepumplaga"
    alias_productivity = "Tootlikkus"
    alias_unit = "Tootlikkuse Mõõtühik"
    alias_manufacturer = "Tootja"
    alias_mark = "Seadme mark"
    alias_install_date = "Paigalduse kp"
    alias_power_w = "Seadme võimsus (W)"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:

    def device_fields():
        # Define the field definitions for DEVICE
        field_definitions = [
            (DeviceFields.field_id, QVariant.Int, True),
            (DeviceFields.field_identification, QVariant.String, 20),
            (DeviceFields.field_type_id, QVariant.Int, False),
            (DeviceFields.field_network_id, QVariant.Int, False),
            (DeviceFields.field_manhole_id, QVariant.Int, False),
            (DeviceFields.field_sw_pumping_station_id, QVariant.Int, False),
            (DeviceFields.field_productivity, QVariant.Double, False),
            (DeviceFields.field_unit, QVariant.String, 10),
            (DeviceFields.field_manufacturer, QVariant.String, 50),
            (DeviceFields.field_mark, QVariant.String, 50),
            (DeviceFields.field_install_date, QVariant.DateTime, False),
            (DeviceFields.field_power_w, QVariant.Double, False),
            (DeviceFields.field_creator, QVariant.String, 30),
            (DeviceFields.field_creation_date, QVariant.DateTime, False),
            (DeviceFields.field_updated_by, QVariant.String, 30),
            (DeviceFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for DEVICE
        primary_key = ("PK_DEVICE", [DeviceFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for DEVICE
        foreign_keys = [
            ("FK_DEVICE_TYPE_ID", DeviceFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_DEVICE_MANHOLE_ID", DeviceFields.field_manhole_id, "evel.SN_WATER_MANHOLE(ID)"),
            ("FK_DEVICE_NETWORK_ID", DeviceFields.field_network_id, "evel.SN_CONSTANT(ID)"),
            ("FK_DEVICE_SW_PUMPING_STATION_ID", DeviceFields.field_sw_pumping_station_id, "evel.SN_SEWER_PUMPING_STATION(ID)")
        ]
        return foreign_keys
