import gc
import os

from qgis.core import (
    QgsFields, QgsVectorFileWriter, QgsWkbTypes,
    QgsCoordinateReferenceSystem, QgsProject, QgsVectorLayer
)
from osgeo import ogr

from typing import Optional

from ..utils.LayerHelpers import LayerSchemas
from ..utils.Logging.Logger import TracebackLogger
from ..config.settings import Filepaths, FilesByNames
from ..KeelelisedMuutujad.FolderHelper import MailablGroupFolders


class GPKGHelpers:
    @staticmethod
    def get_layer_uri(target_layer_for_file: QgsVectorLayer, new_layer_name: str):
        uri = target_layer_for_file.dataProvider().dataSourceUri()
        gpkg_path = uri.split("|")[0]
        layer_uri = f"{gpkg_path}|layername={new_layer_name}"
        print("URI:", uri)
        print("GPKG Path:", gpkg_path)
        return layer_uri, gpkg_path
    @staticmethod
    def gpkg_layer_exists(gpkg_path: str, layer_name: str) -> bool:
        ds = ogr.Open(gpkg_path, 0)  # read-only
        if not ds:
            return False
        return layer_name in [ds.GetLayerByIndex(i).GetName() for i in range(ds.GetLayerCount())]
    @staticmethod
    def load_layer_from_gpkg(gpkg_path: str, layer_name: str, group_name: str = "") -> QgsVectorLayer:
        """
        Safely loads a layer from a GeoPackage into the QGIS project and places it in a group if specified.
        """
        uri = f"{gpkg_path}|layername={layer_name}"
        layer = QgsVectorLayer(uri, layer_name, "ogr")

        if not layer.isValid():
            print(f"❌ Failed to load layer '{layer_name}' from {gpkg_path}")
            return None

        QgsProject.instance().addMapLayer(layer, False)

        if group_name:
            root = QgsProject.instance().layerTreeRoot()
            group = root.findGroup(group_name) or root.addGroup(group_name)
            group.addLayer(layer)  # ✅ This is safe
            print(f"✅ Layer '{layer_name}' loaded into group '{group_name}'")
        else:
            QgsProject.instance().layerTreeRoot().insertLayer(0, layer)
            print(f"✅ Layer '{layer_name}' loaded at top level.")

        return layer
    @staticmethod
    def delete_layer_from_gpkg(gpkg_path: str, layer_name: str) -> bool:
        """
        Deletes a specific layer from a GeoPackage file using OGR,
        and removes it from the current QGIS project if loaded.

        Args:
            gpkg_path (str): Path to the GeoPackage.
            layer_name (str): Name of the layer to delete.

        Returns:
            bool: True if deletion from GPKG succeeded, False otherwise.
        """
        print(f"🧹 Attempting to delete layer '{layer_name}' from GeoPackage: {gpkg_path}")

        if not os.path.exists(gpkg_path):
            print("❌ GeoPackage file not found.")
            return False

        # 🧹 First: remove from project if loaded
        project_layers = QgsProject.instance().mapLayersByName(layer_name)
        if project_layers:
            for lyr in project_layers:
                QgsProject.instance().removeMapLayer(lyr.id())
            print(f"✅ Removed '{layer_name}' from project.")

        # 🧹 Then: remove from GeoPackage
        ds = ogr.Open(gpkg_path, update=1)
        if not ds:
            print("❌ Failed to open GeoPackage.")
            return False

        try:
            ds.DeleteLayer(layer_name)
            print(f"✅ Layer '{layer_name}' deleted from GeoPackage.")
            return True
        except Exception as e:
            print(f"❌ Error deleting layer '{layer_name}' from GeoPackage: {e}")
            return False

    @staticmethod
    def create_empty_gpkg_layer(
        gpkg_path: str,
        layer_name: str,
        geometry_type: QgsWkbTypes.Type,
        crs: QgsCoordinateReferenceSystem,
        fields: QgsFields,
        overwrite: bool = True,
        encoding: str = "UTF-8"
    ) -> bool:
        """
        Creates an empty vector layer in a GeoPackage.

        Args:
            gpkg_path (str): Path to the GeoPackage file.
            layer_name (str): Name of the new layer.
            geometry_type (QgsWkbTypes.Type): Geometry type (e.g., QgsWkbTypes.Polygon).
            crs (QgsCoordinateReferenceSystem): Coordinate reference system.
            fields (QgsFields): Field definitions for the new layer.
            overwrite (bool): Whether to overwrite an existing layer of the same name.
            encoding (str): File encoding (default: UTF-8).

        Returns:
            bool: True if successful, False otherwise.
        """
        print(f"🆕 Creating empty GPKG layer '{layer_name}' at: {gpkg_path}")

        options = QgsVectorFileWriter.SaveVectorOptions()
        options.driverName = "GPKG"
        options.layerName = layer_name
        options.fileEncoding = encoding
        options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer
        transform_context = QgsProject.instance().transformContext()

        result = QgsVectorFileWriter.create(
            gpkg_path,
            fields,
            geometry_type,
            crs,
            transform_context,
            options
        )

        if not result.hasError():
            print(f"✅ Empty layer '{layer_name}' created successfully.")
            return True
        else:
            print(f"❌ Failed to create layer '{layer_name}': {result.errorMessage()}")
            return False


class ArchiveLayerHandler:
    @staticmethod
    def resolve_or_create_archive_layer(source_layer: QgsVectorLayer, archive_layer_name: str) -> Optional[QgsVectorLayer]:
        """
        Ensures the archive layer exists (in project or GPKG). Loads or creates it as needed.

        Args:
            source_layer (QgsVectorLayer): The reference layer used to copy schema if creation is needed.
            archive_layer_name (str): The name of the archive layer.

        Returns:
            QgsVectorLayer or None if failed.
        """
        print(f"📦 Resolving archive layer: {archive_layer_name}")

        # 1. Check if it's already in project
        existing = QgsProject.instance().mapLayersByName(archive_layer_name)
        if existing:
            print(f"✅ Found archive layer in project.")
            return existing[0]

        # 2. Check in GPKG
        uri = source_layer.dataProvider().dataSourceUri()
        gpkg_path = uri.split("|")[0]

        if GPKGHelpers.gpkg_layer_exists(gpkg_path, archive_layer_name):
            print("✅ Layer exists in GPKG — loading it.")
            return GPKGHelpers.load_layer_from_gpkg(gpkg_path, archive_layer_name, group_name=MailablGroupFolders.ARCHIVED_PROPERTIES)

        # 3. Create new layer in GPKG
        print("⚠️ Archive layer not found — creating new one.")
        fields, geometry_type, crs = LayerSchemas._extract_layer_schema(source_layer)

        created = GPKGHelpers.create_empty_gpkg_layer(
            gpkg_path=gpkg_path,
            layer_name=archive_layer_name,
            geometry_type=geometry_type,
            crs=crs,
            fields=fields,
            overwrite=False
        )

        if not created:
            TracebackLogger.log_traceback("Failed to create new archive layer.")
            return None

        print("✅ New archive layer created. Adding to project.")
        new_layer = GPKGHelpers.load_layer_from_gpkg(gpkg_path, archive_layer_name, group_name=MailablGroupFolders.ARCHIVED_PROPERTIES)
        add_style = Filepaths.get_style(FilesByNames().Archived_layer)
        new_layer.loadNamedStyle(add_style)
        gc.collect()
        return new_layer
