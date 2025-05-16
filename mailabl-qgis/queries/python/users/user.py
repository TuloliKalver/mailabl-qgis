import json

from ....KeelelisedMuutujad.messages import Headings
from ....KeelelisedMuutujad.modules import Module

from ..FileLoaderHelper import GraphQLQueryLoader, GraphqlUser
from ..query_tools import requestBuilder
 
pealkiri = Headings()

class UserSettings:
    @staticmethod
    def user_data():
        
        module = Module.USER
        query_name = GraphqlUser.Q_me
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        
        roles = []
        variables = {}

        # Send the request
        response = requestBuilder.construct_and_send_request(query, variables)
        
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
            #print(f"abilities_str: {abilities_str}")
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
                        
            # Return the extracted data if needed for further processing
            return user_name, user_lastname, roles_text, has_qgis_access, properties_create

        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None


    def load_users():
        module = Module.USER
        query_name = GraphqlUser.Q_All_Users
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)
        
        variables = {}

        # Send the request
        response = requestBuilder.construct_and_send_request(query, variables)
        
        if response.status_code == 200:
            data = response.json()
            users_data = data['data']['users']['edges']  # replace `your_data` with the actual variable

            user_names = []
            for user in users_data:
                node = user['node']
                if node.get("deletedAt") is None:
                    first = node.get("firstName", "")
                    last = node.get("lastName", "")
                    if first and last:
                        user_names.append(f"{first} {last}")

        return user_names