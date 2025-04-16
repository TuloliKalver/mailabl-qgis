import requests, platform
from qgis.core import Qgis
from .access_credentials import load_token
from qgis.PyQt.QtCore import QVariant

from ...config.settings import GraphQLSettings
from ...KeelelisedMuutujad.messages import Headings
from ...utils.messagesHelper import ModernMessageDialog
 
pealkiri = Headings()

class requestBuilder:
    @staticmethod
    def construct_and_send_request(query: str, variables: dict) -> requests.Response:       
        graphql_url = GraphQLSettings.graphql_endpoint()
        access_token = load_token()
        if not access_token:
            text = ("Access token not found. Please connect first.")
            heading = pealkiri.infoSimple
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
            return None

        sanitized_variables = requestBuilder.sanitize_for_json(variables)

        # Construct the request payload
        payload = {
            "query": query,
            "variables": sanitized_variables
        }
        #print(f"payload is_printed {payload}")
        # Construct the HTTP headers with the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "User-Agent": f"QGIS/{Qgis.QGIS_VERSION} ({platform.system()} {platform.release()})"
        }
        #print(f"payload is_printed {payload}")
        # Send the POST request to the GraphQL endpoint with timeout
        try:
            # Send the POST request to the GraphQL endpoint with timeout
            response = requests.post(graphql_url, headers=headers, json=payload, timeout=30)
            
            #print(f"response is_printed {response}")
        except requests.Timeout:
            print("Request timed out.")
            return None
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None


        # Handle HTTP status codes
        if response.status_code == 502:
            print("Received 502 Bad Gateway.")
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
            RequestErrorHandler.handle_error(errors)

        

        return response

    @staticmethod
    def sanitize_for_json(obj):
        """
        Recursively convert QVariant types to native Python types for JSON serialization.
        """

        if isinstance(obj, dict):
            return {k: requestBuilder.sanitize_for_json(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [requestBuilder.sanitize_for_json(v) for v in obj]
        elif isinstance(obj, QVariant):
            return None if obj.isNull() else obj.value()  # ✅ this is the key fix
        elif hasattr(obj, 'value'):
            return obj.value()  # handles QVariant-like types
        return obj

class RequestErrorHandler:
    def handle_error(errors):
        if errors:
            error_messages = [error.get('message', 'Unknown error') for error in errors]
            error_message = '\n'.join(error_messages)
            text = (f"GraphQL request failed:\n{error_message}")
            heading = pealkiri.warningSimple
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
            #print(f"Error message: {text}")
            return True  # Indicate that an error occurred
        return False  # No error occurred
