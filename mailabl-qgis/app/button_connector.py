#app/button_connector.py

from ..Functions.EVEL.evel_general import EVELTools
from ..KeelelisedMuutujad.Maa_amet_fields import RemapPropertiesLayer
from ..widgets.connector_widget_engine.UI_controllers import PropertiesConnector
from ..KeelelisedMuutujad.modules import Module

from ..utils.signal_utils import execute_with_block
from ..widgets.properties_connector_UIcontroller import PropertiesConnectorUIController

class SettingsModuleButtonConnector:
    def button_controller(self):
        button_greate_EVEL = getattr(self, 'pbGreateEVEL', None)
        update_dataframe = getattr(self, 'pbUpdateToNewDataframe', None)

        # Define lambdas to connect buttons to functions
        button_functions = {
            button_greate_EVEL: lambda: execute_with_block(button_greate_EVEL, EVELTools.load_widget, self),
            update_dataframe: lambda: execute_with_block(update_dataframe, RemapPropertiesLayer().update_attribute_table)
        }

        # Connect buttons to functions
        for button, function in button_functions.items():
            PropertiesConnector.connect_button(button, function)

        # Populate the buttons list
        buttons = [button_greate_EVEL, update_dataframe]

        return buttons

class PropertiesModuleButtonConnector:
    @staticmethod
    def button_controller(self):
        table_projects = getattr(self, 'tblMailabl_projects', None)
        table_contracts = getattr(self, 'ContractView', None)
        table_easements = getattr(self, 'tweasementView', None)

        button_contracts = getattr(self, 'pbContracts_Connect_properties', None)
        button_projects = getattr(self, 'pbProjects_Connect_properties', None)
        button_easements = getattr(self, 'pbEasementsConnectProperties', None)

        # Define lambdas to connect buttons to functions
        button_functions = {
            button_contracts: lambda: execute_with_block(button_contracts, PropertiesConnectorUIController.load_properties_connector, self, Module.CONTRACT, table_contracts, button_contracts),
            button_projects: lambda: execute_with_block(button_projects, PropertiesConnectorUIController.load_properties_connector, self, Module.PROJECT, table_projects, button_projects),
            button_easements: lambda: execute_with_block(button_easements, PropertiesConnectorUIController.load_properties_connector, self, Module.EASEMENT, table_easements, button_easements),
        }

        # Connect buttons to functions
        for button, function in button_functions.items():
            PropertiesConnector.connect_button(button, function)

        # Populate the buttons list
        buttons = [button_contracts, button_easements, button_projects]

        return buttons
