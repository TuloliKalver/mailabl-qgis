#MapHelpers.py
import gc
from ..utils.ProgressHelper import ProgressDialogModern
from qgis.core import QgsFeatureRequest # type: ignore
from PyQt5.QtCore import QCoreApplication
from ..Common.app_state import PropertiesProcessStage
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from .MapToolsHelper import MapToolsHelper



class MapDataFlowHelper:

    dialog = None  # Class-level variable to store the dialog reference

    @staticmethod
    def set_dialog(main_dialog):
        """Sets the main dialog reference for ButtonHelper."""
        MapDataFlowHelper.dialog = main_dialog

    @classmethod
    def get_sorted_unique_values_from_filtered_layer(cls, field, 
                                                     expression, 
                                                     refresh_layer=False, 
                                                     zoom_to=False):
        """
        Filters the active layer based on an expression, selects only filtered features,
        and returns sorted unique values for the given field.

        Args:
            field (str): Field name to extract unique values from.
            expression (str): The subset expression to apply.

        Returns:
            list: Sorted list of unique values from the filtered features.
        """
        layer = PropertiesProcessStage.active_layer
        validation = MapToolsHelper.validate_active_layer(layer)
        if validation == False:
           # print(f"Failed to validate Layer: {layer}")
            return

        total_features = layer.featureCount()
        
        progress = ProgressDialogModern(title="Andmete laadimine...", value=0)
        progress.update(1, text1="Palun oota...")

        # Remove previous selection and apply subset filter
        MapToolsHelper.apply_subset_expression(layer=layer, 
                                               expression=expression, 
                                               )

        # Get field index once
        field_index = MapToolsHelper.get_field_indices_for_single_field(layer, field)

        # Collect unique values **only from filtered features**
        unique_values = set()
        feature_ids = []
        for idx, feature in enumerate(layer.getFeatures()):
            unique_values.add(feature[field_index])
            feature_ids.append(feature.id())  # Store only necessary feature IDs
            progress.update(value=idx)
        QCoreApplication.processEvents()
        # Ensure progress bar reaches 100% at the end
        progress.update(value=total_features)

        MapToolsHelper.select_features_by_ids(feature_ids=feature_ids, zoom_to=zoom_to)
        progress.close()
        gc.collect()
        return sorted(unique_values)


    @staticmethod
    def get_layer_data_by_defined_fields(expression, zoom_to=False):
        """
        Retrieve limited data for specific fields from the active QGIS layer,
        ensuring UI remains responsive during processing and updating a progress bar.

        Args:
            expression (str): The subset expression to apply.
            progressBar (QProgressBar, optional): The progress bar widget to update.

        Returns:
            tuple: (list of lists containing feature values, list of field names)
        """
        # Get total feature count for progress tracking
        layer = PropertiesProcessStage.active_layer
        validation = MapToolsHelper.validate_active_layer(layer)
        if validation == False:
            print(f"Failed to validate Layer: {layer}")
            return
        
        total_features = layer.featureCount()
        
        progress = ProgressDialogModern(title="Andmete laadimine...", value=0)
        progress.update(1, text1="Palun oota...")
            
        field_names = Katastriyksus.FieldsForTables

        # Apply subset expression
        MapToolsHelper.apply_subset_expression(layer=layer, expression=expression, triger_repaint=False)

        field_indices = MapToolsHelper.get_field_indices_multiple_fields(layer, field_names=field_names)

        request = QgsFeatureRequest()
        request.setSubsetOfAttributes(list(field_indices.values()))

        data = []
        feature_ids = []

        for idx, feature in enumerate(layer.getFeatures(request)):
            # Build a row using a formatter that chooses the right formatter based on field name
            row = MapToolsHelper.build_feature_row(feature=feature, field_indices=field_indices)
            
            data.append(row)
            feature_ids.append(feature.id())

            if idx % 100 == 0:
                progress.update(idx)

            
        MapToolsHelper.select_features_by_ids(feature_ids=feature_ids, zoom_to=zoom_to)
        progress.close()
        gc.collect()
        return data, feature_ids, field_names

