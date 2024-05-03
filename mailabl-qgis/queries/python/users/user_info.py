from ....KeelelisedMuutujad.messages import Headings
from ..DataLoading_classes import GraphQLQueryLoader
from ..query_tools import requestBuilder

 
pealkiri = Headings()

class UserSettings:
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

        if response.status_code == 200:
            data = response.json()
            user = data.get("data", {}).get("me", {})
            user_name = user.get("firstName", "")
            user_lastname = user.get("lastName", "")
            roles = user.get("roles", [])
            role_names = [role.get("displayName", "") for role in roles]
            roles_text = ", ".join(role_names)

        return user_name, user_lastname, roles_text
