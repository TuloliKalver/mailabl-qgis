from qgis.PyQt.QtCore import QVariant

class ExternalDocTypeFields:
    # Define field names as variables
    field_id = "ID"
    field_category_id = "CATEGORY_ID"
    field_type_id = "TYPE_ID"
    field_description = "DESCRIPTION"
    field_directory = "DIRECTORY"
    field_added_by = "ADDED_BY"
    field_added_date = "ADDED_DATE"

class ExternalDocTypeAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_category_id = "Kategooria"
    alias_type_id = "Tüüp"
    alias_description = "Kirjeldus"
    alias_directory = "Kataloog"
    alias_added_by = "Lisaja"
    alias_added_date = "Lisamise kp"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for EXTERNAL_DOC_TYPE
        field_definitions = [
            (ExternalDocTypeFields.field_id, QVariant.Int, True),
            (ExternalDocTypeFields.field_category_id, QVariant.Int, False),
            (ExternalDocTypeFields.field_type_id, QVariant.Int, False),
            (ExternalDocTypeFields.field_description, QVariant.String, 255),
            (ExternalDocTypeFields.field_directory, QVariant.String, 255),
            (ExternalDocTypeFields.field_added_by, QVariant.String, 30),
            (ExternalDocTypeFields.field_added_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for EXTERNAL_DOC_TYPE
        primary_key = ("PK_EXTERNAL_DOC_TYPE", [ExternalDocTypeFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for EXTERNAL_DOC_TYPE
        foreign_keys = [
            ("FK_EXTERNAL_DOC_TYPE_CATEGORY_ID", ExternalDocTypeFields.field_category_id, "evel.SN_CONSTANT(ID)"),
            ("FK_EXTERNAL_DOC_TYPE_TYPE_ID", ExternalDocTypeFields.field_type_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
