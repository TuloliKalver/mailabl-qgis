from qgis.PyQt.QtCore import QVariant

class SNFirePlugFields:
    # Define field names as variables
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_aqua_id = "TYPE_AQUA_ID"
    field_plug_type_id = "PLUG_TYPE_ID"
    field_location_id = "LOCATION_ID"
    field_manufacturer = "MANUFACTURER"
    field_duct_size = "DUCT_SIZE"
    field_capacity = "CAPACITY"
    field_measured_capacity = "MEASURED_CAPACITY"
    field_measure_date = "MEASURE_DATE"
    field_measure_nr = "MEASURE_NR"
    field_connection_standard = "CONNECTION_STANDARD"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNFirePlugAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_aqua_id = "Liik (FIRE_PLUG_TYPE)"
    alias_plug_type_id = "Alamliik (FIRE_PLUG_TYPE_SUB)"
    alias_location_id = "Paiknemine (FIRE_PLUG_LOCATION)"
    alias_manufacturer = "Tootja"
    alias_duct_size = "Tarnetorustiku läbimõõt DN"
    alias_capacity = "Nimitootlikkus Q (l/s)"
    alias_measured_capacity = "Mõõdetud tootlikkus Q (l/s)"
    alias_measure_date = "Mõõtmise kp"
    alias_measure_nr = "Mõõtmise akti nr"
    alias_connection_standard = "Voolikuühenduse standard"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:

    def fields():
        # Define the field definitions for SN_FIRE_PLUG
        field_definitions = [
            (SNFirePlugFields.field_id, QVariant.Int, True),
            (SNFirePlugFields.field_node_id, QVariant.Int, False),
            (SNFirePlugFields.field_type_aqua_id, QVariant.Int, False),
            (SNFirePlugFields.field_plug_type_id, QVariant.Int, False),
            (SNFirePlugFields.field_location_id, QVariant.Int, False),
            (SNFirePlugFields.field_manufacturer, QVariant.String, 64),
            (SNFirePlugFields.field_duct_size, QVariant.Int, False),
            (SNFirePlugFields.field_capacity, QVariant.Int, False),
            (SNFirePlugFields.field_measured_capacity, QVariant.Int, False),
            (SNFirePlugFields.field_measure_date, QVariant.DateTime, False),
            (SNFirePlugFields.field_measure_nr, QVariant.String, 20),
            (SNFirePlugFields.field_connection_standard, QVariant.String, 20),
            (SNFirePlugFields.field_creator, QVariant.String, 64),
            (SNFirePlugFields.field_creation_date, QVariant.DateTime, False),
            (SNFirePlugFields.field_updated_by, QVariant.String, 64),
            (SNFirePlugFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class SNFirePlugKeyDefinitions:
    
    def primary_key():
        # Define the primary key for SN_FIRE_PLUG
        primary_key = ("PK_SN_FIRE_PLUG", [SNFirePlugFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for SN_FIRE_PLUG
        foreign_keys = [
            ("FK_SN_FIRE_PLUG_NODE_ID", SNFirePlugFields.field_node_id, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_FIRE_PLUG_TYPE_AQUA_ID", SNFirePlugFields.field_type_aqua_id, "evel.SN_CONSTANT(ID)"),
            ("FK_PLUG_TYPE_ID", SNFirePlugFields.field_plug_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_PLUG_LOCATION_ID", SNFirePlugFields.field_location_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
