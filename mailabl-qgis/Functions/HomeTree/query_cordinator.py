from ...KeelelisedMuutujad.modules import Modules
from ...queries.python.DataLoading_classes import Graphql_properties, GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder
from ...queries.python.responses import handleResponse
from ...queries.python.DataLoading_classes import Graphql_properties



class PropertiesConnectedElementsQueries:
    module_to_filename = {
        Modules.MODULE_CONTRACTS: "connected_contracts.graphql",
        Modules.MODULE_COORDINATION: "connected_coordinations.graphql",
        Modules.MODULE_EASEMENTS: "connected_easements.graphql",
        Modules.MODULE_PROJECTS: "connected_projects.graphql",
        Modules.MODULE_SPECIFICATIONS: "connected_specifications.graphql",
        Modules.MODULE_SUBMISSIONS: "connected_submissions.graphql",
        Modules.MODULE_TASKS: "connected_tasks.graphql"
    }

    def __init__(self):
        self.query_loader = GraphQLQueryLoader()
        self.handle_response = handleResponse()

    def load_query_properties(self, module_name):
        module_file = self.module_to_filename.get(module_name)
        if not module_file:
            raise ValueError(f"Module name {module_name} is not valid.")
        Graphql_properties().load_query_properties_connected_elements(module_file)


    def fetch_module_data(self, module_name, propertie_id):
        module_file = self.module_to_filename.get(module_name)
        #print(f"module_name: {module_name}")
        #print(f"file_name: {module_file}")


        if not module_file:
            return
            #raise ValueError(f"Module name {module_name} is not valid.")


        query = Graphql_properties().load_query_properties_connected_elements(module_file)

        first_value = 30

        #print(f"guery: {query}")
        if module_name == Modules.MODULE_TASKS:
            variables = {
                "id": propertie_id,
                "first": first_value,
                "orderBy": [
                    {
                    "column": "PRIORITY",
                    "order": "DESC"
                    },
                    {
                    "column": "TITLE",
                    "order": "ASC"
                    }
                ]
                }
        else:
            variables = {
            "id": propertie_id,
            "first": first_value,
            "orderBy": [
                {
                "column": "NUMBER",
                "order": "ASC"
                }
            ] 
            }

        response = requestBuilder().construct_and_send_request(None, query, variables)

        if response.status_code == 200:
            data = response.json()
            result = ProcessElementData().process_response_data(module_name, data)
            #print(f"returned data: {data}")
            return result
        else:
            #print(f"Failed to fetch data: {response.status_code}")
            pass

class ProcessElementData:
    def process_response_data(self, module_name, data):
        result = []
        #print(f"data: {data}")

        # Identify the module name by checking which key exists in the response data
        if module_name == Modules.MODULE_CONTRACTS:
            values = data['data']['property'][Modules.MODULE_CONTRACTS]['edges']
            result.append(values)
        elif module_name == Modules.MODULE_PROJECTS:
            values = data['data']['property'][Modules.MODULE_PROJECTS]['edges']
            result.append(values)
        elif module_name == Modules.MODULE_COORDINATION:
            values = data['data']['property'][Modules.MODULE_COORDINATION]['edges']
            result.append(values)
        elif module_name == Modules.MODULE_EASEMENTS:
            values = data['data']['property'][Modules.MODULE_EASEMENTS]['edges']
            result.append(values)

        elif module_name == Modules.MODULE_SPECIFICATIONS:
            values = data['data']['property'][Modules.MODULE_SPECIFICATIONS]['edges']
            result.append(values)

        elif module_name == Modules.MODULE_SUBMISSIONS:
            values = data['data']['property'][Modules.MODULE_SUBMISSIONS]['edges']
            result.append(values)

        elif module_name == Modules.MODULE_TASKS:
            values = data['data']['property'][Modules.MODULE_TASKS]['edges']
            result.append(values)

        #print(f"result: {result}")
        return result