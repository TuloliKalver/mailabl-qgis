from qgis.core import QgsProject, QgsLayerTreeGroup
from ..processes.OnFirstLoad.AddSetupLayers import SetupLayers
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QDialog

class UICheckboxes:
    water_checkbox = "Vesi"
    sewage_checkbox = "Kanal"
    rainwater_checkbox = "Sademevesi"
    pumpstation_checkbox = "Pumpla"
    treatment_checkbox = "Reoveepuhastid"
    connectionpoint_checkbox = "Liitumispunktid"
    easement_checkbox = "Servituudid"
    services_checkbox = "Võrgusündmused"
    snconstant_checkbox = "SN-väärtused"
    device_checkbox = "Seadmed"
    contract_checkbox = "Lepingud"
    customer_checkbox = "Kliendid"
    external_doc_checkbox = "Välisdokumendid"
    apartment_checkbox = "Korterid"
    flow_meter_checkbox = "Arvestid"
    demarcation_point_checkbox = "Piiritluspunktid"
    fire_plug_checkbox = "Tuletõrjehüdrandid"
    manhole_checkbox = "Kaevud"
    pressure_station_checkbox = "Survejaamad"
    valve_checkbox = "Ventiilid"
    tank_checkbox = "Paagid"
    properties_checkbox = "Kinnistud"
    program_checkbox = "Programmid"
    operation_checkbox = "Operatsioonid"
    error_checkbox = "Veateated"

 # Define a dictionary mapping checkbox object names to their display names
    CHECKBOX_NAMES = {
        'cbWater': water_checkbox,
        'cbSewage': sewage_checkbox,
        'cbRainwater': rainwater_checkbox,
        'cbPumpstation': pumpstation_checkbox,
        'cbSewTreatment': treatment_checkbox,
        'cbConnectionPoints': connectionpoint_checkbox,
        'cbEasements': easement_checkbox,
        'cbServices': services_checkbox,
        'cbSNConstant': snconstant_checkbox,
        'cbDevice': device_checkbox,
        'cbContract': contract_checkbox,
        'cbCustomer': customer_checkbox,
        'cbExternalDoc': external_doc_checkbox,
        'cbApartment': apartment_checkbox,
        'cbFlowMeter': flow_meter_checkbox,
        'cbDemarcationPoint': demarcation_point_checkbox,
        'cbFirePlug': fire_plug_checkbox,
        'cbManhole': manhole_checkbox,
        'cbPressureStation': pressure_station_checkbox,
        'cbValve': valve_checkbox,
        'cbTank': tank_checkbox,
        'cbProperties': properties_checkbox,
        'cbProgram': program_checkbox,
        'cbOperation': operation_checkbox,
        'cbError': error_checkbox,
    }

    @classmethod
    def get_checkbox_display_name(cls, checkbox_object_name):
        """Get the display name of a checkbox based on its object name."""
        return cls.CHECKBOX_NAMES.get(checkbox_object_name, "Unknown")

class EvelLayerNames:
    EASEMENT = "evel_Servituut"
    WATER = "evel_Vesi"
    SEWAGE = "evel_Kanal"
    RAINWATER = "evel_Sademevesi"
    SERVICES = "evel_Töökäsud"
    SEWER = 'evel_Kanalisatsioon'
    FLOW_METER = 'evel_Arvestid'
    CONSUMER_POINT = 'evel_Tarbimispunktid'
    DEMARCATION_POINT = 'evel_Piiritluspunktid'
    CUSTOMER = 'evel_Kliendid'
    CONTRACT = 'evel_Lepingud'
    FIRE_PLUG = 'evel_Tuletõrjehüdrandid'
    MANHOLE = 'evel_Kaevud'
    PUMPING_STATION = 'evel_Pumbajaamad'
    PRESSURE_STATION = 'evel_Survejaamad'
    SEWAGE_TREATMENT = 'evel_Reoveepuhastid'
    VALVE = 'evel_Ventiilid'
    PROPERTIES = "evel_Kinnistud"
    PROGRAM = 'evel_Programmid'
    SN_CONSTANT = 'evel_konstandid'
    SEW_TREATMENT = 'evel_Reoveepuhastid'
    CONNECTION_POINTS = 'evel_Tarbimispunktid'
    APARTMENT = 'evel_Korterid'
    DEVICE = 'evel_Seadmed'
    EXTERNAL_DOC = 'evel_Välisdokumendid'
    OPERATION = 'evel_Operatsioonid'
    ERROR = 'evel_Veateated'
    TANK = 'evel_Paagid'

    
class EvelGroupLayersNames:
    EVEL_MAIN = 'EVEL_Mudel'
    EVEL_GENERAL = 'Üldine'
    EASEMENT = 'Servituut'
    SERVICES = 'Töökäsud'
    SEWER = 'Kanalisatsioon'
    WATER = 'Vesi'
    FLOW_METER = 'Arvestid'
    CONSUMER_POINT = 'Tarbimispunktid'
    DEMARCATION_POINT = 'Piiritluspunktid'
    CUSTOMER = 'Kliendid'
    CONTRACT = 'Lepingud'
    FIRE_PLUG = 'Tuletõrjehüdrandid'
    MANHOLE = 'Kaevud'
    PUMPING_STATION = 'Pumbajaamad'
    PRESSURE_STATION = 'Survejaamad'
    VALVE = 'Ventiilid'
    TANK = 'Paagid'
    PROPERTIES = "Kinnistud"
    PROGRAM = 'Programmid'

class EvelSubGroupLayersNames:
    ATTACHED_DOC = 'Dokumendid'

class EVELSubGoupLayersForServices:
    OPERATION = 'Operatsioonid'
    ERROR = 'Veateated'

class EvelSubGroupLayerNamesForProperties:
    APARTMENT = 'Korterid'
    BUILDING_AREA = 'Hooneala'

class FileNames:
    # List of filenames
    EVEL_ATTACHED_DOC_CUSTOMER = "evel_attached_doc_customer.py"
    EVEL_APARTMENT_DATA = "evel_apartment_data.py"
    EVEL_ATTACHED_DOC_LAND_PREM_AREA = "evel_attached_doc_land_prem_area.py"
    EVEL_ATTACHED_DOC_PLAN = "evel_attached_doc_plan.py"
    EVEL_ATTACHED_DOC_SN_CONSUMER_POINT = "evel_attached_doc_sn_consumer_point.py"
    EVEL_ATTACHED_DOC_SN_ERROR_REPORT = "evel_attached_doc_sn_error_report.py"
    EVEL_ATTACHED_DOC_SN_SEWER_DUCT = "evel_attached_doc_sn_sewer_duct.py"
    EVEL_ATTACHED_DOC_SN_SEWER_NODE = "evel_attached_doc_sn_sewer_node.py"
    EVEL_ATTACHED_DOC_SN_WATER_DUCT = "evel_attached_doc_sn_water_duct.py"
    EVEL_ATTACHED_DOC_SN_WATER_NODE = "evel_attached_doc_sn_water_node.py"
    LAND_PERM_AREA = "land_perm_area.py"
    EVEL_SN_SEWER_DUCT = "evel_sn_sewer_duct.py"
    EVEL_CONSUMER_POINT = "evel_consumer_point.py"
    EVEL_DEVICE = "evel_device.py"
    EVEL_DEMARCATION_POINT = "evel_demarcation_point.py"
    EVEL_CUSTOMER_CONSUMERPOINT = "evel_customer_consumerpoint.py"
    EVEL_CUSTOMER = "evel_customer.py"
    EVEL_CONTRACT = "evel_contract.py"
    EVEL_EXTERNAL_DOC = "evel_external_doc.py"
    EVEL_EXTERNAL_DOC_TYPE = "evel_external_doc_type.py"
    EVEL_FLOW_METER = "evel_flow_meter.py"
    EVEL_SN_CONSTANT = "evel_sn_constant.py"
    EVEL_SN_FIRE_PLUG = "evel_sn_fire_plug.py"
    EVEL_SN_OPERATION = "evel_sn_operation.py"
    EVEL_SN_SEWER_BRANCH = "evel_sn_sewer_branch.py"
    EVEL_SN_SEWER_DUCT_ERROR = "evel_sn_sewer_duct_error.py"
    EVEL_SN_SEWER_DUCT_PROGRAM = "evel_sn_sewer_duct_program.py"
    EVEL_SN_SEWER_MANHOLE = "evel_sn_sewer_manhole.py"
    EVEL_SN_SEWER_NODE = "evel_sn_sewer_node.py"
    EVEL_SN_SEWER_NODE_ERROR = "evel_sn_sewer_node_error.py"
    EVEL_SN_SEWER_NODE_PROGRAM = "evel_sn_sewer_node_program.py"
    EVEL_SN_SEWER_OTHER_NODE = "evel_sn_sewer_other_node.py"
    EVEL_SN_SEWER_PUMP = "evel_sn_sewer_pump.py"
    EVEL_SN_SEWER_PUMPING_STATION = "evel_sn_sewer_pumping_station.py"
    EVEL_SN_SEWER_VALVE = "evel_sn_sewer_valve.py"
    EVEL_SN_SEWER_VALVE_STATE_LOG = "evel_sn_sewer_valve_state_log.py"
    EVEL_SN_WATER_BRANCH = "evel_sn_water_branch.py"
    EVEL_SN_WATER_DUCT = "evel_sn_water_duct.py"
    EVEL_SN_WATER_DUCT_ERROR = "evel_sn_water_duct_error.py"
    EVEL_SN_WATER_DUCT_PROGRAM = "evel_sn_water_duct_program.py"
    EVEL_SN_WATER_MANHOLE = "evel_sn_water_manhole.py"
    EVEL_SN_WATER_NODE = "evel_sn_water_node.py"
    EVEL_SN_WATER_NODE_ERROR = "evel_sn_water_node_error.py"
    EVEL_SN_WATER_NODE_PROGRAM = "evel_sn_water_node_program.py"
    EVEL_SN_WATER_OTHER_NODE = "evel_sn_water_other_node.py"
    EVEL_SN_WATER_PRESSURE_STATION = "evel_sn_water_pressure_station.py"
    EVEL_SN_WATER_PUMP = "evel_sn_water_pump.py"
    EVEL_SN_WATER_PUMPING_STATION = "evel_sn_water_pumping_station.py"
    EVEL_SN_WATER_TANK = "evel_sn_water_tank.py"
    EVEL_SN_WATER_VALVE = "evel_sn_water_valve.py"
    EVEL_SN_WATER_VALVE_STATE_LOG = "evel_sn_water_valve_state_log.py"
    EVEL_BUILDING_AREA = "evel_building_area.py"
    EVEL_SN_OPERATION = "evel_sn_operation.py"

class CheckBoxMappings:
    from ..Functions.EVEL.QGIS_styles.EvelStyles import (
        ElekterSide, Hylsid, Kanalisatsioon, Kliendid, Rennid,
        Servituudid, Teostusjoonis, Veevork, VorgusundmusedAutod
    )

    @staticmethod
    def derive_table_name(file_name):
        return file_name.replace(".py", "") if file_name else None

    MAPPINGS = {
        'cbWater': {
            'group': EvelGroupLayersNames.WATER,
            'style': Veevork.veetorud,
            'layer_name': EvelLayerNames.WATER,
            'file': FileNames.EVEL_SN_WATER_DUCT,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_WATER_DUCT)

        },
        'cbSewage': {
            'group': EvelGroupLayersNames.SEWER,
            'style': Kanalisatsioon.kanalisatsioonitorud,
            'layer_name': EvelLayerNames.SEWAGE,
            'file': FileNames.EVEL_SN_SEWER_DUCT,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_BRANCH)
        },
        'cbRainwater': {
            'group': EvelGroupLayersNames.SEWER,
            'style': Kanalisatsioon.kanalisatsioonitorud,
            'layer_name': EvelLayerNames.RAINWATER,
            'file': FileNames.EVEL_SN_SEWER_DUCT,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_DUCT)
        },
        'cbPumpstation': {
            'group': EvelGroupLayersNames.PUMPING_STATION,
            'style': Kanalisatsioon.pumplad,
            'layer_name': EvelLayerNames.PUMPING_STATION,
            'file': FileNames.EVEL_SN_SEWER_PUMP,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_PUMP)
        },
        'cbSewTreatment': {
            'group': EvelGroupLayersNames.SEWER,
            'style': Kanalisatsioon.pumplad,
            'layer_name': EvelLayerNames.SEWAGE_TREATMENT,
            'file': FileNames.EVEL_SN_SEWER_PUMPING_STATION,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_PUMPING_STATION)
        },
        'cbConnectionPoints': {
            'group': EvelGroupLayersNames.EVEL_GENERAL,
            'style': Kliendid.liitumispunktid,
            'layer_name': EvelLayerNames.CONSUMER_POINT,
            'file': FileNames.EVEL_CONSUMER_POINT,
            'table_name': derive_table_name.__func__(FileNames.EVEL_CONSUMER_POINT)
        },
        'cbEasements': {
            'group': EvelGroupLayersNames.EASEMENT,
            'style': Servituudid.servituudid,
            'layer_name': EvelLayerNames.EASEMENT,
            'file': FileNames.LAND_PERM_AREA,
            'table_name': derive_table_name.__func__(FileNames.LAND_PERM_AREA)
        },
        'cbServices': {
            'group': EvelGroupLayersNames.SERVICES,
            'style': None,
            'layer_name': EvelLayerNames.SERVICES,
            'file': FileNames.EVEL_SN_OPERATION,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_OPERATION)
        },
        'cbSNConstant': {
            'group': EvelGroupLayersNames.EVEL_GENERAL,
            'style': None,
            'layer_name': EvelLayerNames.SN_CONSTANT,
            'file': FileNames.EVEL_SN_CONSTANT,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_CONSTANT)
        },
        'cbDevice': {
            'group': EvelGroupLayersNames.EVEL_GENERAL,
            'style': None,
            'layer_name': EvelLayerNames.DEVICE,
            'file': FileNames.EVEL_DEVICE,
            'table_name': derive_table_name.__func__(FileNames.EVEL_DEVICE)
        },
        'cbContract': {
            'group': EvelGroupLayersNames.PROPERTIES,
            'style': None,
            'layer_name': EvelLayerNames.CONTRACT,
            'file': FileNames.EVEL_CONTRACT,
            'table_name': derive_table_name.__func__(FileNames.EVEL_CONTRACT)
        },
        'cbCustomer': {
            'group': EvelGroupLayersNames.CUSTOMER,
            'style': None,
            'layer_name': EvelLayerNames.CUSTOMER,
            'file': FileNames.EVEL_CUSTOMER,
            'table_name': derive_table_name.__func__(FileNames.EVEL_CUSTOMER)
        },
        'cbExternalDoc': {
            'group': EvelGroupLayersNames.SERVICES,
            'style': None,
            'layer_name': EvelLayerNames.EXTERNAL_DOC,
            'file': FileNames.EVEL_EXTERNAL_DOC,
            'table_name': derive_table_name.__func__(FileNames.EVEL_EXTERNAL_DOC)
        },
        'cbApartment': {
            'group': EvelGroupLayersNames.PROPERTIES,
            'style': None,
            'layer_name': EvelLayerNames.APARTMENT,
            'file': FileNames.EVEL_APARTMENT_DATA,
            'table_name': derive_table_name.__func__(FileNames.EVEL_APARTMENT_DATA)
        },
        'cbFlowMeter': {
            'group': EvelGroupLayersNames.FLOW_METER,
            'style': Kliendid.arvestid,
            'layer_name': EvelLayerNames.FLOW_METER,
            'file': FileNames.EVEL_FLOW_METER,
            'table_name': derive_table_name.__func__(FileNames.EVEL_FLOW_METER)
        },
        'cbDemarcationPoint': {
            'group': EvelGroupLayersNames.DEMARCATION_POINT,
            'style': Kliendid.liitumispunktid,
            'layer_name': EvelLayerNames.DEMARCATION_POINT,
            'file': FileNames.EVEL_DEMARCATION_POINT,
            'table_name': derive_table_name.__func__(FileNames.EVEL_DEMARCATION_POINT)
        },
        'cbFirePlug': {
            'group': EvelGroupLayersNames.FIRE_PLUG,
            'style': Veevork.hydrandid,
            'layer_name': EvelLayerNames.FIRE_PLUG,
            'file': FileNames.EVEL_SN_FIRE_PLUG,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_FIRE_PLUG)
        },
        'cbManhole': {
            'group': EvelGroupLayersNames.MANHOLE,
            'style': Kanalisatsioon.kanalikaevud,
            'layer_name': EvelLayerNames.MANHOLE,
            'file': FileNames.EVEL_SN_SEWER_MANHOLE,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_MANHOLE)
        },
        'cbPressureStation': {
            'group': EvelGroupLayersNames.PRESSURE_STATION,
            'style': Veevork.veetootlusjaamad,
            'layer_name': EvelLayerNames.PRESSURE_STATION,
            'file': FileNames.EVEL_SN_WATER_PRESSURE_STATION,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_WATER_PRESSURE_STATION)
        },
        'cbValve': {
            'group': EvelGroupLayersNames.VALVE,
            'style': Kanalisatsioon.solmed,
            'layer_name': EvelLayerNames.VALVE,
            'file': FileNames.EVEL_SN_SEWER_VALVE,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_VALVE)
        },
        'cbTank': {
            'group': EvelGroupLayersNames.TANK,
            'style': Veevork.veetornid,
            'layer_name': EvelLayerNames.TANK,
            'file': FileNames.EVEL_SN_WATER_TANK,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_WATER_TANK)
        },
        'cbProperties': {
            'group': EvelGroupLayersNames.PROPERTIES,
            'style': None,
            'layer_name': EvelLayerNames.PROPERTIES,
            'file': FileNames.EVEL_BUILDING_AREA,
            'table_name': derive_table_name.__func__(FileNames.EVEL_BUILDING_AREA)
        },
        'cbProgram': {
            'group': EvelGroupLayersNames.PROGRAM,
            'style': None,
            'layer_name': EvelLayerNames.PROGRAM,
            'file': FileNames.EVEL_SN_SEWER_DUCT_PROGRAM,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_DUCT_PROGRAM)
        },
        'cbOperation': {
            'group': EvelGroupLayersNames.SERVICES,
            'style': VorgusundmusedAutod.avariiJaHooldustoöd,
            'layer_name': EvelLayerNames.OPERATION,
            'file': FileNames.EVEL_SN_OPERATION,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_OPERATION)
        },
        'cbError': {
            'group': EvelGroupLayersNames.SERVICES,
            'style': VorgusundmusedAutod.avariiJaHooldustoöd,
            'layer_name': EvelLayerNames.ERROR,
            'file': FileNames.EVEL_SN_SEWER_NODE_ERROR,
            'table_name': derive_table_name.__func__(FileNames.EVEL_SN_SEWER_NODE_ERROR)
        },
    }


    @staticmethod
    def get_file_name(checkbox_name):
        mappings = CheckBoxMappings.get_mappings(checkbox_name)
        return mappings.get('file', None)

    @staticmethod
    def get_mappings(checkbox_name):
        return CheckBoxMappings.MAPPINGS.get(checkbox_name, {})

    @staticmethod
    def get_style_filename(checkbox_name):
        mappings = CheckBoxMappings.get_mappings(checkbox_name)
        return mappings.get('style', None)

    @staticmethod
    def get_group_name(checkbox_name):
        mappings = CheckBoxMappings.get_mappings(checkbox_name)
        return mappings.get('group', None)

    @staticmethod
    def get_layer_name(checkbox_name):
        mappings = CheckBoxMappings.get_mappings(checkbox_name)
        return mappings.get('layer_name', None)

    @staticmethod
    def get_table_name(checkbox_name):
        mappings = CheckBoxMappings.get_mappings(checkbox_name)
        return mappings.get('table_name', None)

    @staticmethod
    def create_reverse_table_to_checkbox_map(mappings):
        reverse_map = {}
        for checkbox_name, props in mappings.items():
            table_name = props.get("table_name")
            if table_name:
                reverse_map[table_name] = checkbox_name
        return reverse_map



