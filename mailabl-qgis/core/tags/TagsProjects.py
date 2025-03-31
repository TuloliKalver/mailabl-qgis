from PyQt5.QtCore import QCoreApplication
from ..DataLoading_classes import GraphQLQueryLoader, Graphql_project
from ..query_tools import requestBuilder




#//TODO: add project tags manager to projects and use it to paint map
class tagManager:
    def load_project_tags(self):
        query_loader = Graphql_project()
        query = GraphQLQueryLoader.load_query(query_loader.Projects_tags)

        # Initialize variables for pagination
        end_cursor = None

        variables = {
            "first": 50,  # Fetch any number of items per one query
            "after": end_cursor if end_cursor else None,  # Use the endCursor as the after value
            "where": {
                "AND": [
                    {
                    "column": "MODULE",
                    "value": "projects",
                    }
                ]
            }
        }

        response = requestBuilder.construct_and_send_request(self, query, variables)
        #print(response)
        if response.status_code == 200:
            data = response.json()
            #pprint(data)
            # Access the relevant part of the data structure
            statuses_data = data.get('data', {}).get('tags', {}).get('edges', [])
            #print(statuses_data)

            # Create a list to store node_info values
            tags_ids = []
            tag_names = []
            # Iterate through the statuses_data
            for status_info in statuses_data:
                # Access the node information
                node_info = status_info.get('node', {})
                tag_id = node_info.get('id',"")
                tag_name = node_info.get('name',"")

                # Append the node_info to the list
                tags_ids.append(tag_id)
                tag_names.append(tag_name)
                QCoreApplication.processEvents()

            #print(f"count tags ids: {len(tags_ids)}")
            return tag_names
