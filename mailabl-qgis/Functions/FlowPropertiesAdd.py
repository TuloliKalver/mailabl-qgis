import os
import gc
from ..utils.LayerHelpers import LayerFilterSetters, LayerProcessHandlers, LayerSetups, fidOperations, DuplicateLayerResolver
from ..Functions.layer_generator import LayerManager
from ..utils.ButtonsHelper import ButtonHelper
from ..utils.MapToolsHelper import MapToolsHelper
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..KeelelisedMuutujad.FolderHelper import MailablLayerNames
from ..Common.app_state import PropertiesProcessStage, Layers_NEED_CENTRALIZING


class AddProperties:
    test = "test"

    @staticmethod
    def set_buttons_in_dev():
        action = 'pbConfirmAction'
        cancel = 'pbCancelAction'
        button_names = [action, cancel]
        buttons = ButtonHelper.get_button_objects(button_names)

        #print(f"Buttons are: {buttons}")
        for button in buttons:
            button.setEnabled(True)
        print("do not forget to remove me!!!")        

    @staticmethod
    def add_properties_final_flow_controller():
        """
        First we copy the layer filter from the active_layer to target layer to query only filtered items on layer. The Layers are loaded on preset parameters. 
        Get current cadastrals on target_layer
        Compare difrences on the two layers and then make list of difrences
        Select diferences on both layers 
        """
        print("stage define layers")
        active_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if info.get('activated')), None)
        target_layer_from_mappings = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if not info.get('activated')), None)
        #print(f"active layer {active_layer}")
        #print(f"target_layer {target_layer_from_mappings}")
        field = Katastriyksus.tunnus
        
        #print("stage load layers")
        LayerFilterSetters._copy_layer_filter_by_preassigned_layers()
        target_cadastrals = LayerProcessHandlers.get_comparison_fields_list_and_element_ids(field_name=field,layer=target_layer_from_mappings)
        active_cadastrals = LayerProcessHandlers.get_comparison_fields_list_and_element_ids(field_name=field, layer=active_layer)

        #print("stage compare layers")
        # Convert keys to sets for comparison
        target_keys = set(target_cadastrals.keys())
        active_keys = set(active_cadastrals.keys())

        # Calculate differences:
        not_available_anymore = target_keys - active_keys  # Keys present in target but missing in active
        missing_in_active = active_keys - target_keys  # Keys present in active but missing in target

        # Retrieve element IDs corresponding to the missing keys (note the swap):
        not_available_anymore_ids = [target_cadastrals[key] for key in not_available_anymore]
        missing_in_active_ids = [active_cadastrals[key] for key in missing_in_active]
        #print(f"to be archived {not_available_anymore_ids}")
        #print(f"to be added {missing_in_active_ids}")

        
        if not_available_anymore:
            print("not available anymore")
            MapToolsHelper.select_features_by_ids(feature_ids=not_available_anymore_ids, 
                                                  layer=target_layer_from_mappings)
            sandbox_layer_name = MailablLayerNames.SANDBOX_LAYER
            print("stage move data")            
            sandbox_layer = LayerManager.check_layer_existance_by_name(sandbox_layer_name)
            #print(f"Returned layer: {layer}")
            if sandbox_layer == None:
                sandbox_layer = LayerManager.create_memory_layer_by_coping_original_layer(sandbox_layer_name, active_layer, is_archive=True)
                LayerManager.add_layer_to_sandbox_group(sandbox_layer)
                gc.collect()  # Force garbage collection
            else:
                print("stage get next fid")
                nex_id=fidOperations.get_next_fid(target_layer=sandbox_layer)
                LayerSetups.register_layer_configuration(sandbox_layer,max_fid=nex_id)
            
            for feat_to_archive in not_available_anymore_ids:
                #move to archive layer
                print(f"targetlayer = {target_layer_from_mappings}")
                result = LayerFilterSetters._move_data_and_geometry_between_layers(input_layer=target_layer_from_mappings, 
                                                                                   feature_id=feat_to_archive,
                                                                                   target_layer=sandbox_layer,
                                                                                   delete_input_data=True,
                                                                                   commit=False)
        
            gc.collect()  # Force garbage collection
            AddProperties.store_to_archive()
            LayerManager.remove_existing_layer(sandbox_layer_name)
            #MessageLoaders.show_message('Tehtud', f"Arhiveeritud id: {feat_to_archive}")
            gc.collect()      
        
        if missing_in_active_ids:
            print("stage missing in active")
            MapToolsHelper.select_features_by_ids(feature_ids=missing_in_active_ids,
                                                  layer=active_layer)
            #print(f"Missing in active ids: {missing_in_active_ids}")
            max_items = len(missing_in_active)
            from ..utils.ProgressHelper import ProgressDialogModern
            heading = "Salvestamine"
            progress = ProgressDialogModern(maximum=max_items, title=heading)

            for count, feat_id in enumerate(missing_in_active_ids, start=1):
                is_last = count == max_items  # Check if this is the last iteration returns True or False
                commit = is_last  # Only commit on the last one

                LayerFilterSetters._move_data_and_geometry_between_layers(
                    input_layer=active_layer,
                    feature_id=feat_id,
                    target_layer=target_layer_from_mappings,
                    delete_input_data=False,
                    commit=commit,
                    update_data=True
                )

                progress.update(value=count)

            progress.close()
            gc.collect()
            return True

        if missing_in_active_ids or not_available_anymore_ids:
            return False
        
         
    @staticmethod
    def store_to_archive() -> bool: 
        """
        Stores the archive memory layer to file and then removes the temporary archive memory layer.
        
        This method:
        - Retrieves the active layer.
        - Checks for the existence of the pre-archive memory layer.
        - If the pre-archive layer is a memory layer, it stores it to the GeoPackage.
        - Attempts to remove the pre-archive layer from the project.
        
        Returns:
            bool: True if the archive was stored and the temporary archive layer was removed successfully;
                False otherwise.
        """
        #TODO Remove after testing
        #layers_config = [            
        #    {"name": Layers_NEED_CENTRALIZING.IMPORT_LAYER_NAME, "activated": True, "cleanup": True},
        #    {"name": Layers_NEED_CENTRALIZING.USER_LAYER_NAME, "activated": False, "cleanup": False}
        #    ]
        #LayerProcessHandlers.load_and_handle_layers(layers_config)
        #TODO Remove after testing until here

        active_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if not info.get('activated')), None)
        
        archive_memory_layer = DuplicateLayerResolver.resolve_duplicate_layers_auto(layer_name=MailablLayerNames.SANDBOX_LAYER)

        print(f"Archive memory layer: {archive_memory_layer}")
        if archive_memory_layer is None:
            print("No pre-archive layer found.")
            return False

        if archive_memory_layer.dataProvider().name() == "memory":
            if archive_memory_layer.isValid():
                #print(f"active_layer: {active_layer}")
                res, returned_features = LayerManager.store_memory_layer_to_geopackage(memory_layer=archive_memory_layer, target_layer_for_file=active_layer, new_layer_name = MailablLayerNames.ARCHIVE_LAYER_NAME)
                
                if res is not None:
                    print(f"Returned features: {returned_features}")
                    print("Stored archive memory layer to file")
                    return True
                else:
                    print("Failed to store archive memory layer to file")
                    return False
            else:
                print("The pre-archive layer is invalid.")
                return False
            
        else:
            print(f"Found a named layer: that is not a memory layer")
            return False

                






class DataComparisons:
    def extract_base_key(full_key, split_level=2):
        """
        Extracts the base part of the cadastral number from a full key.
        
        By default, this function keeps the first two segments of a key separated
        by colons. For example, given "62510:013:0001" and split_level=2, the base
        will be "62510:013".
        
        Args:
            full_key (str): The complete cadastral key.
            split_level (int): The number of segments to keep.
            
        Returns:
            str: The base portion of the key.
        """
        parts = full_key.split(':')
        return ':'.join(parts[:split_level])

    def group_by_base(cadastral_dict, split_level=2):
        """
        Groups dictionary entries by a base key extracted from each full key.
        
        The dictionary values are stored as a list of tuples (full_key, element_id)
        for each base key.
        
        Args:
            cadastral_dict (dict): Dictionary with full cadastral keys as keys.
            split_level (int): The number of segments to use for the base key.
            
        Returns:
            dict: A mapping from base key to a list of (full_key, element_id) tuples.
        """
        grouped = {}
        for full_key, elem_id in cadastral_dict.items():
            base = DataComparisons.extract_base_key(full_key, split_level)
            grouped.setdefault(base, []).append((full_key, elem_id))
        return grouped

    def get_non_matching_by_base(current_cadastrals, import_cadastrals, split_level=2):
        """
        Compares two cadastral dictionaries by their base keys and returns non-matching groups.
        
        Each dictionary is first grouped by its base key (extracted from the full key).
        Then, base keys that do not appear in the other dictionary are returned.
        
        Args:
            current_cadastrals (dict): The first cadastral dictionary.
            import_cadastrals (dict): The second cadastral dictionary.
            split_level (int): The number of segments to use for extracting the base key.
            
        Returns:
            tuple: Two dictionaries:
                - The first dictionary contains base keys (and associated full entries)
                that are present only in current_cadastrals.
                - The second dictionary contains base keys (and associated full entries)
                that are present only in import_cadastrals.
        """
        current_grouped = DataComparisons.group_by_base(current_cadastrals, split_level)
        import_grouped = DataComparisons.group_by_base(import_cadastrals, split_level)
        # Print only the first 10 items from each grouped dictionary
        #print("Current Grouped (first 10):", dict(list(current_grouped.items())[:10]))
        #print("Import Grouped (first 10):", dict(list(import_grouped.items())[:10]))
        current_non_matches = {base: entries for base, entries in current_grouped.items() if base not in import_grouped}
        import_non_matches = {base: entries for base, entries in import_grouped.items() if base not in current_grouped}
        # Limit the printout to the first 10 items
        print("Current Non-Matches (first 10):", dict(list(current_non_matches.items())))
        print("Import Non-Matches (first 10):", dict(list(import_non_matches.items())))        


        return current_non_matches, import_non_matches
