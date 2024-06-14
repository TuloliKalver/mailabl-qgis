from qgis.PyQt.QtCore import QVariant

class ExternalDocFields:
    # Define field names as variables
    field_id = "ID"
    field_type_id = "TYPE_ID"
    field_filename = "FILENAME"
    field_url = "URL"
    field_description = "DESCRIPTION"
    field_pnt_rotation = "PNT_ROTATION"
    field_geom = "GEOM"
    field_file_size = "FILE_SIZE"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class ExternalDocAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_type_id = "Tüüp"
    alias_filename = "Faili nimi"
    alias_url = "URL"
    alias_description = "Kirjeldus"
    alias_pnt_rotation = "Pöördenurk"
    alias_geom = "Geomeetria"
    alias_file_size = "Faili suurus"
    alias_added_by = "Sisestaja"
    alias_added_date = "Sisestamise kp"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kp"

class LayerFunctions:

    def fields():
        # Define the field definitions for EXTERNAL_DOC
        field_definitions = [
            (ExternalDocFields.field_id, QVariant.Int, True),
            (ExternalDocFields.field_type_id, QVariant.Int, False),
            (ExternalDocFields.field_filename, QVariant.String, 1024),
            (ExternalDocFields.field_url, QVariant.String, 1024),
            (ExternalDocFields.field_description, QVariant.String, 1024),
            (ExternalDocFields.field_pnt_rotation, QVariant.Int, False),
            (ExternalDocFields.field_geom, "geometry(point)", False),
            (ExternalDocFields.field_file_size, QVariant.Int, False),
            (ExternalDocFields.field_added_by, QVariant.String, 30),
            (ExternalDocFields.field_added_date, QVariant.DateTime, False),
            (ExternalDocFields.field_updated_by, QVariant.String, 50),
            (ExternalDocFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:
    
    def primary_key():
        # Define the primary key for EXTERNAL_DOC
        primary_key = ("PK_EXTERNAL_DOC", [ExternalDocFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for EXTERNAL_DOC
        foreign_keys = [
            ("FK_EXTERNAL_DOC_TYPE_ID", ExternalDocFields.field_type_id, "evel.EXTERNAL_DOC_TYPE(ID)")
        ]
        return foreign_keys