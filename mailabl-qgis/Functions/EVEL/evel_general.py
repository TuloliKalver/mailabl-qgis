from PyQt5.QtCore import QObject, pyqtSignal
from qgis.core import QgsProject, QgsLayerTreeGroup
from ...processes.OnFirstLoad.AddSetupLayers import SetupLayers
from PyQt5.uic import loadUi
from ...config.settings import Filepaths
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...KeelelisedMuutujad.EVEL_lang_module import EvelGroupLayersNames, EvelSubGroupLayersNames, FileNames
from .evel_common import  EVEL_Creator, EVELCancel
from .LayerVariables.evel_easements import LayerFunctions



pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()

class EVELTools(QObject):
    widgetClosed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.widget_EVEL = None

    def load_widget(self):
        ui_file_path = Filepaths.get_EVEL_tools()
        print(f"File path {ui_file_path}")
        widget_EVEL = loadUi(ui_file_path)  # Use self.widget_EVEL here
        save_button = widget_EVEL.pbSave
        cancel_button = widget_EVEL.pbCancel

        widget_EVEL.show()

        #EVELGroupGenerator.create_evel_group_layer()
        EVELCheckboxes.get_checkbox_info(widget_EVEL)
        pushbutton = widget_EVEL.pbGenerateVrtLayer
        checkbox = widget_EVEL.cbEasements

        # Initial state based on the checkbox
        pushbutton.setEnabled(checkbox.isChecked())

        # Connect checkbox state change to the method
        #checkbox.stateChanged.connect(lambda: EVELTools.update_button_state)

        save_button.clicked.connect(lambda: EVELTools.on_save_button_clicked(self, widget_EVEL))
        cancel_button.clicked.connect(lambda: EVELTools.on_cancel_button_clicked(self, widget_EVEL))

        # Connect closeEvent method to handle window close event
        widget_EVEL.closeEvent = self.closeEvent

    def closeEvent(self, event):
        group_layer = EvelGroupLayersNames.EVEL_MAIN
        EVELCancel.remove_group_and_contents(group_layer)
        event.accept()  # Allow the window to close
        
    def on_save_button_clicked(self, widget_EVEL):
        widget_EVEL.accept()
        
    def on_cancel_button_clicked(self, widget_EVEL):
        print("cancel button clicked")
        group_layer = EvelGroupLayersNames.EVEL_MAIN
        EVELCancel.remove_group_and_contents(group_layer)
        widget_EVEL.reject()
        

class EVELCheckboxes:
    def get_checkbox_info(widget):
        water_checkbox = getattr(widget, 'cbWater', None)
        sewage_checkbox = getattr(widget, 'cbSewage', None)
        rainwater_checkbox = getattr(widget, 'cbRainwater', None)
        pumpstation_checkbox = getattr(widget, 'cbPumpstation', None)
        treatment_checkbox = getattr(widget, 'cbSewTreatment', None)
        connectionpoint_checkbox = getattr(widget, 'cbConnectionPoints', None)
        easement_checkbox = getattr(widget, 'cbEasements', None)
        services_checkbox = getattr(widget, 'cbServices', None)
        snconstant_checkbox = getattr(widget, 'cbSNConstant', None)
        device_checkbox = getattr(widget, 'cbDevice', None)  # new
        contract_checkbox = getattr(widget, 'cbContract', None)  # new                
        customer_checkbox = getattr(widget, 'cbCustomer', None)  # new
        external_doc_checkbox = getattr(widget, 'cbExternalDoc', None)  # new
        apartment_checkbox = getattr(widget, 'cbApartment', None)  # new
        flow_meter_checkbox = getattr(widget, 'cbFlowMeter', None)  # new
        demarcation_point_checkbox = getattr(widget, 'cbDemarcationPoint', None)  # new
        fire_plug_checkbox = getattr(widget, 'cbFirePlug', None)  # new
        manhole_checkbox = getattr(widget, 'cbManhole', None)  # new
        pressure_station_checkbox = getattr(widget, 'cbPressureStation', None)  # new
        valve_checkbox = getattr(widget, 'cbValve', None)  # new
        properties_checkbox = getattr(widget, 'cbProperties', None)  # new
        tank_checkbox = getattr(widget, 'cbTank', None)  # new
        program_checkbox = getattr(widget, 'cbProgram', None)  # new
        operation_checkbox = getattr(widget, 'cbOperation', None)  # new
        error_checkbox = getattr(widget, 'cbError', None)  # new

        from ...KeelelisedMuutujad.EVEL_lang_module import UICheckboxes
        # Define texts for checkboxes
        checkbox_texts = {
            water_checkbox: UICheckboxes.water_checkbox,
            sewage_checkbox: UICheckboxes.sewage_checkbox,
            rainwater_checkbox: UICheckboxes.rainwater_checkbox,
            pumpstation_checkbox: UICheckboxes.pumpstation_checkbox,
            treatment_checkbox: UICheckboxes.treatment_checkbox,
            connectionpoint_checkbox: UICheckboxes.connectionpoint_checkbox,
            easement_checkbox: UICheckboxes.easement_checkbox,
            services_checkbox: UICheckboxes.services_checkbox,
            snconstant_checkbox: UICheckboxes.snconstant_checkbox,
            # New checkboxes
            device_checkbox: UICheckboxes.device_checkbox,  # new
            contract_checkbox: UICheckboxes.contract_checkbox,  # new
            customer_checkbox: UICheckboxes.customer_checkbox,  # new
            external_doc_checkbox: UICheckboxes.external_doc_checkbox,  # new
            apartment_checkbox: UICheckboxes.apartment_checkbox,  # new
            flow_meter_checkbox: UICheckboxes.flow_meter_checkbox,  # new
            demarcation_point_checkbox: UICheckboxes.demarcation_point_checkbox,  # new
            fire_plug_checkbox: UICheckboxes.fire_plug_checkbox,  # new
            manhole_checkbox: UICheckboxes.manhole_checkbox,  # new
            pressure_station_checkbox: UICheckboxes.pressure_station_checkbox,  # new
            valve_checkbox: UICheckboxes.valve_checkbox,  # new
            tank_checkbox: UICheckboxes.tank_checkbox,  # new
            properties_checkbox: UICheckboxes.properties_checkbox,  # new
            program_checkbox: UICheckboxes.program_checkbox,  # new
            operation_checkbox: UICheckboxes.operation_checkbox,  # new
            error_checkbox: UICheckboxes.error_checkbox,  # new
        }


        from .LayerVariables.evel_sn_constant import SnPublicFunctions
        # Define lambdas to connect checkboxes to functions (to be implemented)
        checkbox_functions = {
            water_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(water_checkbox),
            sewage_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(sewage_checkbox),
            rainwater_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(rainwater_checkbox),
            pumpstation_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(pumpstation_checkbox),
            treatment_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(treatment_checkbox),
            connectionpoint_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(connectionpoint_checkbox),
            easement_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(easement_checkbox),
            services_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(services_checkbox),
            
            snconstant_checkbox: lambda: SnPublicFunctions.generate_SN_layer(snconstant_checkbox), #lambda: EVEL_Creator.generate_EVEL_model_layer(snconstant_checkbox),
            # New checkboxes
            device_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(device_checkbox),
            contract_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(contract_checkbox),
            customer_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(customer_checkbox),
            external_doc_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(external_doc_checkbox),
            apartment_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(apartment_checkbox),
            flow_meter_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(flow_meter_checkbox),
            demarcation_point_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(demarcation_point_checkbox),
            fire_plug_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(fire_plug_checkbox),
            manhole_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(manhole_checkbox),
            pressure_station_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(pressure_station_checkbox),
            valve_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(valve_checkbox),
            tank_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(tank_checkbox),
            properties_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(properties_checkbox),
            program_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(program_checkbox),
            operation_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(operation_checkbox),
            error_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(error_checkbox),
        }


        # Create checkboxes_info dictionary
        checkboxes_info = {}
        for checkbox, text in checkbox_texts.items():
            if checkbox:
                checkboxes_info[checkbox] = (text, checkbox_functions.get(checkbox))
        EVELCheckboxes.update_checkboxes(checkboxes_info)
        return checkboxes_info

    @staticmethod
    def update_checkboxes(checkboxes_info):
        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                checkbox.setText(text)
                if connect_function is None:
                    checkbox.setEnabled(False)
                else:
                    checkbox.setEnabled(True)
                    checkbox.clicked.connect(connect_function)

    
class EVELGroupGenerator:
    # Function to get or create a group by name
    def get_or_create_group(parent, group_name):
        group = parent.findGroup(group_name)
        if group is None:
            group = parent.addGroup(group_name)
        return group

    # Function to create the EVEL group layer inside the setup layer
    def create_evel_group_layer():
        # Create the setup layer group
        # Initialize the QGIS project instance
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        setup_layer_name = SetupLayers().mailabl_main_group_name

        setup_layer_group = EVELGroupGenerator.get_or_create_group(root, setup_layer_name)

        # Create the main group within the setup layer group
        main_group = EVELGroupGenerator.get_or_create_group(setup_layer_group, EvelGroupLayersNames.EVEL_MAIN)

        # Create dictionaries to store main and subgroups
        main_group_dict = {}
        sub_group_dict = {}


        # Create main group layers inside the main group (setup_layer)
        for group_name in EvelGroupLayersNames.__dict__.values():
            print(f"group_name: {group_name}")
            if isinstance(group_name, str) and group_name != EvelGroupLayersNames.EVEL_MAIN:
                group = EVELGroupGenerator.get_or_create_group(main_group, group_name)
                main_group_dict[group_name] = group

        # Create subgroups within main groups
        for key, sub_group_name in EvelSubGroupLayersNames.__dict__.items():
            if not key.startswith("__") and not callable(sub_group_name):
                for main_group_name, main_group in main_group_dict.items():
                    sub_group = EVELGroupGenerator.get_or_create_group(main_group, sub_group_name)
                    sub_group_dict[sub_group_name] = sub_group

        # A helper function to add layers to the appropriate group or subgroup
        def add_layer_to_group(layer_name, group):
            # Assuming layers are already loaded in the project
            layers = project.mapLayersByName(layer_name)
            if layers:
                layer = layers[0]
                group.addLayer(layer)

        filenames = FileNames.filenames
        
        # Add layers to respective groups and subgroups
        for filename in filenames:
            matched = False
            for main_group_name, main_group in main_group_dict.items():
                if main_group_name.lower() in filename:
                    add_layer_to_group(filename, main_group)
                    matched = True
                    break
            if not matched:
                for sub_group_name, sub_group in sub_group_dict.items():
                    if sub_group_name.lower() in filename:
                        add_layer_to_group(filename, sub_group)
                        matched = True
                        break
            if not matched:
                print(f"Layer {filename} did not match any group and was not added.")

        print("Layers have been organized into their respective groups and subgroups.")
