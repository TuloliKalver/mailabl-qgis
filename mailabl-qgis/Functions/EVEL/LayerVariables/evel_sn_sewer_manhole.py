from qgis.PyQt.QtCore import QVariant

class SNSewerManholeFields:
    # Defineeri välja nimed muutujatena
    field_id = "ID"
    field_node_id = "NODE_ID"
    field_type_id = "TYPE_ID"
    field_material_id = "MATERIAL_ID"
    field_diameter_type_id = "DIAMETER_TYPE_ID"
    field_diameter_id = "DIAMETER_ID"
    field_firmness_class_id = "FIRMNESS_CLASS_ID"
    field_lid_type_id = "LID_TYPE_ID"
    field_lid_material_id = "LID_MATERIAL_ID"
    field_lid_shape_id = "LID_SHAPE_ID"
    field_lid_diameter_id = "LID_DIAMETER_ID"
    field_lid_capacity_id = "LID_CAPACITY_ID"
    field_access_duct_diam = "ACCESS_DUCT_DIAM"
    field_creator = "CREATOR"
    field_creator_date = "CREATOR_DATE"
    field_updated_by = "UPDATED_BY"
    field_update_date = "UPDATE_DATE"

class SNSewerManholeAliases:
    # Defineeri aliasid muutujatena
    alias_id = "Primaarvõti"
    alias_node_id = "Viide Sõlmele"
    alias_type_id = "Kaevu liik"
    alias_material_id = "Kaevu materjal"
    alias_diameter_type_id = "Läbimõõdu tüüp"
    alias_diameter_id = "Läbimõõt"
    alias_firmness_class_id = "Ringjäikus SN (kN/m2)"
    alias_lid_type_id = "Kaane tüüp"
    alias_lid_material_id = "Kaane materjal"
    alias_lid_shape_id = "Kaane kuju"
    alias_lid_diameter_id = "Kaane läbimõõt"
    alias_lid_capacity_id = "Kaane kandevõime"
    alias_access_duct_diam = "Tõusutoru läbimõõt (mm)"
    alias_creator = "Sisestaja"
    alias_creator_date = "Sisestamise kuupäev"
    alias_updated_by = "Muutja"
    alias_update_date = "Muutmise kuupäev"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Defineeri välja määratlused evel.SN_SEWER_MANHOLE jaoks
        field_definitions = [
            (SNSewerManholeFields.field_id, QVariant.Int, True),
            (SNSewerManholeFields.field_node_id, QVariant.Int, False),
            (SNSewerManholeFields.field_type_id, QVariant.Int, False),
            (SNSewerManholeFields.field_material_id, QVariant.Int, False),
            (SNSewerManholeFields.field_diameter_type_id, QVariant.Int, False),
            (SNSewerManholeFields.field_diameter_id, QVariant.Int, False),
            (SNSewerManholeFields.field_firmness_class_id, QVariant.Int, False),
            (SNSewerManholeFields.field_lid_type_id, QVariant.Int, False),
            (SNSewerManholeFields.field_lid_material_id, QVariant.Int, False),
            (SNSewerManholeFields.field_lid_shape_id, QVariant.Int, False),
            (SNSewerManholeFields.field_lid_diameter_id, QVariant.Int, False),
            (SNSewerManholeFields.field_lid_capacity_id, QVariant.Int, False),
            (SNSewerManholeFields.field_access_duct_diam, QVariant.Int, False),
            (SNSewerManholeFields.field_creator, QVariant.String, False),
            (SNSewerManholeFields.field_creator_date, QVariant.DateTime, False),
            (SNSewerManholeFields.field_updated_by, QVariant.String, False),
            (SNSewerManholeFields.field_update_date, QVariant.DateTime, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Defineeri primaarvõti evel.SN_SEWER_MANHOLE jaoks
        primary_key = ("PK_SN_SEWER_MANHOLE", [SNSewerManholeFields.field_id])
        return primary_key
    
    @staticmethod
    def foreign_keys():
        # Defineeri võõrvõtmed evel.SN_SEWER_MANHOLE jaoks
        foreign_keys = [
            ("FK_SN_SEWER_MANHOLE_NODE_ID", SNSewerManholeFields.field_node_id, "evel.SN_SEWER_NODE(MSLINK)"),
            ("FK_SN_SMANHOLE_TYPE_ID", SNSewerManholeFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_LID_MATERIAL_ID", SNSewerManholeFields.field_lid_material_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_LID_CAPACITY_ID", SNSewerManholeFields.field_lid_capacity_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_DIAMETER_ID", SNSewerManholeFields.field_diameter_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_DIAMETER_TYPE_ID", SNSewerManholeFields.field_diameter_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_MATERIAL_ID", SNSewerManholeFields.field_material_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_LID_TYPE_ID", SNSewerManholeFields.field_lid_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_LID_SHAPE_ID", SNSewerManholeFields.field_lid_shape_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_FIRMNESS_CLASS_ID", SNSewerManholeFields.field_firmness_class_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_SMANHOLE_LID_DIAMETER_ID", SNSewerManholeFields.field_lid_diameter_id, "evel.SN_CONSTANT(ID)")
        ]
        return foreign_keys
