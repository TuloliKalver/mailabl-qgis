import re
from PyQt5.QtCore import QDate, QCoreApplication, QTimer
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog
from qgis.core import (QgsProject, QgsVectorLayer, QgsExpression, QgsExpressionContext, 
                       QgsExpressionContextUtils, QgsField, QgsFeatureRequest, QgsFeature)
from qgis.PyQt.QtCore import QVariant
from qgis.utils import iface
from ..config.settings import SettingsDataSaveAndLoad
from ..utils.window_manager import WindowManager, WindowManagerMinMax
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus, OldKatastriyksus

class SearchProperties:

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
        katastriyksus = OldKatastriyksus()

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
        virtual_field_expression = " || ' ' || ".join([f"lower({name})" for name in field_names])
        expression = QgsExpression(virtual_field_expression)

        # Check if the expression is valid
        if not expression.hasParserError():
            context = QgsExpressionContext()
            context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(self.layer))
            
            # Iterate over features to evaluate the expression and update the new field
            for feature in self.layer.getFeatures():
                context.setFeature(feature)
                value = expression.evaluate(context)
                
                # Update the "search_field" attribute
                self.layer.changeAttributeValue(feature.id(), self.layer.fields().indexFromName(self.search_field), value)

            self.layer.commitChanges()
        else:
            print(f"Expression error: {expression.parserErrorString()}")

    def search_for_item(self, label):
        self.setup_layer()
    

        # Get the label text value
        label_text = label.text() if hasattr(label, 'text') else str(label)

        # Create the search expression
        search_expression = QgsExpression(f"\"search_field\" LIKE '%{label_text}%'")
        print(f"Search expressinon: {search_expression}")
        # Compile the expression

        if search_expression.hasParserError():
            print(f"Expression error: {search_expression.parserErrorString()}")
            return None

        # Perform the search
        request = QgsFeatureRequest(search_expression)
        features = list(self.layer.getFeatures(request))
        
        if not features:
            text = (f"Märksõnale {label_text} ei leitud ühtegi vastet")
            QMessageBox.information(None, "info", text )
            print(f"Label '{label_text}' not found in the search_field.")
            return None
        
        if len(features) == 1:
            return self.select_feature(features[0])
        
        return self.select_from_multiple_features(features, label_text)

    def select_feature(self, feature):
        tunnus_value = feature[Katastriyksus.tunnus]  # Replace 'tunnus' with the actual field name if different
        
        # Select the feature in the layer
        self.layer.selectByIds([feature.id()])
        
        # Zoom to the selected feature
        iface.mapCanvas().zoomToSelected(self.layer)
        
        print(f"Found with tunnus: {tunnus_value}")
        return tunnus_value, feature
    
    def select_from_multiple_features(self, features, label_text):
        items = [f"{feature['search_field']}" for feature in features]
        item, ok = QInputDialog.getItem(None, "Vali nimekirjast", f"Otsingule '{label_text}'leiti mitu vastust:", items, 0, False)

        if ok and item:
            selected_index = items.index(item)
            return self.select_feature(features[selected_index])
        
        print(f"Selection canceled or invalid for label '{label_text}'.")
        return None
