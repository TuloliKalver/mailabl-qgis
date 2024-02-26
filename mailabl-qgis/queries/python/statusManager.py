from .DataLoading_classes import GraphQLQueryLoader, Graphql_project
from .query_tools import requestBuilder



class Statuses:
    def __init__(self):
        self.module_contracts = "contracts" # Assuming you have a stacked widget as an instance attribute
        self.module_projects = "projects"
        self.module_tasks = "tasks"
        self.module_coordination = "coordinations"
        self.module_letter = "letters"
        self.module_specifications = "specifications"
        self.module_easments = "easments"
        self.module_specifications = "specifications"
        self.module_ordinances = "ordinances"
        self.submissions = "submissions"
        
        self.state_open = "OPEN"
        self.state_closed = "CLOSED"

    def by_module_and_state(self, module_name, state_type):
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query(self, query_loader.Projects_Open)
        # Construct the request payload
        variables = {
            "where": {
                "AND":[
                {
                "column": "MODULE",
                "value": module_name,
                },
                {
                "column": "TYPE",
                "value": state_type
                }
                ]
            }
        }
        
        response = requestBuilder.construct_and_send_request(self, query, variables)
        if response.status_code == 200:
            data = response.json()
            # Access the relevant part of the data structure
            statuses_data = data.get('data', {}).get('statuses', {}).get('edges', [])
            #print(statuses_data)
            # Create a list to store node_info values
            status_ids = []
            # Iterate through the statuses_data
            for status_info in statuses_data:
                # Access the node information
                node_info = status_info.get('node', {})
                status_id = node_info.get('id',"")
                # Append the node_info to the list
                status_ids.append(status_id)            
            return status_ids

    def all_by_module(self, module_name):
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query(self, query_loader.Projects_Open)
        # Construct the request payload
        variables = {
            "where": {
                "AND":[
                {
                "column": "MODULE",
                "value": module_name,
                }
                ]
            }
        }
        response = requestBuilder.construct_and_send_request(self, query, variables)
        if response.status_code == 200:
            data = response.json()
            # Access the relevant part of the data structure
            statuses_data = data.get('data', {}).get('statuses', {}).get('edges', [])
            #print(statuses_data)
            # Create a list to store node_info values
            status_ids = []
            # Iterate through the statuses_data
            for status_info in statuses_data:
                # Access the node information
                node_info = status_info.get('node', {})
                status_id = node_info.get('id',"")
                # Append the node_info to the list
                status_ids.append(status_id)
            return status_ids

    def all_by_module_names(self, module_name):
        query_loader = GraphQLQueryLoader()
        query = query_loader.load_query(query_loader.Projects_statuses)
        print(f"query: {query}")
        # Construct the request payload
        variables = {
            "where": {
                "AND":[
                {
                "column": "MODULE",
                "value": module_name,
                }
                ]
            }
        }
        response = requestBuilder.construct_and_send_request(self, query, variables)
        if response.status_code == 200:
            data = response.json()
            # Access the relevant part of the data structure
            statuses_data = data.get('data', {}).get('statuses', {}).get('edges', [])
            print(statuses_data)
            # Create a list to store node_info values
            statuses = []
            # Iterate through the statuses_data
            for status_info in statuses_data:
                # Access the node information
                node_info = status_info.get('node', {})
                status = node_info.get('name',"")
                # Append the node_info to the list
                statuses.append(status)
            return statuses


class insertStatusToComboBox:
    def add_statuses_to_listview (self, comboBox, module_name):
        print(f"module name: {module_name}")
        statuses = Statuses.all_by_module_names(self, module_name)
        # Clear existing items in the combo box
        comboBox.clear()
        comboBox.addItems(statuses)


