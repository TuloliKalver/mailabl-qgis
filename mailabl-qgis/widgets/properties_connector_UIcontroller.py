
from .connector_widget_engine.UI_controllers import PropertiesConnector
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..utils.signal_utils import disable_buttons, reset_buttons
from ..utils.messagesHelper import ModernMessageDialog
class PropertiesConnectorUIController:
    _is_open = False  # Class-level variable to track if the widget is open

    @staticmethod
    def load_properties_connector(self, module, table, button):
        """
        This function updates map selections, manages UI button states, and controls the PropertiesConnector widget.
        Prevents opening multiple instances of the Properties Connector.
        """

        # Check if the Properties Connector is already open
        if PropertiesConnectorUIController._is_open:
            return  # Exit early if it's already open

        PropertiesConnectorUIController._is_open = True  # Mark as open

        button_names = [
            'pbContracts_Connect_properties',
            'pbProjects_Connect_properties',
            'pbEasementsConnectProperties',
            'pbTeostusConnectproperties'
        ]

        # Disable buttons to allow selection time
        disable_buttons(self, button_names, active_button=button)

        # Check if there is a selection in the table
        if PropertiesConnectorUIController._has_selection(table):
            PropertiesConnectorUIController._initialize_properties_connector(self, module, table, button, button_names)
        else:
            PropertiesConnectorUIController._show_no_selection_warning(self, table, button_names, button)
            PropertiesConnectorUIController._is_open = False  # Reset if no selection

    @staticmethod
    def _has_selection(table):
        """
        Checks if there is a selection in the provided table.
        """
        selection_model = table.selectionModel()
        return selection_model.hasSelection()

    @staticmethod
    def _initialize_properties_connector(self, module, table, button, button_names):
        """
        Initializes and loads the properties connector widget.
        """
        self.showMinimized()
        self.properties_connector = PropertiesConnector(table)

        # Connect the widgetClosed signal to handle widget closure
        self.properties_connector.ConnectorWidgetClosed.connect(
            lambda: PropertiesConnectorUIController._on_connector_widget_closed(self, button, button_names)
        )

        # Load the properties connector widget UI with the given module
        self.properties_connector.load_propertiesconnector_widget_ui(module)

    @staticmethod
    def _on_connector_widget_closed(self, button, button_names):
        """
        Handles the logic when the Properties Connector widget is closed.
        Re-enables buttons and resets the widget open flag.
        """
        reset_buttons(self, button, button_names)
        PropertiesConnectorUIController._is_open = False  # Reset the flag so the widget can be opened again

    @staticmethod
    def _show_no_selection_warning(self, table, button_names, button):
        """
        Displays a warning message when no selection is made in the table.
        """
        text = HoiatusTexts().andmed_valimata
        heading = Headings().warningSimple
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)

        # Re-enable buttons since no selection was made
        reset_buttons(self, button, button_names)
