
from PyQt5.QtCore import Qt
from qgis.core import QgsProject, QgsLayerTreeGroup
from qgis.core import QgsDataSourceUri, QgsProviderRegistry
from qgis.core import QgsVectorLayerExporter, QgsDataSourceUri

from PyQt5.QtWidgets import (
    QDialog, QSizePolicy,
    QPushButton, QFrame, QCheckBox
    )
from ...processes.OnFirstLoad.AddSetupLayers import SetupLayers
from PyQt5.uic import loadUi
from ...config.settings import Filepaths
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...KeelelisedMuutujad.EVEL_lang_module import EvelGroupLayersNames, EvelSubGroupLayersNames, FileNames, CheckBoxMappings
from .evel_common import  EVEL_Creator, EVELCancel
from .LayerVariables.evel_easements import LayerFunctions



pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()

class EVELTools:

    @staticmethod
    def load_EVEL_setup():

        ui_file_path = Filepaths.get_EVEL_tools()
        Dialog = loadUi(ui_file_path)  # Use self.Dialog_EVEL here
        Dialog.setAttribute(Qt.WA_DeleteOnClose)

        save_button = Dialog.pbSave
        cancel_button = Dialog.pbCancel

        Dialog.show()

        #EVELGroupGenerator.create_evel_group_layer()
        EVELCheckboxes.get_checkbox_info(Dialog)

        Dialog.gbConnectionDetails.setEnabled(False)
        Dialog.gbUserCreditentials.setEnabled(False)
        Dialog.pbTestConnection.setEnabled(False)

        Dialog.cbGepackage.toggled.connect(lambda: EVELTools.handle_database_type_change(Dialog))
        Dialog.cbSQLDatabase.toggled.connect(lambda: EVELTools.handle_database_type_change(Dialog))
        Dialog.cbPostgreDatabase.toggled.connect(lambda: EVELTools.handle_database_type_change(Dialog))

        # Trigger initial state
        EVELTools.handle_database_type_change(Dialog)

        # Connect checkbox state change to the method
        #checkbox.stateChanged.connect(lambda: EVELTools.update_button_state)

        Dialog.pbTestConnection.clicked.connect(lambda: PostGisDatabase.test_supabase_connection(Dialog))

        save_button.clicked.connect(lambda: EVELTools.on_save_button_clicked(Dialog))
        cancel_button.clicked.connect(lambda: EVELTools.on_cancel_button_clicked(Dialog))
        result = Dialog.exec_()

        if result == QDialog.Accepted:

            return True
        else:
            group_layer = EvelGroupLayersNames.EVEL_MAIN
            EVELCancel.remove_group_and_contents(group_layer)
    
            return None


    @staticmethod
    def handle_database_type_change(Dialog):
        sender = Dialog.sender()
        
        if sender == Dialog.cbGepackage and sender.isChecked():
            Dialog.cbSQLDatabase.setChecked(False)
            Dialog.cbPostgreDatabase.setChecked(False)
            Dialog.gbConnectionDetails.setEnabled(False)
            Dialog.gbUserCreditentials.setEnabled(False)
            Dialog.pbTestConnection.setEnabled(False)

        elif sender == Dialog.cbSQLDatabase and sender.isChecked():
            Dialog.cbGepackage.setChecked(False)
            Dialog.cbPostgreDatabase.setChecked(False)
            Dialog.gbConnectionDetails.setEnabled(True)
            Dialog.gbUserCreditentials.setEnabled(False)
            Dialog.pbTestConnection.setEnabled(True)

        elif sender == Dialog.cbPostgreDatabase and sender.isChecked():
            Dialog.cbGepackage.setChecked(False)
            Dialog.cbSQLDatabase.setChecked(False)
            Dialog.gbConnectionDetails.setEnabled(True)
            Dialog.gbUserCreditentials.setEnabled(True)
            Dialog.pbTestConnection.setEnabled(True)


    @staticmethod
    def closeEvent(self, event):
        event.reject()  # Allow the window to close
    @staticmethod
    def on_save_button_clicked(Dialog):
        Dialog.accept()
    @staticmethod
    def on_cancel_button_clicked(Dialog):
        print("cancel button clicked")
        Dialog.reject()
        





class EVELCheckboxes:
    def get_checkbox_info(Dialog):
        water_checkbox = getattr(Dialog, 'cbWater', None)
        sewage_checkbox = getattr(Dialog, 'cbSewage', None)
        rainwater_checkbox = getattr(Dialog, 'cbRainwater', None)
        pumpstation_checkbox = getattr(Dialog, 'cbPumpstation', None)
        treatment_checkbox = getattr(Dialog, 'cbSewTreatment', None)
        connectionpoint_checkbox = getattr(Dialog, 'cbConnectionPoints', None)
        easement_checkbox = getattr(Dialog, 'cbEasements', None)
        services_checkbox = getattr(Dialog, 'cbServices', None)
        snconstant_checkbox = getattr(Dialog, 'cbSNConstant', None)
        device_checkbox = getattr(Dialog, 'cbDevice', None)  # new
        contract_checkbox = getattr(Dialog, 'cbContract', None)  # new                
        customer_checkbox = getattr(Dialog, 'cbCustomer', None)  # new
        external_doc_checkbox = getattr(Dialog, 'cbExternalDoc', None)  # new
        apartment_checkbox = getattr(Dialog, 'cbApartment', None)  # new
        flow_meter_checkbox = getattr(Dialog, 'cbFlowMeter', None)  # new
        demarcation_point_checkbox = getattr(Dialog, 'cbDemarcationPoint', None)  # new
        fire_plug_checkbox = getattr(Dialog, 'cbFirePlug', None)  # new
        manhole_checkbox = getattr(Dialog, 'cbManhole', None)  # new
        pressure_station_checkbox = getattr(Dialog, 'cbPressureStation', None)  # new
        valve_checkbox = getattr(Dialog, 'cbValve', None)  # new
        properties_checkbox = getattr(Dialog, 'cbProperties', None)  # new
        tank_checkbox = getattr(Dialog, 'cbTank', None)  # new
        program_checkbox = getattr(Dialog, 'cbProgram', None)  # new
        operation_checkbox = getattr(Dialog, 'cbOperation', None)  # new
        error_checkbox = getattr(Dialog, 'cbError', None)  # new

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
        setup_layer_name = SetupLayers().main_group

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


class PostGisDatabase:

    @staticmethod
    def get_connection_info(dialog):
        host = dialog.leHost.text().strip()
        port = dialog.lePort.text().strip()
        dbname = dialog.leDataBase.text().strip()
        user = dialog.leUserName.text().strip()
        password = dialog.lePass.text().strip()

        # 🔒 Validation: Prevent empty fields
        if not all([host, port, dbname, user, password]):
            print("⚠️ Missing connection details. Please fill in all fields.")
            return None

        # 🔧 Build connection URI
        uri = QgsDataSourceUri()
        uri.setConnection(host, port, dbname, user, password)
        return uri

    @staticmethod
    def test_supabase_connection(dialog):
        uri = PostGisDatabase.get_connection_info(dialog)
        if not uri:
            return False

        schema_name = "evel"  # Your desired schema
        try:
            conn_info = uri.uri()
            provider = QgsProviderRegistry.instance().providerMetadata("postgres")
            connection = provider.createConnection(conn_info, {})  # No options

            # 🧪 Check if schema exists
            schemas = connection.schemas()
            #print("📚 Available schemas:", schemas)

            if schema_name not in schemas:
                #print(f"➕ Schema '{schema_name}' does not exist. Creating...")
                ddl = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
                connection.executeSql(ddl)
                #print(f"✅ Schema '{schema_name}' created.")
            
            # 📦 List public schema tables
            tables = connection.tables(schema=schema_name)
            table_names = [t.tableName() for t in tables]
            print("📦 Public schema tables:", table_names)

            Evel_table_names = CheckBoxMappings.create_reverse_table_to_checkbox_map(CheckBoxMappings.MAPPINGS)
            for evel_table, checkbox_name in Evel_table_names.items():
                print(f"🔎 Checking availability of '{evel_table}' table in {schema_name} schema...")
                if evel_table in table_names:
                    print(f"✅ '{evel_table}' table is available in {schema_name} schema.")

                    # 🔘 Try to check the checkbox if it exists
                    checkbox_widget = dialog.findChild(QCheckBox, checkbox_name)
                    if checkbox_widget:
                        checkbox_widget.setChecked(True)
                        print(f"☑️ Checkbox '{checkbox_name}' has been checked.")
                    else:
                        print(f"⚠️ Could not find checkbox widget with objectName='{checkbox_name}'")

                else:
                    print(f"ℹ️ '{evel_table}' table not found in {schema_name} schema.")
                
        except Exception as e:
            print("❌ Connection failed. Reason hidden for security.")
            return False




    def export_layer_to_supabase(layers, dialog):
        uri = PostGisDatabase.get_connection_info(dialog)
        if not uri:
            return False
        
        uri.setSrid("EPSG:3301")  # Adjust this if needed
        schema = "evel"

        for layer in layers:
            if not layer.isValid():
                print("❌ Invalid layer.")
                return False

            table_name = layer.name().lower().replace(" ", "_")  # Use safe table name
            geometry_column = "geom"

            uri.setDataSource(schema, table_name, geometry_column)

            # Export
            options = QgsVectorLayerExporter.ExportOptions()
            result, error_message = QgsVectorLayerExporter.exportLayer(
                layer, uri.uri(), "postgres", layer.crs(), False, options
            )

            if result == QgsVectorLayerExporter.NoError:
                print(f"✅ Layer '{layer.name()}' exported to Supabase successfully.")
                return True
            else:
                print(f"❌ Export failed: {error_message}")
                return False
