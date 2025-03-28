import requests, platform
from qgis.core import Qgis
from .access_credentials import load_token
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import GraphQLSettings
from ...KeelelisedMuutujad.messages import Headings
 
pealkiri = Headings()

class requestBuilder:
    @staticmethod
    def construct_and_send_request(self, query, variables):       
        graphql_url = GraphQLSettings.graphql_endpoint()
        access_token = load_token()
        if not access_token:
            text = ("Access token not found. Please connect first.")
            heading = pealkiri.informationSimple
            QMessageBox.warning(self, heading, text)
            return None

        # Construct the request payload
        payload = {
            "query": query,
            "variables": variables
        }

        # Construct the HTTP headers with the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "User-Agent": f"QGIS/{Qgis.QGIS_VERSION} ({platform.system()} {platform.release()})"
        }

        try:
            # Send the POST request to the GraphQL endpoint with timeout
            response = requests.post(graphql_url, headers=headers, json=payload, timeout=30)
        except requests.Timeout:
            print("Request timed out.")
            return None
        # Check for empty response
        if not response.content:
            print(f"Empty response received for query: {query}")
            return None

        # Parse the JSON response
        data = response.json()
        # Check if the response is empty
        if not data:
            print(f"Data returned empty - maybe need to check query: {query}")
            return None

        # Check for errors in the response
        errors = data.get('errors', [])
        #print(f"Errors: {errors}")
        if errors:
            #print(f"errors: errors")
            RequestErrorHandler.handle_error(self, errors)

        return response

class RequestErrorHandler:
    def handle_error(self, errors):
        if errors:
            error_messages = [error.get('message', 'Unknown error') for error in errors]
            error_message = '\n'.join(error_messages)
            text = (f"GraphQL request failed:\n{error_message}")
            heading = pealkiri.warningSimple
            QMessageBox.warning(self, heading, text)
            return True  # Indicate that an error occurred
        return False  # No error occurred
