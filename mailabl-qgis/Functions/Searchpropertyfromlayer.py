import re
from PyQt5.QtWidgets import QInputDialog, QWidget
from qgis.core import (QgsProject, QgsVectorLayer, QgsExpression, QgsExpressionContext, 
                       QgsExpressionContextUtils, QgsField, QgsFeatureRequest)
from qgis.PyQt.QtCore import QVariant
from qgis.utils import iface
from ..config.settings import SettingsDataSaveAndLoad
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts, HoiatusTextsAuto, EdukuseTexts
from ..utils.messagesHelper import ModernMessageDialog

class SearchProperties:
    def __init__(self, parent: QWidget):
        self.parent = parent


    def setup_layer(self):
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        self.layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        
        if not isinstance(self.layer, QgsVectorLayer):
            return

        iface.setActiveLayer(self.layer)
        self.add_search_field()

        return self.layer


    def add_search_field(self):
        # Initialize Katastriyksus instance
        katastriyksus = Katastriyksus()

        self.search_field = 'search_field'
        
        # Define a list of field names
        field_names = [
            katastriyksus.tunnus,
            katastriyksus.l_aadress,
            katastriyksus.ay_nimi,
            katastriyksus.ov_nimi,
            katastriyksus.mk_nimi,
        ]

        # Check if the "search_field" already exists
        if self.search_field not in [field.name() for field in self.layer.fields()]:
            self.layer.startEditing()
            self.layer.addAttribute(QgsField(self.search_field, QVariant.String))
            self.layer.updateFields()

        # Create a virtual field using a concatenation of the field names
        concatenation_expression = " || ' ' || ".join([f"lower(\"{name}\")" for name in field_names])
        print(f"concatenation_expression: {concatenation_expression}")
        expression = QgsExpression(concatenation_expression)

        # Check if the expression is valid
        if not expression.hasParserError():
            context = QgsExpressionContext()
            context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(self.layer))

            # Iterate over features to evaluate the expression and update the new field
            for feature in self.layer.getFeatures():
                context.setFeature(feature)
                value = expression.evaluate(context)

                # Handle potential null values in the virtual field
                if value is None:
                    value = ""

                # Update the "search_field" attribute
                self.layer.changeAttributeValue(feature.id(), self.layer.fields().indexFromName(self.search_field), value)

            self.layer.commitChanges()
            return True
        else:
            print(f"Expression error: {expression.parserErrorString()}")
            return False


    def search_for_item(self, label):
        self.setup_layer()

        # Ensure the search field exists
        if self.search_field not in [field.name() for field in self.layer.fields()]:
            heading = Headings().infoSimple
            text = "Paistab, et kasutad otsingut esmakordselt."
            text_2 = "Teen vajalikud andmebaasi ettevalmistused."
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text, text_2)
            result = self.add_search_field()
            if result != True:
                heading = Headings().warningCritical
                text = HoiatusTexts().error
                ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
            else:
                heading = Headings().infoSimple
                text = EdukuseTexts().tehtud
                ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)

        # Get the label text value and convert it to lowercase
        label_text = label.text().lower() if hasattr(label, 'text') else str(label).lower()

        # Define a regular expression to identify cadastral code format
        cadastral_code_pattern = r'^\d{5}:\d{3}:\d{4}$'
        is_cadastral_code = re.match(cadastral_code_pattern, label_text) is not None

        if is_cadastral_code:
            # If it's a cadastral code, perform a specific search for it
            search_expression = QgsExpression(f"\"{self.search_field}\" LIKE '%{label_text}%'")
        else:
            # Normalize the label text for street names and numbers
            normalized_label_text = re.sub(r'\s+', ' ', label_text.strip())  # Replace multiple spaces with a single space

            # Split label_text to separate street name and number
            parts = normalized_label_text.split()
            
            # Determine if the input has a number or is just a street name
            if len(parts) == 1:
                street_name = parts[0]
                number = ''
            else:
                street_name = " ".join(parts[:-1])
                number = parts[-1]

            # Handle multiple numbers in the address field
            if number:
                number_patterns = [num.strip() for num in number.split('//')]
            else:
                number_patterns = ['']

            # Define common street patterns
            patterns = [f"{street_name} {num}" for num in number_patterns if num]
            patterns += [f"{street_name} tn {num}" for num in number_patterns if num]
            patterns += [f"{street_name} street {num}" for num in number_patterns if num]
            patterns += [f"{street_name} pst {num}" for num in number_patterns if num]
            patterns += [f"a. h. {street_name} {num}" for num in number_patterns if num]
            patterns += [f"a.h. {street_name} {num}" for num in number_patterns if num]

            if number:
                patterns += [f"{street_name} {num} tn" for num in number_patterns]
                patterns += [f"{street_name} {num} street" for num in number_patterns]
                patterns += [f"{street_name} {num} pst" for num in number_patterns]
                patterns += [f"a. h. {street_name} {num}" for num in number_patterns]
                patterns += [f"a.h. {street_name} {num}" for num in number_patterns]
                patterns += [f"{street_name}-{num}" for num in number_patterns]
                patterns += [f"{street_name}{num}" for num in number_patterns]
            else:
                patterns += [
                    f"{street_name} tn",
                    f"{street_name} street",
                    f"{street_name} pst",
                    f"a. h. {street_name}",
                    f"a.h. {street_name}",
                    f"{street_name}-",
                    f"{street_name}"
                ]

            # Combine patterns into a single search expression
            search_expressions = " OR ".join([f"lower(\"{self.search_field}\") LIKE '%{pattern.lower()}%'" for pattern in patterns])
            search_expression = QgsExpression(search_expressions)

        print(f"Search expression: {search_expression}")

        # Compile the expression
        if search_expression.hasParserError():
            print(f"Expression error: {search_expression.parserErrorString()}")
            return None

        # Perform the search
        request = QgsFeatureRequest(search_expression)
        features = list(self.layer.getFeatures(request))
        
        if not features:
            heading = Headings().infoSimple
            text = HoiatusTextsAuto.no_match_for_this(label_text)
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
            #print(f"Label '{label_text}' not found in the search_field.")
            return None

        if len(features) == 1:
            return self.select_feature_OLD_AND_SLOW(features[0])

        return self.select_from_multiple_features(features, label_text)


    def select_feature_OLD_AND_SLOW(self, feature):
        tunnus_value = feature[Katastriyksus.tunnus]  
        
        # Select the feature in the layer
        self.layer.selectByIds([feature.id()])
        
        # Zoom to the selected feature
        iface.mapCanvas().zoomToSelected(self.layer)
                
        print(f"Found with tunnus: {tunnus_value}")
        return tunnus_value, feature


    def select_from_multiple_features(self, features, label_text):
        items = [f"{feature['search_field']}" for feature in features]
        item, ok = QInputDialog.getItem(self.parent, "Vali nimekirjast", f"Otsingule '{label_text}' leiti mitu vastust:", items, 0, False)

        if ok and item:
            selected_index = items.index(item)
            return self.select_feature_OLD_AND_SLOW(features[selected_index])
        
        print(f"Selection canceled or invalid for label '{label_text}'.")
        return None
