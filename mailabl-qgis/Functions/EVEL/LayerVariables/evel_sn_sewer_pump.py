from qgis.PyQt.QtCore import QVariant

class SNSewerPumpFields:
    # Define field names as variables
    field_id = "ID"
    field_pstation_id = "PSTATION_ID"
    field_type_id = "TYPE_ID"
    field_install_method_id = "INSTALL_METHOD_ID"
    field_install_date = "INSTALL_DATE"
    field_power_w = "POWER_W"
    field_manufacturer = "MANUFACTURER"
    field_mark = "MARK"
    field_productivity = "PRODUCTIVITY"
    field_pump_head = "PUMP_HEAD"
    field_running_time = "RUNNING_TIME"
    field_in_diameter = "IN_DIAMETER"
    field_out_diameter = "OUT_DIAMETER"
    field_engine_current = "ENGINE_CURRENT"
    field_engine_voltage = "ENGINE_VOLTAGE"
    field_remarks = "REMARKS"

class SNSewerPumpAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_pstation_id = "Pumpla ID"
    alias_type_id = "Tööratta tüüp"
    alias_install_method_id = "Paigaldusviis"
    alias_install_date = "Paigaldusaeg"
    alias_power_w = "Pumba võimsus (W)"
    alias_manufacturer = "Tootja"
    alias_mark = "Pumba mark"
    alias_productivity = "Maksimaalne tootlikkus Q (l/s)"
    alias_pump_head = "Maksimaalne tõstekõrgus H (m)"
    alias_running_time = "Töötatud tunnid"
    alias_in_diameter = "Sisendi läbimõõt DN"
    alias_out_diameter = "Väljundi läbimõõt DN"
    alias_engine_current = "Mootori nimivool (A)"
    alias_engine_voltage = "Mootori nimipinge (V)"
    alias_remarks = "Märkused"

class SNSewerPumpFunctions:

    def sn_sewer_pump_fields():
        # Define the field definitions for SN_SEWER_PUMP
        field_definitions = [
            (SNSewerPumpFields.field_id, QVariant.Int, True),
            (SNSewerPumpFields.field_pstation_id, QVariant.Int, True),
            (SNSewerPumpFields.field_type_id, QVariant.Int, True),
            (SNSewerPumpFields.field_install_method_id, QVariant.Int, False),
            (SNSewerPumpFields.field_install_date, QVariant.DateTime, False),
            (SNSewerPumpFields.field_power_w, QVariant.Double, 6),
            (SNSewerPumpFields.field_manufacturer, QVariant.String, 50),
            (SNSewerPumpFields.field_mark, QVariant.String, 30),
            (SNSewerPumpFields.field_productivity, QVariant.Double, 6),
            (SNSewerPumpFields.field_pump_head, QVariant.Double, 6),
            (SNSewerPumpFields.field_running_time, QVariant.Double, 6),
            (SNSewerPumpFields.field_in_diameter, QVariant.Double, 6, 2),
            (SNSewerPumpFields.field_out_diameter, QVariant.Double, 6, 2),
            (SNSewerPumpFields.field_engine_current, QVariant.Double, 6, 2),
            (SNSewerPumpFields.field_engine_voltage, QVariant.Double, 6, 2),
            (SNSewerPumpFields.field_remarks, QVariant.String, 250)
        ]
        return field_definitions

class SNSewerPumpKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_SEWER_PUMP
        primary_key = ("PK_SN_SEWER_PUMP", [SNSewerPumpFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_SEWER_PUMP
        foreign_keys = [
            ("FK_SN_SEWER_PUMP_PSTATION_ID", SNSewerPumpFields.field_pstation_id, "evel.SN_SEWER_PUMPING_STATION(ID)"),
            ("FK_SN_SEWER_PUMP_TYPE_ID", SNSewerPumpFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SEWER_PUMP_INSTALL_METHOD_ID", SNSewerPumpFields.field_install_method_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
