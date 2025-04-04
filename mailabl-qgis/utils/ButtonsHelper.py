#ButtonHelpers.py
from ..Common.app_state import Expressions

from PyQt5.QtWidgets import QPushButton, QListWidget

class ButtonHelper:
    dialog = None  # Class-level variable to store the dialog reference

    @staticmethod
    def set_dialog(main_dialog):
        """Sets the main dialog reference for ButtonHelper."""
        ButtonHelper.dialog = main_dialog

    @staticmethod
    def get_buttons_for_current_flow(flow):
        """
        Retrieves the list of buttons that should be enabled for the current flow state.

        :return: List of button names (strings) or an empty list if none are defined.
        """

        # Retrieve the configuration for the current flow state (default to empty list if not found)
        config = Expressions.FLOW_EXPRESSION_MAPPING.get(flow, {})

        buttons_enable = config.get('buttons_enable', [])
        list_wiget = config.get ('listWidget', [])
        buttons_disable = config.get('buttons_disable', [])
        print(f"Available list_widgets: {list_wiget}")
        #print(f"Available buttons: {buttons_enable}")
        return buttons_enable, buttons_disable, list_wiget

    @staticmethod
    def get_button_objects(button_names):
        """
        Finds button objects in the stored dialog based on a list of button names.

        :param button_names: List of button names (object names in Qt Designer).
        :return: List of QPushButton objects.
        """
        if ButtonHelper.dialog is None:
            #print("❌ Error: Dialog has not been set in ButtonHelper!")
            return []

        button_objects = []
        #print(f"Trying to find buttons {button_names}")
        for name in button_names:
            button = ButtonHelper.dialog.findChild(QPushButton, name)
            if button:
                button_objects.append(button)

        return button_objects
    @staticmethod
    def get_list_widget_objects(list_widget_names):
        """
        Finds list_widget objects in the stored dialog based on a list of button names.

        :param list_widget_names: List of listWidget names (object names in Qt Designer).
        :return: List of QListWidget objects.
        """
        if ButtonHelper.dialog is None:
            #print("❌ Error: Dialog has not been set in ButtonHelper!")
            return []

        List_widget_objects = []
        
        for name in list_widget_names:
            widget = ButtonHelper.dialog.findChild(QListWidget, name)
            if widget:
                List_widget_objects.append(widget)

        return List_widget_objects
    



       
