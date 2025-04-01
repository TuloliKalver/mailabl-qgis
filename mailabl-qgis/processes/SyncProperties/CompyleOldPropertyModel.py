from qgis.core import QgsProject, QgsLayerTree, QgsLayerTreeGroup, QgsLayerTreeLayer, QgsFeature, edit
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import connect_settings_to_layer
from ...config.settings import Filepaths, FilesByNames
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus, OldKatastriyksus, KatasterMappings
from PyQt5.uic import loadUi
from ...utils.messagesHelper import ModernMessageDialog

class LayerCompiler:
    def find_layer_by_name(name, root=None):
        """
        Recursively searches for a layer by name in the layer tree.
        
        :param name: The name of the layer to find.
        :param root: The root of the layer tree to start the search from.
        :return: The layer if found, else None.
        """
        if root is None:
            root = QgsProject.instance().layerTreeRoot()

        for child in root.children():
            if isinstance(child, QgsLayerTreeLayer) and child.layer().name() == name:
                return child.layer()
            elif isinstance(child, QgsLayerTreeGroup):
                layer = LayerCompiler.find_layer_by_name(name, child)
                if layer:
                    return layer
        return None


    def compile_layers(self, new_layer_name):
        """
        Compiles features from the old layer ('OldKatastriyksus') to the new layer ('Katastriyksus').
        
        :param new_layer_name: Name of the new layer to which features will be appended.
        """
        old_layer_name = connect_settings_to_layer.ActiveMailablPropertiesLayer_name()
        print(f"Old Layer Name: {old_layer_name}")

        old_layer = LayerCompiler.find_layer_by_name(old_layer_name)
        new_layer = LayerCompiler.find_layer_by_name(new_layer_name)

        # Create a set of 'tunnus' values from the new layer for quick lookup
        new_layer_tunnus_values = {feature[Katastriyksus.tunnus] for feature in new_layer.getFeatures()}

        # Message box to confirm proceeding after loading layers
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Continue Process")
        msg_box.setText("Layers loaded. Do you want to continue?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg_box.exec_()

        if retval == QMessageBox.No:
            print("Process stopped by user.")
            return

        # Message box to confirm proceeding to add missing features
        msg_box.setText("Field mapping prepared. Do you want to proceed with adding missing features?")
        retval = msg_box.exec_()

        if retval == QMessageBox.No:
            print("Process stopped by user.")
            return

        # Add missing features from old layer to new layer
        with edit(new_layer):
            for old_feature in old_layer.getFeatures():

                # Combine field names and attribute values for clarity
                old_fields = old_layer.fields()  # Get a list of QgsField objects
                old_attributes = old_feature.attributes()  # Get the list of attribute values
                combined_attributes = []
                for i, field in enumerate(old_fields):
                    combined_attributes.append((field.name(), old_attributes[i]))

                # Find the index of the 'tunnus' field in combined_attributes
                tunnus_index = None
                for i, (field_name, _) in enumerate(combined_attributes):
                    if field_name == OldKatastriyksus.tunnus:
                        tunnus_index = i
                        break

                if tunnus_index is not None and combined_attributes[tunnus_index][1] not in new_layer_tunnus_values:
                    # Create a new feature for the new layer
                    new_feature = QgsFeature(new_layer.fields())

                    field_mapping = KatasterMappings.field_mapping

                    # Map attributes from old layer to new layer using field mapping
                    for old_field, new_field in field_mapping.items():
                        if old_field in old_feature.fields().names():
                            new_feature[new_field] = old_attributes[old_feature.fields().lookupField(old_field)]

                    # Set the geometry of the new feature
                    new_feature.setGeometry(old_feature.geometry())

                    # Add the new feature to the new layer
                    new_layer.addFeature(new_feature)

                    # Print the attributes of the new feature being added for testing
                    print(f"Added feature with tunnus: {new_feature[Katastriyksus.tunnus]}")
                    print(f"Attributes: {new_feature.attributes()}")
    
                    # Message box to confirm proceeding after adding each feature
                    msg_box.setText(f"Added feature with tunnus: {new_feature[Katastriyksus.tunnus]}. Do you want to continue?")
                    retval = msg_box.exec_()

                    if retval == QMessageBox.No:
                        print("Process stopped by user.")
                        return

        print("Compilation complete.")



class LayerCompilerSetup():
    
    def load_layer_compiler_widget(self):
        # Load the UI from the specified .ui file
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().layer_compiler)
        print(f"ui path: {ui_file_path}")
        widget = loadUi(ui_file_path)
        # Show the widget
        widget.show()

        # Access the comboboxes and button
        self.old_layer_combo = widget.oldLayerComboBox
        self.new_layer_combo = widget.newLayerComboBox
        self.confirm_button = widget.pbConfirmCompileLayers
        self.cancel_button = widget.pbCancelCompileLayers
        

        # Populate comboboxes with available layers
        LayerCompilerSetup.populate_comboboxes(widget)

        # Connect the confirm button to the compilation function
        self.confirm_button.clicked.connect(lambda: LayerCompilerSetup.on_confirm(widget))
        self.confirm_button.clicked.connect(lambda: LayerCompilerSetup.on_cancel(widget))
        


    def populate_comboboxes(widget):
        layers = QgsProject.instance().mapLayers().values()
        for layer in layers:
            widget.oldLayerComboBox.addItem(layer.name(), layer.id())
            widget.newLayerComboBox.addItem(layer.name(), layer.id())

    @staticmethod
    def on_confirm(widget):
        old_layer_name = widget.oldLayerComboBox.currentText()
        new_layer_name = widget.newLayerComboBox.currentText()

        # Show a message box to confirm the selection
        reply  = QMessageBox.question(None, 'Confirmation', 
                                     f'Are you sure you want to compile layers?\nOld Layer: {old_layer_name}\nNew Layer: {new_layer_name}', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            LayerCompiler().compile_layers(new_layer_name)
        widget.accept()

    @staticmethod
    def on_cancel(widget):
        widget.reject()

    def compile_layers(self, new_layer_name):
        compiler = LayerCompiler()
        compiler.compile_layers(self, new_layer_name)
        heading = "info"
        text = "Layer compilation complete."
        ModernMessageDialog.Info_messages_modern(heading,text)  

