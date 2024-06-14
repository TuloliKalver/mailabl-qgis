from qgis.PyQt.QtCore import QVariant

class ConsumerPointFields:
    # Define field names as variables
    field_id = "ID"
    field_identification = "IDENTIFICATION"
    field_address_id = "ADDRESS_ID"
    field_owner_id = "OWNER_ID"
    field_invoicing_id = "INVOICING_ID"
    field_consumerpoint_g = "CONSUMERPOINT_G"
    field_real_estate_nr = "REAL_ESTATE_NR"
    field_water_junction = "WATER_JUNCTION"
    field_sewer_junction = "SEWER_JUNCTION"
    field_storm_water_junction = "STORM_WATER_JUNCTION"
    field_water_network_node = "WATER_NETWORK_NODE"
    field_sewer_network_node = "SEWER_NETWORK_NODE"
    field_rain_network_node = "RAIN_NETWORK_NODE"
    field_criticalcustomer_is = "CRITICALCUSTOMER_IS"
    field_sprinklercustomer_is = "SPRINKLERCUSTOMER_IS"
    field_industrialwwcont_is = "INDUSTRIALWWCONT_IS"
    field_cp_type_id = "CP_TYPE_ID"
    field_cp_state_id = "CP_STATE_ID"
    field_residents = "RESIDENTS"
    field_comments = "COMMENTS"
    field_geom = "GEOM"
    field_creator = "CREATOR"
    field_creation_date = "CREATION_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class ConsumerPointAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_identification = "Tarbimispunkti tähis"
    alias_address_id = "Tarbimispunkti aadress"
    alias_owner_id = "Omanik, seos kliendiga"
    alias_invoicing_id = "Rentnik, arve saaja"
    alias_consumerpoint_g = "Grupp"
    alias_real_estate_nr = "Katastritunnus"
    alias_water_junction = "Kas vee klient"
    alias_sewer_junction = "Kas kanalisatsiooni klient"
    alias_storm_water_junction = "Kas sadevee klient"
    alias_water_network_node = "Seos WATER_NODE tabeliga"
    alias_sewer_network_node = "Seos SEWER_NODE tabeliga kanalisatsioonikorral"
    alias_rain_network_node = "Seos SEWER_NODE tabeliga sadevee korral"
    alias_criticalcustomer_is = "Kas kriitiline klient"
    alias_sprinklercustomer_is = "Kas sprinkler klient"
    alias_industrialwwcont_is = "Kas tööstuslikud jäätmed"
    alias_cp_type_id = "Tarbimispunkti tüüp"
    alias_cp_state_id = "Tarbimispunkti olek"
    alias_residents = "Elanike arv"
    alias_comments = "Märkused"
    alias_geom = "Geomeetria"
    alias_creator = "Sisestaja"
    alias_creation_date = "Sisestamise aeg"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise aeg"

class LayerFunctions:

    def fields():
        # Define the field definitions for CONSUMER_POINT
        field_definitions = [
            (ConsumerPointFields.field_id, QVariant.Int, True),
            (ConsumerPointFields.field_identification, QVariant.String, 100),
            (ConsumerPointFields.field_address_id, QVariant.Int, False),
            (ConsumerPointFields.field_owner_id, QVariant.Int, False),
            (ConsumerPointFields.field_invoicing_id, QVariant.Int, False),
            (ConsumerPointFields.field_consumerpoint_g, QVariant.Int, False),
            (ConsumerPointFields.field_real_estate_nr, QVariant.String, 14),
            (ConsumerPointFields.field_water_junction, QVariant.Bool, False),
            (ConsumerPointFields.field_sewer_junction, QVariant.Bool, False),
            (ConsumerPointFields.field_storm_water_junction, QVariant.Bool, False),
            (ConsumerPointFields.field_water_network_node, QVariant.Int, False),
            (ConsumerPointFields.field_sewer_network_node, QVariant.Int, False),
            (ConsumerPointFields.field_rain_network_node, QVariant.Int, False),
            (ConsumerPointFields.field_criticalcustomer_is, QVariant.Bool, False),
            (ConsumerPointFields.field_sprinklercustomer_is, QVariant.Bool, False),
            (ConsumerPointFields.field_industrialwwcont_is, QVariant.Bool, False),
            (ConsumerPointFields.field_cp_type_id, QVariant.Int, False),
            (ConsumerPointFields.field_cp_state_id, QVariant.Int, False),
            (ConsumerPointFields.field_residents, QVariant.Int, False),
            (ConsumerPointFields.field_comments, QVariant.String, 2000),
            (ConsumerPointFields.field_geom, QVariant.String, False),
            (ConsumerPointFields.field_creator, QVariant.String, 64),
            (ConsumerPointFields.field_creation_date, QVariant.DateTime, False),
            (ConsumerPointFields.field_updated_by, QVariant.String, 64),
            (ConsumerPointFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for CONSUMER_POINT
        primary_key = ("PK_CONSUMER_POINT", [ConsumerPointFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for CONSUMER_POINT
        foreign_keys = [
            ("FK_CONSUMER_POINT_CP_STATE_ID", ConsumerPointFields.field_cp_state_id, "evel.SN_CONSTANT(ID)"),
            ("FK_CONSUMER_POINT_APARTMENT_DATA", ConsumerPointFields.field_address_id, "evel.APARTMENT_DATA(ID)"),
            ("FK_CONSUMER_POINT_RAIN_NETWORK_NODE", ConsumerPointFields.field_rain_network_node, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_CONSUMER_POINT_SEWER_NETWORK_NODE", ConsumerPointFields.field_sewer_network_node, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_CONSUMER_POINT_CP_TYPE_ID", ConsumerPointFields.field_cp_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_CONSUMER_POINT_OWNER", ConsumerPointFields.field_owner_id, "evel.CUSTOMER(ID)"),
            ("FK_CP_WNETWORK_NODE", ConsumerPointFields.field_water_network_node, "evel.SN_WATER_NODE(MSLINK)"),
            ("FK_SN_CONSUMER_POINT_INVOICE", ConsumerPointFields.field_invoicing_id, "evel.CUSTOMER(ID)"),
            ("FK_CONSUMERPOINT_GROUP", ConsumerPointFields.field_consumerpoint_g, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
