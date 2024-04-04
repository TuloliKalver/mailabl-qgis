import requests, platform
from PyQt5.QtWidgets import QMessageBox
from qgis.core import QgsSettings, Qgis
from ...config.settings import GraphQLSettings
from ...processes.infomessages.messages import Headings
 
pealkiri = Headings()

GRAPHQL_ENDPOINT = GraphQLSettings.graphql_endpoint()


# Declare QgsSettings main paths for user credentials and access token
USER_CREDENTIALS = '/Mailabl/Setting/UC'
UC_USERNAME = '/Mailabl/Setting/UC/username'
UC_PASSWORD = '/Mailabl/Setting/UC/password'
ACCESS_TOKEN = '/Mailabl/Setting/UC/access_token'

# Save the entered username and password
def save_user_name(self):
    settings = QgsSettings()

    username = self.leUsername.text()
    password = self.lePassword.text()

    settings.setValue(UC_USERNAME, username)
    settings.setValue(UC_PASSWORD, password)
    #self.lbUC.setText(f"Kasutaja andmed on järgmised: Kasutaja: {username}, salasõna: {password}")


# Retrieve the saved username from QgsSettings

def get_user_name():
    settings = QgsSettings()
    return settings.value(UC_USERNAME, '', type=str)

# Retrieve the saved password from QgsSettings
def get_user_password():
    settings = QgsSettings()
    return settings.value(UC_PASSWORD, '', type=str)

# Print the saved username and password
def print_result(self):
    user = get_user_name()
    password = get_user_password()
    print(f"username: ", user)
    print(f"password: ", password)
    self.lbUC.setText(f"Kasutaja andmed on järgmised: Kasutaja: {user}, salasõna: {password}")

# Clear the saved user credentials
def clear_UC_data():
    settings = QgsSettings()
    settings.remove(UC_USERNAME)
    settings.remove(UC_PASSWORD)
    settings.remove(ACCESS_TOKEN)

# Load the saved access token from QgsSettings
def load_token():
    settings = QgsSettings()
    return settings.value(ACCESS_TOKEN, '', type=str)

# Obtain and save the access token using user credentials
def get_access_token(self):
    # Replace with your actual username and password
    username = get_user_name()
    password = get_user_password()


    # Construct GraphQL mutation for authentication
    graphql_mutation = f'''
    mutation {{
        login(input: {{ username: "{username}", password: "{password}" }}) {{
            accessToken
            refreshToken
            expiresIn
        }}
    }}
    '''

    # Construct the request payload
    payload = {
        "query": graphql_mutation
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": f"QGIS/{Qgis.QGIS_VERSION} ({platform.system()} {platform.release()})"
    }

    # Send the POST request to the GraphQL endpoint
    response = requests.post(GRAPHQL_ENDPOINT, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()

        if "accessToken" in response_data.get("data", {}).get("login", {}):
            access_token = response_data["data"]["login"]["accessToken"]
            save_access_token(access_token)  # Save the token
            #print(access_token)
            return "success"
        else:
            text = ("Autentimine ebaõnnestus.\nKontrolli kasutajanime ja parooli")
            heading = pealkiri.warningSimple
            QMessageBox.warning(self, heading, text)
            return "error"
    else:
        text = ("Autentimise pöördumine ebaõnnestus.\nProovi mõne hetke pärast uuesti")
        heading = pealkiri.warningSimple
        QMessageBox.warning(self, heading, text )
        return "error"

# Save the obtained access token to QgsSettings
def save_access_token(token):
    settings = QgsSettings()
    settings.setValue(ACCESS_TOKEN, token)
