#LayerHelper.py

import gc
from typing import Optional, List, Dict, Any
from qgis.utils import iface # type: ignore
from qgis.core import QgsFeature, QgsFeatureRequest, QgsProject, QgsVectorLayer # type: ignore
from PyQt5.QtWidgets import QMessageBox
from ..Common.app_state import PropertiesProcessStage, Expressions, MainVariables
from ..utils.MessagesHelpers import MessageLoaders, TextMessages, TitleMessages
from ..utils.Logging.Logger import TracebackLogger


class LayerSetups:

    @classmethod
    #def load_layer_with_activation_option(cls, layer_name, activate=False):
    def load_layer_with_activation_option(cls, layer_name: str, activate: bool = False) -> Optional[QgsVectorLayer]:
        """
        Load a specific QGIS layer by name and optionally activate it.

        Activation includes:
         - Making the layer visible in the layer tree.
         - Setting the layer as active in QGIS.
         - Triggering the selection tool so the user can start selecting features.

        :param layer_name: str
            The name of the layer to load.
        :param activate: bool
            If True, the loaded layer will be activated (made visible, set as active, and selection tool triggered).
            Default is False.
        :return: Optional[QgsVectorLayer]
            Returns the loaded QgsVectorLayer if found; otherwise, returns None.
        """
        # Find the layer by name.
        layer = QgsProject.instance().mapLayersByName(layer_name)
        if layer:
            print(f"Layer '{layer_name}' found.")
            selected_layer = layer[0]
            if activate:
                # Make sure the layer is visible in the layer tree.
                layer_tree = QgsProject.instance().layerTreeRoot()
                layer_node = layer_tree.findLayer(selected_layer.id())
                if layer_node:
                    layer_node.setItemVisibilityChecked(True)
                
                # Set the layer as active in QGIS.
                iface.setActiveLayer(selected_layer)
                # Activate the selection tool so the user can select features.
                iface.actionSelect().trigger()
            return selected_layer
        else:
            MessageLoaders.layername_error(layer_name)
            TracebackLogger.log_traceback(custom_message=layer_name)
            return None

    @classmethod
    def unload_layer_usage(cls, layer: QgsVectorLayer):
        """
        Unload the usage of the provided layer instance by:
        - Clearing any selections on the layer.
        - Ending editing mode if the layer is editable.
        - Switching to the pan tool to ensure no other tool remains active.
        - Resetting the layer's feature filter expression.
        """

        if not layer:
            MessageLoaders.show_message(TitleMessages.error, TextMessages.no_layer_provided)
            TracebackLogger.log_traceback(custom_message=layer.name())
            return

        # Clear any selection on the layer (for vector layers)
        try:
            layer.removeSelection()
        except Exception:
            # If the layer type doesn't support selection removal, ignore the error.
            pass

        # If the layer is in editing mode, toggle editing off.
        if layer.isEditable():
            iface.actionToggleEditing().trigger()

        # Activate the pan tool to deactivate any other active tools.
        iface.actionPan().trigger()

        # Clear the feature filter expression.
        try:
            layer.setSubsetString('')
        except Exception:
            # If the layer does not support subset string changes, ignore the error.
            pass

    @staticmethod
    def register_layer_configuration(layer: QgsVectorLayer, activate: bool = False, cleanup: bool = False, is_archive_memory: bool = False,  max_fid: Optional[int] = None) -> None:
        """
        Register the configuration settings for a layer by storing it in AppState.loaded_layers.

        :param layer: QgsVectorLayer - the layer to register.
        :param activate: bool - indicates if the layer should be activated (default is False).
        :param cleanup: bool - indicates if the layer should be flagged for cleanup (default is False).
        :param max_fid: Optional[int] - the maximum feature ID; if None, it defaults to 1.
        :return: None
        """
        if max_fid is None:
            max_fid = 1
        layer_name: str = layer.name()
        PropertiesProcessStage.loaded_layers[layer_name] = {
            MainVariables.Layer: layer,
            MainVariables.CLEANUP: cleanup,
            MainVariables.ACTIVATE: activate,
            MainVariables.MAX_ID: max_fid,
            MainVariables.IS_ARCHIVE: is_archive_memory

        }
        gc.collect()  # Force garbage collection after updating configuration
        #print(f"Layer '{layer_name}' registered with settings: activate={activate}, cleanup={cleanup}, max_fid={max_fid}")

    @staticmethod
    def unregister_layer_configuration(layer_name: str) -> bool:
        """
        Unregister a layer from the AppState.loaded_layers configuration.

        :param layer: QgsVectorLayer - the layer to unregister.
        :return: bool - True if the layer was successfully removed, False otherwise.
        """
        if layer_name in PropertiesProcessStage.loaded_layers:
            del PropertiesProcessStage.loaded_layers[layer_name]
            gc.collect()  # Force garbage collection after removal
            #print(f"Layer '{layer_name}' removed from loaded layers.")
            return True
        else:
            #print(f"Layer '{layer_name}' not found in loaded layers.")
            return False

class DuplicateLayerResolver:
    @staticmethod
    def resolve_duplicate_layers(layer_name):
        """
        Resolves duplicate layers by letting the user choose which one to keep.
        Each layer with the given name is activated in turn and the user is prompted
        with a message dialog. As soon as the user chooses to keep a layer, all
        other layers with the same name are removed.
        If no layer is chosen (user declines for all), the first layer is kept by default.
        """
        # Retrieve all layers with the given name.
        layers = QgsProject.instance().mapLayersByName(layer_name)
        
        if not layers:
            QMessageBox.information(None, "Layer Resolution",
                                    f"No layers found with the name '{layer_name}'.")
            return

        if len(layers) == 1:
            QMessageBox.information(None, "Layer Resolution",
                                    f"Only one layer found with the name '{layer_name}'. Nothing to resolve.")
            return

        final_keep = None
        total = len(layers)

        # Iterate over layers and ask the user which one to keep.
        for idx, layer in enumerate(layers, start=1):
            # Activate the current layer for visual inspection.
            iface.setActiveLayer(layer)
            answer = QMessageBox.question(
                None,
                "Keep Layer?",
                f"({idx} of {total}) Do you want to keep the layer '{layer.name()}'?\n"
                "Click Yes to keep this layer (all others will be removed), or No to consider the next one.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if answer == QMessageBox.Yes:
                final_keep = layer
                break

        # If the user did not choose any layer, default to the first one.
        if final_keep is None:
            final_keep = layers[0]
            QMessageBox.information(None, "Default Selection",
                                    f"No selection was made. Defaulting to keep the first layer: '{final_keep.name()}'.")

        # Remove all layers with the same name except the final kept one.
        for layer in layers:
            if layer.id() != final_keep.id():
                QgsProject.instance().removeMapLayer(layer.id())
                QMessageBox.information(None, "Layer Removed",
                                        f"Removed layer '{layer_name}'.")

        QMessageBox.information(None, "Layer Resolution Complete",
                                f"Final kept layer: '{final_keep.name()}'.")
        return final_keep
    
    @staticmethod
    def resolve_duplicate_layers_auto(layer_name: str):
        """
        Automatically resolves duplicate layers by keeping the first layer with the specified name
        and removing all other duplicates. A summary message is displayed at the end.
        """
        layers = QgsProject.instance().mapLayersByName(layer_name)
        total_layers = len(layers)
        # Handle case where no layers exist.
        if not layers:
            QMessageBox.information(None, "Layer Resolution",
                                    f"No layers found with the name '{layer_name}'.")
            return None

        # If there's only one layer, return it directly.
        if len(layers) == 1:
            #QMessageBox.information(None, "Layer Resolution",
            #                        f"Only one layer found with the name '{layer_name}'. Nothing to resolve.")
            return layers[0]  # Return the single layer directly

        # Keep the first layer and remove the rest.
        kept_layer = layers[0]
        duplicates_removed = 0

        for layer in layers:
            if layer.id() != kept_layer.id():
                QgsProject.instance().removeMapLayer(layer.id())
                duplicates_removed += 1

        # Show summary message.
        QMessageBox.information(None, "Layer Resolution Complete",
                                f"Removed {duplicates_removed} duplicate(s) from {total_layers} layers.\n"
                                f"Kept layer: '{kept_layer.name()}'.")
        return kept_layer

    
class LayerProcessHandlers:
    @classmethod
    def load_and_handle_layers(cls, layers_info):
        """
        Load multiple layers based on the provided configuration.
        Each dictionary in layers_info should have:
        - "name": layer name
        - "activate": bool indicating if the layer should be activated
        - "cleanup": bool indicating if the layer should be unloaded during cleanup
        Returns True if all layers are loaded successfully, False otherwise.
        """
        PropertiesProcessStage.loaded_layers = {}  # Reset the loaded layers dictionary.

        for info in layers_info:
            layer_name = info.get(MainVariables.NAME)
            activate = info.get(MainVariables.ACTIVATE, False)
            cleanup = info.get(MainVariables.CLEANUP, False)
            print(f"Loading layer: {layer_name}. Activate: {activate}, Cleanup: {cleanup}")
            layer = LayerSetups.load_layer_with_activation_option(layer_name, activate=activate)
            max_fid = fidOperations.get_next_fid(target_layer=layer)
            if not layer:
                MessageLoaders.layername_error(layer_name)
                return False

            LayerSetups.register_layer_configuration(layer=layer,activate=activate,cleanup=cleanup, max_fid=max_fid)
            # Directly assign AppState.active_layer if activate is True
            if activate:
                PropertiesProcessStage.active_layer = layer 
        gc.collect()  # Force garbage collection
        return True
    
    @staticmethod
    def set_or_reset_fid(layer_name, max_fid=None):
        # Find the layer by name.
        layer = QgsProject.instance().mapLayersByName(layer_name)
        if layer:
            layer = layer[0]
        LayerSetups.register_layer_configuration(layer=layer, max_fid=max_fid)
        
    @staticmethod
    def get_comparison_fields_list_and_element_ids(field_name, layer):
        """
        Retrieve non-null field values and their corresponding element IDs from a QGIS layer,
        and combine them in a dictionary for easy lookup.

        This function iterates over the features in the provided layer, extracts the value 
        for the specified field (if it's not None), and maps it to the feature's ID in a dictionary.
        Note: If the same field value appears more than once, later features will overwrite earlier ones.

        Args:
            field_name (str): The field name to extract values from.
            layer (QgsVectorLayer): The QGIS layer to process.

        Returns:
            dict: A dictionary where each key is a field value and each value is the corresponding feature ID.
        """
        field_value_to_id = {}
        
        for feature in layer.getFeatures():
            value = feature[field_name]
            if value is not None:
                field_value_to_id[value] = feature.id()
        
        return field_value_to_id




class LayerFilterSetters:
    @staticmethod
    def _copy_layer_filter_by_preassigned_layers():
        active_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if info.get('activated')), None)
        target_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if not info.get('activated')), None)

        # Get references to the layers
        if active_layer is None or target_layer is None:
            print("Error: One or both layers not found.")
            return

        # Retrieve the filter from the input layer
        expression = active_layer.subsetString()

        if expression is None:
            print("Error: No filter found on the input layer.")
            return
        target_layer.setSubsetString(expression)

    @staticmethod
    def _reset_layer_filters():
        target_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if not info.get('activated')), None)
        expression = Expressions.clear
        target_layer.setSubsetString(expression)

    @staticmethod
    def _move_data_and_geometry_between_layers(input_layer, 
                                               feature_id, 
                                               target_layer, 
                                               delete_input_data=False,
                                               commit=False,
                                               update_data=False):
        """
        Move features (geometry and attributes) from the input_layer to the target_layer.
        New features will be created so that QGIS assigns them new unique IDs.
        
        :param input_layer: QgsVectorLayer from which features will be moved.
        :param feature_ids: List of feature IDs to move.
        :param target_layer: The target QgsVectorLayer where features will be added.
        :param delete_input_data: If True, delete the features from the input_layer after moving.
        """

        result = FeaturePreparations._feature_preparations_between_layers_using_name_for_field_detections(input_layer=input_layer, target_layer=target_layer, feature_id=feature_id)
        if result is False:
            print("The function returned False: no features found in the archive layer.")
            return False
        elif result is None:
            print("The function returned None: no connection values found in the archive layer.")
            return False
        else:
            # If a tuple is returned, unpack it.
            new_features, success = result
            if success:
                #Add the features to the memory layer
                LayerActions._add_feature_to_layer_with_commit_option(layer=target_layer, 
                                                             new_feature=new_features,
                                                             commit=commit)

                #delete the elements from the layer if requested!
                LayerActions._delete_element_from_layer(input_data=delete_input_data, feature_id=feature_id, layer=input_layer)
                
                
                
                return True

    @staticmethod
    def _select_target_features_based_on_temporary_archived_elements(target_layer, archive_layer, connection_field):
        """
        Select features in the target_layer based on connection values (e.g., source_id)
        found in the archive_layer.
        
        :param target_layer: QgsVectorLayer - the target layer in which to select features.
        :param archive_layer: QgsVectorLayer - the archive layer that holds moved features.
        :param connection_field: str - the field name used to connect features between layers.
        """
        # Collect unique connection values from the archived layer.
        connection_values = set()
        features = archive_layer.getfeatures()
        # Check if the features list is empty
        if len(features) == 0:
            print("no features found")
            return False
        else:
            for feat in archive_layer.getFeatures():
                val = feat[connection_field]
                if val is not None:
                    connection_values.add(val)
            
            if not connection_values:
                print("No connection values found in the archive layer.")
                return None

        # Determine if the connection field is text or numeric based on a sample value.
        sample_value = next(iter(connection_values))
        if isinstance(sample_value, str):
            # Wrap text values in single quotes.
            values_list = ", ".join(f"'{val}'" for val in connection_values)
        else:
            values_list = ", ".join(map(str, connection_values))
        
        # Build the expression for selection. Note the use of double quotes around the field name.
        expression = f"\"{connection_field}\" IN ({values_list})"
        print(f"Selecting features in target layer using expression: {expression}")

        # Apply the selection on the target layer.
        target_layer.selectByExpression(expression)
        return values_list, True

class LayerActions:
    @staticmethod
    def _delete_element_from_layer(input_data, feature_id, layer: QgsVectorLayer) -> None:
        # If deletion is requested, remove features from the input layer.
        if input_data:
            res = layer.dataProvider().deleteFeatures([feature_id])
            if res:
                print(f"Successfully deleted features from input layer '{layer.name()}'.")
            else:
                print(f"Failed to delete features from input layer '{layer.name()}'.")
            layer.triggerRepaint()

    @staticmethod
    def _get_layer_fetaures_by_id(layer: QgsVectorLayer, feature_id: int) -> QgsFeature:

        request = QgsFeatureRequest().setFilterFids([feature_id])
        feat = next(layer.getFeatures(request), None)

        if feat:
            # Do something with the retrieved feature.
            #print(f"Feature found: {feat}")
            pass
        else:
            print(f"Feature with id {feature_id} not found.")

        return feat
    @staticmethod
    def _get_all_features_from_layer(layer: QgsVectorLayer) -> List[QgsFeature]:
        """
        Retrieves all features from the provided layer.
        """
        features = [f for f in layer.getFeatures()]
        if not features:
            print(f"No features found in layer '{layer.name()}'.")
            return []
        return features        
    @staticmethod
    def _map_attributes_by_name(input_feature: QgsFeature, target_fields: List) -> List:
        """
        Map attributes from an input feature to a list of attribute values that match
        the target layer's fields by name. If the input feature doesn't have a field,
        assign None.
        
        :param input_feature: QgsFeature from the input layer.
        :param target_fields: QgsFields object from the target layer.
        :return: List of attribute values in the order of target_fields.
        """
        # Get the names of fields present in the input feature.
        input_field_names = input_feature.fields().names()
        new_attrs = []
        for field in target_fields:
            field_name = field.name()
            if field_name in input_field_names:
                new_attrs.append(input_feature[field_name])
            else:
                # Field not present in input; assign a default value.
                new_attrs.append(None)
        return new_attrs

    @staticmethod
    def _map_attributes_by_feature(feature: QgsFeature) -> List: 
        """
        Creates a new QGIS feature by copying the geometry and attributes from the provided feature.
        
        This helper function replicates the behavior of the `_map_attributes_by_name` function,
        but should only be used when the source and target fields match exactly. It copies the
        geometry and attributes from the source feature into a new feature, then sets the new
        feature's ID to -1 so that QGIS will assign a unique ID when it is added to a layer.
        
        Parameters:
            feature (QgsFeature): The source feature whose geometry and attributes are to be copied.
            
        Returns:
            list: A list containing a single QgsFeature. This feature has the same geometry and attributes
                as the input feature, but with a new, system-assigned unique ID.
        """
        features = []

        feat = QgsFeature()                     
        feat.setGeometry(feature.geometry())    
        feat.setAttributes(feature.attributes())  
        feat.setId(-1)                          
        features.append(feat)

        return features


    @staticmethod
    def _add_feature_to_layer_with_commit_option(layer: QgsVectorLayer, new_feature: QgsFeature, commit=False) -> bool:
        """
        Adds the provided features to the target layer, updates its extents, and triggers a repaint.
        
        This helper function abstracts the logic of adding features to a layer. It attempts to add the new features,
        prints a success or failure message based on the outcome, updates the layer's extents, and triggers a repaint.
        
        Parameters:
            target_layer (QgsVectorLayer): The layer to which the features will be added.
            new_features (List[QgsFeature]): A list of features to be added.
        
        Returns:
            bool: True if the features were successfully added; otherwise, False.
        """
        if commit:
            if not layer.isEditable():
                    layer.startEditing()
                    print(f"Started editing layer '{layer.name()}'.")

        loaded_layer_settings = PropertiesProcessStage.loaded_layers
        #print(f"Loaded Layers Settings: {loaded_layer_settings}")
        layer_name = layer.name()
        #print(f"Layer_name {layer_name} from {layer} ")
        layer_info = loaded_layer_settings.get(layer_name, {})
        new_feature_fid = layer_info.get(MainVariables.MAX_ID)
        #print(f"Max Fid {new_feature_fid}")
        if not new_feature:  # Check if the list is empty
            print(f"No features provided to add to layer '{layer.name()}'.")
            return False

        # Take the first feature from the list (assuming single feature for now)
        feature_to_add = new_feature[0]

        # Replace or set the fid field (assuming the target layer has an 'fid' field)
        fid_index = layer.fields().indexOf('fid')  # Get the index of the 'fid' field
        if fid_index != -1:  # Check if 'fid' field exists
            print(f"Setting atribute on fid_index {fid_index} of {new_feature_fid}")
            feature_to_add.setAttribute(fid_index, new_feature_fid)
        
        # addFeatures expects a list, so wrap the single feature in a list
        res, _ = layer.dataProvider().addFeatures([feature_to_add])
        print(f"Added features to layer '{layer.name()}': {res}")
        
        if commit:
            layer.commitChanges()
        
        #optimized target feature creation 
        #new_generated_max = fidOperations.get_next_fid(target_layer=layer)
        
        new_generated_max = new_feature_fid + 1
        
        LayerSetups.register_layer_configuration(layer=layer, max_fid=new_generated_max)
        gc.collect()
        return res

class fidOperations:
    @staticmethod
    def get_current_max_fid(target_layer: QgsVectorLayer) -> Optional[int]:
        """
        Retrieves the current maximum 'fid' value from the target_layer.
        
        Parameters:
            target_layer (QgsVectorLayer): The layer in which to look for the maximum fid.
        
        Returns:
            int | None: The maximum fid value found, or None if the 'fid' field does not exist
                        or no valid fid values are found.
        """
        # Get the index of the 'fid' field.
        if target_layer is None:
            TracebackLogger.log_traceback(custom_message="Target layer is None.")
            return None
        
        fid_index = target_layer.fields().indexOf('fid')
        if fid_index == -1:
            TracebackLogger.log_traceback(custom_message="No 'fid' field found.")
            return None
        
        fid_values = []
        # Iterate over features to collect valid fid values.
        for feature in target_layer.getFeatures():
            fid = feature.attribute('fid')
            if fid is not None and isinstance(fid, (int, float)):
                fid_values.append(fid)
        
        if fid_values:
            return int(max(fid_values))
        else:
            print("No valid 'fid' values found.")
            return None

    @staticmethod
    def get_next_fid(target_layer: QgsVectorLayer, starting_fid: int = 1) -> int:
        """
        Computes the next available unique feature ID for the target_layer using the
        current maximum fid. If no valid 'fid' values are found, returns starting_fid.
        
        Parameters:
            target_layer (QgsVectorLayer): The layer where features are being added.
            starting_fid (int): The fid value to use if the layer is empty or has no valid 'fid' field.
                                Default is 1.
        
        Returns:
            int: The next available unique feature ID.
        """
        # Retrieve the current maximum fid using the helper function.
        current_max_fid = fidOperations.get_current_max_fid(target_layer)
        
        if current_max_fid is None:
            # No valid fid values found; return the starting fid.
            return starting_fid
        else:
            # Return the next fid (max fid + 1).
            return current_max_fid + 1


class FeaturePreparations:
    @staticmethod
    def _feature_preparations_between_layers_using_name_for_field_detections(input_layer, target_layer, feature_id) -> tuple[list[Any], bool]:
        #print(f"target_layer: {target_layer}")
        #get layer features by fature_id 
        feat = LayerActions._get_layer_fetaures_by_id(layer=input_layer, feature_id=feature_id)
             
        # Create new features for the target layer, ensuring new IDs are assigned.
        new_features = []
        target_fields = target_layer.fields()  # Get the target layer's fields once.
        new_feat = QgsFeature()  # Create a new, empty feature.
        new_feat.setGeometry(feat.geometry())  # Copy geometry.
        # Map attributes based on matching field names.
        new_attr_values = LayerActions._map_attributes_by_name(feat, target_fields)
        #print(f"New attr values: {new_attr_values}")
        new_feat.setAttributes(new_attr_values)
        new_features.append(new_feat)
        gc.collect()
        return new_features, True
    
