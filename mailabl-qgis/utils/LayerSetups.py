from qgis.utils import iface 
from typing import Optional, Any
from qgis.core import QgsProject, QgsVectorLayer 
from ..Common.app_state import MainVariables, PropertiesProcessStage
from ..utils.Logging.Logger import TracebackLogger
from ..utils.MessagesHelpers import MessageLoaders, TextMessages, TitleMessages


import gc


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