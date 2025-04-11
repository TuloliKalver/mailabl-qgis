

from typing import List, Tuple, Optional
from qgis.core import QgsVectorLayer, QgsVectorLayerExporter, QgsProject

from qgis.utils import iface 
from qgis.core import QgsVectorLayer


from ..KeelelisedMuutujad.FolderHelper import MailablGroupFolders
from ..utils.LayerGroupHelpers import LayerGroupHelper
from ..utils.Logging.Logger import TracebackLogger
from ..utils.ArchiveLayerHandler import ArchiveLayerHandler


class GeopakagegeHandler:

    @staticmethod
    def testing():
        cadastral_numbers = ["63901:001:4910", "63901:001:0028"]
        field = 'tunnus'

        print(f"Testing for cadastral numbers: {cadastral_numbers}")
        source_layer = QgsProject.instance().mapLayersByName('Kalver_test')[0]

        all_features = list(source_layer.getFeatures())
        matching_features = []

        for cadastral_number in cadastral_numbers:
            for feature in all_features:
                if feature[field].startswith(cadastral_number) and feature.geometry() and not feature.geometry().isEmpty():
                    print(f"✅ Match: {feature[field]}")
                    matching_features.append(feature)

        if not matching_features:
            print("❌ No valid features found.")
            return

        # Zoom + select
        from ..utils.LayerHelpers import LayerProcessHandlers
        LayerProcessHandlers.zoom_to_features_extent(matching_features)
        source_layer.selectByIds([f.id() for f in matching_features])

        # Resolve archive layer
        from ..KeelelisedMuutujad.FolderHelper import MailablLayerNames
        archive_layer_name = MailablLayerNames.ARCHIVE_LAYER_NAME

        archive_layer = ArchiveLayerHandler.resolve_or_create_archive_layer(source_layer, archive_layer_name)

        if not archive_layer:
            print("❌ Archive layer could not be resolved.")
            return

        print(f"✅ Archive layer ready: {archive_layer.name()}")











    @staticmethod
    def store_memory_layer_to_geopackage(memory_layer: QgsVectorLayer=None, target_layer_for_file: QgsVectorLayer=None, new_layer_name: str=None) -> Tuple[bool, Optional[List]]:
  
        layer_uri, gpkg_path = get_layer_uri(target_layer_for_file, new_layer_name)
        
        if gpkg_layer_exists(gpkg_path, new_layer_name):
            print(f"Layer '{new_layer_name}' already exists in GPKG. Loading into project.")

            #existing_layer = QgsVectorLayer(layer_uri, new_layer_name, "ogr")
            #if not existing_layer.isValid():
            #    TracebackLogger.log_traceback(custom_message="Failed to load existing layer from GPKG.")
            #    return False, []

            #layer = _load_and_prepare_existing_layer(existing_layer, new_layer_name)
            #if layer:
            #    return True, []  # No data operation — just loaded
            #else:
            #    TracebackLogger.log_traceback(custom_message="Failed to add existing layer to group.")
            #    return False, []

        else:
            print(f"Layer '{new_layer_name}' does not exist. Creating from memory.")
            err = QgsVectorLayerExporter.exportLayer(
                memory_layer,
                gpkg_path,
                "ogr",
                memory_layer.crs(),
                False,
                {"layerName": new_layer_name}
            )

            #if err[0] == QgsVectorLayerExporter.NoError:
            #    new_layer = QgsVectorLayer(layer_uri, new_layer_name, "ogr")
            #    if new_layer.isValid():
            #        layer = LayerGroupHelper.add_layer_to_projct_in_given_group(
            #            layer=new_layer,
            #            group_name=MailablGroupFolders.ARCHIVED_PROPERTIES
            #        )
            #        style_path = Filepaths.get_style(FilesByNames().Archived_layer)
            #        layer.loadNamedStyle(style_path)
            #        SettingsDataSaveAndLoad().save_archived_layers(layer.name())

            #        return True, []
            #    else:
            #        TracebackLogger.log_traceback(custom_message="New layer is not valid after saving.")
            #        return False, []
            #else:
            #    TracebackLogger.log_traceback(custom_message=f"Failed to save memory layer to GPKG: {err}")
            #    return False, []
