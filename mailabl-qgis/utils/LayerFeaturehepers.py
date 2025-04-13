#LayerFeaturehelpers.py

from typing import List


from qgis.core import (
    QgsFeatureRequest,
    QgsVectorLayer,
    QgsFeature,

    QgsExpression,
    QgsExpressionContext,
    QgsExpressionContextUtils
)

from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..utils.fidOperationsHelper import fidOperations
class LayerFeatureHelpers:

    @staticmethod
    def _get_layer_fetaures_by_id(layer: QgsVectorLayer, feature_id: int) -> QgsFeature:
        print(f"🔍 Searching for feature ID {feature_id} in layer '{layer.name()}'.")
        request = QgsFeatureRequest().setFilterFids([feature_id])
        feature = next(layer.getFeatures(request), None)

        if feature and feature.isValid():
            return feature
        print(f"⚠️ Feature ID {feature_id} not found.")
        return None
    
    @staticmethod
    def _get_feature_attributes_as_dict(feature: QgsFeature) -> dict:
        return {field.name(): feature[field.name()] for field in feature.fields()}

    @staticmethod
    def _get_all_features_from_layer(layer: QgsVectorLayer) -> List[QgsFeature]:
        """
        Retrieves all features from the provided layer.
        """
        features = [f for f in layer.getFeatures()]
        if not features:
            print(f"No features found in layer '{layer.name()}'.")
            return []
        return features
    @staticmethod
    def _map_attributes_by_name(input_feature: QgsFeature, target_fields: List) -> List:
        """
        Map attributes from an input feature to a list of attribute values that match
        the target layer's fields by name. If the input feature doesn't have a field,
        assign None.

        :param input_feature: QgsFeature from the input layer.
        :param target_fields: QgsFields object from the target layer.
        :return: List of attribute values in the order of target_fields.
        """
        # Get the names of fields present in the input feature.
        input_field_names = input_feature.fields().names()
        new_attrs = []
        for field in target_fields:
            field_name = field.name()
            if field_name in input_field_names:
                new_attrs.append(input_feature[field_name])
            else:
                # Field not present in input; assign a default value.
                new_attrs.append(None)
        return new_attrs

    @staticmethod
    def _map_attributes_by_feature(feature: QgsFeature) -> List:
        """
        Creates a new QGIS feature by copying the geometry and attributes from the provided feature.

        This helper function replicates the behavior of the `_map_attributes_by_name` function,
        but should only be used when the source and target fields match exactly. It copies the
        geometry and attributes from the source feature into a new feature, then sets the new
        feature's ID to -1 so that QGIS will assign a unique ID when it is added to a layer.

        Parameters:
            feature (QgsFeature): The source feature whose geometry and attributes are to be copied.

        Returns:
            list: A list containing a single QgsFeature. This feature has the same geometry and attributes
                as the input feature, but with a new, system-assigned unique ID.
        """
        features = []

        feat = QgsFeature()
        feat.setGeometry(feature.geometry())
        feat.setAttributes(feature.attributes())
        feat.setId(-1)
        features.append(feat)

        return features

    @staticmethod
    def _update_search_fields_in_layer(layer: QgsVectorLayer):
        """
        Recomputes and updates the search field for all features in the layer.
        """
        search_field = Katastriyksus().search_field
        search_value_fields = Katastriyksus().search_field_items

        if search_field not in layer.fields().names():
            print(f"❌ Field '{search_field}' not found in layer.")
            return

        # Build expression like: lower(field1) || ' ' || lower(field2) || ...
        expr_str = " || ' ' || ".join([f"lower(\"{f}\")" for f in search_value_fields])
        exp = QgsExpression(expr_str)

        context = QgsExpressionContext()
        context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

        if not layer.isEditable():
            layer.startEditing()

        for feature in layer.getFeatures():
            context.setFeature(feature)
            value = exp.evaluate(context)

            if exp.hasEvalError():
                print(f"⚠️ Expression error for feature {feature.id()}: {exp.evalErrorString()}")
                continue

            layer.changeAttributeValue(feature.id(), layer.fields().indexOf(search_field), value)

        layer.commitChanges()
        #print("✅ Search fields updated.")        
        
    @staticmethod
    def _add_feature_to_layer_with_commit_option(layer: QgsVectorLayer, new_feature: QgsFeature, commit=False) -> bool:
        """
        Safely adds a new feature to a layer, avoiding both internal FID and 'fid' field conflicts.
        """

        # Start editing if needed
        if layer.isEditable():
            layer.startEditing()
            #print(f"✍️ Started editing layer '{layer.name()}'.")
        
        target_fields = layer.fields()  # Get the target layer's fields once.
        new_attrs = LayerFeatureHelpers._map_attributes_by_name(new_feature, target_fields)
        #print(f"attributes before new max fid:")
        #print(new_attrs)
        

        max_fid = fidOperations._get_next_fid(layer)
        #print(max_fid)
        # Set the value for the 'fid' field if it exists
        fid_index = target_fields.indexOf("fid")
        new_attrs[fid_index] = max_fid


        # ✅ Update the feature *before* adding it
        new_feature.setAttributes(new_attrs)
        # Insert feature
        res, _ = layer.dataProvider().addFeatures([new_feature])
        #print(f"✅ Feature added to layer '{layer.name()}': {res}")

        # Commit edits
        if commit:
            layer.commitChanges()
            #print("💾 Changes committed.")

        return res

    @staticmethod
    def _delete_element_from_layer(delete: bool, feature_id, layer: QgsVectorLayer) -> None:
        # If deletion is requested, remove features from the input layer.
        if delete is True:
            res = layer.dataProvider().deleteFeatures([feature_id])
            if res:
                print(f"Successfully deleted features from input layer '{layer.name()}'.")
            else:
                print(f"Failed to delete features from input layer '{layer.name()}'.")
            layer.triggerRepaint()

    @staticmethod
    def _delete_feature_object(feature: QgsFeature, layer: QgsVectorLayer, repaint: bool = True) -> bool:
        """
        Deletes the given QgsFeature object from the specified layer.
        """
        if not feature or not layer:
            #print("❌ Missing feature or layer.")
            return False

        fid = feature.id()
        res = layer.dataProvider().deleteFeatures([fid])
        
        if res:
            #print(f"🗑️ Feature {fid} deleted from layer '{layer.name()}'.")
            if repaint:
                layer.triggerRepaint()
            return True
        else:
            print(f"⚠️ Failed to delete feature {fid} from layer '{layer.name()}'.")
            return False
