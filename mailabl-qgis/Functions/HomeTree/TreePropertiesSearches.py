from ...config.settings import  SettingsDataSaveAndLoad
from PyQt5.QtWidgets import QMessageBox
from .BuildTree import MyTreeHome
from .BuildViewTree import MyTreeHomeView

from qgis.core import QgsProject, QgsVectorLayer
from qgis.utils import iface
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus

class FeatureInfoTool:
    def __init__(self, label, reset_timer_callback, treeWidget):
        self.layer = None
        self.label = label
        self.reset_timer_callback = reset_timer_callback
        
        self.treewidget = treeWidget
        

        self.setup_layer()

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
        selected_features = [self.layer.getFeature(fid) for fid in selected]

        # Check if more than one feature is selected
        if len(selected_features) > 1:
            text = "Valitud on rohkem kui üks objekt. Palun valige uuesti. Hetkel on toetatud ainult üksiku kinnistu valik!"
            heading = "info"
            QMessageBox.information(None, heading, text) 
            self.layer.removeSelection()
            return
        
        else:    
            # Extract the index of the "TUNNUS" field
            field_index = self.layer.fields().indexFromName(Katastriyksus().tunnus)

            tunnus_field_name = Katastriyksus().tunnus
            field_index = FeatureInfoTool.find_field_index(self.layer, tunnus_field_name)

        # If the field "TUNNUS" exists, extract its data from selected features
            if field_index != -1:
                tunnus_data = [str(feature.attribute(field_index)) for feature in selected_features]

                # Format the data as a string
                tunnus_str = ", ".join(tunnus_data)
                print("TUNNUS data of selected features:", tunnus_data)

                # Update the label only if tunnus_str is not empty
                if tunnus_str != "":
                    self.label.setText(f"Valitud kataster: {tunnus_str}")
                    MyTreeHome.update_tree_with_modules( self.treewidget, tunnus_data)
                    # This is possible if cell coloring can be implemented
                    #MyTreeHomeView.update_tree_with_modules( self.treeView, tunnus_data)
                else:
                    self.label.setText("Oih midgai läks valesti")
                
                return tunnus_data
            else:
                self.label.setText("Oih midgai läks valesti")
                print("Oih midgai läks valesti")
                return []


    def disconnect_signal(self):
        if self.layer:
            try:
                self.layer.selectionChanged.disconnect(self.on_selection_changed)
                print("Disconnected the selectionChanged signal.")
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