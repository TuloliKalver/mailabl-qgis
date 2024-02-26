import requests
from .access_credentials import load_token
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import GraphQLSettings

class requestBuilder:
    @staticmethod
    def construct_and_send_request(self, query, variables):       
        graphql_url = GraphQLSettings.graphql_endpoint()
        access_token = load_token()
        if not access_token:
            QMessageBox.warning(self, "Error", "Access token not found. Please connect first.")
            return None

        # Construct the request payload
        payload = {
            "query": query,
            "variables": variables
        }
        #print("'variables'")
        #print(f"'{variables}'")
        # Print the query before sending
        #print("GraphQL Query:")
        #print(query)

        # Construct the HTTP headers with the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Send the POST request to the GraphQL endpoint
        response = requests.post(graphql_url, headers=headers, json=payload)
        #print("response")
        #print(response)
        # Check for empty response
        if not response.content:
            print(f"Empty response received for query: {query}")
            return None

        # Parse the JSON response
        data = response.json()
        #print("'data'")
        #print(data)
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
            QMessageBox.warning(None, "Error", f"GraphQL request failed:\n{error_message}")
            return True  # Indicate that an error occurred
        return False  # No error occurred
