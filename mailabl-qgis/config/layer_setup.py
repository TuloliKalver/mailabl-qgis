

from PyQt5.uic import loadUi
#from .config.ui_directories import Path_loader_simple,PathLoader, plugin_dir_path, UI_multiline_Statusbar
from .settings import Filepaths, SettingsDataSaveAndLoad, settingPageElements
from PyQt5 import QtWidgets

from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox


class Setup_CadastralsLayers:
    def __init__(self):
        # Assuming you have a stacked widget as an instance attribute
        pass
                
    def load_layer_settings_widget(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems):
        # Get the file path for the Layer Settings Widget .ui file
        ui_file_path = Filepaths.Config_LayerSettings_Widget(self)
        #print(f"path: {ui_file_path}")
        widget = loadUi(ui_file_path)
        # Show the loaded widget
        widget.show()

        # Access the ComboBox within the loaded widget and clear it
        cmbCurrent_Layer = widget.cbCurrent_Cadastral
        cmbTarget_layer = widget.cbTarget_Cadastral
        save_button = widget.pbSaveLayerSettings
        cancel_button = widget.pbCancelSave
        
        QGIS_items.clear_and_populate_combo_box(self, cmbCurrent_Layer)
        QGIS_items.clear_and_populate_combo_box(self, cmbTarget_layer)

        
        # Access the variables through the instance
        save_button.clicked.connect(lambda: Setup_CadastralsLayers.on_save_button_clicked(
                                                                    self, widget, cmbCurrent_Layer, cmbTarget_layer, 
                                                                    self.lblcurrent_main_layer_label, 
                                                                    self.lblnewCadastrals_input_layer_label,
                                                                    self.lblSHPNewItems))
        cancel_button.clicked.connect(lambda: Setup_CadastralsLayers.on_cancel_button_clicked(widget))
        
        

    def on_save_button_clicked(self, widget, cmbCurrent_Layer, cmbTarget_layer,lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems):
        # Handle logic when the save button is clicked
        SettingsDataSaveAndLoad.on_save_button_clicked_cadastrals(self, cmbCurrent_Layer, cmbTarget_layer)
        lblLayerProjects_Properties = self.lblLayerProjects_Properties
        SettingsDataSaveAndLoad.startup_label_loader(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, lblLayerProjects_Properties)
        text = "Kõik sai salvestatud"
        heading = "Supper"
        QMessageBox.information(widget, heading, text)
        # Additional logic if needed

        widget.accept()  # Close the dialog

    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked
        text = "Seekord nii ja homme naa"
        heading = "Hoiatus"
        QMessageBox.information(widget, heading, text)
        widget.reject()  # Close the dialog        


class QGIS_items:
    def __init__(self):
        pass
    
    def clear_and_populate_combo_box(self, combo_box):
        combo_box.clear()
        layer_names = QGIS_items.get_sorted_layer_names(self)
        combo_box.addItems(layer_names)

    def get_sorted_layer_names(self):
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
        
    def set_layer_settings_labels(self):
        #load = SettingsDataSaveAndLoad()
        current_label = self.lblCurrentLayer
        #Mailabl_Project_Label = self.lblSHPNewItems_2
        load = SettingsDataSaveAndLoad()
        load.startup_label_loader(current_label)
        

class Setup_ProjectLayers:
    def load_project_settings_widget(self):
        
        ui_file_path = Filepaths.Config_ProjectSettings_Widget(self)
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel
        
        widget.show()
        
        cmb_layers  = widget.cmbProjects_Layer
        QGIS_items.clear_and_populate_combo_box(self, cmb_layers)
        
        # Connect signals to functions
        save_button.clicked.connect(lambda: Setup_ProjectLayers.on_save_button_clicked(self, widget, cmb_layers))
        cancel_button.clicked.connect(lambda: Setup_ProjectLayers.on_cancel_button_clicked(self, widget))



    def on_save_button_clicked(self, widget, cmb_layers):
        # Handle logic when the save button is clicked
        lblLayerProjects_Properties = self.lblLayerProjects_Properties
        lblcurrent_main_layer_label = self.lblcurrent_main_layer_label
        lblnewCadastrals_input_layer_label = self.lblnewCadastrals_input_layer_label
        lblSHPNewItems = self.lblSHPNewItems
        
        SettingsDataSaveAndLoad.on_save_button_clicked_projects(self, cmb_layers)
        SettingsDataSaveAndLoad.startup_label_loader(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, lblLayerProjects_Properties)
        text = "Kõik sai salvestatud"
        heading = "Supper!"
        QMessageBox.information(widget, heading, text)
        # Additional logic if needed

        widget.accept()  # Close the dialog

    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked
        text = "Seekord nii ja homme naa"
        heading = "Olgu"
        QMessageBox.information(widget, heading, text)
        widget.reject()  # Close the dialog        

