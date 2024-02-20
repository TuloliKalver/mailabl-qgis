import time
import os
import re
import json
import requests
from requests.exceptions import Timeout
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QHeaderView
from .DataLoading_classes import GraphQLQueryLoader, Graphql_properties
from .responses import handleResponse
from .query_tools import requestBuilder
from ...config.ui_directories import PathLoaderSimple


items_to_fetch = 100


plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))
#Status bar widget folder
widgets_folder = "widgets"
process_folder = "processes"
importProcess_folder = "ImportProcesses"
widgets_path = os.path.join(plugin_dir, process_folder, importProcess_folder, widgets_folder, "WStatusBar.ui")


class Properties:

    def get_property_CSC(self):
        query_loader = Graphql_properties()
        query = GraphQLQueryLoader.load_query_properties(self,query_loader.Q_Property_CSC)
        
        total_fetched = 0
        current_page = 1
        last_page = None  # Set this value based on the server's response
        end_cursor = None  # Initialize end_cursor before the loop
        fetched_items = []  # Initialize an empty list to store fetched items

        while (not items_to_fetch or total_fetched < items_to_fetch) and (not last_page or current_page <= last_page):
            variables = {
                "first": 50,  # Fetch 50 items per query
                "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            }
            response = requestBuilder.construct_and_send_request(self, query, variables)
            if response.status_code == 200:
                data = response.json()
                fetched_data = data.get("data", {}).get("properties", {}).get("edges", [])
                pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")
                last_page = pageInfo.get("lastPage")
                # Append the fetched_data to the fetched_items list
                fetched_items.extend(fetched_data)
                # Update total_fetched by adding the length of fetched_data
                total_fetched += len(fetched_data)
                if total_fetched >= items_to_fetch:
                    break  # Exit the loop if desired_total_items are reached
            else:
                #print(f"Error: {response.status_code}")
                return None  # Return None if there's an error in the response
            # Move to the next page
            current_page += 1
        return fetched_items  # Return the fetched items after the loop

    def get_properties(self, progress_bar):
        # Set up the progress bar
        #progress_bar.setVisible(True)
        progress_bar.setValue(41)

        query_loader = Graphql_properties()
        query = GraphQLQueryLoader.load_query_properties(self,query_loader.Q_All_Properties)

        total_fetched = 0
        current_page = 1
        last_page = None  # Set this value based on the server's response
        end_cursor = None  # Initialize end_cursor before the loop
        
        fetched_items = [] # Initialize an empty list to store fetched items

        progress_bar.setValue(50)

        while (not items_to_fetch or total_fetched < items_to_fetch) and (not last_page or current_page <= last_page):
            variables = {
                "first": 50,  # Fetch 50 items per query
                "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            }

            progress_bar.setValue(55)
            # Send the POST request to the GraphQL endpoint
            response = requestBuilder.construct_and_send_request(self, query, variables)
            progress_bar.setValue(65)
            #start do use data
            if response.status_code == 200:
                data = response.json()
                #print(f"Data {data}")
                fetched_data = data.get("data", {}).get("properties", {}).get("edges", [])
                #print(f"Peamised kinnistud: {fetched_data}")
                
                pageInfo = data.get("data",{}).get("properties",{}).get("pageInfo",{})#.get("currentPage")
                #print(f"Current page: '{pageInfo}")
                end_cursor = pageInfo.get("endCursor")
                #print(f"End cursor: {end_cursor}")
                last_page = pageInfo.get("lastPage")
                #print(f"Last page: {last_page}")
                
                # Append the fetched_data to the fetched_items list
                fetched_items.extend(fetched_data)
                
                total_fetched += len(fetched_data)
                
                if total_fetched >= items_to_fetch:
                    break  # Exit the loop if desired_total_items are reached
                
            else:
                print(f"Error: {response.status_code}")
                return None

            # Move to the next page
            current_page += 1
            
            # Return only the desired number of items
        return fetched_items#[:desired_total_items]

    def properties_list(self):
        model = QStandardItemModel()

        # Set header labels
        header_labels = ['ID','Vastutav isik','Kataster', 'Aadress', 'Pindala','Looja', 'Lisatud']
        

        model.setHorizontalHeaderLabels(header_labels)
        # Set column width mode to adjust to contents
        self.tblOfContents.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        data = Properties.get_properties(self)

        # Display the fetched properties
        for property_item in data:
            property_node = property_item.get("node", {})
            id_item = QStandardItem(str(property_node.get("id", "")))
            address_item = QStandardItem(property_node.get("displayAddress", ""))
            x_item = QStandardItem(property_node.get("cadastralUnit", {}).get("number",""))
            size_item = QStandardItem(str(property_node.get("area", {}).get("size", "")))
            creator_item = QStandardItem(str(property_node.get("creator", {}).get("displayName", "N/A")) if property_node.get("creator") else QStandardItem("N/A"))
            created_item = QStandardItem(str(property_node.get("createdAt", "")))

        # Extract manager information
            managers = property_node.get("managers", {}).get("edges", [])
            manager_names = [manager["node"]["displayName"] for manager in managers]
            manager_item = QStandardItem(", ".join(manager_names)) if manager_names else QStandardItem("N/A")

        # Extract contact information
            contacts = property_node.get("contacts", {}).get("edges", [])
            contact_items = []

            for contact in contacts:
                contact_node = contact.get("node", {})
                contact_display_name = contact_node.get("displayName", "N/A")
                contact_type = contact_node.get("type", "N/A")
                    
                if contact_type:
                    contact_items.append(f"{contact_display_name} ({contact_type})")
                else:
                    contact_items.append(contact_display_name)

            contact_item = QStandardItem(", ".join(contact_items)) if contact_items else QStandardItem("N/A")

            # Convert the list of strings to a list of QStandardItems
            property_items = [id_item, 
                            x_item, 
                            manager_item,
                            address_item, 
                            size_item, 
                            creator_item, 
                            created_item
                            ]
            
            # Append the list of QStandardItems to the table model
            model.appendRow(property_items)
            
        return model
    
    def properties_list_for_deleting(self, progress_bar):
        progress_bar.setValue(10)
        model = QStandardItemModel()

        # Set header labels
        header_labels = ['ID', 'HKT kood', 'Kataster', 'Aadress', 'Esmane registrering', 'Mailabli lisatud', 'Looja',]

        model.setHorizontalHeaderLabels(header_labels)

        try:
            # Attempt to fetch data from Properties.get_properties
            data = Properties.get_properties(self, progress_bar)
            if data is None:
                raise Exception("Error: No data retrieved from Properties.get_properties.")
            
            progress_bar.setValue(1)

            # Display the fetched properties
            index = 1
            for property_item in data:
                property_node = property_item.get("node", {})
                id_item = QStandardItem(str(property_node.get("id", "")))
                immovableNumber_item = QStandardItem(str(property_node.get("immovableNumber","")))
                address_item = QStandardItem(property_node.get("displayAddress", ""))
                cadastralUnit_item = QStandardItem(property_node.get("cadastralUnit", {}).get("number",""))
                firstRegistration_item = QStandardItem(property_node.get("cadastralUnit", {}).get("firstRegistration",""))
                size_item = QStandardItem(str(property_node.get("area", {}).get("size", "")))
                creator_item = QStandardItem(str(property_node.get("creator", {}).get("displayName", "N/A")) if property_node.get("creator") else QStandardItem("N/A"))
                created_item = QStandardItem(str(property_node.get("createdAt", "")))
                # Your existing code to populate the table model

                # Convert the list of strings to a list of QStandardItems
                property_items = [id_item, 
                                immovableNumber_item,
                                cadastralUnit_item, 
                                address_item, 
                                firstRegistration_item,
                                created_item,
                                creator_item 
                                ]

                # Append the list of QStandardItems to the table model
                model.appendRow(property_items)
                index += 1
                progress_bar.setValue(index)

        except Exception as e:
            # Handle exceptions here
            print(f"Error: {e}")
            # You can raise or handle the exception as appropriate for your use case.
            # For now, just printing the error message.

        return model

    def county_list_model(self):
        data = Properties.get_property_CSC(self)
        unique_counties = set()  # Initialize an empty set to store unique county names
        
        # Display the fetched properties
        for property_item in data:
            property_node = property_item.get("node", {})
            county_name = property_node.get("address", {}).get("county")
            
            # Check if county_name is not None and not already in the set
            if county_name:
                unique_counties.add(county_name)
        
        # Convert the set of unique county names to QStandardItem objects
        county_items = [QStandardItem(county) for county in unique_counties]

        return county_items

    def county_list_text(self):
        data = Properties.get_property_CSC(self)
        property_items = []  # Initialize an empty list to store county names
        
        # Display the fetched properties
        for property_item in data:
            property_node = property_item.get("node", {})
            county_item = QStandardItem(str(property_node.get("address", {}).get("county", ""))) if property_node.get("address") else QStandardItem()
            county_text = county_item.text()  # Get the text of the QStandardItem
            
            if county_text:  # Only add non-empty county names to the list
                property_items.append(county_text)
        
        return property_items

class WhereProperties:
    @staticmethod
    def Return_Mailabl_County_list_with_where_COUNTY_NOT_IN(self, county_items):
        query_loader = Graphql_properties()
        query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_Address_County)
        #print("Query added")

        items_for_page = 1  # Adjust this to your desired value
        end_cursor = None  # Initialize end_cursor before the loop

        variables = {
            "first": items_for_page,  # Fetch 50 items per query
            "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            "where": {
                    "OR": [
                            {
                            "column": "COUNTY",
                            "operator": "NOT_IN",
                            "value": county_items
                            }
                        ]
                    }
                }
        
        response = requestBuilder.construct_and_send_request(self, query, variables)
        county_names = []
        #start do use data
        if response.status_code == 200:
            data = response.json()
            #print(f"Data {data}")
            pageInfo = data.get("data",{}).get("properties",{}).get("pageInfo",{})
            #print(f"PageInfo: {pageInfo}")
            #print(f"End cursor: {end_cursor}")
            hasNextPage = pageInfo.get("hasNextPage")
            #print(f"Last page: {hasNextPage}")
            total = pageInfo.get("total","")
            
            fetched_data_list = data.get("data", {}).get("properties", {}).get("edges", [])
            for item in fetched_data_list:
                node = item.get("node", {})
                address = node.get("address", {})
                county_name = address.get("county", "")
                #print(f"county_name {county_name}")
                county_names.append(county_name)
                #print (f"county_names{county_names}")
        return county_names, hasNextPage, total

    @staticmethod  
    def Return_Mailabl_State_list_Where_county_IN(self, county_item, state_item, end_cursor):
        query_loader = Graphql_properties()
        query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_Address_State)
        #print("Query added")

        items_for_page = 1  # Adjust this to your desired value
        #end_cursor = None  # Initialize end_cursor before the loop

        variables_first = {
            "first": items_for_page,  # Fetch 50 items per query
            "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            "where": {
                    "OR": [
                            {
                            "column": "COUNTY",
                            "operator": "EQ",
                            "value": county_item
                            },
                        ]
                    }
                }


        variables_after = {
            "first": items_for_page,  # Fetch 50 items per query
            "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            "where": {
                    "AND": [
                            {
                            "column": "COUNTY",
                            "operator": "EQ",
                            "value": county_item
                            },
                        
                        {
                            "column": "STATE",
                            "operator": "NOT_IN",
                            "value": state_item
                        }
                    ]
                    }
                }

        if not state_item:
            variables = variables_first
        else:
            variables = variables_after
            
        response = requestBuilder.construct_and_send_request(self,query, variables)
       # print(f"response: {response}")
        #start do use data
        if response.status_code == 200:
            data = response.json()
            #print(f"Data {data}")
            pageInfo = data.get("data",{}).get("properties",{}).get("pageInfo",{})
            #print(f"PageInfo: {pageInfo}")
            end_cursor = pageInfo.get("endCursor")
            #print(f"End cursor: {end_cursor}")
            hasNextPage = pageInfo.get("hasNextPage")
            #print(f"Last page: {hasNextPage}")
            total = pageInfo.get("total","")
            
            state_name = ""  # Initialize with a default value
            fetched_data_list = data.get("data", {}).get("properties", {}).get("edges", [])
            #print(f"fetched data for state imet guery: {fetched_data_list}")
            for item in fetched_data_list:
                node = item.get("node", {})
                address = node.get("address", {})
                state_name  = address.get("state", "")
                
        return state_name, hasNextPage, end_cursor
    
    @staticmethod            
    def Return_Mailabl_City_list_Where_State_IN(self, state_item, city_item):
        query_loader = Graphql_properties()
        query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_Address_City)
        #print("Query added")
        items_for_page = 1  # Adjust this to your desired value
        end_cursor = None  # Initialize end_cursor before the loop

        variables_first = {
            "first": items_for_page,  # Fetch 50 items per query
            "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            "where": {
                    "OR": [
                            {
                            "column": "STATE",
                            "operator": "EQ",
                            "value": state_item
                            },
                        ]
                    }
                }

        variables_after = {
            "first": items_for_page,  # Fetch 50 items per query
            "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            "where": {
                    "AND": [
                            {
                            "column": "STATE",
                            "operator": "EQ",
                            "value": state_item
                            },
                        
                        {
                            "column": "CITY",
                            "operator": "NOT_IN",
                            "value": city_item
                        }
                    ]
                    }
                }

        if not city_item:
            #print("not city item")
            variables = variables_first
        else:
            #print("not city item")
            variables = variables_after
            
        response = requestBuilder.construct_and_send_request(self, query, variables)

        #start do use data
        if response.status_code == 200:
            data = response.json()
            #print(f"Data {data}")
            pageInfo = data.get("data",{}).get("properties",{}).get("pageInfo",{})
            end_cursor = pageInfo.get("endCursor")
            total = pageInfo.get("total","")
            count = pageInfo.get("count","")
            hasNextPage = pageInfo.get("hasNextPage")
            total = pageInfo.get("total","")
            
            city_name = ""  # Initialize with a default value
            fetched_data_list = data.get("data", {}).get("properties", {}).get("edges", [])
            for item in fetched_data_list:
                node = item.get("node", {})
                address = node.get("address", {})
                city_name  = address.get("city", "")
                
        return city_name, hasNextPage, total, count, end_cursor
   
    @staticmethod
    def Return_Mailabl_Properties_Where_City_IN(self, city_item, state_item, next_page):
        query_loader = Graphql_properties()
        query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_ID_CadastralNR)
        #print("Query added")

        items_for_page = 50  # Adjust this to your desired value
        #next_page = None  # Initialize end_cursor before the loop

        variables = {
            "first": items_for_page,  # Fetch 50 items per query
            "after": next_page if next_page else None,  # Use the endCursor as the after value
            "where": {
                    "AND": [
                            {
                            "column": "STATE",
                            "operator": "EQ",
                            "value": state_item
                            },
                        
                        {
                            "column": "CITY",
                            "operator": "EQ",
                            "value": city_item
                        }
                    ]
                    }
                }
        
        response = requestBuilder.construct_and_send_request(self,query, variables)

        #start do use data
        if response.status_code == 200:
            data = response.json()
            #print(f"Data {data}")
            pageInfo = data.get("data",{}).get("properties",{}).get("pageInfo",{})
            #print(f"PageInfo: {pageInfo}")
            #print(f"End cursor: {end_cursor}")
            hasNextPage = pageInfo.get("hasNextPage")
            end_cursor = pageInfo.get("endCursor")
            #print(f"Last page: {hasNextPage}")
            total = pageInfo.get("total","")
            count = pageInfo.get("count","")
            fetched_data_list = data.get("data", {}).get("properties", {}).get("edges", [])
            #print(f"data list: {fetched_data_list} ")
            cadastral_units = []
            for item in fetched_data_list:
                node = item.get("node", {})
                cadastral_unit = node.get("cadastralUnit", {})
                cadastral_unit_value = cadastral_unit.get("number", "")
                cadastral_units.append(cadastral_unit_value)
                QCoreApplication.processEvents()
        return cadastral_units, hasNextPage, total, count, end_cursor

class deleteProperty:
    def delete_single_item(self, item):
        query_loader = Graphql_properties()
        query = GraphQLQueryLoader.load_query_properties(self,query_loader.D_ALL_properties)
    
        variables = {
            "id": item  # ID of property i want to delete
            }
        response = requestBuilder.construct_and_send_request(self, query, variables)
        
        # Check the response for errors
        if response.status_code != 200:
            print(f"Failed to delete property with ID {item}. Status Code: {response.status_code}")
            raise Exception(f"GraphQL request failed. Status Code: {response.status_code}")
        
        data = response.json()
    
        # Get the ID of the deleted property
        deleted_property_id = data.get("data", {}).get("deleteProperty", {}).get("id")
        if deleted_property_id:
            pass
            #print(f"Successfully deleted property with ID: {deleted_property_id}")
        else:
            print(f"Property with ID {item} not found.")

        # Check the response for errors
        #if response.status_code != 200:
         #   raise Exception("GraphQL request failed")

        # Get the ID of the deleted property
        #deleted_property_id = response.json()#["data"]["deleteProperty"]["id"]

        #print(deleted_property_id)

    @staticmethod
    def delete_multiple_items(self, item_list):
        total = len(item_list)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)
        progress_widget.setWindowTitle("Eemaldan kinnistuid")
        progress_widget.show()
        import time
        count = 0
        paus_interval = 25  # Set the interval for the sleep timer
        sleep_duration = 1  # Set the sleep duration in seconds

        for item in item_list:
            deleteProperty.delete_single_item(self, item)
            count += 1
            progress_bar.setValue(count)
            QCoreApplication.processEvents()

            if count % paus_interval == 0:
                time.sleep(sleep_duration)
                
class add_properties:
    # Function to extract street name and house number
    def get_address_details_from_street(street):
        data = {}
        
        # Find the position of the first digit in the street address
        number_match = re.search(r'\d', street)

        # If at least one digit is found
        if number_match:
            number_index = number_match.start()
            data['street'] = street[:number_index].strip()
            data['house'] = street[number_index:].strip()
        else:
            data['street'] = street.strip()
        return data

    def add_single_property_item(self,item):
        query_loader = Graphql_properties()
        query = GraphQLQueryLoader.load_query_properties(self, query_loader.ADD_Selected_properties)

        # Assuming item is a JSON string
        item_dict = json.loads(item)
        #print(f"item {item_dict}")

        variables = {
            "input": item_dict
        }

        try:
            # Send the POST request to the GraphQL endpoint with a 30-second timeout
            response = requestBuilder.construct_and_send_request(self, query, variables)
            # Check the response for errors
            response.raise_for_status()
            # Get the ID of the added property
            added_property = response.json()
            #print(f"Inserted item {added_property}")
            # Extract the 'id' from the dictionary
            property_id = added_property['data']['createProperty']['id']
            # Print the extracted ID
            #print(f"Extracted ID: {property_id}")
            return property_id
        
        except Timeout:
            # Handle timeout: prompt the user with a messagebox
            user_response = input("No response received within 30 seconds. Do you want to continue? (yes/no): ").lower()
            if user_response == 'yes':
                # Retry the request
                response = requestBuilder.construct_and_send_request(self, query, variables)
                response.raise_for_status()
                added_property = response.json()
                property_id = added_property['data']['createProperty']['id']
                return property_id
            
            else:
                print("Operation canceled.")
                return

        except requests.exceptions.RequestException as e:
            # Handle other request exceptions
            print(f"GraphQL request failed: {e}")
            return

    def add_additional_property_data(self, input_id, uses_input):

            query_loader = Graphql_properties()
            query = GraphQLQueryLoader.load_query_properties(self, query_loader.ADD_properties_purpose)
        # Construct the list of PropertyIntendedUseInput
            variables = {
                "input": {
                    "id": input_id,
                    "uses": uses_input
                }
            }
            # Send the POST request to the GraphQL endpoint
            response = requestBuilder.construct_and_send_request(self, query, variables)
            # Check the response for errors
            if response.status_code != 200:
                raise Exception("GraphQL request failed")
            # Get the ID of the deleted property
            added_input = response.json()#["data"]["deleteProperty"]["id"]
            print(f"inserted item {added_input}")

    @staticmethod
    def add_multiple_items(self, item_list):
        total = len(item_list)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)
        progress_widget.setWindowTitle("Lisan kinnistud mailabli")
        progress_widget.show()
        import time
        count = 0
        delete_interval = 25  # Set the interval for the sleep timer
        sleep_duration = 1  # Set the sleep duration in seconds

        for item in item_list:
            add_properties.add_single_property_item(self, item)
            progress_bar.setValue(count)
            QCoreApplication.processEvents()

            if count % delete_interval == 0:
                # Sleep for 0.5 seconds after every delete_interval items
                time.sleep(sleep_duration)

class MyLablChecker:
    def create_batches(self, data, batch_size):
        return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

    def process_data_in_batches_with_progress(self, items):
        """
        Process data in batches, update progress, and return the final result.
        """
        batch_size = 50
        batched_data_list = list(self.create_batches(items, batch_size))
        #print("batched_data_list:")
        #pprint(batched_data_list)

        batches_done = 0
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(len(batched_data_list))  # Set the maximum value of the progress bar
        progress_widget.show()
        progress_widget.setWindowTitle("Andmete eelkontoll")

        progress_bar.setValue(0)
        QCoreApplication.processEvents()
        import time
        final_data = []
        for batch in batched_data_list:
            #print(f"batch = {batch}")
            data_returned = self.get_properties_where_for_duplicates(batch)
            #print(f"Final results of non duplicates = {data_returned}")
            final_data.extend(data_returned)
            batches_done += 1
            progress_bar.setValue(batches_done)
            time.sleep(1)
            QCoreApplication.processEvents()
        progress_bar.close()
        #print(f"final data = {final_data}")
        return final_data

    def DeleteProcess_Data_preparation(self, items):
        """
        Process data in batches, update progress, and return the final result.
        """
        batch_size = 50
        batched_data_list = list(MyLablChecker.create_batches(self,items, batch_size))
        #print("batched_data_list:")
        #pprint(batched_data_list)

        batches_done = 0
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(len(batched_data_list))  # Set the maximum value of the progress bar
        progress_widget.show()
        progress_bar.setValue(0)    
        QCoreApplication.processEvents()

        final_data = []
        for batch in batched_data_list:
            print(f"batch = {batch}")
            #data_returned, ids  =  DeleteFunctions.DeleteProcess_get_properties_where_for_duplicates(self, batch)
            
            returned_ids = PropertiesGeneralQueries.get_properties_MyLabl_ids(self, batch)
            print(f"returned_ids: {returned_ids}")
            if returned_ids is None:
                returned_ids = ""        
            final_data.extend(returned_ids)
            #final_ids.extend(ids)
            batches_done += 1
            progress_bar.setValue(batches_done)
            QCoreApplication.processEvents()
        progress_bar.close()
        print(f"final data = {final_data}")
        return final_data




    def clean_import_data_from_duplicates(self, data, confirmation_list, total):
        #print(f"Data in 'clean_import_data_from_duplicates': {data}")
        #print(f"confirmation_list in 'clean_import_data_from_duplicates': {confirmation_list}")
        true_values_count = 0
        false_values_count = 0
        false_values = []
        true_values = []
        cadastral_numbers = []
        if not isinstance(data, dict):
            print("Invalid data format. Expected a dictionary.")
            
        keys_done =  0
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
        progress_widget.show()
        progress_bar.setValue(keys_done)    
        QCoreApplication.processEvents()

        for key, value in data.items():
            try:
                item_data = json.loads(value)
                #print(f"item_data")
            except json.JSONDecodeError as e:
                #print(f"Error decoding JSON for key {key}: {e}")
                continue

            cadastral_unit = item_data.get("cadastralUnit", {})
            cadastral_number = cadastral_unit.get("number", "")
            #print(f"cadastral_unit = {cadastral_unit}")
            #print(f"Cadastral_number = {cadastral_number}")
        
            if cadastral_number in confirmation_list:
                #print("Number found in data")
                #print(f"{number} in {data}")
                true_values.append(item_data)
                cadastral_numbers.append(cadastral_number)
                true_values_count += 1
                #keys.append(key)
                #print(f"output item = {output}")
            if cadastral_number not in confirmation_list:
                false_values.append(item_data)
                false_values_count +=1           
            else:
                pass
                #pass
                #print("Number not found in data")
                #print(f"{number} not in {item_data}")
                #print("Discard")
            keys_done += 1
            progress_bar.setValue(keys_done)           
            QCoreApplication.processEvents()
    
        progress_bar.close()
        #print(f"False_values_in 'clean_import_data_from_duplicates': {false_values}")
        #print(f"Tue_values_in 'clean_import_data_from_duplicates': {cadastral_numbers}")
        return false_values, true_values_count, false_values_count, cadastral_numbers


    def get_properties_where_for_duplicates(self, item):

        query_loader = Graphql_properties()
        query = GraphQLQueryLoader.load_query_properties(self,query_loader.W_properties_number)

        #print("Query added")
        end_cursor = None  # Initialize end_cursor before the loop
        
        variables = {
                    "first": 50,  # Fetch 50 items per query
                    "after": end_cursor,  # Use the endCursor as the after value
                    "where":
                            {
                            "column": "CADASTRAL_UNIT_NUMBER",
                            "operator": "IN", # oli EQ = equals ehk võrdne 
                            "value": item #array anna siin items
                            }
                    }

        response = requestBuilder.construct_and_send_request(self, query, variables)
#        print(f"response {response}")
        #start do use data
        if response.status_code == 200:
            data = handleResponse.response_properties_data_edges(response)
            #pprint(data)
            missing_items = MyLablChecker.find_missing_items(self, item_list=item, graphql_data=data)
            #print("missing item")
            #print(missing_items)
            return missing_items
        
        else:
            print(f"Error: {response.status_code}")
            return None

    def find_missing_items(self, item_list, graphql_data):
        returned_items = set()
        # Extract unique item numbers from the GraphQL data
        for result in graphql_data:
            if 'node' in result and 'cadastralUnit' in result['node']:
                number = result['node']['cadastralUnit']['number']
                returned_items.add(number)
        #print(f"Mailabl returned data: {returned_items}")
        # Find items that are not returned
        missing_items = [item for item in item_list if item not in returned_items]
        return missing_items

class PropertiesGeneralQueries:
    def get_properties_MyLabl_ids(self, properties_list):
        total_in_list = len(properties_list)
        
        query_loader = Graphql_properties()
        query = GraphQLQueryLoader.load_query_properties(self, query_loader.W_properties_number)
        
        sleep_duration = 1
        chunk_size = 50
        
        total_fetched = 0
        total_chunk = 0  # Initialize total_chunk
        end_cursor = None  # Initialize end_cursor before the loop
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(len(properties_list))
        progress_widget.setWindowTitle("Valmistan andmeid ette")
        progress_widget.show()
        
        cadasters = []
        fetched_items = []
        
        while total_fetched < total_in_list:
            chunk = properties_list[total_fetched:total_fetched + chunk_size]  # Slice next chunk of data
            
            variables = {
                "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value   
                "where": {
                    "column": "CADASTRAL_UNIT_NUMBER",
                    "operator": "IN",
                    "value": chunk
                }
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                returned_id = handleResponse.response_properties_data_ids(response)
                cadaster = handleResponse.response_properties_cadastral_numbers(response)
                
                data = response.json()
                pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")
                
                fetched_items.extend(returned_id)
                cadasters.extend(cadaster)
                
                total_fetched += len(returned_id)  # Adjust total_fetched based on the returned items
                total_chunk += 1  # Increment total_chunk
                
                progress_bar.setValue(total_fetched)
                QCoreApplication.processEvents()
            
            if len(chunk) < chunk_size or total_fetched % chunk_size == 0:
                time.sleep(sleep_duration)

        return fetched_items, cadasters

    def get_properties_MyLabl_ids_repaired(self, properties_list):
        total_in_list = len(properties_list)
        
        query_loader = Graphql_properties()
        query = GraphQLQueryLoader.load_query_properties(self, query_loader.W_properties_number)
        
        sleep_duration = 1
        chunk_size = 50        
        total_fetched = 0
        total_chunk = 0  # Initialize total_chunk
        end_cursor = None  # Initialize end_cursor before the loop

        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(len(properties_list))
        progress_widget.setWindowTitle("Valmistan andmeid ette")
        progress_widget.show()
        
        fetched_items = []
        
        while total_fetched < total_in_list:
            chunk = properties_list[total_fetched:total_fetched + chunk_size]  # Slice next chunk of data
            
            variables = {
                "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value   
                "where": {
                    "column": "CADASTRAL_UNIT_NUMBER",
                    "operator": "IN",
                    "value": chunk
                }
            }

            response = requestBuilder.construct_and_send_request(self, query, variables)

            if response.status_code == 200:
                returned_id = handleResponse.response_properties_data_ids(response)
                #cadaster = handleResponse.response_properties_cadastral_numbers(response)
                
                data = response.json()
                pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")
                
                fetched_items.extend(returned_id)
                #cadasters.extend(cadaster)
                
                total_fetched += len(returned_id)  # Adjust total_fetched based on the returned items
                total_chunk += 1  # Increment total_chunk
                
                progress_bar.setValue(total_fetched)
                QCoreApplication.processEvents()
            
            if len(chunk) < chunk_size or total_fetched % chunk_size == 0:
                time.sleep(sleep_duration)

        return fetched_items

