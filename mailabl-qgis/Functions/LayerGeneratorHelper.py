import datetime
from qgis.core import QgsVectorFileWriter # type: ignore
from ..utils.fidOperationsHelper import fidOperations
from ..utils.MessagesHelpers import MessageLoaders
from ..utils.messagesHelper import ModernMessageDialog
from ..utils.Logging.Logger import TracebackLogger
from ..utils.LayerGroupHelpers import LayerGroupHelper
from qgis.core import QgsVectorFileWriter, QgsVectorLayer, QgsProject # type: ignore


class ArchiveOptionBuilder:
    @staticmethod
    def build_options(gpkg_path, existing_layer, new_layer_name, options, memory_layer):
        print("Starting ArchiveOptionBuilder.build_options...")
        
        if existing_layer.isValid():
            print("Existing layer is valid.")
            clicked, appendButton, replaceButton, cancelButton = MessageLoaders.ask_append_or_replace(new_layer_name)
            
            if clicked == cancelButton:
                print("Operation cancelled by user.")
                success = False
                returned_ids = []
                return success, returned_ids

            if clicked == replaceButton:
                print("User selected REPLACE option.")
                transform_context = QgsProject.instance().transformContext()
                options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer

                # Choose the correct writer based on QGIS version.
                if hasattr(QgsVectorFileWriter, "writeAsVectorFormatV3"):
                    print("Using writeAsVectorFormatV3 for layer replacement.")
                    result = QgsVectorFileWriter.writeAsVectorFormatV3(
                        memory_layer, 
                        gpkg_path, 
                        transform_context, 
                        options
                    )
                else:
                    print("Using writeAsVectorFormatV2 for layer replacement.")
                    result = QgsVectorFileWriter.writeAsVectorFormatV2(
                        memory_layer,
                        gpkg_path,
                        transform_context,
                        options
                    )
                
                if result[0] != QgsVectorFileWriter.NoError:
                    print("Error writing layer:", result[1])
                    success = False
                    returned_ids = []
                    return success, returned_ids
                
                print("Layer not loaded; attempting to load the new layer from the GeoPackage.")
                created_layer = QgsVectorLayer(f"{gpkg_path}|layername={new_layer_name}", new_layer_name, "ogr")
                if not created_layer.isValid():
                    TracebackLogger.log_traceback("New layer failed to load after replacement.")
                    return False, []

                new_layer = LayerGroupHelper.add_layer_to_goup_new(layer_name=new_layer_name)
                if new_layer:
                    print("Appending archive items to the existing layer...")
                    success, returned_ids = ArchiveOptionBuilder.append_archive_items_to_layer(
                        memory_layer=memory_layer, existing_layer=new_layer
                    )
                    print(f"Append result: success={success}, returned_ids={returned_ids}")
                    return success, returned_ids
                else:
                    print("New layer failed to load. Operation aborted.")
                    return False, []
            
            elif clicked == appendButton:
                print("User selected APPEND option.")
                success, returned_ids = ArchiveOptionBuilder.append_archive_items_to_layer(
                    memory_layer=memory_layer, existing_layer=existing_layer
                )
                print(f"Append result: success={success}, returned_ids={returned_ids}")
                return success, returned_ids
        else:
            print("Existing layer is not valid. Operation cannot proceed.")
            return False, []
    @staticmethod
    def append_archive_items_to_layer(memory_layer: QgsVectorLayer, target_layer: QgsVectorLayer) -> tuple[bool, list[int]]:
        """
        Appends features from a memory layer to a target layer, updating attributes in the process.

        Steps performed:
        1. Retrieves the current timestamp.
        2. Starts an editing session on the target layer.
        3. Retrieves all features from the memory layer.
        4. Determines the next feature ID (fid) to assign.
        5. Updates each feature with the current timestamp ('backup_date') and a new 'fid'.
        6. Appends the updated features to the target layer using its data provider.
        7. Commits the changes on the target layer.
        
        :param memory_layer: The source QgsVectorLayer containing features to be appended.
        :param target_layer: The target QgsVectorLayer to which the features will be appended.
        :return: A tuple (success: bool, returned_ids: list[int]) indicating whether the operation succeeded,
                and the list of new feature IDs if successful.
        """
        import datetime  # Ensure datetime is imported for timestamping

        # Step 1: Get the current timestamp.
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

        # Step 2: Start an editing session on the target layer.
        target_layer.startEditing()

        new_features = []
        # Step 3: Retrieve all features from the memory layer.
        features = list(memory_layer.getFeatures())

        # Step 4: Get the current maximum feature ID and determine the next ID.
        current_max_fid = fidOperations._get_next_fid(target_layer=target_layer)
        max_fid = current_max_fid + 1

        # Step 5: Update each feature with a backup timestamp and new feature ID.
        for feature in features:
            feature["backup_date"] = timestamp  # Update the backup date attribute.
            feature["fid"] = max_fid              # Assign a new feature ID.
            new_features.append(feature)
            max_fid += 1

        # Step 6: Append the new features to the target layer using its data provider.
        provider = target_layer.dataProvider()
        success, returned_features = provider.addFeatures(new_features)
        if success:
            print(f"Features appended successfully. New feature IDs: {returned_features}")
        else:
            print("Failed to append features.")

        # Step 7: Commit the changes to the target layer.
        if target_layer.commitChanges():
            return True, returned_features
        else:
            return False, []

