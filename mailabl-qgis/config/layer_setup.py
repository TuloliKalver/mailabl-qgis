# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module,import-error


# Related Third-Party Imports
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from qgis.core import QgsMapLayer, QgsProject

# Local Application or Library Imports
from .settings import Filepaths, SettingsDataSaveAndLoad, FilesByNames
from ..processes.infomessages.messages import Headings, HoiatusTexts, EdukuseTexts



pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()

class SetupCadastralLayers:

    def load_layer_settings_widget(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems):
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
        
        QGIS_items.clear_and_populate_combo_box(self, cmbCurrent_Layer)
        QGIS_items.clear_and_populate_combo_box(self, cmbTarget_layer)

        
        # Access the variables through the instance
        save_button.clicked.connect(lambda: SetupCadastralLayers.on_save_button_clicked(
                                                                    self, widget, cmbCurrent_Layer, cmbTarget_layer, 
                                                                    lblcurrent_main_layer_label,
                                                                    lblnewCadastrals_input_layer_label,
                                                                    lblSHPNewItems))
        cancel_button.clicked.connect(lambda: SetupCadastralLayers.on_cancel_button_clicked(self, widget))
        
        

    def on_save_button_clicked(self, widget, cmbCurrent_Layer, cmbTarget_layer,lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems):
        # Handle logic when the save button is clicked
        SettingsDataSaveAndLoad.on_save_button_clicked_cadastrals(self, cmbCurrent_Layer, cmbTarget_layer)
        lblLayerProjects_Properties = self.lblLayerProjects_Properties # pylint: disable=no-member
        SettingsDataSaveAndLoad.startup_label_loader(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, lblLayerProjects_Properties)
        text = "Kõik sai salvestatud"
        heading = pealkiri.tubli
        QMessageBox.information(widget, heading, text)
        # Additional logic if needed

        widget.accept()  # Close the dialog

    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.informationSimple
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
        current_label = self.lblCurrentLayer # pylint: disable=no-member
        #Mailabl_Project_Label = self.lblSHPNewItems_2
        load = SettingsDataSaveAndLoad()
        load.startup_label_loader(current_label)
        

class Setup_ProjectLayers:
    def load_project_settings_widget(self):
        
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().projects_setup_ui)
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
        lblLayerProjects_Properties = self.lblLayerProjects_Properties # pylint: disable=no-member
        lblcurrent_main_layer_label = self.lblcurrent_main_layer_label # pylint: disable=no-member
        lblnewCadastrals_input_layer_label = self.lblnewCadastrals_input_layer_label # pylint: disable=no-member
        lblSHPNewItems = self.lblSHPNewItems # pylint: disable=no-member
        
        SettingsDataSaveAndLoad.on_save_button_clicked_projects(self, cmb_layers)
        SettingsDataSaveAndLoad.startup_label_loader(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, lblLayerProjects_Properties)        
        text = edu.salvestatud
        heading = pealkiri.tubli
        QMessageBox.information(widget, heading, text)
        # Additional logic if needed

        widget.accept()  # Close the dialog

    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        QMessageBox.information(widget, heading, text)
        widget.reject()  # Close the dialog        

