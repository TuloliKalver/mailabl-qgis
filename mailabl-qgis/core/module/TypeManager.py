from ...config.settings import SettingsDataSaveAndLoad
from ...KeelelisedMuutujad.modules import Module
from ...queries.python.Statuses.statusManager import Statuses, ContractTypes, EasementTypes

class TypeManager:
    def __init__(self):
        self.type_sources = {
            Module.CONTRACT: ContractTypes.get_contract_types,
            Module.EASEMENT: EasementTypes.get_easement_types,
            # Add more as needed
        }

        self.preferred_item_ids = {
            Module.CONTRACT: lambda: SettingsDataSaveAndLoad().load_contracts_type_names(),    
            Module.EASEMENT: lambda: SettingsDataSaveAndLoad().load_easements_type_names(),
        }

        self.status_sources = {
            Module.PROJECT: lambda: SettingsDataSaveAndLoad().load_projects_status_id(),
            Module.CONTRACT: lambda:SettingsDataSaveAndLoad().load_contract_status_ids(),
            Module.EASEMENT: lambda:SettingsDataSaveAndLoad().load_easements_status_ids(),
            # Add more as needed
        }

        self.module_statuses_sources = {
            module: lambda m=module: Statuses().get_all_statuses_by_module(m)
            for module in [Module.PROJECT, 
                           Module.CONTRACT, 
                           Module.EASEMENT]
        }


    def _get_preferred_item_ids(self, module):
        """Return a set of preferred item IDs for the given module."""
        fn = self.preferred_item_ids.get(module, [])
        if not fn:
            return []
        return fn() if callable(fn) else fn
     
    def _get_preferred_statuses_for_module(self, module):
        fn = self.status_sources.get(module)
        if not fn:
            return []

        result = fn() if callable(fn) else fn
        return result if isinstance(result, list) else [result]

    def _get_all_statuses_for_module(self, module):
        print("Getting all statuses for module:", module)
        fn = self.module_statuses_sources.get(module)
        if not fn:
            return []
        return fn() if callable(fn) else fn

    def _get_types_for_module(self, module, context):
        """
        Calls the correct type provider based on the module.
        Passes `context` (usually `self` from calling class).
        """
        if module not in self.type_sources:
            raise ValueError(f"No type source registered for module: {module}")

        provider_fn = self.type_sources[module]
        return provider_fn(context)

        
