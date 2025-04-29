import re
from PyQt5.QtCore import QDate, QCoreApplication

from qgis.core import QgsProject, QgsVectorLayer
from qgis.utils import iface

from ...config.settings import SettingsDataSaveAndLoad
from .BuildTree import MyTreeHome
from .BuildViewTree import MyTreeHomeView
from ...utils.messagesHelper import ModernMessageDialog
from ...utils.UIWindowHelpers import WindowPositionHelper, WindowManagerMinMax
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts
class FeatureInfoTool:
    def __init__(self, label, lblCadastralNr, lblRegistry, address, purpose, area, created_at, updated_at, treeWidget, reset_timer, main_window, pbOProperty, treeView):
        self.layer = None
        self.label = label
        self.lblRegistry = lblRegistry
        self.lblCadastralNr = lblCadastralNr
        self.reset_timer_callback = reset_timer
        self.lbladdress = address 
        self.lblpurpose = purpose
        self.lblarea = area
        self.lblcreated_at = created_at
        self.lblupdated_at = updated_at
        self.lbltreewidget = treeWidget
        self.tree_View = treeView
        self.main_window = main_window
        self.window_manager = WindowPositionHelper(self.main_window)
        self.window_manager_minMax = WindowManagerMinMax(self.main_window)
        self.setup_layer()
        self.katastriyksus = Katastriyksus()
        self.pbOProperty = pbOProperty

    

    def setup_layer(self):
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        self.layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        
        if not isinstance(self.layer, QgsVectorLayer):
            return

        iface.setActiveLayer(self.layer)

        # Print statement to monitor layer selection
        print(f"Selected input layer: {self.layer.name()}")

        self.layer.removeSelection()
        iface.actionSelect().trigger()
        self.label.setText("")

        # Connect the selectionChanged signal to the handler
        self.layer.selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselected, clearAndSelect):
        print(f"selected: {selected}")
        selected_features = [self.layer.getFeature(fid) for fid in selected]

        # Check if more than one feature is selected
        if len(selected_features) > 1:
            text = HoiatusTexts().Liiga_palju_kinnistuid
            heading = Headings().warningSimple
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading=heading, message=text)
            self.window_manager_minMax._restore_window()
            self.disconnect_signal()
            self.layer.removeSelection()
            self.pbOProperty.setEnabled(True)        
            return
            
        
        else:    
            # Initialize Katastriyksus instance
            katastriyksus = Katastriyksus()
            
            # Define a list of field names
            field_names = [
                katastriyksus.tunnus, 
                katastriyksus.l_aadress,
                katastriyksus.ay_nimi,
                katastriyksus.ov_nimi,
                katastriyksus.mk_nimi,
                katastriyksus.muudet,
                katastriyksus.registr,
                katastriyksus.siht1,
                katastriyksus.siht2,
                katastriyksus.siht3,
                katastriyksus.so_prts1,
                katastriyksus.so_prts2,
                katastriyksus.so_prts3,
                katastriyksus.pindala,
                katastriyksus.kinnistu
            ]
            
            # Dictionary to hold field names and their corresponding indices
            field_indices = {}

            # Find and store the field indices
            for field_name in field_names:
                field_index = FeatureInfoTool.find_field_index(self.layer, field_name)
                field_indices[field_name] = field_index
                #print(f"Index for {field_name}: {field_index}")

            # Extract and print the data from selected features
            feature_data = {}
            for field_name, field_index in field_indices.items():
                feature_data[field_name] = [str(feature.attribute(field_index)) for feature in selected_features]
                feature_data[field_name] = ", ".join(feature_data[field_name])
                #print(f"{field_name} data of selected features: {feature_data[field_name]}")
            
            if feature_data:
                # Extract values into variables
                tunnus_value = self.set_values_to_labels(feature_data)

                self.window_manager_minMax._restore_window()
                
                MyTreeHome.update_tree_with_modules(self, self.lbltreewidget, tunnus_value)
                #TODO - This version works but it's not possible to color cells based on the search results.
                #MyTreeHomeView.update_tree_with_modules(self.tree_View, tunnus_value)
                # This is possible if cell coloring can be implemented
                
            else:
                self.label.setText("Oih midgai läks valesti")
            QCoreApplication.processEvents()

            self.pbOProperty.setEnabled(True)        
            return tunnus_value

    def set_values_to_labels(self, feature_data):
        tunnus_value = self.set_address(feature_data)
        self.set_purpose(feature_data)
        self.set_dates(feature_data)

        area_value = feature_data.get(self.katastriyksus.pindala,'')
        self.lblarea.setText(f"{area_value}")
        QCoreApplication.processEvents()

        return tunnus_value

    def set_dates(self, feature_data):
        created_at_value = feature_data.get(self.katastriyksus.registr, '')
        updated_at_value = feature_data.get(self.katastriyksus.muudet, '')

        created_at_str = self.date_to_string(created_at_value)
        updated_at_str = self.date_to_string(updated_at_value)
        self.lblcreated_at.setText(created_at_str)
        self.lblupdated_at.setText(updated_at_str)

    def set_purpose(self, feature_data):
        purpose1_value = feature_data.get(self.katastriyksus.siht1, '')
        #print(f"purpose1_value: {purpose1_value}")
        purpose2_value = feature_data.get(self.katastriyksus.siht2, '')
        #print(f"purpose2_value: {purpose2_value}")
        purpose3_value = feature_data.get(self.katastriyksus.siht3, '')
        #print(f"purpose3_value: {purpose3_value}")
        percentage1_value = feature_data.get(self.katastriyksus.so_prts1, '') 
        percentage2_value = feature_data.get(self.katastriyksus.so_prts2, '')
        percentage3_value = feature_data.get(self.katastriyksus.so_prts3, '') 
        self.add_purposes(purpose1_value, purpose2_value, purpose3_value, percentage1_value, percentage2_value, percentage3_value)

    def set_address(self, feature_data):
        tunnus_value = feature_data.get(self.katastriyksus.tunnus, '')
        address_value = feature_data.get(self.katastriyksus.l_aadress, '')
        address_value1 = feature_data.get(self.katastriyksus.mk_nimi, '')
        address_value2 = feature_data.get(self.katastriyksus.ov_nimi, '')
        address_value3 = feature_data.get(self.katastriyksus.ay_nimi, '')
        regNr_Value = feature_data.get(self.katastriyksus.kinnistu, '')
        self.lbladdress.setText(f"{address_value}, {address_value2}, {address_value1}, {address_value3}")
        self.lblCadastralNr.setText(tunnus_value)
        if regNr_Value == "NULL":
            self.lblRegistry.setText("Andmed puuduvad")
        else:
            self.lblRegistry.setText(regNr_Value)        #self.label.setText(f"Valitud kinnistu: {tunnus_value}")
        return tunnus_value

    def add_purposes(self, purpose1_value, purpose2_value, purpose3_value, percentage1_value, percentage2_value, percentage3_value):
        
        if purpose1_value !="NULL":
            purpose1 = (f"{purpose1_value} {percentage1_value}%")
        else:
            purpose1 = ""
        if purpose2_value !="NULL":
            purpose2 = (f", {purpose2_value} {percentage2_value}%")
        else:
            purpose2 = ""
        if purpose3_value !="NULL":
            purpose3 = (f", {purpose3_value} {percentage3_value}%")
        else:
            purpose3 = ""
        self.lblpurpose.setText(f"{purpose1}{purpose2}{purpose3}")

    def date_to_string(self, date_item):
        #print(f"date_item: {date_item}")
        #print(f"type of date_item: {type(date_item)}")

        if isinstance(date_item, str):
            match = re.search(r'QDate\((\d+), (\d+), (\d+)\)', date_item)
            if match:
                year, month, day = match.groups()
                original_date = QDate(int(year), int(month), int(day))
                if original_date.isValid():
                    formatted_date = original_date.toString("dd.MM.yyyy")
                    #print(f"Formatted date: {formatted_date}")
                    return formatted_date
                else:
                    print("Invalid QDate extracted from string")
            else:
                print("No valid QDate pattern found in the string")
        else:
            print("date_item is not a valid QDate string")
        
        return ""

    def disconnect_signal(self):
        if self.layer:
            try:
                self.layer.selectionChanged.disconnect(self.on_selection_changed)
                #print("Disconnected the selectionChanged signal.")
                self.layer.removeSelection()
                self.label.clear()
            except TypeError:
                print("Signal was not connected.")
                pass
                
    def disconnect_signal_timed(self):
        if self.layer:
            try:
                self.layer.selectionChanged.disconnect(self.on_selection_changed)
            except TypeError:
                print("Signal was not connected.")
                pass
                
    # Function to find field index case-insensitively
    def find_field_index(layer, field_name):
        # Get all field names from the layer
        field_names = [field.name() for field in layer.fields()]
        
        # Try to find the field index case-insensitively
        for i, name in enumerate(field_names):
            if name.lower() == field_name.lower():
                return i
        
        # If not found, return -1
        return -1


class FeatureInfoToolSearch:
#    def __init__(self, window):
#        self.window = window

    def __init__(self, window, lblCadastralNr, lblRegistry, address, purpose, area, created_at, updated_at, treeWidget, property_button):
        self.window = window
        self.lblRegistry = lblRegistry
        self.lblCadastralNr = lblCadastralNr
        self.lbladdress = address 
        self.lblpurpose = purpose
        self.lblarea = area
        self.lblcreated_at = created_at
        self.lblupdated_at = updated_at
        self.lbltreewidget = treeWidget
        self.katastriyksus = Katastriyksus()
        self.property_button = property_button

    def for_search_results(self):
        
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        print(f"Layer: {layer}")

        # Get the selected feature IDs from the layer
        selected = layer.selectedFeatureIds()
        # Ensure the feature IDs are integers
        selected_features = [layer.getFeature(int(fid)) for fid in selected]
        katastriyksus = Katastriyksus()
        
        # Define a list of field names
        field_names = [
            katastriyksus.tunnus, 
            katastriyksus.l_aadress,
            katastriyksus.ay_nimi,
            katastriyksus.ov_nimi,
            katastriyksus.mk_nimi,
            katastriyksus.muudet,
            katastriyksus.registr,
            katastriyksus.siht1,
            katastriyksus.siht2,
            katastriyksus.siht3,
            katastriyksus.so_prts1,
            katastriyksus.so_prts2,
            katastriyksus.so_prts3,
            katastriyksus.pindala,
            katastriyksus.kinnistu
            ]
            
        # Dictionary to hold field names and their corresponding indices
        field_indices = {}

        # Find and store the field indices
        for field_name in field_names:
            field_index = FeatureInfoTool.find_field_index(layer, field_name)
            field_indices[field_name] = field_index
            print(f"Index for {field_name}: {field_index}")

        # Extract and print the data from selected features
        feature_data = {}
        for field_name, field_index in field_indices.items():
            feature_data[field_name] = [str(feature.attribute(field_index)) for feature in selected_features]
            feature_data[field_name] = ", ".join(feature_data[field_name])
            print(f"{field_name} data of selected features: {feature_data[field_name]}")
        
        if feature_data:
            # Extract values into variables
            tunnus_value = self.set_values_to_labels(feature_data)
            MyTreeHome.update_tree_with_modules(self, self.lbltreewidget, tunnus_value)
            # This is possible if cell coloring can be implemented
        QCoreApplication.processEvents()
        self.property_button.setEnabled(True)
        return tunnus_value

    def set_values_to_labels(self, feature_data):
        tunnus_value = self.set_address(feature_data)
        self.set_purpose(feature_data)
        self.set_dates(feature_data)

        area_value = feature_data.get(self.katastriyksus.pindala,'')
        self.lblarea.setText(f"{area_value}")
        return tunnus_value

    def set_dates(self, feature_data):
        created_at_value = feature_data.get(self.katastriyksus.registr, '')
        updated_at_value = feature_data.get(self.katastriyksus.muudet, '')

        created_at_str = self.date_to_string(created_at_value)
        updated_at_str = self.date_to_string(updated_at_value)
        self.lblcreated_at.setText(created_at_str)
        self.lblupdated_at.setText(updated_at_str)

    def set_purpose(self, feature_data):
        purpose1_value = feature_data.get(self.katastriyksus.siht1, '')
        #print(f"purpose1_value: {purpose1_value}")
        purpose2_value = feature_data.get(self.katastriyksus.siht2, '')
        #print(f"purpose2_value: {purpose2_value}")
        purpose3_value = feature_data.get(self.katastriyksus.siht3, '')
        #print(f"purpose3_value: {purpose3_value}")
        percentage1_value = feature_data.get(self.katastriyksus.so_prts1, '') 
        percentage2_value = feature_data.get(self.katastriyksus.so_prts2, '')
        percentage3_value = feature_data.get(self.katastriyksus.so_prts3, '') 
        self.add_purposes(purpose1_value, purpose2_value, purpose3_value, percentage1_value, percentage2_value, percentage3_value)

    def set_address(self, feature_data):
        tunnus_value = feature_data.get(self.katastriyksus.tunnus, '')
        address_value = feature_data.get(self.katastriyksus.l_aadress, '')
        address_value1 = feature_data.get(self.katastriyksus.mk_nimi, '')
        address_value2 = feature_data.get(self.katastriyksus.ov_nimi, '')
        address_value3 = feature_data.get(self.katastriyksus.ay_nimi, '')
        regNr_Value = feature_data.get(self.katastriyksus.kinnistu, '')
        self.lbladdress.setText(f"{address_value}, {address_value2}, {address_value1}, {address_value3}")
        self.lblCadastralNr.setText(tunnus_value)
        if regNr_Value == "NULL":
            self.lblRegistry.setText("Andmed puuduvad")
        else:
            self.lblRegistry.setText(regNr_Value)
        #self.label.setText(f"Valitud kinnistu: {tunnus_value}")
        return tunnus_value

    def add_purposes(self, purpose1_value, purpose2_value, purpose3_value, percentage1_value, percentage2_value, percentage3_value):
        
        if purpose1_value !="NULL":
            purpose1 = (f"{purpose1_value} {percentage1_value}%")
        else:
            purpose1 = ""
        if purpose2_value !="NULL":
            purpose2 = (f", {purpose2_value} {percentage2_value}%")
        else:
            purpose2 = ""
        if purpose3_value !="NULL":
            purpose3 = (f", {purpose3_value} {percentage3_value}%")
        else:
            purpose3 = ""
        self.lblpurpose.setText(f"{purpose1}{purpose2}{purpose3}")

    def date_to_string(self, date_item):
        #print(f"date_item: {date_item}")
        #print(f"type of date_item: {type(date_item)}")

        if isinstance(date_item, str):
            match = re.search(r'QDate\((\d+), (\d+), (\d+)\)', date_item)
            if match:
                year, month, day = match.groups()
                original_date = QDate(int(year), int(month), int(day))
                if original_date.isValid():
                    formatted_date = original_date.toString("dd.MM.yyyy")
                    #print(f"Formatted date: {formatted_date}")
                    return formatted_date
                else:
                    print("Invalid QDate extracted from string")
            else:
                print("No valid QDate pattern found in the string")
        else:
            print("date_item is not a valid QDate string")
        
        return ""