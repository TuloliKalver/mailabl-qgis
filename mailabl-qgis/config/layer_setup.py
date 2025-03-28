# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module,import-error


# Related Third-Party Imports
import re
from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtWidgets import QMessageBox, QFrame
from PyQt5.QtWidgets import  QListView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

# Local Application or Library Imports
from ..KeelelisedMuutujad.modules import Modules
from .settings import Filepaths, SettingsDataSaveAndLoad, FilesByNames
from .QGISSettingPaths import LayerSettings, SettingsLoader, UserSettings
from ..app.ComboBoxTools import ComboBoxTools
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ..queries.python.Statuses.statusManager import InsertStatusToComboBox
from ..queries.python.Types_Tags.type_tag_manager import InsertTypesToComboBox
from ..config.mainwidget import WidgetInfo


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
        
        QGIS_items.clear_and_add_layerNames(self, cmbCurrent_Layer)
        QGIS_items.clear_and_add_layerNames(self, cmbTarget_layer)

        
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
        lblProjectsFolder_location = self.lblProjectsFolder_location 
        lblProjectsTargetFolder_location = self.lblProjectsTargetFolder_location
        lbl_preferred_project_status = self.lbl_preferred_project_status
        lbl_preferred_contract_status = self.lbl_preferred_contract_status
        lblPreferredContractsTypes_value = self.lblPreferredContractsTypes_value

        SettingsDataSaveAndLoad.startup_label_loader(self, lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,
                                                     lblSHPNewItems, lblLayerProjects_Properties, lblProjectsFolder_location, 
                                                     lblProjectsTargetFolder_location, lbl_preferred_project_status, lbl_preferred_contract_status, lblPreferredContractsTypes_value)
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
    
    def clear_and_add_layerNames(self, combo_box):
        combo_box.clear()
        layer_names = QGIS_items.get_sorted_layer_names(self)
        combo_box.addItems(layer_names)

    def clear_and_add_layerNames_selected(self, combo_box, layer_name):
        combo_box.clear()
        layer_names = QGIS_items.get_sorted_layer_names(self)
        combo_box.addItems(layer_names)   
        # Set the current text of the combo box to the layer name if it exists
        if layer_name:
            combo_box.setCurrentText(layer_name)

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
        


class Setup_ProjectLayers:
    def load_project_settings_widget(self):
        
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().projects_setup_ui)
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel
        
        widget.show()
        
        widget.lblPhtoslabel.setEnabled(False)
        widget.lePhotos.setEnabled(False)
        module = Modules.MODULE_PROJECTS
 
        cmb_layers  = widget.cmbProjects_Layer
        QGIS_items.clear_and_add_layerNames(self, cmb_layers)
 
        combo_box = widget.cmbPreferred_Project_status
        #QTimer.singleShot(500, lambda: Projects.load_Mailabl_projects_list(self, table))
        status_id = SettingsDataSaveAndLoad.load_projects_status_id(self)
        if status_id is None or '':
            InsertStatusToComboBox.add_statuses_to_listview(self, combo_box, module)
        else:
           InsertStatusToComboBox.add_statuses_to_combobox_and_set_preferes_status(self, combo_box, module, status_id)

        copy_folder_path = SettingsDataSaveAndLoad.load_projcets_copy_folder_path_value(self)
        if copy_folder_path:
            lblProjectsFolder_location = widget.leProjectsFolder_location
            lblProjectsFolder_location.setText(copy_folder_path)
                    
        target_folder_path = SettingsDataSaveAndLoad.load_target_Folder_path_value(self)
        if target_folder_path:
            lblProjectsTargetFolder_location = widget.leProjectsTargetFolder_location
            lblProjectsTargetFolder_location.setText(target_folder_path)

        folder_structure_text = SettingsDataSaveAndLoad.load_projects_prefered_folder_name_structure(self)
        if folder_structure_text:
            widget.lblPreferedFolderNamStructure.setText(folder_structure_text)
            combo_box_name = widget.cmbNameElements

            # Disable all items in the combo box
            for i in range(combo_box_name.count()):
                index = combo_box_name.model().index(i, 0)
                if index.isValid():
                    item = combo_box_name.model().itemFromIndex(index)
                    if item:
                        item.setEnabled(False)
                        done_icon_path = ":/qt-project.org/styles/commonstyle/images/standardbutton-apply-16.png"
                        icon = QIcon(done_icon_path)
                        item.setIcon(icon)

            # Check if all items are disabled
            all_disabled = all(not combo_box_name.model().item(i).isEnabled() for i in range(combo_box_name.count()))
            if all_disabled:
                widget.Confir_selecteded_element.setEnabled(False)  # Disable the button
                widget.Confir_selecteded_element.hide()
                
        line_edit_symbol = widget.leSymbolCharacter
        line_edit_symbol.setVisible(False)

      # Connect signal to function
        cmb_folder_name_optoins = widget.cmbNameElements
        cmb_folder_name_optoins.currentIndexChanged.connect(lambda index: Setup_ProjectLayers.checkSelectedId(index, widget))

        append_button = widget.Confir_selecteded_element
        append_button.clicked.connect(lambda: Setup_ProjectLayers.addSelectedItem(widget))

        reset_button = widget.pbResetFolderSetup
        reset_button.clicked.connect(lambda: Setup_ProjectLayers.reset_setup_of_folder_setup(widget))

        # Connect signals to functions
        save_button.clicked.connect(lambda: Setup_ProjectLayers.on_save_button_clicked(self, widget, cmb_layers, combo_box))
        cancel_button.clicked.connect(lambda: Setup_ProjectLayers.on_cancel_button_clicked(self, widget))



    def on_save_button_clicked(self, widget, cmb_layers, combo_box):
        # Handle logic when the save button is clicked
        lblLayerProjects_Properties = self.lblLayerProjects_Properties # pylint: disable=no-member
        lblcurrent_main_layer_label = self.lblcurrent_main_layer_label # pylint: disable=no-member
        lblnewCadastrals_input_layer_label = self.lblnewCadastrals_input_layer_label # pylint: disable=no-member
        project_status_label = self.lbl_preferred_project_status
        lblSHPNewItems = self.lblSHPNewItems # pylint: disable=no-member
        lblProjectsTargetFolder_location = self.lblProjectsTargetFolder_location
        lblProjectsFolder_location = self.lblProjectsFolder_location
        lbl_preferred_project_status = self.lbl_preferred_project_status
        input_value = widget.leProjectsFolder_location
        target_value = widget.leProjectsTargetFolder_location
        lbl_preferred_contract_status = self.lbl_preferred_contract_status
        lblPreferredContractsTypes_value = self.lblPreferredContractsTypes_value
        lblPreferredFolderName_structure = self.lblPreferredFolderName_structure
        


        status_value_id = InsertStatusToComboBox.get_selected_status_id(combo_box)
        status_value_name = InsertStatusToComboBox.get_selected_status_name(combo_box)
        SettingsDataSaveAndLoad.save_preferred_projects_status_id(self, status_value_id, status_value_name, project_status_label)
        prefered_folder_name_structure = widget.lblPreferedFolderNamStructure.text()
        SettingsDataSaveAndLoad.save_projects_folder_preferred_name_structure(self, prefered_folder_name_structure)
        lblPreferredFolderName_structure.setText(prefered_folder_name_structure)
        SettingsDataSaveAndLoad.on_save_button_clicked_projects(self, cmb_layers, lblProjectsTargetFolder_location, 
                                                                lblProjectsFolder_location, target_value, 
                                                                input_value)
        SettingsDataSaveAndLoad.startup_label_loader(self,lblcurrent_main_layer_label,lblnewCadastrals_input_layer_label,lblSHPNewItems, 
                              lblLayerProjects_Properties, lblProjectsFolder_location, lblProjectsTargetFolder_location,
                              lbl_preferred_project_status, lbl_preferred_contract_status, 
                              lblPreferredContractsTypes_value)        
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

    def addSelectedItem(widget):
        combo_box_name = widget.cmbNameElements
        label_prefered_name = widget.lblPreferedFolderNamStructure
        label_symbol = widget.leSymbolCharacter

        selected_item = combo_box_name.currentText()
        if selected_item:
            # Check if the button was clicked and the index is 1
            if widget.Confir_selecteded_element.isEnabled() and combo_box_name.currentIndex() == 1:
                label_text = label_prefered_name.text()
                symbol_text = label_symbol.text()
                label_symbol.setStyleSheet("border: None")
                if symbol_text == '' or None:
                    label_symbol.setStyleSheet("border: 1px solid #D32F2F;")
                    QMessageBox.warning(widget, pealkiri.warningSimple, sisu.puudulikud_andmed)
                    return
                # Check if the symbol_text contains disallowed characters
                if re.search(r'[<>:"/\\|?*.]', symbol_text):
                    # Display warning message
                    label_symbol.setStyleSheet("border: 1px solid #D32F2F;")
                    QMessageBox.warning(widget, pealkiri.warningSimple, sisu.korrigeeri_sümbolit)
                    return
                else:
                    # Add selected item to label with or without parentheses
                    label_symbol.setStyleSheet("border: None")
                    if label_text:
                        label_prefered_name.setText(f"{label_text} + {selected_item}({symbol_text})")
                    else:
                        label_prefered_name.setText(f"{selected_item}({symbol_text})")
                    # Hide symbol line edit
                    label_symbol.hide()
            else:
                # Hide symbol line edit and set border to None
                label_symbol.clear()
                label_symbol.hide()

                # Add selected item to label without parentheses
                label_text = label_prefered_name.text()
                if label_text:
                    current_text = f"{label_text} + {selected_item}"
                else:
                    current_text = selected_item
                label_prefered_name.setText(current_text)

            # Disable selected item in combobox
            index = combo_box_name.findText(selected_item)
            if index != -1:
                item = combo_box_name.model().item(index)
                item.setEnabled(False)

                # Set icon for the disabled item
                done_icon_path = ":/qt-project.org/styles/commonstyle/images/standardbutton-apply-16.png"
                icon = QIcon(done_icon_path)
                item.setIcon(icon)

            # Reset combobox to index -1
            combo_box_name.setCurrentIndex(-1)

            # Check if all items are disabled
            all_disabled = all(not combo_box_name.model().item(i).isEnabled() for i in range(combo_box_name.count()))
            if all_disabled:
                widget.Confir_selecteded_element.setEnabled(False)  # Disable the button
                widget.Confir_selecteded_element.hide()



    def reset_setup_of_folder_setup(widget):
        # Clear the label text
        widget.lblPreferedFolderNamStructure.clear()

        # Enable all items in the combo box
        combo_box_name = widget.cmbNameElements
        for i in range(combo_box_name.count()):
            index = combo_box_name.model().index(i, 0)
            if index.isValid():
                item = combo_box_name.model().itemFromIndex(index)
                if item:
                    item.setEnabled(True)
                    # Clear the icon
                    item.setIcon(QIcon())

        # Show and enable the hidden button
        widget.Confir_selecteded_element.setEnabled(True)
        widget.Confir_selecteded_element.show()


    def checkSelectedId(index, widget):
        # Check if the selected item has id 1
        line_edit = widget.leSymbolCharacter
        line_edit.setStyleSheet("border: None")
        line_edit.clear()
        if index != -1:
            #selected_id = widget.cmbProjects_Layer.itemData(index)
            if index == 1:
                line_edit.setVisible(True)

            else:
                line_edit.setVisible(False)



class Setup_Conrtacts:
    def load_contract_settings_widget(self):
        
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().contracts_setup_ui)
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel
        
        widget.show()

        module = Modules.MODULE_CONTRACTS
        statuses_combo_box = widget.cmbPreferredContractStatuses
        types_combo_box = widget.cbcb_PreferredContractTypes
        # Assuming types_combo_box is an instance of QgsSelectableComboBox

        status_id = SettingsDataSaveAndLoad.load_contract_status_ids(self)
        if status_id is None or '':
            InsertStatusToComboBox.add_statuses_to_listview(self, statuses_combo_box, module)
        else:
            InsertStatusToComboBox.add_statuses_to_combobox_and_set_preferes_status(self, statuses_combo_box, module, status_id)

        #InsertStatusToComboBox.add_statuses_to_listview(self, statuses_combo_box, module )
        preferred_types = SettingsDataSaveAndLoad.load_contracts_type_names(self)
        
        InsertTypesToComboBox.add_elementTypes_to_listview(self, types_combo_box, preferred_types, module)

        # Connect signals to functions
        save_button.clicked.connect(lambda: Setup_Conrtacts.on_save_button_clicked(self, widget, statuses_combo_box, types_combo_box))
        cancel_button.clicked.connect(lambda: Setup_Conrtacts.on_cancel_button_clicked(self, widget))

    def on_save_button_clicked(self, widget, statuses_combo_box, combo_box_checkable):
        # Handle logic when the save button is clicked
  
        status_value_name = InsertStatusToComboBox.get_selected_status_name(statuses_combo_box)
        status_value_ids = InsertStatusToComboBox.get_selected_status_id(statuses_combo_box)
        checked_indexes = combo_box_checkable.checkedItemsData()
        print(checked_indexes)
        selected_types = combo_box_checkable.checkedItems()

        selected_types_text = ''
        for i, item in enumerate(selected_types):
            if i % 1 == 0 and i > 0:
                selected_types_text += ',\n'
            elif i > 0:
                selected_types_text += ', '
            selected_types_text += item
        label = self.lblPreferredContractsTypes_value
        label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label.setAlignment(Qt.AlignBottom | Qt.AlignLeft)



        SettingsDataSaveAndLoad.save_contract_settings(self, selected_types_text, status_value_name, status_value_ids)

        label.setText(selected_types_text)
        self.lbl_preferred_contract_status.setText(status_value_name)

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


class SetupEasments:
    def load_easements_settings_widget(self):
        
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().easements_setup_ui)
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel
        
        widget.show()

        module = Modules.MODULE_EASEMENTS
        statuses_combo_box = widget.cmbPreferredEasementStatuses
        types_combo_box = widget.cbcb_PreferredEasementTypes
        water_cb = widget.cbWater_Pipes
        sewer_cb = widget.cbSewer_pipes
        sewer_pressure_cb = widget.cbSewer_Pressure_pipes
        drainage_cb = widget.cbDrainage_Pipes

        water_layer_name = SettingsLoader.get_setting(LayerSettings.WATER_LAYER)
        sewer_layer_name = SettingsLoader.get_setting(LayerSettings.SEWER_LAYER)
        pressure_sewer_layer_name = SettingsLoader.get_setting(LayerSettings.PRESSURE_SEWER_LAYER)
        drainage_layer_name = SettingsLoader.get_setting(LayerSettings.DRAINAGE_LAYER)


        QGIS_items.clear_and_add_layerNames_selected(self, water_cb, water_layer_name)
        QGIS_items.clear_and_add_layerNames_selected(self, sewer_cb, sewer_layer_name)
        QGIS_items.clear_and_add_layerNames_selected(self, sewer_pressure_cb, pressure_sewer_layer_name)
        QGIS_items.clear_and_add_layerNames_selected(self, drainage_cb, drainage_layer_name)

        # Assuming types_combo_box is an instance of QgsSelectableComboBox

        status_id = SettingsDataSaveAndLoad.load_easements_status_ids(self)
        if status_id is None or '':
            InsertStatusToComboBox.add_statuses_to_listview(self, statuses_combo_box, module)
        else:
            InsertStatusToComboBox.add_statuses_to_combobox_and_set_preferes_status(self, statuses_combo_box, module, status_id)

        preferred_types = SettingsDataSaveAndLoad.load_easements_type_names(self)
        
        InsertTypesToComboBox.add_elementTypes_to_listview(self, types_combo_box, preferred_types, module)

        # Connect signals to functions
        save_button.clicked.connect(lambda: SetupEasments.on_save_button_clicked(self, widget, statuses_combo_box, types_combo_box, water_cb, sewer_cb, sewer_pressure_cb, drainage_cb))
        cancel_button.clicked.connect(lambda: SetupEasments.on_cancel_button_clicked(self, widget))

    def on_save_button_clicked(self, widget, statuses_combo_box, combo_box_checkable, water_cb, sewer_cb, sewer_pressure_cb, drainage_cb):
        # Handle logic when the save button is clicked

        water_layer_name = ComboBoxTools.get_selected_item_name(water_cb)
        sewer_layer_name = ComboBoxTools.get_selected_item_name(sewer_cb)
        pressure_sewer_layer_name = ComboBoxTools.get_selected_item_name(sewer_pressure_cb)
        drainage_layer_name = ComboBoxTools.get_selected_item_name(drainage_cb)

        SettingsLoader.save_setting(LayerSettings().WATER_LAYER,water_layer_name)
        SettingsLoader.save_setting(LayerSettings().SEWER_LAYER, sewer_layer_name)
        SettingsLoader.save_setting(LayerSettings().PRESSURE_SEWER_LAYER, pressure_sewer_layer_name)
        SettingsLoader.save_setting(LayerSettings().DRAINAGE_LAYER, drainage_layer_name)


        status_value_name = InsertStatusToComboBox.get_selected_status_name(statuses_combo_box)
        status_value_ids = InsertStatusToComboBox.get_selected_status_id(statuses_combo_box)
        checked_indexes = combo_box_checkable.checkedItemsData()
        #print(checked_indexes)
        selected_types = combo_box_checkable.checkedItems()

        selected_types_text = ''
        for i, item in enumerate(selected_types):
            if i % 1 == 0 and i > 0:
                selected_types_text += ',\n'
            elif i > 0:
                selected_types_text += ', '
            selected_types_text += item
        label = self.lblPreferredEasementsTypes_value
        label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label.setAlignment(Qt.AlignBottom | Qt.AlignLeft)



        water_layer_name = SettingsLoader.get_setting(LayerSettings().WATER_LAYER)
        sewer_layer_name = SettingsLoader.get_setting(LayerSettings().SEWER_LAYER)
        pressure_sewer_layer_name = SettingsLoader.get_setting(LayerSettings().PRESSURE_SEWER_LAYER)
        drainage_layer_name = SettingsLoader.get_setting(LayerSettings().DRAINAGE_LAYER)
        

        SettingsDataSaveAndLoad.save_easements_settings(self, selected_types_text, status_value_name, status_value_ids)



        label.setText(selected_types_text)
        self.lblPreferredEasementsStatus.setText(status_value_name)
        self.lblWaterPipesValue.setText(water_layer_name)
        self.lblSewerPipesValue.setText(sewer_layer_name)
        self.lblPrSewagePipesValue.setText(pressure_sewer_layer_name)
        self.lblDrainagePipesValue.setText(drainage_layer_name)

        text = edu.salvestatud
        heading = pealkiri.tubli
        QMessageBox.information(widget, heading, text)
        # Additional logic if needed
        print("saved")

        widget.accept()  # Close the dialog


    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked

        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        QMessageBox.information(widget, heading, text)
        widget.reject()  # Close the dialog       

class SetupUsers:
    def load_user_settings_widget(self):
        
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().user_setup_ui)
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel
        combobox = widget.cmbUserMain

        stackedwidget = self.swWorkSpace

        items = WidgetInfo.get_stacked_widget_info(stackedwidget)
        #print(f"items: {items}")
        id = SettingsDataSaveAndLoad.load_user_prefered_startpage_index(self)
        WidgetInfo.create_visible_name_dropdown(items, combobox, id)


        widget.show()

        
        prefered_homepage = SettingsLoader.get_setting(UserSettings.USER_PREFERRED_PAGE)
        print(f"Load surer page: {prefered_homepage}")     
        
        # Connect signals to functions
        save_button.clicked.connect(lambda: SetupUsers.on_save_button_clicked(self, widget, combobox))
        cancel_button.clicked.connect(lambda: SetupUsers.on_cancel_button_clicked(self, widget))

    def on_save_button_clicked(self, widget, combobox):

        page_name = InsertStatusToComboBox.get_selected_status_name(combobox)
        selected_index = WidgetInfo.get_selected_index(combobox)
        
        SettingsDataSaveAndLoad.save_user_prefered_startpage(self,selected_index, page_name)
        print(f"Nimetus: {page_name}")
        print(f"selected_index: {selected_index}")
        label = self.lblSettings_preferedHomePage

        label.setText(page_name)
        
        text = edu.salvestatud
        heading = pealkiri.tubli
        QMessageBox.information(widget, heading, text)
        # Additional logic if needed
        print("saved")
        widget.accept()  # Close the dialog


    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked

        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        QMessageBox.information(widget, heading, text)
        widget.reject()  # Close the dialog       
