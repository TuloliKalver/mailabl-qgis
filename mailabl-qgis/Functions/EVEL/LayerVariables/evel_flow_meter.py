from qgis.PyQt.QtCore import QVariant

class FlowMeterFields:
    # Define field names as variables
    field_id = "ID"
    field_identification = "IDENTIFICATION"
    field_consumer_id = "CONSUMER_ID"
    field_manhole_id = "MANHOLE_ID"
    field_sw_pumping_station_id = "SW_PUMPING_STATION_ID"
    field_class_id = "CLASS_ID"
    field_water_type_id = "WATER_TYPE_ID"
    field_flow_meter_type = "FLOW_METER_TYPE"
    field_mark = "MARK"
    field_size_id = "SIZE_ID"
    field_console_length_id = "CONSOLE_LENGTH_ID"
    field_nominal_value = "NOMINAL_VALUE"
    field_install_date = "INSTALL_DATE"
    field_seal_nr = "SEAL_NR"
    field_control_date = "CONTROL_DATE"
    field_control_date_next = "CONTROL_DATE_NEXT"
    field_removed = "REMOVED"
    field_module_number = "MODULE_NUMBER"
    field_manufacturer = "MANUFACTURER"
    field_backwards = "BACKWARDS"
    field_consumption_estimate = "CONSUMPTION_ESTIMATE"
    field_max_reading = "MAX_READING"
    field_remotely_readable = "REMOTELY_READABLE"

class FlowMeterAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_identification = "Arvesti tähis/nr"
    alias_consumer_id = "Seos tarbimispunktiga"
    alias_manhole_id = "Seos mõõtekaevuga"
    alias_sw_pumping_station_id = "Seos reoveepumplaga"
    alias_class_id = "Arvesti klass"
    alias_water_type_id = "Mõõdetava vee liik"
    alias_flow_meter_type = "Arvesti tüüp"
    alias_mark = "Arvesti mark"
    alias_size_id = "Veearvesti toru läbimõõt"
    alias_console_length_id = "Veearvesti pikkus (mm)"
    alias_nominal_value = "Veearvesti nominaalkulu (m3/h)"
    alias_install_date = "Paigaldamise aeg"
    alias_seal_nr = "Plommi number"
    alias_control_date = "Taatlemise aeg"
    alias_control_date_next = "Järgmise taatlemise aeg"
    alias_removed = "Kas eemaldatud"
    alias_module_number = "Mooduli number"
    alias_manufacturer = "Tootja"
    alias_backwards = "Mõlemasuunaline"
    alias_consumption_estimate = "Eeldatav tarbimine (m3)"
    alias_max_reading = "Maksimaalne näit"
    alias_remotely_readable = "Kaugloetav"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for FLOW_METER
        field_definitions = [
            (FlowMeterFields.field_id, QVariant.Int, True),
            (FlowMeterFields.field_identification, QVariant.String, 20),
            (FlowMeterFields.field_consumer_id, QVariant.Int, False),
            (FlowMeterFields.field_manhole_id, QVariant.Int, False),
            (FlowMeterFields.field_sw_pumping_station_id, QVariant.Int, False),
            (FlowMeterFields.field_class_id, QVariant.Int, False),
            (FlowMeterFields.field_water_type_id, QVariant.Int, False),
            (FlowMeterFields.field_flow_meter_type, QVariant.Int, False),
            (FlowMeterFields.field_mark, QVariant.String, 50),
            (FlowMeterFields.field_size_id, QVariant.Int, False),
            (FlowMeterFields.field_console_length_id, QVariant.Int, False),
            (FlowMeterFields.field_nominal_value, QVariant.Double, 8.2),
            (FlowMeterFields.field_install_date, QVariant.DateTime, False),
            (FlowMeterFields.field_seal_nr, QVariant.String, 20),
            (FlowMeterFields.field_control_date, QVariant.DateTime, False),
            (FlowMeterFields.field_control_date_next, QVariant.DateTime, False),
            (FlowMeterFields.field_removed, QVariant.Bool, False),
            (FlowMeterFields.field_module_number, QVariant.String, 1024),
            (FlowMeterFields.field_manufacturer, QVariant.String, 50),
            (FlowMeterFields.field_backwards, QVariant.Bool, False),
            (FlowMeterFields.field_consumption_estimate, QVariant.Int, False),
            (FlowMeterFields.field_max_reading, QVariant.Int, False),
            (FlowMeterFields.field_remotely_readable, QVariant.Bool, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for FLOW_METER
        primary_key = ("PK_FLOW_METER", [FlowMeterFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for FLOW_METER
        foreign_keys = [
            ("FK_FLOW_METER_WATER_TYPE_ID", FlowMeterFields.field_water_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_FLOW_METER_SW_PUMPING_STATION_ID", FlowMeterFields.field_sw_pumping_station_id, "evel.SN_SEWER_PUMPING_STATION(ID)"),
            ("FK_CONSUMER_ID", FlowMeterFields.field_consumer_id, "evel.CONSUMER_POINT(ID)"),
            ("FK_FLOW_METER_CLASS_ID", FlowMeterFields.field_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_FLOW_METER_MANHOLE_ID", FlowMeterFields.field_manhole_id, "evel.SN_WATER_MANHOLE(ID)"),
            ("FK_FLOW_METER_SIZE_ID", FlowMeterFields.field_size_id, "evel.SN_CONSTANT(ID)"),
            ("FK_FLOW_METER_FLOW_METER_TYPE_ID", FlowMeterFields.field_flow_meter_type, "evel.SN_CONSTANT(ID)"),
            ("FK_FLOW_METER_CONSOLE_LENGTH_ID", FlowMeterFields.field_console_length_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
