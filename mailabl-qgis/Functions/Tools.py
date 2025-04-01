import json
import uuid


from ..queries.python.property_data import add_properties
from PyQt5.QtCore import QCoreApplication
from pprint import pprint
from PyQt5.uic import loadUi
from ..config.ui_directories import PathLoaderSimple
from ..KeelelisedMuutujad.messages import Headings
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..utils.messagesHelper import ModernMessageDialog

pealkiri = Headings()

data_handler = add_properties



class TableSelections:
    @staticmethod
    def selected_rows(table):
        if table is None:
            #print("Andmeid ei ole valitud.")            
            text = ("Andmeid ei ole valitud")
            heading = pealkiri.warningSimple
            ModernMessageDialog.Info_messages_modern(heading,text)
            return None
        
        selection_model = table.selectionModel()
        selected_indexes = selection_model.selectedRows()

        # Collect selected row indexes
        selected_row_indexes = [index.row() for index in selected_indexes]
        #print(f"indexes that are selected before deleting: {selected_row_indexes}")

        # Remove non-selected rows
        model = table.model()
        for row in range(model.rowCount(), -1, -1):  # Iterate in reverse order to avoid issues with row removal
            if row not in selected_row_indexes:
                model.removeRow(row)
        
        # Update selected indexes after removal
        selected_indexes = selection_model.selectedRows()
        selected_row_indexes = [index.row() for index in selected_indexes]
        #print(f"indexes that are selected after deleting: {selected_row_indexes}")
        
        return selected_row_indexes



    
class tableFunctions:
    def RemoveNonSelectedRowsFromTable(self, table): #returns row, index and cadastral number
        selected_indexes = TableSelections.selected_rows(table)
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        counter = 0
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(len(selected_indexes))  # Set the maximum value of the progress bar
        progress_widget.show()
        progress_widget.setWindowTitle("Eemaldan mittevaltud read")
        
        # Dictionary to store data
        data = {}
        
        for row_index in selected_indexes:
            print(f"in for loop row_index: {row_index}")
            tunnus_column = 0



            index = table.model().index(row_index, tunnus_column)  # Assuming column 0 contains the cadastral unit number
            each_data = tableFunctions.extract_cadastralNrData_from_table(self, index, table)
            
            #each_data = tableFunctions.extract_cadastralNrData_from_table(self, row_index, table)
            if each_data:
                # Use the selected row index as the ID
                each_data_id = row_index
                # Add the ID and data to the dictionary
                data[each_data_id] = each_data
                
                counter += 1
                progress_bar.setValue(counter)
                QCoreApplication.processEvents()
        #print(f"in 'Functions/Tools.py' data is: {data}")
        # Assuming 'indexes' is a list of QModelIndex objects representing selected rows
        return data


    #Extracts table data and assigns row index to data!
    def extract_table_indexes_and_cadasters_from_data(data):
        #print(f"values of data {data}")
        CadastralUnits = []
        RowIndexes_and_cadastralUnits = []
        total = 0
        for item_index, item_json in data.items():
            try:
                # Parse the JSON string to a dictionary
                item_dict = json.loads(item_json)
                #print(f"item_dict {item_dict}")
                # Access the "number" value
                cadaster_value = item_dict['cadastralUnit']['number']
                
                # Append the item ID and "number" value to the list
                CadastralUnits.append(cadaster_value)
                
                # Append the item ID and "number" value as a dictionary to the list
                RowIndexes_and_cadastralUnits.append({'index': item_index, 'number': cadaster_value})
    
                total +=1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for item with ID {item_index}: {e}")

        #print("before outbut number values:" )
        #pprint(number_values)
        return CadastralUnits, total, RowIndexes_and_cadastralUnits

    #Extracts table data and assigns row index to data!
    def for_deleting_extract_table_indexes_and_cadasters_from_data(data):
        #print(f"values of data {data}")
        CadastralUnits = []
        RowIndexes_and_cadastralUnits = []
        total = 0
        for item_index, item_json in data.items():
            try:
                # Parse the JSON string to a dictionary
                item_dict = json.loads(item_json)
                #print(f"item_dict {item_dict}")
                # Access the "number" value
                cadaster_value = item_dict['cadastralUnit']['number']
                
                # Append the item ID and "number" value to the list
                CadastralUnits.append(cadaster_value)
                
                # Append the item ID and "number" value as a dictionary to the list
                RowIndexes_and_cadastralUnits.append({'index': item_index, 'number': cadaster_value})
    
                total +=1
                QCoreApplication.processEvents()
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for item with ID {item_index}: {e}")

        #print("before outbut number values:" )
        #pprint(number_values)
        return CadastralUnits



    
    def return_id(self, index, table):
        # Assuming you want data from column 0 (index 0 in Python)
        id_column_index = 0
        # Retrieve the data from the selected row's column 0
        id_data = table.model().data(table.model().index(index.row(), id_column_index))
        # If id_data is None or empty, return an empty string
        if id_data is None or id_data == "":
            return ""
        #print(id_data)
        # Now you have the ID value from the selected row, column 0
        #return str(id_data)
        return (id_data)
    
    
    def custom_encoder(obj):
        if isinstance(obj, str):
            return obj.encode('utf-8').decode('unicode-escape')
        return obj
        

    
    def extract_property_data(self, index, table):
        # Assuming table is a QTableView and has a QStandardItemModel set
        model = table.model()

        # Get the header data, which contains column names
        header_data = []
        for col in range(model.columnCount()):
            header_item = model.horizontalHeaderItem(col)
            if header_item is not None:
                header_data.append(header_item.text())

        # Define column names
        cadastral_unit_number_column = Katastriyksus.tunnus 
        immovable_number_column = Katastriyksus.hkood #"HKOOD"
        county_column = Katastriyksus.mk_nimi #"MK_NIMI"
        state_column = Katastriyksus. ov_nimi #"OV_NIMI"
        city_column = Katastriyksus.ay_nimi #"AY_NIMI"
        street_column = Katastriyksus.l_aadress #"L_AADRESS"
        firstRegistrationDate_column = Katastriyksus.registr #"REGISTR"
        lastUpdated_column = Katastriyksus.muudet #"MUUDET"
        size_column = Katastriyksus.pindala #"PINDALA"
        unit_column = None#"REG_YHIK"  uues andmestikus alates 03.06.2024 ei ole enam kasutuses 


        # Get the column indexes based on column names
        cadastral_unit_number_index = header_data.index(cadastral_unit_number_column) if cadastral_unit_number_column in header_data else -1
        immovable_number_index = header_data.index(immovable_number_column) if immovable_number_column in header_data else -1
        county_index = header_data.index(county_column) if county_column in header_data else -1
        state_index = header_data.index(state_column) if state_column in header_data else -1
        city_index = header_data.index(city_column) if city_column in header_data else -1
        street_index = header_data.index(street_column) if street_column in header_data else -1
        firstRegistrationDate_index = header_data.index(firstRegistrationDate_column) if firstRegistrationDate_column in header_data else -1
        lastUpdated_index = header_data.index(lastUpdated_column) if lastUpdated_column in header_data else -1
        size_index = header_data.index(size_column) if size_column in header_data else -1
        unit_index = header_data.index(unit_column) if unit_column in header_data else -1

        # Retrieve property data from the selected row's columns
        street_input = table.model().data(table.model().index(index.row(), street_index))
        street_data = data_handler.get_address_details_from_street(street_input)
        immovable_number = table.model().data(table.model().index(index.row(), immovable_number_index))
        cadastral_unit_number = table.model().data(table.model().index(index.row(), cadastral_unit_number_index))
        county = table.model().data(table.model().index(index.row(), county_index))
        state = table.model().data(table.model().index(index.row(), state_index))
        city = table.model().data(table.model().index(index.row(), city_index))
        firstRegistrationDate = table.model().data(table.model().index(index.row(), firstRegistrationDate_index))               
        lastUpdated = table.model().data(table.model().index(index.row(), lastUpdated_index)) 
        size_raw = table.model().data(table.model().index(index.row(), size_index))
        unit_raw = table.model().data(table.model().index(index.row(), unit_index))
        #unit = AreaUnit.convert_to_area_unit(unit_raw)        
        size, unit = AreaUnit.process_size_and_unit(size_raw, unit_raw)
        # Extract house number from street_data
        house_number = street_data.get('house', '')

        # Create the required dictionary for GraphQL query
        input_data = {
            "immovableNumber": immovable_number,
            "cadastralUnit": {
                "number": cadastral_unit_number,
                "firstRegistration": firstRegistrationDate,
                "lastUpdated": lastUpdated
            },
            "address": {
                "street": street_data['street'],
                "houseNumber": house_number, 
                "city": city,
                "state": state,
                "county": county
                },    
            "area": {
                "size": size,
                "unit": unit
            }
        }
        
        # Convert the dictionary to a JSON string with special characters preserved        
        encoded_input_data = json.dumps(input_data, default=tableFunctions.custom_encoder, ensure_ascii=False)
        # Print the JSON-like string
        #print(f"encoded_input_data:{encoded_input_data}")
        #return (encoded_input_data)
        #print(input_data)
        return encoded_input_data
    
    
    def extract_cadastralNrData_from_table(self, indexes, table):
        #print(f"index in 'extract_cadastralNrData_from_table': {indexes}")
        # Assuming table is a QTableView and has a QStandardItemModel set
        selected_indexes = TableSelections.selected_rows(table)
        #print(f"selected_indexes: {selected_indexes}")

        model = table.model()
        units = []
        # Get the header data, which contains column names
        header_data = []
        for col in range(model.columnCount()):
            header_item = model.horizontalHeaderItem(col)
            if header_item is not None:
                header_data.append(header_item.text())
                QCoreApplication.processEvents()

        # Define column names
        cadastral_unit_number_column = Katastriyksus.tunnus 
        # Get the column indexes based on column names
        cadastral_unit_number_index = header_data.index(cadastral_unit_number_column) if cadastral_unit_number_column in header_data else -1
        #cadastral_unit_number_index = 0
        # Retrieve property data from the selected row's columns
        for index in selected_indexes:
            cadastral_unit_number = table.model().data(table.model().index(indexes.row(), cadastral_unit_number_index))
            
            # Create the required dictionary for GraphQL query
            input_data = {
                "cadastralUnit": {
                    "number": cadastral_unit_number,
                }
            }
            units.append(input_data)
        encoded_input_data = json.dumps(input_data, default=tableFunctions.custom_encoder, ensure_ascii=False)
        #return (encoded_input_data)
        #print(input_data)
        return encoded_input_data


    

    def find_missing_items(item_list, graphql_data):
        #print("Item list")
        #pprint(item_list)
        
        #print("graphql data")
        #pprint(graphql_data)
        
        returned_items = set()

        # Extract unique item numbers from the GraphQL data
        for result in graphql_data:
            if 'node' in result and 'cadastralUnit' in result['node']:
                number = result['node']['cadastralUnit']['number']
                returned_items.add(number)

        # Find items that are not returned
        missing_items = [item for item in item_list if item not in returned_items]

        return missing_items

class Convertor:
    M = "SQM"
    H = "H"

    def convert_to_area_unit(value):
        if value == "M":
            return Convertor.M
        elif value == "H":
            return Convertor.H
        else:
            # Handle invalid input, if necessary
            return Convertor.M  # Default value

    def process_size_and_unit(size, unit_raw):
        try:
            size = float(size)  # Convert size to float
        except ValueError:
            # Handle the case where size is not a valid number
            return "Invalid Size"

        if unit_raw == "H":
            value = size / 1000  # Divide size by 1000 if unit is "M"
        elif unit_raw == "M":
            value = size
        else:
            # Handle invalid unit_raw values
            return "Invalid Unit"

        # Convert the result to text before returning
        return str(value)

class AreaUnit:
    M = "SQM"
    H = "H"

    def convert_to_area_unit(value):
        if value == "M":
            return AreaUnit.M
        elif value == "H":
            return AreaUnit.H
        else:
            # Handle invalid input, if necessary
            return AreaUnit.M  # Default value

    def process_size_and_unit(size, unit_raw):
        try:
            size = float(size)  # Convert size to float
        except ValueError:
            # Handle the case where size is not a valid number
            return "Invalid Size"

        if unit_raw == "H":
            value = size / 1000  # Divide size by 1000 if unit is "H"
        elif unit_raw == "M":
            value = size
        elif unit_raw is None:
            value = size
            unit_raw = AreaUnit.M
        else:
            # Handle invalid unit_raw values
            return "Invalid Unit"

        return str(value), unit_raw

    
class propertyUsages:
    def extract_intendedUse_data(self, index, table):
        # Assuming table is a QTableView and has a QStandardItemModel set
        model = table.model()

        # Get the header data, which contains column names
        header_data = []
        for col in range(model.columnCount()):
            header_item = model.horizontalHeaderItem(col)
            if header_item is not None:
                header_data.append(header_item.text())

        # Create the required list of dictionaries for GraphQL query
        input_data = []
        num_siht_items = 3
        siht_field = Katastriyksus.siht1 #siht1
        prts_field = Katastriyksus.so_prts1 #so_prts1
        siht_base = siht_field[:-1]
        prts_base = prts_field[:-1]

        for i in range(1, num_siht_items + 1):
            siht_name = f"{siht_base}{i}"
            so_prts_name = f"{prts_base}{i}"

            siht_index = header_data.index(siht_name) if siht_name in header_data else -1
            so_prts_index = header_data.index(so_prts_name) if so_prts_name in header_data else -1

            if siht_index != -1 and so_prts_index != -1:
                siht_data = table.model().data(table.model().index(index.row(), siht_index))
                so_prts_data = table.model().data(table.model().index(index.row(), so_prts_index))

                # Convert the "percentage" values to integers
                so_prts_data = int(so_prts_data) if so_prts_data.isdigit() else 0

                if siht_data == "NULL":
                    continue
                
                intended_use = {
                    "sortOrder": i,
                    "name": siht_data,
                    "percentage": so_prts_data,
                }

                input_data.append(intended_use)

        return input_data