

from typing import List, Tuple, Optional
from qgis.core import  QgsProject


from ..utils.ArchiveLayerHandler import ArchiveLayerHandler
from ..utils.LayerHelpers import LayerProcessHandlers


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
        LayerProcessHandlers._zoom_to_features_extent(matching_features)
        source_layer.selectByIds([f.id() for f in matching_features])

        # Resolve archive layer
        from ..KeelelisedMuutujad.FolderHelper import MailablLayerNames
        archive_layer_name = MailablLayerNames.ARCHIVE_LAYER_NAME

        archive_layer = ArchiveLayerHandler.resolve_or_create_archive_layer(source_layer, archive_layer_name)

        if not archive_layer:
            print("❌ Archive layer could not be resolved.")
            return

        print(f"✅ Archive layer ready: {archive_layer.name()}")



            
  