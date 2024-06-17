from qgis.PyQt.QtCore import QVariant

class ContractFields:
    # Define field names as variables
    field_id = "ID"
    field_contract_number = "CONTRACT_NUMBER"
    field_type_id = "TYPE_ID"
    field_customer_id = "CUSTOMER_ID"
    field_cp_id = "CP_ID"
    field_startdate = "STARTDATE"
    field_enddate = "ENDDATE"
    field_joining_payment = "JOINING_PAYEMENT"

class ContractAliases:
    # Define aliases as variables
    alias_id = "Primaarvõti"
    alias_contract_number = "Lepingu number"
    alias_type_id = "Lepingu tüüp"
    alias_customer_id = "Kliendi ID"
    alias_cp_id = "Tarbimispunkti ID"
    alias_startdate = "Lepingu kehtivuse algus"
    alias_enddate = "Lepingu kehtivuse lõpp"
    alias_joining_payment = "Liitumistasu"

class LayerFunctions:
    
    @staticmethod
    def fields():
        # Define the field definitions for CONTRACT
        field_definitions = [
            (ContractFields.field_id, QVariant.Int, True),
            (ContractFields.field_contract_number, QVariant.String, 64),
            (ContractFields.field_type_id, QVariant.Int, False),
            (ContractFields.field_customer_id, QVariant.Int, False),
            (ContractFields.field_cp_id, QVariant.Int, False),
            (ContractFields.field_startdate, QVariant.DateTime, False),
            (ContractFields.field_enddate, QVariant.DateTime, False),
            (ContractFields.field_joining_payment, QVariant.Int, False)
        ]
        return field_definitions

class KeyDefinitions:

    @staticmethod
    def primary_key():
        # Define the primary key for CONTRACT
        primary_key = ("PK_CONTRACT_ID", [ContractFields.field_id])
        return primary_key
    
    def foreign_keys():
        # Define the foreign keys for CONTRACT
        foreign_keys = [
            ("FK_CONTRACT_TYPE_ID", ContractFields.field_type_id, "evel.SN_CONSTANT(ID)"),
            ("FK_SN_CONTRACT_CUSTOMER_ID", ContractFields.field_customer_id, "evel.CUSTOMER(ID)"),
            ("FK_SN_CONTRACT_CPID", ContractFields.field_cp_id, "evel.CONSUMER_POINT(ID)")
        ]
        return foreign_keys
