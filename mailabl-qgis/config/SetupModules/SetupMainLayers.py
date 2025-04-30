# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module,import-error


# Related Third-Party Imports
from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtWidgets import QListView, QComboBox, QPushButton
from PyQt5.uic import loadUi
from ..settings import Filepaths, SettingsDataSaveAndLoad, FilesByNames
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog
from ..settings import Filepaths, FilesByNames, SettingsDataSaveAndLoad, StartupSettingsLoader


pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()

class SetupCadastralLayers:
    def __init__(self, parent) -> None:
        self.dialog = parent

    def load_layer_settings_widget(self, lblMainLayerValue,lblMainTargetLayerValue,lblSHPLayerValue):
        # Get the file path for the Layer Settings Widget .ui file
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().layer_setup_ui)
        #print(f"path: {ui_file_path}")
        widget = loadUi(ui_file_path)
        # Show the loaded widget
        widget.show()

        # Access the ComboBox within the loaded widget and clear it
        cmbCurrent_Layer = widget.cbCurrent_Cadastral
        cmbTarget_layer = widget.cbTarget_Cadastral
        save_button = widget.pbSaveLayerSettings
        cancel_button = widget.pbCancelSave

        QGIS_items.clear_and_add_layerNames(cmbCurrent_Layer)
        QGIS_items.clear_and_add_layerNames(cmbTarget_layer)

        
        # Access the variables through the instance
        save_button.clicked.connect(lambda: SetupCadastralLayers.on_save_button_clicked(
                                                                    self, widget, cmbCurrent_Layer, cmbTarget_layer, 
                                                                    lblMainLayerValue,
                                                                    lblMainTargetLayerValue,
                                                                    lblSHPLayerValue))
        cancel_button.clicked.connect(lambda: SetupCadastralLayers.on_cancel_button_clicked(self, widget))
        
    def on_save_button_clicked(self, widget, cmbCurrent_Layer, cmbTarget_layer,lblMainLayerValue,lblMainTargetLayerValue,lblSHPLayerValue):
        # Handle logic when the save button is clicked
        SettingsDataSaveAndLoad.on_save_button_clicked_cadastrals(self, cmbCurrent_Layer, cmbTarget_layer)
        loader = StartupSettingsLoader(self)
        loader.startup_label_loader()
        
        text = "Kõik sai salvestatud"
        heading = pealkiri.tubli
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
        # Additional logic if needed

        widget.accept()  # Close the dialog

    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.infoSimple
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
        widget.reject()  # Close the dialog        


class QGIS_items:
    def __init__(self):
        pass
    #//TODO: refactor this class into a ComboBox helper module
    def clear_and_add_layerNames(combo_box: QComboBox):
        combo_box.clear()
        layer_names = QGIS_items._get_sorted_layer_names()
        combo_box.addItems(layer_names)
        combo_box.setView(QListView())

    def clear_and_add_layerNames_selected(combo_box: QComboBox, layer_name: str = None):
        combo_box.clear()
        layer_names = QGIS_items._get_sorted_layer_names()
        combo_box.addItems(layer_names)   
        # Set the current text of the combo box to the layer name if it exists
        if layer_name:
            combo_box.setCurrentText(layer_name)
        combo_box.setView(QListView())
    
    @staticmethod
    def _get_sorted_layer_names():
        excluded_group = 'Imporditavad kinnistud' 
        layers = []
        for layer_id, layer in QgsProject.instance().mapLayers().items():
            if isinstance(layer, QgsMapLayer) and layer.type() == QgsMapLayer.VectorLayer:
                layer_node = QgsProject.instance().layerTreeRoot().findLayer(layer_id)
                if layer_node is not None and layer_node.parent() is not None and layer_node.parent().name() != excluded_group:
                    layers.append(layer)

        # Get the names of the layers
        layer_names = [layer.name() for layer in layers]

        # Sort layer names alphabetically
        sorted_layer_names = sorted(layer_names)
        return sorted_layer_names
        



