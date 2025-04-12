from qgis.utils import iface # type: ignore
from qgis.core import QgsVectorLayer # type: ignore
from typing import List, Optional
from ..KeelelisedMuutujad.MaaAmetFieldFormater import format_field
from ..Common.app_state import PropertiesProcessStage
from ..utils.LayerHelpers import LayerProcessHandlers
            

class MapToolsHelper:
    @staticmethod
    def get_field_indices_multiple_fields(layer: QgsVectorLayer, field_names: List[str]):
        """
        Retrieve indices for the specified fields in the provided QGIS layer.

        This function iterates over the list of field names, retrieving the corresponding
        index from the layer's fields. If any of the fields cannot be found (i.e., the index
        is -1), it prints an error message and returns None.

        Args:
            layer (QgsVectorLayer): The active QGIS layer from which field indices are extracted.
            field_names (list of str): A list of field names to retrieve indices for.

        Returns:
            dict or None: A dictionary mapping each field name to its index if all fields are found;
            otherwise, returns None.
        """
        field_indices = {field: layer.fields().indexFromName(field) for field in field_names}
        missing = [field for field, idx in field_indices.items() if idx == -1]
        if missing:
            print(f"Fields not found: {', '.join(missing)}")
            return None

        return field_indices
    
    @staticmethod
    def get_field_indices_for_single_field(layer: QgsVectorLayer, field_name: str):
        #print(f"Field name: {field_name}")
        field_index = layer.fields().lookupField(field_name)
        if field_index == -1:
            print(f"Field '{field_name}' not found in the layer.")
            return []
        return field_index

    @staticmethod
    def build_feature_row(feature, field_indices):
        """
        Construct a formatted data row from a feature using the provided field indices.

        For every field specified in the `field_indices` dictionary, this function retrieves
        the corresponding attribute value from the feature and applies a formatter function
        (assumed to be defined elsewhere as `format_field`).

        Args:
            feature (QgsFeature): The feature containing attribute values.
            field_indices (dict): A dictionary mapping field names to their corresponding indices.

        Returns:
            list: A list of formatted attribute values for the feature.
        """
        return [
            format_field(field_name, feature[field_idx])
            for field_name, field_idx in field_indices.items()
        ]

    @staticmethod
    def apply_subset_expression(layer: QgsVectorLayer, expression: str, triger_repaint:bool=False):
        """
        Apply a subset expression to the given QGIS layer and trigger a repaint.

        This method sets a filter expression on the layer to limit the features that are displayed,
        and then forces the layer to repaint so that changes are visible.

        Args:
            layer (QgsVectorLayer): The QGIS layer on which to apply the subset expression.
            expression (str): The SQL-like expression used to filter the layer's features.
        """
        layer.setSubsetString(expression if expression else "")
        if triger_repaint:
            layer.triggerRepaint()
            
    @staticmethod
    def select_features_by_ids(feature_ids: List[int],
                            layer: Optional[QgsVectorLayer] = None, 
                            refresh: bool = True,
                            zoom_to: bool = False
                            ) -> None:
        """
        Select features on the specified layer by their IDs. If no layer is provided,
        the active layer (AppState.active_layer) is used.

        The function also optionally removes any existing selection, refreshes the map
        canvas, and/or zooms to the selected features.

        :param feature_ids: List[int] - A list of feature IDs to be selected.
        :param layer: Optional[QgsVectorLayer] - The layer on which to apply the selection.
                    If None, the active layer is used.
        :param refresh: bool - If True, refreshes the map canvas after selection (default is True).
        :param zoom_to: bool - If True, zooms to the selected features (default is False).
        :return: None
        """
        # Use the provided layer; if not, default to the active layer.
        if layer is None:
            layer = PropertiesProcessStage.active_layer
            layer.removeSelection()
            layer.selectByIds(feature_ids)

            # Remove any previous selection and then select the new features.
        else:
            layer.removeSelection()
            layer.selectByIds(feature_ids)
            
        if zoom_to:
            #iface.mapCanvas().zoomToSelected(layer)
            
            #features = LayerProcessHandlers._get_all_features_from_layer(layer)
            features = LayerProcessHandlers._get_selected_features_from_layer(layer)
            LayerProcessHandlers._zoom_to_features_extent(features=features)

        if refresh:
            iface.mapCanvas().refresh()

    @staticmethod
    def validate_active_layer(layer):
        """
        Check if the active QGIS layer is valid.

        Validates that the provided layer exists and is in a valid state for processing.
        If the layer is invalid or missing, an error message is printed.

        Args:
            layer (QgsVectorLayer): The layer to be validated.

        Returns:
            bool: True if the layer is valid; otherwise, False.
        """
        if not layer or not layer.isValid():
            print("Invalid or no active layer.")
            return False
        return True

