import requests
from .DataLoading_classes import GraphQLQueryLoader
from .access_credentials import load_token
from qgis.PyQt.QtWidgets import QMessageBox, QHeaderView
from qgis.PyQt.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QLineEdit
from ...config.settings import GraphQLSettings


GRAPHQL_ENDPOINT = GraphQLSettings.graphql_endpoint()


class contracts:
    loader = GraphQLQueryLoader
    
    def __init__(self, data, node):
        self.id = data.get("id")
        self.name = data.get('name')
        self.number = data.get('number')
        status = data.get('status',{})
        self.status = status.get('name',"")
        self.startAt =   data.get('startAt')
        self.dueAt = data.get('dueAt')
        self.isPublic = data.get('isPublic')
        self.isSubproject = data.get('isSubproject')
        self.FilePath = data.get('filesPath')
        self.description = data.get('description')
        self.notes = data.get('notes')

    
    
    def fetch_and_display_contracts(self):
        access_token = load_token()
        if not access_token:
            QMessageBox.warning(self, "Error", "Access token not found. Please connect first.")
            return

        # Construct the GraphQL query
        query = """
        query GetContracts($first: Int, $after: String) {
        contracts(first: $first, after: $after) {
            pageInfo {
            count
            currentPage
            startCursor
            endCursor
            hasNextPage
            hasPreviousPage
            lastPage
            total
            }
            edges {
            node {
                id
                immovableNumber
                displayAddress
                # Add other contract fields you need
            }
            }
        }
        }
        """

        # Set desired total number of items to fetch
        desired_total_items = 200  # Adjust this to your desired value

        # Initialize variables for pagination
        total_fetched = 0
        current_page = 1
        end_cursor = None
        contracts_data = []

        while (not desired_total_items or total_fetched < desired_total_items):
            variables = {
                "first": 50,  # Fetch any number of items per one query
                "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            }

            # Construct the request payload
            payload = {
                "query": query,
                "variables": variables
            }

            # Construct the HTTP headers with the access token
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }

            # Send the POST request to the GraphQL endpoint
            response = requests.post(GRAPHQL_ENDPOINT, headers=headers, json=payload)

            if response.status_code == 200:
                data = response.json()
                contracts = data.get("data", {}).get("contracts", {}).get("edges", [])

                # Update end_cursor based on the server's response
                pageInfo = data.get("data", {}).get("contracts", {}).get("pageInfo", {})
                end_cursor = pageInfo.get("endCursor")

                # Append the fetched contracts to the contracts_data list
                contracts_data.extend(contracts)

                # Increment total_fetched inside the loop
                total_fetched += len(contracts)

                if not pageInfo.get("hasNextPage"):
                    break  # Exit the loop if there are no more pages

            else:
                print(f"Error: {response.status_code}")
                return None

            # Move to the next page
            current_page += 1

        # Display the contracts_data in a QTableView
        self.display_contracts_in_tableview(contracts_data)

    def display_contracts_in_tableview(self, contracts_data):
        # Create a QStandardItemModel for Contracts data
        model = QStandardItemModel()

        # Set header labels
        header_labels = ['ID', 'Immovable Number', 'Display Address']
        model.setHorizontalHeaderLabels(header_labels)

        # Process the contracts_data and add it to the model
        for contract in contracts_data:
            node = contract.get("node", {})
            data_items = [
                QStandardItem(str(node.get("id", ""))),
                QStandardItem(node.get("immovableNumber", "")),
                QStandardItem(node.get("displayAddress", "")),
            ]
            model.appendRow(data_items)

        # Set the model for the QTableView
        self.tblContracts.setModel(model)
        self.tblContracts.resizeColumnsToContents()
