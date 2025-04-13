from typing import Optional
from qgis.core import QgsVectorLayer


from ..utils.Logging.Logger import TracebackLogger


class fidOperations:
    @staticmethod
    def _get_current_max_fid(target_layer: QgsVectorLayer) -> Optional[int]:
        """
        Retrieves the current maximum 'fid' value from the attribute field,
        ignoring any subset filters or layer-level filters.
        """
        if target_layer is None:
            TracebackLogger.log_traceback(custom_message="Target layer is None.")
            return None

        # Get base data source WITHOUT the subset string
        base_source = target_layer.dataProvider().dataSourceUri().split("|")[0]
        provider_type = target_layer.providerType()

        # Create clean layer without filters
        raw_layer = QgsVectorLayer(base_source, "raw_layer", provider_type)

        if not raw_layer.isValid():
            TracebackLogger.log_traceback(custom_message="Could not load raw version of target layer.")
            return None

        fid_index = raw_layer.fields().indexOf('fid')
        if fid_index == -1:
            TracebackLogger.log_traceback(custom_message="No 'fid' field found in raw layer.")
            return None

        max_fid = None
        for feature in raw_layer.getFeatures():
            fid = feature.attribute('fid')
            if fid is not None and isinstance(fid, (int, float)):
                max_fid = max(fid, max_fid) if max_fid is not None else fid

        return int(max_fid) if max_fid is not None else None

    @staticmethod
    def _get_next_fid(target_layer: QgsVectorLayer, starting_fid: int = 1) -> int:
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
        current_max_fid = fidOperations._get_current_max_fid(target_layer)

        if current_max_fid is None:
            # No valid fid values found; return the starting fid.
            return starting_fid
        else:
            # Return the next fid (max fid + 1).
            return current_max_fid + 1