from ....KeelelisedMuutujad.messages import Headings
from ....KeelelisedMuutujad.modules import Module

from ..DataLoading_classes import GraphQLQueryLoader
from ..query_tools import requestBuilder
import json
 
pealkiri = Headings()


class UserSettings:
    @staticmethod
    def user_data():
        module = Module.USER
        

        query = GraphQLQueryLoader.load_query_by_module(module, GraphQLQueryLoader().Q_me)
        
        
        roles = []
        variables = {}

        # Send the request
        response = requestBuilder.construct_and_send_request(None, query, variables)
        
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
            print(f"abilities_str: {abilities_str}")
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
            
            properties_create = any(
                ability.get("action") == "create" and ability.get("subject") == ["Property","properties"]
                for ability in abilities
            )
            
            # Output the extracted data for debugging or further use
            #print(f"User: {user_name} {user_lastname}")
            #print(f"Roles: {roles_text}")
            #print(f"Has QGIS Access: {has_qgis_access}")
            #print(f"Abilities: {abilities}")
            
            # Return the extracted data if needed for further processing
            return user_name, user_lastname, roles_text, has_qgis_access, properties_create

        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None



