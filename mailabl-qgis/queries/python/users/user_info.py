from ....KeelelisedMuutujad.messages import Headings
from ..DataLoading_classes import GraphQLQueryLoader
from ..query_tools import requestBuilder
import json
 
pealkiri = Headings()

class UserSettings_old:
    def user_data(self, username):
        items_for_page = 1  # Adjust this to your desired value
        #items_for_properties_page = 50
        end_cursor = None # Initialize end_cursor before the loop
        # Initialize an empty list to store fetched items
    
        loader = GraphQLQueryLoader()
        query = loader.load_query_users(loader.Q_me)
        roles = []
        variables = {}

        response = requestBuilder.construct_and_send_request(self, query, variables)
        print(f"response {response}")
        if response.status_code == 200:
            data = response.json()
            user = data.get("data", {}).get("me", {})
            user_name = user.get("firstName", "")
            user_lastname = user.get("lastName", "")
            roles = user.get("roles", [])
            role_names = [role.get("displayName", "") for role in roles]
            roles_text = ", ".join(role_names)


        return user_name, user_lastname, roles_text





class UserSettings:

    def user_data(self, username):
        items_for_page = 1  # Adjust this to your desired value
        end_cursor = None  # Initialize end_cursor before the loop
        
        loader = GraphQLQueryLoader()
        query = loader.load_query_users(loader.Q_me)
        roles = []
        variables = {}

        # Send the request
        response = requestBuilder.construct_and_send_request(self, query, variables)
        
        if response.status_code == 200:
            data = response.json()
            user = data.get("data", {}).get("me", {})
            
            # Extract user information
            user_name = user.get("firstName", "")
            user_lastname = user.get("lastName", "")
            
            # Extract roles
            roles = user.get("roles", [])
            role_names = [role.get("displayName", "") for role in roles]
            roles_text = ", ".join(role_names)
            
            # Extract abilities (which is a JSON string in the response)
            abilities_str = user.get("abilities", "[]")  # Default to empty list if not found
            
            try:
                # Parse the JSON string into a Python list
                abilities = json.loads(abilities_str)
            except json.JSONDecodeError:
                abilities = []
            
            # Check if the user has access to QGIS
            has_qgis_access = any(
                ability.get("action") == "access" and ability.get("subject") == "QGIS"
                for ability in abilities
            )
            
            # Output the extracted data for debugging or further use
            print(f"User: {user_name} {user_lastname}")
            print(f"Roles: {roles_text}")
            print(f"Has QGIS Access: {has_qgis_access}")
            #print(f"Abilities: {abilities}")
            
            # Return the extracted data if needed for further processing
            return user_name, user_lastname, roles_text, has_qgis_access

        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None



