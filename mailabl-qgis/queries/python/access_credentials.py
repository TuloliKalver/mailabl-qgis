import requests, platform
from qgis.core import QgsSettings, Qgis
from ...config.settings import GraphQLSettings
from .FileLoaderHelper import GraphQLQueryLoader
from ...KeelelisedMuutujad.messages import Headings
from ...utils.messagesHelper import ModernMessageDialog
from ...KeelelisedMuutujad.modules import Module
#from ...queries.python.query_tools import requestBuilder
# Kontolli ja lahenda lõplikult miks ei saa kasutada request builderit selles moodulis?
 
pealkiri = Headings()

GRAPHQL_ENDPOINT = GraphQLSettings.graphql_endpoint()


# Declare QgsSettings main paths for user credentials and access token
USER_CREDENTIALS = '/Mailabl/Setting/UC'
UC_USERNAME = '/Mailabl/Setting/UC/username'
UC_PASSWORD = '/Mailabl/Setting/UC/password'
ACCESS_TOKEN = '/Mailabl/Setting/UC/access_token'
USER_FIRST = '/Mailabl/Setting/UC/first_name'
USER_LAST = '/Mailabl/Setting/UC/last_name'

# Save the entered username and password
def save_user_name(self):
    settings = QgsSettings()

    username = self.leUsername.text()
    password = self.lePassword.text()

    settings.setValue(UC_USERNAME, username)
    settings.setValue(UC_PASSWORD, password)
    return username




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
    username = get_user_name()
    password = get_user_password()

    # Construct GraphQL mutation for authentication
    graphql = f'''
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
        "query": graphql
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
            return True  # Authentication success
        else:
            text = "Autentimine ebaõnnestus.\nKontrolli kasutajanime ja parooli"
            heading = pealkiri.warningSimple
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
            return False  # Authentication failure
    else:
        text = "Autentimise pöördumine ebaõnnestus.\nProovi mõne hetke pärast uuesti"
        heading = pealkiri.warningSimple
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
        return False  # Network or other error


# Save the obtained access token to QgsSettings
def save_access_token(token):
    settings = QgsSettings()
    settings.setValue(ACCESS_TOKEN, token)

