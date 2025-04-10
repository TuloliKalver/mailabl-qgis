import os
from ...KeelelisedMuutujad.modules import Module


class QueryFolders:
    PROPERTIES_FOLDER = 'queries/graphql/properties'
    PROPERTIES_WHERE_FOLDER = 'queries/graphql/properties/WHERE'
    PROPERTIES_CONNECTIONS = 'queries/graphql/properties/Connected_data'
    USER_FOLDER = 'queries/graphql/user'
    EASEMENTS_FOLDER = 'queries/graphql/easements'
    PROJECTS_FOLDER = 'queries/graphql/projects'
    CONTRACTS_FOLDER = 'queries/graphql/contracts'
    TAGS_FOLDER = 'queries/graphql/tags'
    STATUS_FOLDERS = 'queries/graphql/statuses'



class Graphql_project:
    def __init__(self):
        self.projects_folder = 'queries/graphql/projects'

        self.Q_All_Projects = 'projects.graphql'
        self.Q_Where_By_status_Projects = 'W_project_status.graphql'
        self.Q_where_Projects_related_properties = 'W_projects_id.graphql'
        self.UPDATE_project_properties = 'update_project_properties.graphql'
        self.Projects_tags = 'projects_tags.graphql'
        self.Projects_Open = 'Statuses_where_condition.graphql' #query statuses for different modules, returns ID
        self.Q_Properties_related_projects = 'propertiesrelated_projects.graphql'

    def load_query_for_projects(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(path.plugin_dir, path.projects_folder, query_file_name)
        print(f"path: {graphql_path}")
        with open(graphql_path, 'r') as file:
            return file.read()


class GraphqlProperties:
    PROPERTIES_TAGS = 'Tags.graphql'
    UPDATE_TAGS = 'UpdateTags.graphql'
    UPDAT_STREET_NAME = 'UpdateStreetName.graphql'


    W_properties_number = 'id_number.graphql'
    W_properties_number_improwed = 'id_number.graphql'
    W_properties_Address_County = 'ADDRESS_County.graphql'
    W_properties_Address_State = 'ADDRESS_State.graphql'
    W_properties_Address_City = 'ADDRESS_City.graphql'
    W_properties_ID_CadastralNR = 'ADDRESS_ID_CadastralNR.graphql'
    ADD_Selected_properties = 'Add_property.graphql'
    ADD_properties_purpose = 'Add_purpose.graphql'
    UPDATE_project_properties = 'update_project_properties.graphql'
    CHECK_properties_Mylabl = 'Properties_ID_Cadastral.graphql'
    #delete
    D_ALL_properties = 'deleteProperty.graphql'


    def __init__(self):
        #Folders
        self.properties_folder = 'queries/graphql/properties'
        self.properties_WHERE_folder = 'queries/graphql/properties/WHERE'







    def load_query_properties_connected_elements(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(GraphQLQueryLoader.PLUGIN_DIR, path.properties_connections, query_file_name)
        #print(f"graphql path: {graphql_path}")
        with open(graphql_path, 'r') as file:
            return file.read()

class GraphqlContracts:

    ALL_CONTRACTS = 'contracts.graphql'
    CONTRACTS_MINIMAL = 'contracts_minimal.graphql'
    RELATED_PROPERTIES = 'W_contract_id.graphql'
    BY_CADASTRAL = 'propertiesrelated_contracts.graphql'
    UPDATE_CONTRACT_PROPERTIES = 'update_contract_properties.graphql'
    CONTRACT_TYPES = 'contract_types.graphql'
    WHERE_CONTRACTS_TYPE_STATUS = 'contracts_type_status.graphql'


class GraphqlEasements:
    EASMENT_TYPES = 'easements_types.graphql'
    WHERE_EASEMENTS_TYPE_STATUS = 'easements_type_status.graphql'
    UPDATE_EASEMENTS_PROPERTIES = 'update_easements_properties.graphql'
    Q_WHERE_EASEMENT_RELATED_PROPERTYS = 'W_easement_id.graphql'
    Q_All_EASEMENTS = 'easements.graphql'


class GraphqlTags:
    CREATE_TAG = 'CreateTag.graphql'
    TAGS_BY_MODULE = 'TagsByModule.graphql'
    TAGS_ID_BY_MODULE_AND_NAME = 'IDByModuleAndName.graphql'

class GraphqlStatuses:
    STATUSES = 'statuses.graphql'



class GraphQLQueryLoader:
    CURRENT_DIR = os.path.abspath(__file__)
    PLUGIN_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..', '..'))

    def __init__(self):
        
        # Navigate to the 'queries/graphql' folder and then into the 'graphql' subfolder
        self.graphql_folder = 'queries/graphql'
        self.properties_folder = 'queries/graphql/properties'

        self.properties_connections = 'queries/graphql/properties/Connected_data'
        self.projects_folder = 'queries/graphql/projects'
        self.contracts_folder ='queries/graphql/contracts'
        self.user_folder ='queries/graphql/user'
        self.easements_folder = 'queries/graphql/easements'

        

            #User related queries
        self.Q_All_Users = 'users.graphql'
        self.Q_Where_user = 'users_where.graphql'
        self.Q_me = 'me.graphql'

            #Projects related queries
        self.UPDATE_project_properties = 'update_project_properties.graphql'

        
        
    def load_query(self, query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(GraphQLQueryLoader.PLUGIN_DIR, path.graphql_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()
    @staticmethod
    def load_query_for_projects(query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(GraphQLQueryLoader.PLUGIN_DIR, path.projects_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()

    @staticmethod
    def load_query_properties( query_file_name):
        path = GraphQLQueryLoader()
        graphql_path = os.path.join(GraphQLQueryLoader.PLUGIN_DIR, path.properties_folder, query_file_name)
        with open(graphql_path, 'r') as file:
            return file.read()

    
    @staticmethod
    def load_query_by_module(module: Module, filename: str) -> str:

        folders = {
            Module.PROPRETIE: QueryFolders.PROPERTIES_FOLDER,
            Module.USER: QueryFolders.USER_FOLDER,
            Module.EASEMENT: QueryFolders.EASEMENTS_FOLDER,
            Module.PROJECT: QueryFolders.PROJECTS_FOLDER,
            Module.CONTRACT: QueryFolders.CONTRACTS_FOLDER,
            Module.TAGS: QueryFolders.TAGS_FOLDER,
            Module.STATUSES: QueryFolders.STATUS_FOLDERS
        }

        folder = folders.get(module)
        if not folder:
            raise ValueError(f"Unknown module: {module}")

        graphql_path = os.path.join(GraphQLQueryLoader.PLUGIN_DIR, folder, filename)
        with open(graphql_path, 'r') as file:
            return file.read()