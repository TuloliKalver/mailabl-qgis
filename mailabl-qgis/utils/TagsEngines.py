from ..KeelelisedMuutujad.modules import Module
from ..queries.python.query_tools import requestBuilder
from ..queries.python.FileLoaderHelper import GraphQLQueryLoader, GraphqlTags


MODULE = Module.TAGS
class TagsEngines:
    @staticmethod
    def create_tag(tag_name: str, module: str) -> bool:
        module_tags = Module.TAGS
        module_name = str(module).upper()
        module = module_name + "S"

        query_file = GraphqlTags.CREATE_TAG
        query = GraphQLQueryLoader.load_query_by_module(module=module_tags, filename=query_file)

        variables = {
            "input": {
                "name": tag_name,
                "module": module
            }
        }

        response = requestBuilder.construct_and_send_request(query, variables)
        if not response:
            print("Create tag failed — no response")
            return False

        result = response.json()
        if "errors" in result:
            print("Create tag error:", result["errors"])
            return False

        created_tag = result["data"]["createTag"]
        created_tag_id = created_tag["id"]
        print(f"Tag created: ID {created_tag_id} -> Name: {created_tag['name']}")
        return created_tag_id

    @staticmethod
    def load_tags_by_module(module: str ,first: int = 50, after: str = None, ) -> list:

        query_file = GraphqlTags.TAGS_BY_MODULE
        query = GraphQLQueryLoader.load_query_by_module(module=module, filename=query_file)


        variables = {
            "first": first,
            "after": after,
            "where": {
                "column": "MODULE",
                "value": module
            }
        }

        response = requestBuilder.construct_and_send_request(query, variables)
        if not response:
            print("Tag loading failed — no response")
            return []

        result = response.json()
        if "errors" in result:
            print("Tag loading error:", result["errors"])
            return []

        tags_data = result["data"]["tags"]
        tags = [edge["node"] for edge in tags_data["edges"]]

        print(f"Loaded {len(tags)} tags for {module} module:")
        for tag in tags:
            print(f" - {tag['id']}: {tag['name']}")

        return tags

    @staticmethod
    def get_modules_tag_id_by_name(tag_name: str,module: str) -> str: 
        #tag_name = "Arhiveeritud"
        module_name = str(module).upper()
        module = module_name + "S"

        query_file = GraphqlTags.TAGS_ID_BY_MODULE_AND_NAME
        query = GraphQLQueryLoader.load_query_by_module(module=MODULE, filename=query_file)

        variables = {
            "first": 50,
            "after": None,
            "where": {
                "column": "MODULE",
                "value": module
            }
        }

        response = requestBuilder.construct_and_send_request(query, variables)
        if not response:
            print("Failed to load tags")
            return None

        result = response.json()
        if "errors" in result:
            print("Error loading tags:", result["errors"])
            return None

        tags = result["data"]["tags"]["edges"]
        for tag in tags:
            if tag["node"]["name"].lower() == tag_name.lower():
                #print(f"Found tag '{tag_name}' -> ID: {tag['node']['id']}")
                return tag["node"]["id"]

        #print(f"Tag '{tag_name}' not found in module '{module}'")
        return None