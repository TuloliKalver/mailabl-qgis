from ....processes.infomessages.messages import Headings
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
        query = loader.load_query_users(loader.Q_Where_user)
        roles = []
        variables = {
                "first": items_for_page,
                "after": end_cursor if end_cursor else None,
                "where": {
                    "AND": [
                        {"column": "EMAIL", "operator": "IN", "value": [username]}
                    ]
                }
            }

        response = requestBuilder.construct_and_send_request(self, query, variables)

        if response.status_code == 200:
            data = response.json()
            user_maindata = data.get("data", {}).get("users", {}).get("edges", [])
            pageInfo = data.get("data", {}).get("users", {}).get("pageInfo", {})
            end_cursor = pageInfo.get("endCursor")

            for edge in user_maindata:
                user_node = edge.get("node", {})
                user_name = user_node.get("firstName", "")
                user_lastname = user_node.get("lastName", "")
                print(f"user_name: {user_name}")
                print(f"user_lastname: {user_lastname}")
                roles = user_node.get("roles", [])
                role_names = [role.get("displayName", "") for role in roles]
                roles_text = ", ".join(role_names)
                print(f"Roles: {roles_text}")

        if end_cursor:
            return user_name, user_lastname, roles_text
