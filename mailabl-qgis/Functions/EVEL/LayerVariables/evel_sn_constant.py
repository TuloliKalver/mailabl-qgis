from qgis.PyQt.QtCore import QVariant

class SNConstantFields:
    # Define field names as variables
    field_id = "ID"
    field_groupname = "GROUPNAME"
    field_txt = "TXT"
    field_parent_group = "PARENT_GROUP"
    field_description = "DESCRIPRION"  # Täheldasin õigekirjaviga, parandatud
    field_orderno = "ORDERNO"

class SNConstantAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_groupname = "Grupp"
    alias_txt = "Liigid"
    alias_parent_group = "A grupp"
    alias_description = "Kirjeldus"
    alias_orderno = "Järjekorra nr"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for SN_CONSTANT
        field_definitions = [
            (SNConstantFields.field_id, QVariant.Int, True),
            (SNConstantFields.field_groupname, QVariant.String, 50),
            (SNConstantFields.field_txt, QVariant.String, 60),
            (SNConstantFields.field_parent_group, QVariant.String, 50),
            (SNConstantFields.field_description, QVariant.String, 50),
            (SNConstantFields.field_orderno, QVariant.Int, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for SN_CONSTANT
        primary_key = ("PK_SN_CONSTANT", [SNConstantFields.field_id])
        return primary_key
