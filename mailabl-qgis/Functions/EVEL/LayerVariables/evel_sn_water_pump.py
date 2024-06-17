from qgis.PyQt.QtCore import QVariant

class SNWaterPumpFields:
    # Defineeri välja nimed muutujatena
    field_id = "ID"
    field_pstation_id = "PSTATION_ID"
    field_el_cons_pnt_id = "EL_CONS_PNT_ID"
    field_type_id = "TYPE_ID"
    field_manufacturer = "MANUFACTURER"
    field_productivity = "PRODUCTIVITY"
    field_pump_head = "PUMP_HEAD"
    field_mark = "MARK"
    field_install_date = "INSTALL_DATE"
    field_power_w = "POWER_W"
    field_running_time = "RUNNING_TIME"
    field_pipe_fitting = "PIPE_FITTING"
    field_remarks = "REMARKS"

class SNWaterPumpAliases:
    # Defineeri aliasid muutujatena
    alias_id = "Primaarvõti"
    alias_pstation_id = "Puurkaev-Pumpla ID"
    alias_el_cons_pnt_id = "Tarbimispunkti ID"
    alias_type_id = "Pumba tüüp"
    alias_manufacturer = "Tootja"
    alias_productivity = "Maksimaalne tootlikkus Q (l/s)"
    alias_pump_head = "Maksimaalne tõstekõrgus H (m)"
    alias_mark = "Pumba mark"
    alias_install_date = "Paigalduse aeg"
    alias_power_w = "Pumba võimsus (W)"
    alias_running_time = "Töötatud tunnid"
    alias_pipe_fitting = "Ühendus toruga (tollides)"
    alias_remarks = "Märkused"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Defineeri välja määratlused SN_WATER_PUMP jaoks
        field_definitions = [
            (SNWaterPumpFields.field_id, QVariant.Int, True),
            (SNWaterPumpFields.field_pstation_id, QVariant.Int, True),
            (SNWaterPumpFields.field_el_cons_pnt_id, QVariant.Int, False),
            (SNWaterPumpFields.field_type_id, QVariant.Int, True),
            (SNWaterPumpFields.field_manufacturer, QVariant.String, 50),
            (SNWaterPumpFields.field_productivity, QVariant.Double, False),
            (SNWaterPumpFields.field_pump_head, QVariant.Double, False),
            (SNWaterPumpFields.field_mark, QVariant.String, 30),
            (SNWaterPumpFields.field_install_date, QVariant.DateTime, False),
            (SNWaterPumpFields.field_power_w, QVariant.Double, False),
            (SNWaterPumpFields.field_running_time, QVariant.Double, False),
            (SNWaterPumpFields.field_pipe_fitting, QVariant.String, 6),
            (SNWaterPumpFields.field_remarks, QVariant.String, 250)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti SN_WATER_PUMP jaoks
        primary_key = ("PK_SN_WATER_PUMP", [SNWaterPumpFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed SN_WATER_PUMP jaoks
        foreign_keys = [
            ("FK_SN_WPUMP_SN_WATER_PUMPING_STATION_ID", SNWaterPumpFields.field_pstation_id, "evel.SN_WATER_PUMPING_STATION(ID)"),
            ("FK_SN_WATER_PUMP_TYPE_ID", SNWaterPumpFields.field_type_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
