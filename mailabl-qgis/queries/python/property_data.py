import time
import os
import re

import requests
from requests.exceptions import Timeout
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from .FileLoaderHelper import GraphQLQueryLoader, GraphqlProperties
from .responses import HandlePropertiesResponses
from .query_tools import requestBuilder
from ...config.ui_directories import PathLoaderSimple
from ...utils.TagsEngines import TagsEngines
from ...KeelelisedMuutujad.modules import Module
from ...utils.ProgressHelper import ProgressDialogModern

items_to_fetch = 100


class WhereProperties:
    @staticmethod
    def Return_Mailabl_County_list_with_where_COUNTY_NOT_IN(self, county_items):
        #query_loader = GraphqlProperties()
        #query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_Address_County)
        #print("Query added")

        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_Address_County
        query = GraphQLQueryLoader.load_query_by_module(module, file)



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
        
        response = requestBuilder.construct_and_send_request(query, variables)
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
        #query_loader = GraphqlProperties()
        #query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_Address_State)
        #print("Query added")


        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_Address_State
        query = GraphQLQueryLoader.load_query_by_module(module, file)





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
            
        response = requestBuilder.construct_and_send_request(query, variables)
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
        #query_loader = GraphqlProperties()
        #query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_Address_City)
        #print("Query added")
        
        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_Address_City
        query = GraphQLQueryLoader.load_query_by_module(module, file)

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
            
        response = requestBuilder.construct_and_send_request(query, variables)

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
        #query_loader = GraphqlProperties()
        #query = query_loader.load_query_for_properties_WHERE(query_loader.W_properties_ID_CadastralNR)
                
        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_ID_CadastralNR
        query = GraphQLQueryLoader.load_query_by_module(module, file)

        items_for_page = 50  # Adjust this to your desired value

        # Counter to keep track of consecutive requests
        consecutive_requests = 0
        
        # Attempt the request at least 10 times
        for _ in range(10):
            try:
                variables = {
                    "first": items_for_page,
                    "after": next_page if next_page else None,
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
                
                response = requestBuilder.construct_and_send_request(query, variables)

                # Check if response is None
                if response is not None:
                    # Proceed with processing the response
                    if response.status_code == 200:
                        data = response.json()
                        pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
                        hasNextPage = pageInfo.get("hasNextPage")
                        end_cursor = pageInfo.get("endCursor")
                        total = pageInfo.get("total", "")
                        count = pageInfo.get("count", "")
                        fetched_data_list = data.get("data", {}).get("properties", {}).get("edges", [])
                        cadastral_units = []
                        for item in fetched_data_list:
                            node = item.get("node", {})
                            cadastral_unit = node.get("cadastralUnit", {})
                            cadastral_unit_value = cadastral_unit.get("number", "")
                            cadastral_units.append(cadastral_unit_value)
                        return cadastral_units, hasNextPage, total, count, end_cursor
                    else:
                        print("Error: Response status code is not 200")
                        # Optionally, you can raise an exception here if needed
                else:
                    print("Error: Response is None")
                    # Optionally, you can raise an exception here if needed
            except Exception as e:
                # Handle any exceptions that occur during the request
                print(f"Error occurred: {e}")
            
            # Increment the consecutive requests counter
            consecutive_requests += 1
            
            # Check if 10 consecutive requests have been made
            if consecutive_requests == 10:
                # Rest for 3 seconds
                time.sleep(3)
                # Reset the consecutive requests counter
                consecutive_requests = 0
        
        # If the request fails after 10 attempts, return default values or handle the failure accordingly
        return [], False, "", "", ""

class deleteProperty:
    @staticmethod
    def delete_single_item(item: str):

        module = Module.PROPRETIE

        file =  GraphqlProperties.D_ALL_properties
        query = GraphQLQueryLoader.load_query_by_module(module, file)


        variables = {
            "id": item  # ID of property i want to delete
            }
        response = requestBuilder.construct_and_send_request(query, variables)
        
        # Check the response for errors
        if response.status_code != 200:
            print(f"Failed to delete property with ID {item}. Status Code: {response.status_code}")
            return False
        else:
            return True
                
class add_properties:
    # Function to extract street name and house number
    @staticmethod
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

        module = Module.PROPRETIE

        file =  GraphqlProperties.ADD_Selected_properties
        query = GraphQLQueryLoader.load_query_by_module(module, file)


        # Assuming item is a JSON string
        #if item.startswith("{"):
        #    item = json.loads(item) 
        #print(f"item {item_dict}")

        variables = {
            "input": item
        }

        try:
            # Send the POST request to the GraphQL endpoint with a 30-second timeout
            response = requestBuilder.construct_and_send_request(query, variables)
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
                response = requestBuilder.construct_and_send_request(query, variables)
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

        module = Module.PROPRETIE

        file =  GraphqlProperties.ADD_properties_purpose
        query = GraphQLQueryLoader.load_query_by_module(module, file)

    # Construct the list of PropertyIntendedUseInput
        variables = {
            "input": {
                "id": input_id,
                "uses": uses_input
            }
        }
        # Send the POST request to the GraphQL endpoint
        response = requestBuilder.construct_and_send_request(query, variables)
        # Check the response for errors
        if response.status_code != 200:
            raise Exception("GraphQL request failed")
        # Get the ID of the deleted property
        added_input = response.json()
        #print(f"inserted item {added_input}")



class MyLablChecker:

    def get_properties_where_for_duplicates(self, item):

        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_number
        query = GraphQLQueryLoader.load_query_by_module(module, file)


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

        response = requestBuilder.construct_and_send_request(query, variables)
#        print(f"response {response}")
        #start do use data
        if response.status_code == 200:
            data = HandlePropertiesResponses._response_properties_data_edges(response)
            #pprint(data)
            missing_items = MyLablChecker.find_missing_items(self, item_list=item, graphql_data=data)
            #print("missing item")
            #print(missing_items)
            return missing_items
        else:
            print(f"Error: {response.status_code}")
            return None


    def _get_propertie_ids_by_cadastral_numbers_EQUALS(item: str)->bool:

        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_number
        query = GraphQLQueryLoader.load_query_by_module(module, file)


        #print("Query added")
        end_cursor = None  # Initialize end_cursor before the loop
        
        variables = {
                    "first": 50,  # Fetch 50 items per query
                    "after": end_cursor,  # Use the endCursor as the after value
                    "where":
                            {
                            "column": "CADASTRAL_UNIT_NUMBER",
                            "operator": "EQ", 
                            "value": item #array anna siin items
                            }
                    }

        response = requestBuilder.construct_and_send_request(query, variables)
#        print(f"response {response}")
        #start do use data
        if response.status_code == 200:
            data = HandlePropertiesResponses._response_properties_data_edges(response)
            print(data)
            if data:
                print("is present in mylabl")
                return False, data
            else:
                #print("missing item")
                return True, []
            
        else:
            print(f"Error: {response.status_code}")
            return False, []


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
    def get_properties_MyLabl_idsAndCadastrals(self, properties_list):
        total_in_list = len(properties_list)
        
        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_number
        query = GraphQLQueryLoader.load_query_by_module(module, file)

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
        has_next_page = True
        while total_fetched < total_in_list or has_next_page:
            chunk_start = total_fetched
            chunk_end = total_fetched + chunk_size
            chunk = properties_list[chunk_start:chunk_end]  # Slice next chunk of data

            variables = {
                "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value   
                "where": {
                    "column": "CADASTRAL_UNIT_NUMBER",
                    "operator": "IN",
                    "value": chunk
                }
            }

            response = requestBuilder.construct_and_send_request(query, variables)

            if response.status_code == 200:
                returned_id = HandlePropertiesResponses._response_properties_data_ids(response)
                cadaster = HandlePropertiesResponses._response_properties_cadastral_numbers(response)
                
                data = response.json()
                pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")
                print(f"End cursor: {end_cursor}")
                has_next_page = pageInfo.get("hasNextPage")
                fetched_items.extend(returned_id)
                cadasters.extend(cadaster)
                
                total_fetched += len(returned_id)  # Adjust total_fetched based on the returned items
                total_chunk += 1  # Increment total_chunk
                
                progress_bar.setValue(total_fetched)
                QCoreApplication.processEvents()
            
            if len(chunk) < chunk_size or total_fetched % chunk_size == 0:
                time.sleep(sleep_duration)


        return fetched_items, cadasters

    @staticmethod
    def _get_properties_MyLabl_ids(properties_list):
        #print(f"propertie list: {properties_list}")
        total_in_list = len(properties_list)
        
        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_number
        query = GraphQLQueryLoader.load_query_by_module(module, file)

        sleep_duration = 1
        chunk_size = 50        
        total_fetched = 0
        total_chunk = 0  # Initialize total_chunk
        end_cursor = None  # Initialize end_cursor before the loop

        progress = ProgressDialogModern(maximum=100)
        
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

            response = requestBuilder.construct_and_send_request(query, variables)

            if response.status_code == 200:
                returned_id = HandlePropertiesResponses._response_properties_data_ids(response)
                #cadaster = handleResponse.response_properties_cadastral_numbers(response)
                
                data = response.json()
                pageInfo = data.get("data", {}).get("properties", {}).get("pageInfo", {})
                print(f"page info: {pageInfo}")
                end_cursor = pageInfo.get("endCursor")
                
                fetched_items.extend(returned_id)
                #cadasters.extend(cadaster)
                
                total_fetched += len(returned_id)  # Adjust total_fetched based on the returned items
                total_chunk += 1  # Increment total_chunk
                
                progress.update(total_fetched)
                QCoreApplication.processEvents()
            
            if len(chunk) < chunk_size or total_fetched % chunk_size == 0:
                time.sleep(sleep_duration)
        progress.close()
        return fetched_items

    @staticmethod
    def _get_properties_street_name_to_achived(property_id) -> bool:
        #item_id: str, notes_text: str

        old_name = "Õpetajate tee"

        query = """
            query GetPropertyName($id: ID!) {
                property(id: $id) {
                    id
                    address {
                            street 
                        }
                    }
                }
            """
        variables = {"id": property_id}

        response = requestBuilder.construct_and_send_request(query, variables)
        if not response:
            print("Failed to fetch property.")
            return False

        data = response.json()
        if "errors" in data or not data.get("data"):
            print("Error fetching property name:", data.get("errors"))
            return False

        current_name = data["data"]["property"]["address"].get('street')

        return current_name


class UpdateData:
        
    @staticmethod
    def _update_properties_name(propertie_id, new_name, module):
        
        mutation_file =  GraphqlProperties.UPDAT_STREET_NAME
        mutation = GraphQLQueryLoader.load_query_by_module(module=module, filename=mutation_file)

        variables = {
            "input": {
                "id": propertie_id,
                "address": {
                    "street": new_name
                        }
            }
        }
        
        response = requestBuilder.construct_and_send_request(mutation, variables)
        if not response:
            print("Test update failed — no response")
            return False

        result = response.json()
        if "errors" in result:
            print("Test update error:", result["errors"])
            return False
        if result:
            print(result)
        else:
            print("No result received.")

    @staticmethod
    def _update_property_tags(property_id: str, module: str, tag_id: str) -> bool:
        #property_id = "133842"
        #tag_id = "91"
        

        query_file = GraphqlProperties.PROPERTIES_TAGS
        query = GraphQLQueryLoader.load_query_by_module(module=module, filename=query_file)

        variables = {"id": property_id}

        response = requestBuilder.construct_and_send_request(query, variables)
        if not response:
            print("Failed to fetch current tags")
            return False

        current_data = response.json()
        #print(f"Current data: {current_data}")
        current_tags = current_data["data"]["property"]["tags"]["edges"]
        current_tag_ids = [tag["node"]["id"] for tag in current_tags]

        if tag_id not in current_tag_ids:
            current_tag_ids.append(tag_id)
        #print(f"Adding tag with ID {tag_id} to property {property_id}")
        #print(f"Current tags for property {property_id}: {[tag['node']['name'] for tag in current_tags]}")
        #print(f"Tags in input: {current_tag_ids}")
        # Step 2: Re-assign ALL tags

        update_guery_file = GraphqlProperties.UPDATE_TAGS
        update_mutation = GraphQLQueryLoader.load_query_by_module(module=module, filename=update_guery_file)
        variables = {
            "input": {
                "id": property_id,
                "tags": {
                    "associate": current_tag_ids
                }
            }
        }

        update_response = requestBuilder.construct_and_send_request(update_mutation, variables)
        if not update_response:
            print("Failed to update tags")
            return False

        updated_data = update_response.json()
        if "errors" in updated_data:
            print("Tag update error:", updated_data["errors"])
            return False

        updated_tags = updated_data["data"]["updateProperty"]["tags"]["edges"]
        tag_names = [tag["node"]["name"] for tag in updated_tags]
        #print(f"Updated tags for property {property_id}: {', '.join(tag_names)}")
        return True


    @staticmethod
    def _remove_property_tag(property_id: str, module: str, tag_id: str) -> bool:
        update_query_file = GraphqlProperties.UPDATE_TAGS
        update_mutation = GraphQLQueryLoader.load_query_by_module(module=module, filename=update_query_file)

        update_variables = {
            "input": {
                "id": property_id,
                "tags": {
                    "dissociate": [tag_id]
                }
            }
        }

        print(f"🚀 Sending dissociate mutation: {update_variables}")

        update_response = requestBuilder.construct_and_send_request(update_mutation, update_variables)
        if not update_response:
            print("❌ Failed to update tags")
            return False

        updated_data = update_response.json()
        if "errors" in updated_data:
            print("❌ Tag removal error:", updated_data["errors"])
            return False

        updated_tags = updated_data["data"]["updateProperty"]["tags"]["edges"]
        updated_tag_names = [tag["node"]["name"] for tag in updated_tags]
        print(f"✅ Tags after dissociation: {updated_tag_names}")

        return True






    @staticmethod
    def _update_archived_properies_data(item_id: str, recovery_name: str = None) -> bool:
        if isinstance(item_id, list):
            # Get the first node's ID
            item_id = item_id[0]["node"]["id"]
        elif isinstance(item_id, dict):
            item_id = item_id["node"]["id"]
        # If it's already a str, nothing to do

        #print(f"✔️ Final item_id to use: {item_id} ({type(item_id)})")
        module=Module.PROPRETIE
        tag_name = "Arhiveeritud"
        tag_id = TagsEngines.get_modules_tag_id_by_name(tag_name=tag_name, module=module)
        if tag_id == None:
            res = TagsEngines.create_tag(tag_name=tag_name, module=module)

            if res is not False:
                tag_id=res

        UpdateData._update_property_tags(property_id=item_id, module=module, tag_id=tag_id)

        current_name = PropertiesGeneralQueries._get_properties_street_name_to_achived(property_id=item_id)
        if recovery_name:
            new_name = recovery_name
        else:
            print(current_name)
            new_name = "ARHIIVEERITUD - " + current_name
        
        UpdateData._update_properties_name(propertie_id=item_id, new_name=new_name, module=module)

    @staticmethod
    def _unarchive_property_data(item_id: str) -> bool:
        if isinstance(item_id, list):
            item_id = item_id[0]["node"]["id"]
        elif isinstance(item_id, dict):
            item_id = item_id["node"]["id"]
        
        module = Module.PROPRETIE
        tag_name = "Arhiveeritud"
        
        # Get the ID of the tag to remove (no need to create if missing!)
        tag_id = TagsEngines.get_modules_tag_id_by_name(tag_name=tag_name, module=module)
        if tag_id:
            # Remove the tag
            UpdateData._remove_property_tag(property_id=item_id, module=module, tag_id=tag_id)

        # Restore original name (remove prefix if it exists)
        current_name = PropertiesGeneralQueries._get_properties_street_name_to_achived(property_id=item_id)

        if current_name.startswith("ARHIIVEERITUD - "):
            new_name = current_name.replace("ARHIIVEERITUD - ", "", 1)
            UpdateData._update_properties_name(propertie_id=item_id, new_name=new_name, module=module)
