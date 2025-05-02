#TypeManager.py
from PyQt5.QtCore import QCoreApplication

from ...config.settings import SettingsDataSaveAndLoad
from ...config.settings_new import PluginSettings
from ...KeelelisedMuutujad.modules import Module
from .statusManager import ModuleStatuses

from PyQt5.QtCore import QCoreApplication
from ...queries.python.FileLoaderHelper import GraphQLQueryLoader, GraphqlContracts, GraphqlEasements, GraphqlTasks
from ...queries.python.query_tools import requestBuilder



class TypeModuleSetup:
    def __init__(self, module):
        self.module = module
        s = PluginSettings()

        self.graphql_queries = {
            Module.CONTRACT: lambda: GraphqlTasks.TYPES,
            Module.EASEMENT: lambda: GraphqlTasks.TYPES,
            Module.TASK: lambda: GraphqlTasks.TYPES
            # Add more as needed
        }

        self.preferred_item_ids = {
            Module.CONTRACT: lambda: PluginSettings.load_setting(module=Module.CONTRACT,
                                                                context=s.CONTEXT_PREFERRED,
                                                                subcontext=s.OPTION_TYPE, 
                                                                key_type=s.SUB_CONTEXT_IDs),    
            Module.EASEMENT: lambda: PluginSettings.load_setting(module=Module.EASEMENT,
                                                                context=s.CONTEXT_PREFERRED,
                                                                subcontext=s.OPTION_TYPE, 
                                                                key_type=s.SUB_CONTEXT_IDs),
            Module.TASK: lambda: PluginSettings.load_setting(module=Module.TASK,
                                                                context=s.CONTEXT_PREFERRED,
                                                                subcontext=s.OPTION_TYPE, 
                                                                key_type=s.SUB_CONTEXT_IDs)
        }

        self.preferred_item_names = {
            Module.CONTRACT: lambda: PluginSettings.load_setting(module=Module.CONTRACT,
                                                                context=s.CONTEXT_PREFERRED,
                                                                subcontext=s.OPTION_TYPE, 
                                                                key_type=s.SUB_CONTEXT_NAME,
                                                                ),    
    
            Module.EASEMENT: lambda: PluginSettings.load_setting(module=Module.EASEMENT,
                                                                context=s.CONTEXT_PREFERRED,
                                                                subcontext=s.OPTION_TYPE, 
                                                                key_type=s.SUB_CONTEXT_NAME,
                                                                ),
            Module.TASK: lambda: PluginSettings.load_setting(module=Module.TASK,
                                                                context=s.CONTEXT_PREFERRED,
                                                                subcontext=s.OPTION_TYPE, 
                                                                key_type=s.SUB_CONTEXT_NAME,
                                                                )
        }



    @staticmethod
    def build_type_query_string(module):
        return f"""
        query {module}Types($first: Int, $after: String) {{
            {module}Types(first: $first, after: $after) {{
                pageInfo {{
                    hasNextPage
                    endCursor
                    currentPage
                    total
                }}
                edges {{
                    node {{
                        id
                        name
                    }}
                }}
            }}
        }}
        """
    @staticmethod
    def build_type_query_variables(after_cursor=None, items_per_page=50):
        return {
            "first": items_per_page,
            "after": after_cursor if after_cursor else None
        }



    def _get_preferred_item_ids_or_names(self, module, name=False):
        """Return a set of preferred item IDs for the given module."""
        
        if name:
            fn = self.preferred_item_names.get(module, [])
        else:
            fn = self.preferred_item_ids.get(module, [])
    
        if not fn:
            return None
        return fn() if callable(fn) else fn

    def get_type_query(self, module):
        """Returns the GraphQL query string for a given module."""
        fn = self.graphql_queries.get(module)
        return fn() if fn else None 
    
    def _get_types_for_module(self, module=None):
        module = module or self.module
        #print("Getting all types for module:", module)
        return self.get_module_types(module)


    def get_module_types(self, module):
        query = self.build_type_query_string(module)
        types = []
        end_cursor = None

        while True:
            variables = {"first": 50, "after": end_cursor}
            response = requestBuilder.construct_and_send_request(query, variables)

            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                return None

            data = response.json()
            edges = data.get("data", {}).get(f"{module}Types", {}).get("edges", [])
            page_info = data.get("data", {}).get(f"{module}Types", {}).get("pageInfo", {})
            #print(f"page info is: {page_info}")
            for edge in edges:
                node = edge.get("node", {})
                types.append((node.get("name", ""), node.get("id", "")))
            #print(f"types are: {types}")
            if not page_info.get("hasNextPage"):
                break

            end_cursor = page_info.get("endCursor")

        return types


