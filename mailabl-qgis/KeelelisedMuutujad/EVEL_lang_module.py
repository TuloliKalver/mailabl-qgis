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

class EvelLayerNames:
    EASEMENT = "evel_Servituut"
    WATER = "evel_Vesi"
    SEWAGE = "evel_Kanal"
    SERVICES = "evel_Töökäsud"
    SEWER = 'Kanalisatsioon'
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
    PROPERTIES = "Kinnistud"
    PROGRAM = 'Programmid'

class EvelGroupLayersNames:
    EVEL_MAIN = 'EVEL_Mudel'
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

class CheckBoxGroups:
    # Mapping checkboxes to main groups
    checkbox_to_group = {
        UICheckboxes.water_checkbox: EvelGroupLayersNames.WATER,
        UICheckboxes.sewage_checkbox: EvelGroupLayersNames.SEWER,
        UICheckboxes.rainwater_checkbox: EvelGroupLayersNames.SEWER,
        UICheckboxes.pumpstation_checkbox: EvelGroupLayersNames.PUMPING_STATION,
        UICheckboxes.treatment_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.connectionpoint_checkbox: EvelGroupLayersNames.CONSUMER_POINT,
        UICheckboxes.easement_checkbox: EvelGroupLayersNames.EASEMENT,
        UICheckboxes.services_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.device_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.contract_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.customer_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.external_doc_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.apartment_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.flow_meter_checkbox: EvelGroupLayersNames.FLOW_METER,
        UICheckboxes.demarcation_point_checkbox: EvelGroupLayersNames.DEMARCATION_POINT,
        UICheckboxes.fire_plug_checkbox: EvelGroupLayersNames.FIRE_PLUG,
        UICheckboxes.manhole_checkbox: EvelGroupLayersNames.MANHOLE,
        UICheckboxes.pressure_station_checkbox: EvelGroupLayersNames.PRESSURE_STATION,
        UICheckboxes.valve_checkbox: EvelGroupLayersNames.VALVE,
        UICheckboxes.tank_checkbox: EvelGroupLayersNames.TANK,
        UICheckboxes.properties_checkbox: EvelGroupLayersNames.PROPERTIES,
        UICheckboxes.program_checkbox: EvelGroupLayersNames.PROGRAM,
        UICheckboxes.operation_checkbox: EvelGroupLayersNames.SERVICES,
        UICheckboxes.error_checkbox: EvelGroupLayersNames.SERVICES,
    }

class FileNames:
    # List of filenames
    EVEL_ATTACHED_DOC_CUSTOMER = "evel_attached_doc_customer_name.py"
    EVEL_APARTMENT_DATA = "evel_apartment_data_name.py"
    EVEL_ATTACHED_DOC_LAND_PREM_AREA = "evel_attached_doc_land_prem_area_name.py"
    EVEL_ATTACHED_DOC_PLAN = "evel_attached_doc_plan_name.py"
    EVEL_ATTACHED_DOC_SN_CONSUMER_POINT = "evel_attached_doc_sn_consumer_point_name.py"
    EVEL_ATTACHED_DOC_SN_ERROR_REPORT = "evel_attached_doc_sn_error_report_name.py"
    EVEL_ATTACHED_DOC_SN_SEWER_DUCT = "evel_attached_doc_sn_sewer_duct_name.py"
    EVEL_ATTACHED_DOC_SN_SEWER_NODE = "evel_attached_doc_sn_sewer_node_name.py"
    EVEL_ATTACHED_DOC_SN_WATER_DUCT = "evel_attached_doc_sn_water_duct_name.py"
    EVEL_ATTACHED_DOC_SN_WATER_NODE = "evel_attached_doc_sn_water_node_name.py"
    EVEL_SN_SEWER_DUCT = "evel_sn_sewer_duct_name.py"
    EVEL_CONSUMER_POINT = "evel_consumer_point_name.py"
    EVEL_DEVICE = "evel_device_name.py"
    EVEL_DEMARCATION_POINT = "evel_demarcation_point_name.py"
    EVEL_CUSTOMER_CONSUMERPOINT = "evel_customer_consumerpoint_name.py"
    EVEL_CUSTOMER = "evel_customer_name.py"
    EVEL_CONTRACT = "evel_contract_name.py"
    EVEL_EXTERNAL_DOC = "evel_external_doc_name.py"
    EVEL_EXTERNAL_DOC_TYPE = "evel_external_doc_type_name.py"
    EVEL_FLOW_METER = "evel_flow_meter_name.py"
    EVEL_SN_CONSTANT = "evel_sn_constant_name.py"
    EVEL_SN_FIRE_PLUG = "evel_sn_fire_plug_name.py"
    EVEL_SN_OPERATION = "evel_sn_operation_name.py"
    EVEL_SN_SEWER_BRANCH = "evel_sn_sewer_branch_name.py"
    EVEL_SN_SEWER_DUCT_ERROR = "evel_sn_sewer_duct_error_name.py"
    EVEL_SN_SEWER_DUCT_PROGRAM = "evel_sn_sewer_duct_program_name.py"
    EVEL_SN_SEWER_MANHOLE = "evel_sn_sewer_manhole_name.py"
    EVEL_SN_SEWER_NODE = "evel_sn_sewer_node_name.py"
    EVEL_SN_SEWER_NODE_ERROR = "evel_sn_sewer_node_error_name.py"
    EVEL_SN_SEWER_NODE_PROGRAM = "evel_sn_sewer_node_program_name.py"
    EVEL_SN_SEWER_OTHER_NODE = "evel_sn_sewer_other_node_name.py"
    EVEL_SN_SEWER_PUMP = "evel_sn_sewer_pump_name.py"
    EVEL_SN_SEWER_PUMPING_STATION = "evel_sn_sewer_pumping_station_name.py"
    EVEL_SN_SEWER_VALVE = "evel_sn_sewer_valve_name.py"
    EVEL_SN_SEWER_VALVE_STATE_LOG = "evel_sn_sewer_valve_state_log_name.py"
    EVEL_SN_WATER_BRANCH = "evel_sn_water_branch_name.py"
    EVEL_SN_WATER_DUCT = "evel_sn_water_duct_name.py"
    EVEL_SN_WATER_DUCT_ERROR = "evel_sn_water_duct_error_name.py"
    EVEL_SN_WATER_DUCT_PROGRAM = "evel_sn_water_duct_program_name.py"
    EVEL_SN_WATER_MANHOLE = "evel_sn_water_manhole_name.py"
    EVEL_SN_WATER_NODE = "evel_sn_water_node_name.py"
    EVEL_SN_WATER_NODE_ERROR = "evel_sn_water_node_error_name.py"
    EVEL_SN_WATER_NODE_PROGRAM = "evel_sn_water_node_program_name.py"
    EVEL_SN_WATER_OTHER_NODE = "evel_sn_water_other_node_name.py"
    EVEL_SN_WATER_PRESSURE_STATION = "evel_sn_water_pressure_station_name.py"
    EVEL_SN_WATER_PUMP = "evel_sn_water_pump_name.py"
    EVEL_SN_WATER_PUMPING_STATION = "evel_sn_water_pumping_station_name.py"
    EVEL_SN_WATER_TANK = "evel_sn_water_tank_name.py"
    EVEL_SN_WATER_VALVE = "evel_sn_water_valve_name.py"
    EVEL_SN_WATER_VALVE_STATE_LOG = "evel_sn_water_valve_state_log_name.py"
    EVEL_BUILDING_AREA = "evel_building_area_name.py"
    EVEL_SN_OPERATION = "evel_sn_operation_name.py"

class CheckBoxFileMapping:
    # Mapping files to corresponding checkboxes
    file_to_checkbox = {
        FileNames.EVEL_ATTACHED_DOC_CUSTOMER: UICheckboxes.services_checkbox,
        FileNames.EVEL_APARTMENT_DATA: UICheckboxes.apartment_checkbox,
        FileNames.EVEL_ATTACHED_DOC_LAND_PREM_AREA: UICheckboxes.easement_checkbox,
        FileNames.EVEL_ATTACHED_DOC_PLAN: UICheckboxes.services_checkbox,
        FileNames.EVEL_ATTACHED_DOC_SN_CONSUMER_POINT: UICheckboxes.connectionpoint_checkbox,
        FileNames.EVEL_ATTACHED_DOC_SN_ERROR_REPORT: UICheckboxes.error_checkbox,
        FileNames.EVEL_ATTACHED_DOC_SN_SEWER_DUCT: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_ATTACHED_DOC_SN_SEWER_NODE: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_ATTACHED_DOC_SN_WATER_DUCT: UICheckboxes.water_checkbox,
        FileNames.EVEL_ATTACHED_DOC_SN_WATER_NODE: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_SEWER_DUCT: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_CONSUMER_POINT: UICheckboxes.connectionpoint_checkbox,
        FileNames.EVEL_DEVICE: UICheckboxes.device_checkbox,
        FileNames.EVEL_DEMARCATION_POINT: UICheckboxes.demarcation_point_checkbox,
        FileNames.EVEL_CUSTOMER_CONSUMERPOINT: UICheckboxes.connectionpoint_checkbox,
        FileNames.EVEL_CUSTOMER: UICheckboxes.customer_checkbox,
        FileNames.EVEL_CONTRACT: UICheckboxes.contract_checkbox,
        FileNames.EVEL_EXTERNAL_DOC: UICheckboxes.external_doc_checkbox,
        FileNames.EVEL_EXTERNAL_DOC_TYPE: UICheckboxes.external_doc_checkbox,
        FileNames.EVEL_FLOW_METER: UICheckboxes.flow_meter_checkbox,
        FileNames.EVEL_SN_CONSTANT: UICheckboxes.snconstant_checkbox,
        FileNames.EVEL_SN_FIRE_PLUG: UICheckboxes.fire_plug_checkbox,
        FileNames.EVEL_SN_OPERATION: UICheckboxes.operation_checkbox,
        FileNames.EVEL_SN_SEWER_BRANCH: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_SN_SEWER_DUCT_ERROR: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_SN_SEWER_DUCT_PROGRAM: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_SN_SEWER_MANHOLE: UICheckboxes.manhole_checkbox,
        FileNames.EVEL_SN_SEWER_NODE: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_SN_SEWER_NODE_ERROR: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_SN_SEWER_NODE_PROGRAM: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_SN_SEWER_OTHER_NODE: UICheckboxes.sewage_checkbox,
        FileNames.EVEL_SN_SEWER_PUMP: UICheckboxes.pumpstation_checkbox,
        FileNames.EVEL_SN_SEWER_PUMPING_STATION: UICheckboxes.pumpstation_checkbox,
        FileNames.EVEL_SN_SEWER_VALVE: UICheckboxes.valve_checkbox,
        FileNames.EVEL_SN_SEWER_VALVE_STATE_LOG: UICheckboxes.valve_checkbox,
        FileNames.EVEL_SN_WATER_BRANCH: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_DUCT: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_DUCT_ERROR: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_DUCT_PROGRAM: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_MANHOLE: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_NODE: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_NODE_ERROR: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_NODE_PROGRAM: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_OTHER_NODE: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_PRESSURE_STATION: UICheckboxes.pressure_station_checkbox,
        FileNames.EVEL_SN_WATER_PUMP: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_PUMPING_STATION: UICheckboxes.water_checkbox,
        FileNames.EVEL_SN_WATER_TANK: UICheckboxes.tank_checkbox,
        FileNames.EVEL_SN_WATER_VALVE: UICheckboxes.valve_checkbox,
        FileNames.EVEL_SN_WATER_VALVE_STATE_LOG: UICheckboxes.valve_checkbox,
        FileNames.EVEL_BUILDING_AREA: UICheckboxes.properties_checkbox,
        FileNames.EVEL_SN_OPERATION: UICheckboxes.operation_checkbox,
    }
