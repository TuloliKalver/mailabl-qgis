import re
import gc
from typing import List
from qgis.PyQt.QtCore import QVariant

from qgis.core import (
    QgsFeatureRequest,
    QgsVectorLayer,
    QgsFeature,
    QgsField,
    QgsExpression,
    QgsExpressionContext,
    QgsExpressionContextUtils,
    QgsFields
)



from ..config.mylabl_API.settings import AreaUnit
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..KeelelisedMuutujad.MaaAmetFieldFormater import date_formatter_for_Mailabl_insertion



class LayerFeaturehepers:
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

    @staticmethod
    def _get_layer_fetaures_by_id(layer: QgsVectorLayer, feature_id: int) -> QgsFeature:

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
    def _get_geometry_as_wkt(feature: QgsFeature) -> str:
        return feature.geometry().asWkt() if feature.hasGeometry() else ""
    
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
    def update_search_fields_in_layer(layer: QgsVectorLayer):
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
    def _add_feature_to_layer_with_commit_option(layer: QgsVectorLayer, new_feature: QgsFeature, commit=False) -> bool:
        """
        Safely adds a new feature to a layer, avoiding both internal FID and 'fid' field conflicts.
        """

        # Start editing if needed
        if layer.isEditable():
            layer.startEditing()
            #print(f"✍️ Started editing layer '{layer.name()}'.")
        
        target_fields = layer.fields()  # Get the target layer's fields once.
        new_attrs = LayerFeaturehepers._map_attributes_by_name(new_feature, target_fields)
        #print(f"attributes before new max fid:")
        #print(new_attrs)
        
        from ..utils.LayerHelpers import fidOperations
        max_fid = fidOperations.get_next_fid(layer)
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

    
class DataMappers:
    
    @staticmethod
    def _map_properties_main_details_from_input(layer_data: dict) -> dict:

        siht1 = layer_data.get(Katastriyksus.siht1)
        #print(f"siht1 {siht1}")
        if siht1 in ("TRANSPORTIMAA", "KAITSEALUNE_MAA"):
            #print("Extracting address details from street as transpordimaa or kaitsealune maa...")
            street = layer_data.get(Katastriyksus.l_aadress)
            house_number = ""
        else:
            #print("Extracting address details from street...")
            street_data = layer_data.get(Katastriyksus.l_aadress)
            data = AddressUtils._get_address_details_from_street(street_data)
            street = data.get("street")
            house_number = data.get("house", "")


        prepared_data = {
            "immovableNumber": layer_data.get(Katastriyksus.hkood),
            "cadastralUnit": {
                "number": layer_data.get(Katastriyksus.tunnus),

                "firstRegistration": date_formatter_for_Mailabl_insertion(layer_data.get(Katastriyksus.registr)),
                "lastUpdated": date_formatter_for_Mailabl_insertion(layer_data.get(Katastriyksus.muudet))
            },
            "address": {
                "street": street,
                "houseNumber": house_number,  # Can extract this later if needed
                "city": layer_data.get(Katastriyksus.ay_nimi),
                "state": layer_data.get(Katastriyksus.ov_nimi),
                "county": layer_data.get(Katastriyksus.mk_nimi)
            },
            "area": {
                "size": layer_data.get(Katastriyksus.pindala),
                "unit": AreaUnit.M
            }
        }

        usage_data = AddressUtils._extract_intended_use_data(layer_data)
        return prepared_data, usage_data
    
class AddressUtils:
    @staticmethod
    def _get_address_details_from_street(street: str) -> dict:
        data = {}
         # Handle None, QVariant, "NULL", etc.
        if not street or str(street).upper() == "NULL":
            data['street'] = ""
            data['house'] = ""
            return data

        # 💡 Case: building-like code (e.g., "L1", "T2")
        if re.fullmatch(r'^[A-Za-z]{1,2}\d{1,2}$', street):
            #print("📦 Detected building-like code → treat as full street")
            data['street'] = street
            return data

        # 💡 Check for street + number (or fancy house number)
        match = re.match(r'^(.*?)(\d+.*)$', street)
        if match:
            possible_street = match.group(1).strip()
            possible_house = match.group(2).strip()
            #print(f"🔧 Regex match → street: '{possible_street}', house: '{possible_house}'")

            if re.match(r'^\d+', possible_house):
                #print("✅ House part starts with number → valid house number")
                data['street'] = possible_street
                data['house'] = possible_house
            else:
                #print("⚠️ House part doesn't start with number → fallback to full string as street")
                data['street'] = street
        else:
            #print("❌ No match found → fallback to full string as street")
            data['street'] = street

        #print(f"✅ Final parsed result: {data}")
        return data

    @staticmethod
    def _extract_intended_use_data(layer_data: dict) -> dict:
        usage_data = []
        num_siht_items = 3

        siht_field = Katastriyksus.siht1
        prts_field = Katastriyksus.so_prts1
        siht_base = siht_field[:-1]
        prts_base = prts_field[:-1]

        for i in range(1, num_siht_items + 1):
            siht_name = f"{siht_base}{i}"
            so_prts_name = f"{prts_base}{i}"

            purpouse = layer_data.get(siht_name)

            # ✅ Skip immediately if siht_name is empty or null
            if not purpouse or str(purpouse).strip().upper() == "NULL":
                continue

            so_prts_data = layer_data.get(so_prts_name)

            intended_use = {
                "sortOrder": i,
                "name": AddressUtils.normalize_purpose_name(purpouse),
                "percentage": so_prts_data,
            }

            usage_data.append(intended_use)

        return usage_data

    
    @staticmethod
    def normalize_purpose_name(raw_name: str) -> str:
        if not raw_name:
            return ""

        # Step 1: Lowercase and replace underscores
        raw_name = raw_name.replace("_", " ").lower().strip()

        # Step 2: Split into words
        words = raw_name.split()

        # Step 3: Capitalize only the first word
        if words:
            words[0] = words[0].capitalize()

        # Step 4: Optional Estonian mapping on first word
        estonian_fixes = {
            "Uhiskondlike": "Ühiskondlike",
            "Toostusmaa": "Tööstusmaa",
            "Jaatmehoidla": "Jäätmehoidla",
            "Maetoostusmaa": "Mäetööstusmaa",
            "Turbatoostusmaa": "Turbatööstsmaa",
            "üldkastutatav": "üldkasutatav"
            # Add more if needed
        }


        for word in words:
            word = estonian_fixes.get(word)

        return " ".join(words)
