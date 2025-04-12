#MapHelpers.py
import gc
from ..utils.LayerHelpers import FeatuerHelpers
from ..utils.ProgressHelper import ProgressDialogModern
from qgis.core import QgsFeatureRequest, QgsExpression # type: ignore
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
    def get_sorted_unique_values_from_filtered_layer_old(cls, field, 
                                                    expression, 
                                                    refresh_layer=False, 
                                                    zoom_to=False,
                                                    select=False):
        """
        Filters the active layer using an expression, then returns sorted unique
        values for a given field, with optional selection and zoom.

        Args:
            field (str): Field name to extract from.
            expression (str): Filter expression to apply.
            refresh_layer (bool): Trigger repaint or refresh.
            zoom_to (bool): Zoom to filtered features.
            select (bool): Select filtered features.

        Returns:
            list: Sorted unique values from filtered results.
        """

        layer = PropertiesProcessStage.active_layer
        if not MapToolsHelper.validate_active_layer(layer):
            print("❌ Layer validation failed.")
            return []

        progress = ProgressDialogModern(title=f"Andmete laadimine...{field}", value=0)
        progress.update(1, text1="Palun oota...")

        if refresh_layer:
            layer.triggerRepaint()

        # Apply expression
        print(f"Applying expression: {expression} on layer '{layer.name()}'")
        MapToolsHelper.apply_subset_expression(layer=layer, expression=expression)

        # Extract field index
        field_index = MapToolsHelper.get_field_indices_for_single_field(layer, field)

        # Get unique values and matching feature IDs
        unique_values, feature_ids = FeatuerHelpers.fast_collect_unique_values_and_ids(
            layer=layer,
            field_index=field_index,
            progress=progress
        )

        if select:
            MapToolsHelper.select_features_by_ids(feature_ids=feature_ids, zoom_to=zoom_to)

        progress.update(value=layer.featureCount())
        progress.close()
        gc.collect()

        return sorted(unique_values)  # Or: return sorted(unique_values), feature_ids


    @classmethod
    def get_sorted_unique_values_from_filtered_layer(cls, field: str, expression: str,
                                                    refresh_layer=False, zoom_to=False, select=False) -> list:
        """
        Efficiently retrieves sorted unique values for a field using expression-based filtering.
        Applies geometry + zooming only if requested.

        Args:
            field (str): Field name to extract unique values from.
            expression (str): QGIS expression string to filter features.
            refresh_layer (bool): Whether to refresh the layer after applying expression.
            zoom_to (bool): Whether to zoom to filtered features.
            select (bool): Whether to select filtered features.

        Returns:
            list: Sorted list of unique field values.
        """
        layer = PropertiesProcessStage.active_layer
        if not MapToolsHelper.validate_active_layer(layer):
            print("❌ Layer validation failed.")
            return []

        progress = ProgressDialogModern(title=f"Andmete laadimine...{field}", value=0)
        progress.update(1, text1="Palun oota...")

        if refresh_layer:
            layer.triggerRepaint()

        # ✅ Build expression or skip if empty
        if expression.strip():
            print(f"🔍 Applying filter: {expression}")
            exp = QgsExpression(expression)
            if exp.hasParserError():
                print(f"❌ Expression parse error: {exp.parserErrorString()}")
                progress.close()
                return []
            request = QgsFeatureRequest(exp)
        else:
            print("⚠️ No expression applied. Fetching all features.")
            request = QgsFeatureRequest()

        # ✅ Optimize request
        request.setSubsetOfAttributes([field], layer.fields())
        if not zoom_to:
            request.setFlags(QgsFeatureRequest.NoGeometry)

        unique_values = set()
        feature_ids = []

        for feature in layer.getFeatures(request):
            value = feature[field]
            unique_values.add(value)
            if select or zoom_to:
                feature_ids.append(feature.id())

        if select:
            MapToolsHelper.select_features_by_ids(feature_ids=feature_ids, zoom_to=zoom_to)

        progress.update(value=layer.featureCount())
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

        append_data = data.append
        append_ids = feature_ids.append
        get_features = layer.getFeatures(request)

        for idx, feature in enumerate(get_features):            # Build a row using a formatter that chooses the right formatter based on field name
            row = MapToolsHelper.build_feature_row(feature=feature, field_indices=field_indices)
            
            append_data(row)
            append_ids(feature.id())

            if idx % 10 == 0:
                progress.update(idx)

        MapToolsHelper.select_features_by_ids(feature_ids=feature_ids, zoom_to=zoom_to)
        progress.close()
        gc.collect()
        return data, feature_ids, field_names

