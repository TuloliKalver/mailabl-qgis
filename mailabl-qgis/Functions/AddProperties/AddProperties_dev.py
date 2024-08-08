from ..Tools import tableFunctions
from qgis.core import QgsProject
from ...Functions.AddProperties.CompareChangesForExistingData import ChangeComparer
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...config.settings import SettingsDataSaveAndLoad


import json

table_data = tableFunctions

class AddProperties_dev:
    @staticmethod
    def check_for_duplicates_and_add_only_matches(self):
        # Load necessary layers and prepare setup

        active_layer_name,input_layer_name = AddProperties_dev.load_import_and_activ_layers(self)

        button = self.pbConfirm_action
        table_properties = self.tblvResults_Confirm
        table_streets = self.tblvResults_streets_Confirm
        table_target = self.tblNew
        tab_widget = self.tabWidget_Propertie_list

        cadastral_numbers = AddProperties_dev.cadastral_number_list_from_tables(self, table_properties, table_streets)

        print("Cadastral numbers combined:")
        print(cadastral_numbers)

        # TODO: Check if cadastral_numbers already on the active layer
        existing_numbers_on_active_layer = AddProperties_dev.get_existing_numbers_on_active_layer(self)
        existing_numbers_in_mylabl = AddProperties_dev.get_existing_numbers_in_mylabl(self, existing_numbers_on_active_layer)

        print("existing number on active layer")
        print(existing_numbers_on_active_layer)

        print("existing numbers in Mylabl")
        print(existing_numbers_in_mylabl)

        numbers_to_add, numbers_in_layer = AddProperties_dev.compare_layers_for_update(cadastral_numbers, existing_numbers_on_active_layer)


        if numbers_in_layer:
            AddProperties_dev.update_active_layer_data(numbers_in_layer, active_layer_name, input_layer_name)

            # TODO: Check if cadastral numbers are already in "mylabl"
            existing_numbers_in_mylabl = AddProperties_dev.get_existing_numbers_in_mylabl(self, numbers_in_layer, input_layer_name)

        for number in numbers_to_add:
            if number in existing_numbers_in_mylabl:
                # TODO: Prompt user with data from "mylabl" and the data to be imported
                user_accepted = AddProperties_dev.prompt_user_for_data(self, number, existing_numbers_in_mylabl[number])

                if user_accepted:
                    # TODO: Update values in "mylabl"
                    AddProperties_dev.update_mylabl(self, number)
                    # TODO: Update values in active layer property data
                    #AddProperties_dev.update_active_layer(self, number)
                    # TODO: Handle archived properties
                    AddProperties_dev.handle_archived_properties(self, number)
                else:
                    # User declined the change - pass
                    continue
            else:
                # TODO: Import into "mylabl" as before
                AddProperties_dev.import_into_mylabl(self, number)

        clear_sub_string = ""
        active_layer_name, input_layer_name = AddProperties_dev.load_import_and_activ_layers(self)
        # Get references to the layers
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        active_layer.setSubsetString(clear_sub_string)
        button.blockSignals(False)

    @staticmethod
    def compare_layers_for_update(cadastral_numbers, existing_numbers_on_active_layer):
        numbers_to_add = [num for num in cadastral_numbers if num not in existing_numbers_on_active_layer]
        numbers_in_layer = [num for num in cadastral_numbers if num in existing_numbers_on_active_layer]
        print("numbers_to_add:")
        print(numbers_to_add)
        print("numbers in layer:")
        print(numbers_in_layer)
        return numbers_to_add, numbers_in_layer

    @staticmethod
    def cadastral_number_list_from_tables(self, table_properties, table_streets):
        data_properties = table_data.RemoveNonSelectedRowsFromTable(self, table_properties)
        print("data_properties:")
        print(data_properties)
        data_streets = table_data.RemoveNonSelectedRowsFromTable(self, table_streets)
        print("data_streets:")
        print(data_streets)

        # Initialize an empty list to store the cadastral numbers
        cadastral_numbers = []

        # Extract numbers from data_properties
        for key, value in data_properties.items():
            data = json.loads(value)
            number = data["cadastralUnit"]["number"]
            cadastral_numbers.append(number)

        # Extract numbers from data_streets
        for key, value in data_streets.items():
            data = json.loads(value)
            number = data["cadastralUnit"]["number"]
            cadastral_numbers.append(number)
        return cadastral_numbers

    @staticmethod
    def get_existing_numbers_on_active_layer(self):

        active_layer_cadastral_numbers = []
        active_layer_name, input_layer_name = AddProperties_dev.load_import_and_activ_layers(self)
        # Get references to the layers
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        AddProperties_dev.copy_layer_filter(active_layer_name, input_layer_name)
        field_name = Katastriyksus.tunnus

        # Retrieve the cadastral numbers from the active layer
        for feature in active_layer.getFeatures():
            if feature[field_name] is not None:
                active_layer_cadastral_numbers.append(feature[field_name])

        # Placeholder method to get existing numbers on the active layer
        return active_layer_cadastral_numbers

    #TODO
    @staticmethod
    def get_existing_numbers_in_mylabl(self, property_numbers, input_layer_name):

        # Placeholder method to get existing numbers in "mylabl"
        return {}

    #TODO
    @staticmethod
    def prompt_user_for_data(self, number, existing_data):
        # Placeholder method to prompt user with data from "mylabl" and the data to import
        # Simulate user decision (for demonstration purposes)
        return True

    #TODO
    @staticmethod
    def update_mylabl(self, number):
        # Placeholder method to update values in "mylabl"
        pass





    @staticmethod
    def update_active_layer_data(properties_to_update, active_layer_name, input_layer_name):
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if active_layer is None or input_layer is None:
            print("Error: One or both layers not found.")
            return

        mfn = Katastriyksus.tunnus

        # Dictionary to map tunnus to features in active layer for quick lookup
        active_layer_features = {f[mfn]: f for f in active_layer.getFeatures()}

        changes = []

        # Collect changes that will be made
        for input_feature in input_layer.getFeatures():
            tunnus_value = input_feature[mfn]
            if tunnus_value in active_layer_features:
                active_feature = active_layer_features[tunnus_value]

                attr_changes = {}
                geom_changed = False

                for field_name in input_feature.fields().names():
                    if field_name in active_feature.fields().names() and field_name != mfn:
                        if input_feature[field_name] != active_feature[field_name]:
                            attr_changes[field_name] = (active_feature[field_name], input_feature[field_name])

                if input_feature.geometry() is not None and not input_feature.geometry().equals(active_feature.geometry()):
                    geom_changed = True

                if attr_changes or geom_changed:
                    changes.append((tunnus_value, attr_changes, geom_changed))

        if not changes:
            print("No changes to update.")
            return

        # Show changes summary and ask for user confirmation
        if not ChangeComparer.show_changes_summary(changes):
            print("Update cancelled by user.")
            return

        # Start an edit session on the active layer
        active_layer.startEditing()

        # Apply changes
        for tunnus_value, attr_changes, geom_changed in changes:
            active_feature = active_layer_features[tunnus_value]

            for field_name, (old_value, new_value) in attr_changes.items():
                active_feature.setAttribute(field_name, new_value)

            if geom_changed:
                input_feature = input_layer.getFeature(active_feature.id())
                active_feature.setGeometry(input_feature.geometry())

            active_layer.updateFeature(active_feature)

        # Commit changes
        if active_layer.commitChanges():
            print("Successfully updated the active layer with data from the input layer.")
        else:
            print("Failed to update the active layer.")

    #TODO
    @staticmethod
    def handle_archived_properties(self, number):
        # Placeholder method to handle archived properties
        pass

    #TODO
    @staticmethod
    def import_into_mylabl(self, number):
        # Placeholder method to import into "mylabl"
        pass



    @staticmethod
    def copy_layer_filter(active_layer_name, input_layer_name):

        # Get references to the layers
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]

        if input_layer is None or active_layer is None:
            print("Error: One or both layers not found.")
            return

        # Retrieve the filter from the input layer
        input_layer_filter_expression = input_layer.subsetString()

        if input_layer_filter_expression is None:
            print("Error: No filter found on the input layer.")
            return

        active_layer.setSubsetString(input_layer_filter_expression)



    @staticmethod
    def get_list_of_selected_cadastral_numbers(self, table_properties, table_streets):
        data_properties = table_data.RemoveNonSelectedRowsFromTable(self, table_properties)
        print("data_properties:")
        print(data_properties)
        data_streets = table_data.RemoveNonSelectedRowsFromTable(self, table_streets)
        print("data_streets:")
        print(data_streets)

        # Initialize an empty list to store the cadastral numbers
        cadastral_numbers = []

        # Extract numbers from data_properties
        for key, value in data_properties.items():
            data = json.loads(value)
            number = data["cadastralUnit"]["number"]
            cadastral_numbers.append(number)

        # Extract numbers from data_streets
        for key, value in data_streets.items():
            data = json.loads(value)
            number = data["cadastralUnit"]["number"]
            cadastral_numbers.append(number)
        return cadastral_numbers

    @staticmethod
    def load_import_and_activ_layers(self):
        active_cadastral_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        #print(f"active layer: {active_cadastral_layer_name}")
        input_layer_name = SettingsDataSaveAndLoad.load_SHP_inputLayer_name(self)
        return active_cadastral_layer_name,input_layer_name


    def find_missing_or_outdated_items(self, item_list, graphql_data):
        returned_items = set()
        outdated_items = []
        # Extract unique item numbers and their data from the GraphQL data
        returned_data = {}
        for result in graphql_data:
            if 'node' in result and 'cadastralUnit' in result['node']:
                unit = result['node']['cadastralUnit']
                number = unit['number']
                returned_data[number] = unit
                returned_items.add(number)

        # Find items that are missing or outdated
        missing_items = []
        for item in item_list:
            number = item['number']
            if number not in returned_items:
                missing_items.append(item)
            else:
                # Check if the data is outdated
                returned_item = returned_data[number]
                if not self.is_data_up_to_date(item, returned_item):
                    outdated_items.append(item)

        return missing_items, outdated_items

    def is_data_up_to_date(self, item, returned_item):
        las_updated = 'muudet'


        for key, value in item.items():
            if key != 'number' and returned_item.get(key) != value:
                return False
        return True