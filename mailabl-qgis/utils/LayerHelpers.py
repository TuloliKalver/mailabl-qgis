#LayerHelper.py

import gc
from typing import Any, List
from qgis.utils import iface 

from qgis.core import QgsVectorLayer, QgsFields, QgsWkbTypes, QgsCoordinateReferenceSystem, QgsFeature, QgsProject,  QgsRectangle
from typing import Tuple
from PyQt5.QtCore import QCoreApplication


from PyQt5.QtWidgets import QMessageBox

from ..utils.fidOperationsHelper import fidOperations
from .DataMapperHelper import DataMapperHelper
from ..utils.LayerSetups import LayerSetups
from ..utils.LayerFeaturehepers import LayerFeatureHelpers
from ..Common.app_state import PropertiesProcessStage, Expressions, MainVariables
from ..utils.MessagesHelpers import MessageLoaders
from ..Functions.add_items import add_properties
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..queries.python.property_data import MyLablChecker, UpdateData
from ..widgets.decisionUIs.DecisionMaker import DecisionDialogHelper
from ..app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts



class FeatuerHelpers:
    @staticmethod
    def fast_collect_unique_values_and_ids(layer: QgsVectorLayer, field_index: int, progress=None):
        unique_values = set()
        feature_ids_append = feature_ids = []

        feature_ids_append = feature_ids.append  # Local var for faster access
        add_value = unique_values.add            # Local var for faster access

        features = layer.getFeatures()
        total = layer.featureCount()

        for idx, feature in enumerate(features):
            try:
                add_value(feature[field_index])
                feature_ids_append(feature.id())
            except Exception as e:
                print(f"Skipping feature {feature.id()}: {e}")

            if progress:
                progress.update(value=idx)
                if idx % 10 == 0:  # Don’t call this every iteration — only every few
                    QCoreApplication.processEvents()

        if progress:
            progress.update(value=total)

        return unique_values, feature_ids

class LayerSchemas:
    @staticmethod
    def _extract_layer_schema(layer: QgsVectorLayer) -> Tuple[QgsFields, QgsWkbTypes.Type, QgsCoordinateReferenceSystem]:
        """
        Extracts the schema (fields, geometry type, CRS) from a given vector layer.

        Args:
            layer (QgsVectorLayer): The source layer.

        Returns:
            Tuple[QgsFields, QgsWkbTypes.Type, QgsCoordinateReferenceSystem]: 
                A tuple containing (fields, geometry_type, crs).
        """
        if not layer.isValid():
            raise ValueError("Layer is not valid.")

        fields = layer.fields()
        geometry_type = layer.wkbType()
        crs = layer.crs()

        return fields, geometry_type, crs

class DuplicateLayerResolver:
    @staticmethod
    def _resolve_duplicate_layers(layer_name: str):
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
    def _resolve_duplicate_layers_auto(layer_name: str):
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

################################################################################################################
class LayerProcessHandlers:
    @classmethod
    def _load_and_handle_layers(cls, layers_info):
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
            #print(f"Loading layer: {layer_name}. Activate: {activate}, Cleanup: {cleanup}")
            layer = LayerSetups.load_layer_with_activation_option(layer_name, activate=activate)
            max_fid = fidOperations._get_layers_next_ids(target_layer=layer)
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
    def _set_or_reset_fid(layer_name, max_fid=None):
        # Find the layer by name.
        layer = QgsProject.instance().mapLayersByName(layer_name)
        if layer:
            layer = layer[0]
        LayerSetups.register_layer_configuration(layer=layer, max_fid=max_fid)
        
    @staticmethod
    def _get_comparison_fields_list_and_element_ids(field_name: List[str], layer: QgsVectorLayer):
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

    @staticmethod
    def _zoom_to_features_in_layer(features: List[QgsFeature], layer: QgsVectorLayer) -> None:
        """
        Selects the given features in a layer and zooms the map canvas to them.

        Args:
            features (List[QgsFeature]): A list of QgsFeature objects to zoom to.
            layer (QgsVectorLayer): The layer that contains the features.

        Returns:
            None
        """
        feature_ids = [feature.id() for feature in features]
        layer.selectByIds(feature_ids)
        iface.mapCanvas().zoomToSelected(layer)

    @staticmethod
    def _zoom_to_features_extent(features: List[QgsFeature]) -> None:
        """
        Zooms to the combined extent of the given features without selecting them.

        Args:
            features (List[QgsFeature]): Features to zoom to.

        Returns:
            None
        """
        if not features:
            print("⚠️ No features provided.")
            return

        extent = QgsRectangle()
        extent.setMinimal()

        valid_feature_found = False

        #print(f"🔍 Received {len(features)} features.")
        
        for i, feature in enumerate(features):
            geom = feature.geometry()
            if geom and not geom.isEmpty():
                bbox = geom.boundingBox()
                #print(f"  Feature {i} → BBox: {bbox.toString()}")
                extent.combineExtentWith(bbox)
                valid_feature_found = True
            else:
                print(f"⚠️ Feature {i} has no geometry!")

        if not valid_feature_found:
            print("❌ No valid geometries found in features.")
            return

        #print(f"✅ Combined extent: {extent.toString()}")

        extent.scale(1.1)  # 10% buffer
        iface.mapCanvas().setExtent(extent)
        iface.mapCanvas().refresh()

    @staticmethod
    def _get_selected_elemntsID_from_layer(layer: QgsVectorLayer):
        selected_features = []
        for feature in layer.selectedFeatures():
            selected_features.append(feature.id())
        if not selected_features:
            print("No features were selected.")
            return []
        return selected_features

    def _get_selected_features_from_layer(layer: QgsVectorLayer):
        features = []
        for feature in layer.selectedFeatures():
            features.append(feature)
        if not features:
            print("No objects were selected.")
            return []
        return features

    @staticmethod
    def _get_all_features_from_layer(layer: QgsVectorLayer) -> List[QgsFeature]:
        """
        Returns a list of all feature objects from the given QgsVectorLayer.

        :param layer: The QgsVectorLayer to read from.
        :return: List of QgsFeature objects.
        """
 
        return [feature for feature in layer.getFeatures()]
    
    @staticmethod
    def _get_features_or_IDs_from_layer(layer: QgsVectorLayer, return_ids_only: bool = False) -> list[Any]:
        """
        Retrieve either all feature IDs or all QgsFeature objects from a layer.

        :param layer: The QgsVectorLayer to read from.
        :param return_ids_only: If True, return feature IDs instead of QgsFeature objects.
        :return: List of feature IDs or QgsFeature objects.
        """
        if not layer or not layer.isValid():
            print("Invalid layer provided.")
            return []

        if return_ids_only:
            return [feature.id() for feature in layer.getFeatures()]
        else:
            return [feature for feature in layer.getFeatures()]

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
        return active_layer, target_layer

    @staticmethod
    def _reset_layer_filters():
        target_layer = next((info['layer'] for info in PropertiesProcessStage.loaded_layers.values() if not info.get('activated')), None)
        expression = Expressions.clear
        target_layer.setSubsetString(expression)
    @staticmethod
    def _reset_layer(layer_name: str, set_visible=True):
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        if set_visible:
            QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        else:
            QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(False)
        layer.removeSelection()
        expression = Expressions.clear
        layer.setSubsetString(expression)

    @staticmethod
    def _move_feature_data_and_geometry_between_layers(input_layer, 
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


        print(f"Moving feature with ID {feature_id} from {input_layer.name()} to {target_layer.name()}...")
        #print(f"step 1 get features by id")
        new_feature = LayerFeatureHelpers._get_layer_fetaures_by_id(layer=input_layer, feature_id=feature_id)

        # Add the new feature to the target layer
        #print(f"step 2 add feature to target layer")
        LayerFeatureHelpers._add_feature_to_layer_with_commit_option(layer=target_layer, 
                                                        new_feature=new_feature,
                                                        commit=commit)
        #print(f"step 3 update search fields in target layer")
        #update search fields in the target_layer
        LayerFeatureHelpers._update_search_fields_in_layer(layer=target_layer)
        #print(f"step 4 delete feature object from input layer")
        #delete the elements from the layer if requested!
        LayerFeatureHelpers._delete_element_from_layer(delete=delete_input_data, feature_id=feature_id, layer=input_layer)
        #print(f"step 5 update search fields in input layer: {input_layer.name()}")
        #update search fields in the input_layer
        LayerFeatureHelpers._update_search_fields_in_layer(layer=input_layer)
        #print(f"step 6 done!")
        gc.collect()
        if update_data is False:
            return True
        else:
            layer_data = LayerFeatureHelpers._get_feature_attributes_as_dict(feature=new_feature)
            #print (f"layer_data: {layer_data}")
            tunnus = layer_data.get(Katastriyksus.tunnus)
            #print (f"Tunnus: {tunnus}")            
            res, data = MyLablChecker._get_propertie_ids_by_cadastral_numbers_EQUALS(item=tunnus)
            if res is True:

                prepared_data, usage_data = DataMapperHelper._map_properties_main_details_from_input(layer_data=layer_data)
                #print(f"street and house from prepared data: {prepared_data['address'].get('street')} and {prepared_data['address'].get('houseNumber')}")                
                #print(f"usage_data: {usage_data}")

                property_id = add_properties.add_single_property_item(None, prepared_data)
                #print(f"usage_data: {usage_data}")
                add_properties.add_additional_property_data(None, property_id, usage_data)            
                gc.collect()
                return True
            else:

                print ("Duplicate found!")
                buttons={"cancel": "Edasi",
                        "keep": "Tühista"
                        }
                ret = DecisionDialogHelper.ask_user(
                    title=Headings.inFO_SIMPLE,
                    message=f"❌ Kataster '{tunnus}'  on juba Mailablis! \n\n Kas uuendan andmeid?",
                    options=buttons,
                    parent=None,
                    type= AnimatedGradientBorderFrame.WARNING
                        )
                #print(ret)
                if ret is None:
                    #print("Updating existing property...")
                    #print(f"property_id: {data}")
                    for item in data:
                        #print(f"item: {item}")
                        display_address = item.get("node", {}).get("displayAddress", "")

                        if display_address.startswith("ARHIIVEERITUD"):
                            print("🚫 Archived property — allow new one to be added")
                            pass
                        else:
                            print("✅ Active address — check for duplicates or updates")
                            Maylabl_id = item.get("node", {}).get("id", "")
                            details , usage_data = DataMapperHelper._map_properties_main_details_from_input(layer_data=layer_data)
                            variables = {
                            "input": {
                    
                                "id": Maylabl_id,
                                    **details
                                    }
                            }
                            UpdateData._update_property_address_details(variables=variables)
                            #print(f"usage_data: {usage_data}")
                            add_properties.add_additional_property_data(None, Maylabl_id, usage_data)
                    return True
                elif ret is False:
                    print("Operation cancelled.")
                    return False

