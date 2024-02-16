import os

class GraphQLQueryLoader:
    def __init__(self):
        # Get the current file's directory
        current_dir = os.path.abspath(__file__)
        # Navigate back to the 'connectmailabl' folder
        self.plugin_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
        # Navigate to the 'queries/graphql' folder and then into the 'graphql' subfolder
        self.graphql_folder = 'queries/graphql'
        # Define query files
        self.Q_All_Properties = 'propertyQuery.graphql'
        self.Q_All_Users = 'users.graphql'
        self.Q_All_Projects = 'projects.graphql'
        self.Q_All_contracts = 'contracts.graphql'

    def load_query(self, query_file_name):
        graphql_path = os.path.join(self.plugin_dir, self.graphql_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()
