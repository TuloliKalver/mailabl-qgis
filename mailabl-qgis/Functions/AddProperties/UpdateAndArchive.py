from qgis.core import QgsProject
from qgis.core import  QgsProject, QgsVectorLayerExporter, QgsVectorFileWriter


from ...Functions.AddProperties.CompareChangesForExistingData import ChangeComparer
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...KeelelisedMuutujad.FolderHelper import MailablGroupFolders, MailablLayerNames
from ...Functions.layer_generator import LayerCopier

class UpdateAndArchive:
    @staticmethod
    def update_active_layer_data_old(self, properties_to_update, active_layer_name, input_layer_name):
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if active_layer is None or input_layer is None:
            print("Error: One or both layers not found.")
            return

        mfn = Katastriyksus.tunnus

        # Dictionary to map tunnus to features in active layer for quick lookup
        active_layer_features = {f[mfn]: f for f in active_layer.getFeatures()}

        changes = []

        # Collect changes that will be made
        for input_feature in input_layer.getFeatures():
            tunnus_value = input_feature[mfn]
            if tunnus_value in active_layer_features:
                active_feature = active_layer_features[tunnus_value]

                attr_changes = {}
                geom_changed = False

                for field_name in input_feature.fields().names():
                    if field_name in active_feature.fields().names() and field_name != mfn:
                        if input_feature[field_name] != active_feature[field_name]:
                            attr_changes[field_name] = (active_feature[field_name], input_feature[field_name])

                if input_feature.geometry() is not None and not input_feature.geometry().equals(active_feature.geometry()):
                    geom_changed = True

                if attr_changes or geom_changed:
                    changes.append((tunnus_value, attr_changes, geom_changed))

        if not changes:
            print("No changes to update.")
            return

        # Show changes summary and ask for user confirmation
        if not ChangeComparer.show_changes_summary(changes, self):
            print("Update cancelled by user.")
            return

        # Start an edit session on the active layer
        active_layer.startEditing()

        # Apply changes
        for tunnus_value, attr_changes, geom_changed in changes:
            active_feature = active_layer_features[tunnus_value]

            for field_name, (old_value, new_value) in attr_changes.items():
                active_feature.setAttribute(field_name, new_value)

            if geom_changed:
                input_feature = input_layer.getFeature(active_feature.id())
                active_feature.setGeometry(input_feature.geometry())

            active_layer.updateFeature(active_feature)

        # Commit changes
        if active_layer.commitChanges():
            print("Successfully updated the active layer with data from the input layer.")
        else:
            print("Failed to update the active layer.")


    @staticmethod
    def update_active_layer_data(self, properties_to_update, active_layer_name, input_layer_name):
        archive_layer_name = MailablLayerNames.PROPERTIES_ARCHIVE
        archchive_group_name = MailablGroupFolders.ARCHIVE

        # Retrieve layers by name
        input_layers = QgsProject.instance().mapLayersByName(input_layer_name)
        active_layers = QgsProject.instance().mapLayersByName(active_layer_name)
        archive_layers = QgsProject.instance().mapLayersByName(archive_layer_name)

        # Check if the layers exist
        if not input_layers:
            print(f"Error: Input layer '{input_layer_name}' not found.")
            return
        if not active_layers:
            print(f"Error: Active layer '{active_layer_name}' not found.")
            return

        input_layer = input_layers[0]
        active_layer = active_layers[0]

        if not archive_layers:
            memory_layer_name = LayerCopier.copy_virtual_layer_for_properties(archive_layer_name, group_name=archchive_group_name)
            
            '''
            archive_layer = QgsProject.instance().mapLayersByName(memory_layer_name)[0]

            # Get the source of the active layer (assumed to be a GeoPackage)
            source = active_layer.source()

            # Define the output file path and layer name in the GeoPackage
            output_uri = f"{source}|layername={archive_layer_name}"

            # Export the virtual layer to the GeoPackage
            error = QgsVectorLayerExporter.exportLayer(
                archive_layer, output_uri, "GPKG", archive_layer.crs()
            )

            if error[0] != QgsVectorLayerExporter.NoError:
                print(f"Error: Could not save layer to GeoPackage: {error[1]}")
            else:
                print(f"Successfully saved layer '{archive_layer_name}' to GeoPackage.")
        else:
            print(f"Error: Archive layer '{archive_layer_name}' already exists.")
            '''



    # Placeholder method to handle archived properties
    @staticmethod
    def handle_archived_properties(self, number):
        pass

