
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QListWidgetItem



class ListViewSelectionFlowController:
    """
    Controls the selection flow in three steps:
      1. County selection
      2. Municipality selection
      3. Settlement selection

    Each step disables future elements until the current selection is confirmed.
    """
    # Possible states: "county", "municipality", "settlement", "complete"
    current_state = None

    @classmethod
    def show_message(cls, title, text):
        # In your main project, replace this with your full message display.
        print(f"{title}: {text}")


class ListViewTools:
    def insert_values_to_listView_object(self, object, data):
        """
        Helper function to insert values into a list view and update the widget.
        """
        object.clear()
        for feature in data:
            list_item = QListWidgetItem(feature)
            object.addItem(list_item)
            QCoreApplication.processEvents()
            object.update() 




class CheckboxSelectionReactions:
    @staticmethod
    def toggle_road_selection(state):
        """
        Toggle road selection based on the checkbox state.
        Replace this print statement with your actual logic.
        """
        print(f"Toggle road selection triggered with state: {state}")

    @staticmethod
    def select_all_municipalities(state):
        """
        Select all municipalities if the checkbox is checked.
        Replace this print statement with your actual logic.
        """
        print(f"Select all municipalities triggered with state: {state}")

    @staticmethod
    def select_all_settlements(state):
        """
        Select all settlements if the checkbox is checked.
        Replace this print statement with your actual logic.
        """
        print(f"Select all settlements triggered with state: {state}")

    @staticmethod
    def setup_checkbox_actions(checkbox_actions):
        """
        Setup checkbox-action mapping and connections.
        :param checkbox_actions: A dict mapping QCheckBox instances to their action functions.
        """
        for checkbox, func in checkbox_actions.items():
            # Connect the stateChanged signal to a lambda that calls the function with the state.
            checkbox.stateChanged.connect(lambda state, func=func: func(state))
