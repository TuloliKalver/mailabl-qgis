import os
import gc

from qgis.core import QgsVectorLayer
from ..utils.fidOperationsHelper import fidOperations

from ..utils.LayerSetups import LayerSetups
from ..utils.LayerHelpers import LayerFilterSetters, LayerProcessHandlers, DuplicateLayerResolver
from ..Functions.layer_generator import LayerManager
from ..utils.ButtonsHelper import ButtonHelper
from ..utils.MapToolsHelper import MapToolsHelper
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..KeelelisedMuutujad.FolderHelper import MailablLayerNames
from ..Common.app_state import PropertiesProcessStage
from ..utils.LayerFeaturehepers import LayerFeatureHelpers
from ..queries.python.property_data import MyLablChecker, UpdateData
from ..utils.ArchiveLayerHandler import ArchiveLayerHandler
from ..utils.ProgressHelper import ProgressDialogModern

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
        heading = "Kinnistute haldamine..."
        progress = ProgressDialogModern(title=heading)
        progress.update(purpouse="Võrdlen kaardikihte...")
        field = Katastriyksus.tunnus
        
        active_layer, target_layer_from_mappings = LayerFilterSetters._copy_layer_filter_by_preassigned_layers()
        target_cadastrals = LayerProcessHandlers._get_comparison_fields_list_and_element_ids(field_name=field,layer=target_layer_from_mappings)
        active_cadastrals = LayerProcessHandlers._get_comparison_fields_list_and_element_ids(field_name=field, layer=active_layer)

        progress.update(text1=f"{target_cadastrals} / {active_cadastrals}")
        target_keys = set(target_cadastrals.keys())
        active_keys = set(active_cadastrals.keys())

        # Calculate differences:
        not_available_anymore = target_keys - active_keys  # Keys present in target but missing in active
        missing_in_active = active_keys - target_keys  # Keys present in active but missing in target

        # Retrieve element IDs corresponding to the missing keys (note the swap):
        not_available_anymore_ids = [target_cadastrals[key] for key in not_available_anymore]
        missing_in_active_ids = [active_cadastrals[key] for key in missing_in_active]
        print(f"to be archived {not_available_anymore_ids}")
        print(f"to be added {missing_in_active_ids}")

        progress.update(text1=f"Arhiveeritavate koguarv: {len(not_available_anymore)}\nUuendatavate koguarv: {len(missing_in_active)}", value=len(not_available_anymore))

        if not missing_in_active and not not_available_anymore:
            progress.close()
            return False



        if not_available_anymore:
            MapToolsHelper.select_features_by_ids(feature_ids=not_available_anymore_ids, 
                                                  layer=target_layer_from_mappings)
            
            
            max_items = len(not_available_anymore_ids)

            progress.update(purpouse=f"Arhiveerimine...", maximum=max_items)

            sandbox_layer_name = MailablLayerNames.SANDBOX_LAYER
            sandbox_layer = LayerManager._check_layer_existance_by_name(sandbox_layer_name)
            
            #print(f"Returned layer: {layer}")
            if sandbox_layer == None:
                sandbox_layer = LayerManager._create_memory_layer_by_coping_original_layer(sandbox_layer_name, active_layer, is_archive=True)
                LayerManager._add_layer_to_sandbox_group(sandbox_layer)
                gc.collect()  # Force garbage collection
            else:
                nex_id=fidOperations._get_layers_next_ids(target_layer=sandbox_layer)
                LayerSetups.register_layer_configuration(sandbox_layer,max_fid=nex_id)
            
            

            for count, feat_id in enumerate(not_available_anymore_ids, start=1):
                is_last = count == max_items  # Check if this is the last iteration returns True or False
                commit = is_last  # Only commit on the last one

                LayerFilterSetters._move_feature_data_and_geometry_between_layers(input_layer=target_layer_from_mappings, 
                                                                                    feature_id=feat_id,
                                                                                    target_layer=sandbox_layer,
                                                                                    delete_input_data=True,
                                                                                    commit=commit)
                
            archive_features = LayerProcessHandlers._get_features_or_IDs_from_layer(sandbox_layer, return_ids_only=True)
                            
            archive_layer_name = MailablLayerNames.ARCHIVE_LAYER_NAME
            archive_layer = ArchiveLayerHandler.resolve_or_create_archive_layer(target_layer_from_mappings, archive_layer_name)
            
            res = AddProperties.store_to_archive_PROCESS(archive_layer, archive_features, sandbox_layer, progress)
            if res:
                LayerManager.remove_existing_layer(sandbox_layer_name)
                #MessageLoaders.show_message('Tehtud', f"Arhiveeritud id: {feat_to_archive}")
                gc.collect()      
        
            if not missing_in_active_ids:
                progress.close()
                return True
                

        if missing_in_active_ids:

            max_items = len(missing_in_active)

            progress.update(purpouse=f"Uute andmete lisamine...", maximum=max_items)

            MapToolsHelper.select_features_by_ids(feature_ids=missing_in_active_ids,
                                                  layer=active_layer)
            #print(f"Missing in active ids: {missing_in_active_ids}")

            for count, feat_id in enumerate(missing_in_active_ids, start=1):
                is_last = count == max_items  # Check if this is the last iteration returns True or False
                commit = is_last  # Only commit on the last one

                LayerFilterSetters._move_feature_data_and_geometry_between_layers(
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

        
         
    @staticmethod
    def store_to_archive_PROCESS(arvhive_layer: QgsVectorLayer, features_ids:int, archive_memory_layer, progress) -> bool: 
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
                
        max_items = len(features_ids)

        progress.update(maximum=max_items)

        for count, feat_id in enumerate(features_ids, start=1):
            is_last = count == max_items  # Check if this is the last iteration returns True or False
            commit = is_last  # Only commit on the last one
        
            LayerFilterSetters._move_feature_data_and_geometry_between_layers(
            input_layer=archive_memory_layer,
            feature_id=feat_id,
            target_layer=arvhive_layer,
            delete_input_data=False,
            commit=commit)


            print(f"Layer archiving completed.")
            
            feature =LayerFeatureHelpers._get_layer_fetaures_by_id(layer=archive_memory_layer, feature_id=feat_id)

            layer_data = LayerFeatureHelpers._get_feature_attributes_as_dict(feature=feature)
            #print (f"layer_data: {layer_data}")
            tunnus = layer_data.get(Katastriyksus.tunnus)
            #print (f"Tunnus: {tunnus}")            
            res, id = MyLablChecker._get_propertie_ids_by_cadastral_numbers_EQUALS(item=tunnus)
            #print(f"res: {res} and id: {id}")
            if res is True:
                print(f"No property with ID {id} found.")
                print("No need to update data!")
            else:
                UpdateData._update_archived_properies_data(id)
            progress.update(value=count)

        return True

                