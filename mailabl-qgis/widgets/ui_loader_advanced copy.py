import os

#testing imports remove in real life!
from ..utils.utilys import random_string
import random



plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))


class Directories:
    # Declare catalogues and links
    # Main directory
    plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Status bar widget folder
    widgets_folder = "widgets"
    WStatusBar = "WStatusBar.ui"
    WConfirmation = "Confirmation_list.ui"

    # Full paths for the widgets
    WstatusBar_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, WStatusBar))
    WConfirmation_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, WConfirmation))

    # Define widget names
    WIDGET_NAMES = {
        "WStatusBar.ui": WStatusBar,
        "Confirmation_list.ui": WConfirmation
        # Add more widgets as needed
    }


class loader():
    
    # Generate dummy data
    false_items_c = [random_string() for _ in range(3)]
    true_items_C = [random_string() for _ in range(3)]
    false_values = [random.randint(1, 100) for _ in range(3)]
    Row_indexes_and_cadastralUnits_properties = [
        {'index': random.randint(1, 10), 'number': random_string()} for _ in range(3)
    ]
    # Print generated data
    print("false_items_c:", false_items_c)
    print("true_items_C:", true_items_C)
    print("false_values:", false_values)
    print("Row_indexes_and_cadastralUnits_properties:", Row_indexes_and_cadastralUnits_properties)


    def load_ui_WConfirmation(self, false_itemsC, true_itemsC, 
                            false_values,
                            table,
                            RowIndexes_and_cadastralUnits_properties,
                            input_layer_name):
        print("Loading UI for Confirmation")

        # Simulate loading UI file
        print("UI file loaded")

        # Simulate setting up UI with specific data
        print(f"Setting up UI with data: {false_itemsC}, {true_itemsC}")

        # Simulate waiting for user interaction
        print("Waiting for user interaction")

        # Simulate user interaction result
        result = "Accepted"  # Change this based on your testing

        if result == "Accepted":
            print("User pressed OK")
            # Simulate clearing table and inserting items
            self.clear_table_from_inMailabl_rows(input_layer_name, table, RowIndexes_and_cadastralUnits_properties, [])
            print("Selected items inserted into the table")
        else:
            print("User pressed Cancel")

    def clear_table_from_inMailabl_rows(self, input_layer_name, table_1, number_values_with_ids_1, returned_cadastral_units):
        print("Clearing table from inMailabl rows")

        # Simulate iterating through items
        for item_s1 in number_values_with_ids_1:
            # Simulate processing each item
            print(f"Processing item: {item_s1}")

            index_value = item_s1['index']
            number_value = item_s1['number']

            if number_value in returned_cadastral_units:
                print(f"Number {number_value} found in returned_cadastral_units")
                # Simulate removing rows from the table
                print(f"Removing row with index {index_value} from the table")

        # Simulate updating the table view
        print("Table view updated")

        # Simulate additional processing
        print("Additional processing after clearing the table")
