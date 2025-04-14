from typing import Optional
from qgis.core import QgsVectorLayer


from ..utils.Logging.Logger import TracebackLogger


class fidOperations:
    @staticmethod
    def _get_current_max_fid(target_layer: QgsVectorLayer) -> Optional[int]:
        """
        Retrieves the current maximum value from the 'fid' attribute field.
        Removes any subset string to access full data in the correct layer.
        """
        if not target_layer or not target_layer.isValid():
            TracebackLogger.log_traceback(custom_message="Invalid or None target layer.")
            return None

        # Clone the same layer to preserve the correct data source and layer name
        raw_layer = QgsVectorLayer(target_layer.source(), "raw_layer", target_layer.providerType())
        if not raw_layer.isValid():
            TracebackLogger.log_traceback(custom_message="Could not clone layer.")
            return None

        # Remove any subset filter
        raw_layer.setSubsetString("")  # this exposes all features

        fid_index = raw_layer.fields().indexOf('fid')
        if fid_index == -1:
            TracebackLogger.log_traceback(custom_message="No 'fid' field found in raw layer.")
            return None

        max_fid = None
        for feature in raw_layer.getFeatures():
            fid_val = feature.attribute('fid')
            if fid_val is not None and isinstance(fid_val, (int, float)):
                max_fid = fid_val if max_fid is None else max(max_fid, fid_val)

        print(f"🧬 Max FID in {target_layer.name()} (unfiltered): {max_fid}")
        return int(max_fid) if max_fid is not None else 0

    @staticmethod
    def _get_layers_next_ids(target_layer: QgsVectorLayer, starting_fid: int = 1) -> int:
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