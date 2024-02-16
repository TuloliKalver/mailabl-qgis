import requests
from PyQt5.QtWidgets import QMessageBox
from qgis.core import QgsSettings
from qgis.PyQt.QtGui import QStandardItemModel
from qgis.PyQt.QtWidgets import QMessageBox

from .access_credentials import load_token
from .DataLoading import load_user_query
from ...config.settings import GraphQLSettings

"
GRAPHQL_ENDPOINT = GraphQLSettings.graphql_endpoint()

# Declare QgsSettings main paths for user credentials and access token
USER_CREDITENTIALS = '/Mailabl/Setting/UC'
UC_USERNAME = '/Mailabl/Setting/UC/username'
UC_PASSWORD = '/Mailabl/Setting/UC/password'
ACCES_TOKEN = '/Mailabl/Setting/UC/access_token'


def user_verification(self):
# Assuming you have fetched the list of user items and stored them in the variable 'user_items'
    #print("started")
    access_token = load_token()
    if not access_token:
        QMessageBox.warning(self, "Error", "Oih, midagi läks valesti. Pöördu adminni poole.")
        return
    #print("token loaded")
    graphql_query = load_user_query()
    #print("query loaded")
    # Construct the request payload

# Set column width mode to adjust to contents

# Create a QStandardItemModel for user data
    user_model = QStandardItemModel()

    payload = {
        "query": graphql_query,
    }

    # Construct the HTTP headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Send the POST request to the GraphQL endpoint
    response = requests.post(GRAPHQL_ENDPOINT, headers=headers, json=payload)
    #print(f"Response: ", response)
    if response.status_code == 200:
        response_data = response.json()

        # Process response_data as needed
        fetched_users = response_data.get("data", {}).get("users", {}).get("edges", [])


    uc_username = QgsSettings().value(UC_USERNAME)

    # Initialize a list to store users with matching emails
    matching_users = []

    # Iterate through user items
    for user_item in fetched_users:
        user_email = user_item.get("node", {}).get("email", "")

        # Compare the user's email with UC_USERNAME
        if user_email == uc_username:
            matching_users.append(user_item)

    # 'matching_users' will now contain the user(s) with matching emails
    if matching_users:
            QMessageBox.information(None, "Success", f"Kasutaja {len(matching_users)} tuvastatud.")
    else:
        QMessageBox.warning(None, "Error", "Puudub kasutaja.")

    
def user_verification_with_login(self):
# Assuming you have fetched the list of user items and stored them in the variable 'user_items'
    #print("started")
    access_token = load_token()
    if not access_token:
        QMessageBox.warning(self, "Error", "Oih, midagi läks valesti. Pöördu adminni poole.")
        return
    #print("token loaded")
    graphql_query = load_user_query()
    #print("query loaded")
    # Construct the request payload

    payload = {
        "query": graphql_query,
    }

    # Construct the HTTP headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Send the POST request to the GraphQL endpoint
    response = requests.post(GRAPHQL_ENDPOINT, headers=headers, json=payload)
    #print(f"Response: ", response)
    if response.status_code == 200:
        response_data = response.json()

        # Process response_data as needed
        fetched_users = response_data.get("data", {}).get("users", {}).get("edges", [])


    uc_username = self.lblCheckUC_username.text()

    # Initialize a list to store users with matching emails
    matching_users = []

    # Iterate through user items
    for user_item in fetched_users:
        user_email = user_item.get("node", {}).get("email", "")

        # Compare the user's email with UC_USERNAME
        if user_email == uc_username:
            matching_users.append(user_item)

    # 'matching_users' will now contain the user(s) with matching emails
    if matching_users:
            QMessageBox.information(None, "Success", f"Kasutaja tuvastatud {len(matching_users)}.")
    else:
        QMessageBox.warning(None, "Error", "Puudub kasutaja.")
