#from ..Tools import tableFunctions
from qgis.core import QgsProject
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
#from ...config.settings import SettingsDataSaveAndLoad
#from .UpdateAndArchive import UpdateAndArchive

import json

class AddProperties_dev:
    @staticmethod
    def check_for_duplicates_and_add_only_matches(self):

        active_layer_name,input_layer_name = AddProperties_dev.load_import_and_activ_layers(self)

        button = self.pbConfirm_action
        table_properties = self.tblvResults_Confirm
        table_streets = self.tblvResults_streets_Confirm
        table_target = self.tblNew
        tab_widget = self.tabWidget_Propertie_list

        # Extracts all cadastral numbers from the list!
        cadastral_numbers = AddProperties_dev.cadastral_number_list_from_tables(self, table_properties, table_streets)

        print("Cadastral numbers combined:")
        print(cadastral_numbers)

        # TODO: Check if cadastral_numbers already on the active layer
        existing_numbers_on_active_layer = AddProperties_dev.get_existing_numbers_on_active_layer(self)
        #existing_numbers_in_mylabl = AddProperties_dev.get_existing_numbers_in_mylabl(existing_numbers_on_active_layer, input_layer_name)

        print("existing number on active layer")
        print(existing_numbers_on_active_layer)

        #print("existing numbers in Mylabl")
        #print(existing_numbers_in_mylabl)

        numbers_to_add, numbers_in_layer = AddProperties_dev.compare_layers_for_update(cadastral_numbers, existing_numbers_on_active_layer)


        if numbers_in_layer:
            UpdateAndArchive.update_active_layer_data(self, numbers_in_layer, active_layer_name, input_layer_name)
            
            
        
        for number in numbers_to_add:
            # TODO: Handle archived properties
            #AddProperties_dev.handle_archived_properties(self, number)
            # TODO: Import into "mylabl" as before
            AddProperties_dev.import_into_mylabl(self, number)
            

        clear_sub_string = ""
        #active_layer_name, input_layer_name = AddProperties_dev.load_import_and_activ_layers(self)
        # Get references to the layers
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        active_layer.setSubsetString(clear_sub_string)
        button.blockSignals(False)




    @staticmethod
    def get_existing_numbers_on_active_layer(self):

        """
        This function retrieves and returns a list of cadastral numbers from the active layer 
        that correspond to the same geographical area or selection criteria currently applied 
        to the import layer. 

        By applying the same filter or selection criteria from the import layer onto the active layer, 
        the function ensures that the cadastral numbers returned reflect only those features in the 
        active layer that match the area of interest as defined by the import layer.
        """

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
    def handle_archived_properties(self, number):
        # Placeholder method to handle archived properties
        pass





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