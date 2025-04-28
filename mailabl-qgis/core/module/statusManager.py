from PyQt5.QtCore import QCoreApplication
from ...queries.python.FileLoaderHelper import GraphQLQueryLoader,GraphqlStatuses, GraphqlTasks, GraphqlContracts, GraphqlProjects, GraphqlEasements
from ...queries.python.query_tools import requestBuilder
from ...KeelelisedMuutujad.modules import Module
from ...config.settings_new import PluginSettings


class ModuleStatuses:
    def __init__(self, module):
        self.module = module
        self.graphql_queries = {
            Module.PROJECT: GraphqlStatuses.STATUSES,
            Module.CONTRACT: GraphqlStatuses.STATUSES,
            Module.EASEMENT: GraphqlStatuses.STATUSES,
            Module.TASK: GraphqlStatuses.STATUSES,
        }

        self.preferred_ids = {
            Module.PROJECT: lambda:  PluginSettings.load_setting(module = Module.PROJECT, context=PluginSettings.CONTEXT_PREFERRED, key_type=PluginSettings.SUB_CONTEXT_IDs),
            Module.CONTRACT: lambda: PluginSettings.load_setting(module = Module.CONTRACT, context=PluginSettings.CONTEXT_PREFERRED, key_type=PluginSettings.SUB_CONTEXT_IDs),    
            Module.EASEMENT: lambda: PluginSettings.load_setting(module = Module.EASEMENT, context=PluginSettings.CONTEXT_PREFERRED, key_type=PluginSettings.SUB_CONTEXT_IDs),
            Module.TASK: lambda: PluginSettings.load_setting(module = Module.TASK, context=PluginSettings.CONTEXT_PREFERRED, key_type=PluginSettings.SUB_CONTEXT_IDs)
        }


        self.preferred_names = {
            Module.PROJECT: lambda:  PluginSettings.load_setting(module = Module.PROJECT, 
                                                                context=PluginSettings.CONTEXT_PREFERRED,
                                                                subcontext=PluginSettings.OPTION_STATUS,
                                                                key_type=PluginSettings.SUB_CONTEXT_NAME),
            Module.CONTRACT: lambda: PluginSettings.load_setting(module = Module.CONTRACT, 
                                                                context=PluginSettings.CONTEXT_PREFERRED,
                                                                subcontext=PluginSettings.OPTION_STATUS,
                                                                key_type=PluginSettings.SUB_CONTEXT_NAME),    
            Module.EASEMENT: lambda: PluginSettings.load_setting(module = Module.EASEMENT, 
                                                                context=PluginSettings.CONTEXT_PREFERRED,
                                                                subcontext=PluginSettings.OPTION_STATUS,
                                                                key_type=PluginSettings.SUB_CONTEXT_NAME),
            Module.TASK: lambda: PluginSettings.load_setting(module = Module.TASK, 
                                                                context=PluginSettings.CONTEXT_PREFERRED,
                                                                subcontext=PluginSettings.OPTION_STATUS,
                                                                key_type=PluginSettings.SUB_CONTEXT_NAME)
        }



    def _get_preferred_item_ids_or_names(self, module, name=False):
        """Return a set of preferred item IDs for the given module."""
        
        if name:
            fn = self.preferred_names.get(module, [])
        else:
            fn = self.preferred_ids.get(module, [])
    
        if not fn:
            return None
        return fn() if callable(fn) else fn



    def _get_all_statuses_for_module(self, module=None):
        module = module or self.module
        #print("Getting all statuses for module:", module)
        return self.get_module_statuses(module)


    def get_module_statuses(self, module):
        query_file = self.graphql_queries.get(module)
        if not query_file:
            print(f"⚠️ No GraphQL query registered for module: {module}")
            return []

        status_module = Module.STATUSES
        query = GraphQLQueryLoader.load_query_by_module(status_module, query_file)

        variables = {
            "where": {
                "AND": [
                    {
                        "column": "MODULE",
                        "value": f"{module}s",
                    }
                ]
            }
        }

        response = requestBuilder.construct_and_send_request(query, variables)
        if response is None or response.status_code != 200:
            print(f"❌ Error fetching statuses: {response.status_code if response else 'No response'}")
            return []

        QCoreApplication.processEvents()
        statuses_data = response.json().get("data", {}).get("statuses", {}).get("edges", [])

        statuses = []
        for status_info in statuses_data:
            node = status_info.get("node", {})
            status_name = node.get("name", "")
            status_id = node.get("id", "")
            statuses.append((status_name, status_id))

        QCoreApplication.processEvents()
        return statuses
