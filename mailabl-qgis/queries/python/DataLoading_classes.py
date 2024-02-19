import os

class Graphql_project:
    def __init__(self):
        self.Q_All_Projects = 'projects.graphql'
        self.Q_Where_By_status_Projects = 'W_project_status.graphql'
        self.Q_where_Projects_related_properties = 'W_projects_id.graphql'
        self.UPDATE_project_properties = 'update_project_properties.graphql'
        self.Projects_tags = 'projects_tags.graphql'
        self.Projects_Open = 'Statuses_where_condition.graphql'  #query statuses for different modules, returns ID

class Graphql_properties:
    def __init__(self):
        #Folders
        self.properties_folder = 'queries/graphql/properties'
        self.properties_WHERE_folder = 'queries/graphql/properties/WHERE'
        #General
        self.Q_Property_CSC = 'property_CSC.graphql'
        self.Q_All_Properties = 'propertyQuery.graphql'
        self.Q_where_Projects_related_properties = 'W_projects_id.graphql'
        #Where type
        self.W_properties_number = 'id_number.graphql'
        self.W_properties_Address_County = 'ADDRESS_County.graphql'
        self.W_properties_Address_State = 'ADDRESS_State.graphql'
        self.W_properties_Address_City = 'ADDRESS_City.graphql'
        self.W_properties_ID_CadastralNR = 'ADDRESS_ID_CadastralNR.graphql'
        self.W_Conditional_properties = 'Properties_where.graphql'
        #Add
        self.ADD_Selected_properties = 'Add_property.graphql'
        self.ADD_properties_purpose = 'Add_purpose.graphql'
        #update   
        self.UPDATE_project_properties = 'update_project_properties.graphql'
        #check
        self.CHECK_properties_Mylabl = 'Properties_ID_Cadastral.graphql'
        #delete
        self.D_ALL_properties = 'deleteProperty.graphql'


    def load_query_for_properties_WHERE(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(path.plugin_dir, path.properties_WHERE_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()

class Graphql_contracts:
    def __init__(self):
        self.Q_All_contracts = 'contracts.graphql'
        self.Q_contract_minimal = 'contracts_minimal.graphql'
        self.Q_where_Contracts_related_properties = 'W_contract_id.graphql'
        

class GraphQLQueryLoader:
    def __init__(self):
        # Get the current file's directory
        current_dir = os.path.abspath(__file__)
        # Navigate back to the 'connectmailabl' folder
        self.plugin_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
        # Navigate to the 'queries/graphql' folder and then into the 'graphql' subfolder
        self.graphql_folder = 'queries/graphql'
        self.properties_folder = 'queries/graphql/properties'
        self.properties_WHERE_folder = 'queries/graphql/properties/WHERE'
        self.projects_folder = 'queries/graphql/projects'
        self.contracts_folder ='queries/graphql/contracts'
        
        
        # Define query files
            #Properties related queries
        self.Q_Property_CSC = 'property_CSC.graphql'
        self.Q_All_Properties = 'propertyQuery.graphql'
        
        self.D_ALL_properties = 'deleteProperty.graphql'
        
        self.W_Conditional_properties = 'Properties_where.graphql'
        self.W_properties_number = 'id_number.graphql'
        self.W_properties_Address_County = 'ADDRESS_County.graphql'
        self.W_properties_Address_State = 'ADDRESS_State.graphql'
        self.W_properties_Address_City = 'ADDRESS_City.graphql'
        self.W_properties_ID_CadastralNR = 'ADDRESS_ID_CadastralNR.graphql'
        
        self.ADD_Selected_properties = 'Add_property.graphql'
        self.ADD_properties_purpose = 'Add_purpose.graphql'
        
        self.CHECK_properties_mylabl = 'Properties_ID_Cadastral.graphql'
        

            #User related queries
        self.Q_All_Users = 'users.graphql'

            #Projects related queries
        self.Q_All_Projects = 'projects.graphql'
        self.Q_Where_By_status_Projects = 'W_project_status.graphql'
        self.Q_where_Projects_related_properties = 'w_projects_id.graphql'
        self.UPDATE_project_properties = 'update_project_properties.graphql'
        self.Projects_tags = 'projects_tags.graphql'
        
        
    def load_query(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(path.plugin_dir, path.graphql_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()

    def load_query_for_projects(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(path.plugin_dir, path.projects_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()

    def load_query_for_contracts(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(path.plugin_dir, path.contracts_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()


    def load_query_properties(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(path.plugin_dir, path.properties_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()

    def load_query_for_contracts(self,query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(path.plugin_dir, path.contracts_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()