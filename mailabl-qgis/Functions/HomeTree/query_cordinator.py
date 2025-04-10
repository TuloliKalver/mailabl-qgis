from ...KeelelisedMuutujad.modules import Module
from ...queries.python.FileLoaderHelper import GraphqlProperties, GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder
from ...queries.python.responses import HandlePropertiesResponses
from ...queries.python.FileLoaderHelper import GraphqlProperties



class PropertiesConnectedElementsQueries:
    module_to_filename = {
        Module.CONTRACT: "connected_contracts.graphql",
        Module.COORDINATION: "connected_coordinations.graphql",
        Module.EASEMENT: "connected_easements.graphql",
        Module.PROJECT: "connected_projects.graphql",
        Module.SPECIFICATION: "connected_specifications.graphql",
        Module.SUBMISSION: "connected_submissions.graphql",
        Module.TASK: "connected_tasks.graphql"
    }

    def __init__(self):
        self.query_loader = GraphQLQueryLoader()
        self.handle_response = HandlePropertiesResponses()

    def load_query_properties(module_name):
        cl = PropertiesConnectedElementsQueries()
        module_file = cl.module_to_filename.get(module_name)
        if not module_file:
            raise ValueError(f"Module name {module_name} is not valid.")
        GraphqlProperties().load_query_properties_connected_elements(module_file)


    def fetch_module_data(self, module_name, propertie_id):
        module_file = self.module_to_filename.get(module_name)
        #print(f"module_name: {module_name}")
        #print(f"file_name: {module_file}")


        if not module_file:
            return
            #raise ValueError(f"Module name {module_name} is not valid.")

        query = GraphqlProperties().load_query_properties_connected_elements(module_file)

        first_value = 30

        #print(f"guery: {query}")
        if module_name == Module.TASK:
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

        response = requestBuilder().construct_and_send_request(query, variables)

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
        if module_name == Module.CONTRACT:
            values = data['data']['property'][f"{Module.CONTRACT}s"]['edges']
            result.append(values)
        elif module_name == Module.PROJECT:
            values = data['data']['property'][f"{Module.PROJECT}s"]['edges']
            result.append(values)
        elif module_name == Module.COORDINATION:
            values = data['data']['property'][f"{Module.COORDINATION}s"]['edges']
            result.append(values)
        elif module_name == Module.EASEMENT:
            values = data['data']['property'][f"{Module.EASEMENT}s"]['edges']
            result.append(values)

        elif module_name == Module.SPECIFICATION:
            values = data['data']['property'][f"{Module.SPECIFICATION}s"]['edges']
            result.append(values)

        elif module_name == Module.SUBMISSION:
            values = data['data']['property'][f"{Module.SUBMISSION}s"]['edges']
            result.append(values)

        elif module_name == Module.TASK:
            values = data['data']['property'][f"{Module.TASK}s"]['edges']
            result.append(values)

        #print(f"result: {result}")
        return result