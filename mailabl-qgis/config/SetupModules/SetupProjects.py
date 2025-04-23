from ...KeelelisedMuutujad.modules import Module
from ...config.SetupModules.SetupMainLayers import QGIS_items
from ...config.settings import Filepaths, FilesByNames, SettingsDataSaveAndLoad
from ...utils.ComboboxHelper import GetValuesFromComboBox
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog

from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi


import re


pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()


class SetupProjects:
    def load_project_settings_widget(self):
        module = Module.PROJECT
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().projects_setup_ui)
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel

        widget.show()

        widget.lblPhtoslabel.setEnabled(False)
        widget.lePhotos.setEnabled(False)

        cmb_layers  = widget.cmbProjects_Layer
        QGIS_items.clear_and_add_layerNames(cmb_layers)

        statuses_combo_box = widget.cmbPreferred_Project_status
        combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            module=module,
            context=self,
            preferred_items=True
        )

        copy_folder_path = SettingsDataSaveAndLoad.load_projcets_copy_folder_path_value(self)
        if copy_folder_path:
            lblProjectsFolderValue = widget.leProjectsFolder_location
            lblProjectsFolderValue.setText(copy_folder_path)

        target_folder_path = SettingsDataSaveAndLoad.load_target_Folder_path_value(self)
        if target_folder_path:
            lblProjectsTargetFolderValue = widget.leProjectsTargetFolder_location
            lblProjectsTargetFolderValue.setText(target_folder_path)

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
        cmb_folder_name_optoins.currentIndexChanged.connect(lambda index: SetupProjects.checkSelectedId(index, widget))

        append_button = widget.Confir_selecteded_element
        append_button.clicked.connect(lambda: SetupProjects.addSelectedItem(widget))

        reset_button = widget.pbResetFolderSetup
        reset_button.clicked.connect(lambda: SetupProjects.reset_setup_of_folder_setup(widget))

        # Connect signals to functions
        save_button.clicked.connect(lambda: SetupProjects.on_save_button_clicked(self, widget, cmb_layers, statuses_combo_box))
        cancel_button.clicked.connect(lambda: SetupProjects.on_cancel_button_clicked(self, widget))
    def on_save_button_clicked(self, widget, cmb_layers, combo_box):
        # Handle logic when the save button is clicked
        lblLayerProjectsValue = self.lblLayerProjectsValue # pylint: disable=no-member
        lblMainLayerValue = self.lblMainLayerValue # pylint: disable=no-member
        lblMainTargetLayerValue = self.lblMainTargetLayerValue # pylint: disable=no-member
        project_status_label = self.lblPreferredProjectStatusValue
        lblSHPLayerValue = self.lblSHPLayerValue # pylint: disable=no-member
        lblProjectsTargetFolderValue = self.lblProjectsTargetFolderValue
        lblProjectsFolderValue = self.lblProjectsFolderValue
        lblPreferredProjectStatusValue = self.lblPreferredProjectStatusValue
        input_value = widget.leProjectsFolder_location
        target_value = widget.leProjectsTargetFolder_location
        lblPreferredContractStatusValue = self.lblPreferredContractStatusValue
        lblPreferredContractsTypesValue = self.lblPreferredContractsTypesValue
        lblPreferredFolderNameValue = self.lblPreferredFolderNameValue



        status_value_id = GetValuesFromComboBox._get_selected_status_id_from_combobox(combo_box)
        status_value_name = GetValuesFromComboBox._get_selected_status_name_from_combobox(combo_box)
        SettingsDataSaveAndLoad.save_preferred_projects_status_id(self, status_value_id, status_value_name, project_status_label)
        prefered_folder_name_structure = widget.lblPreferedFolderNamStructure.text()
        SettingsDataSaveAndLoad.save_projects_folder_preferred_name_structure(self, prefered_folder_name_structure)
        lblPreferredFolderNameValue.setText(prefered_folder_name_structure)
        SettingsDataSaveAndLoad.on_save_button_clicked_projects(self, cmb_layers, lblProjectsTargetFolderValue,
                                                                lblProjectsFolderValue, target_value,
                                                                input_value)
        SettingsDataSaveAndLoad.startup_label_loader(self,lblMainLayerValue,lblMainTargetLayerValue,lblSHPLayerValue,
                              lblLayerProjectsValue, lblProjectsFolderValue, lblProjectsTargetFolderValue,
                              lblPreferredProjectStatusValue, lblPreferredContractStatusValue,
                              lblPreferredContractsTypesValue)
        text = edu.salvestatud
        heading = pealkiri.tubli
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
        # Additional logic if needed

        widget.accept()  # Close the dialog
    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
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
                    heading = Headings.warningSimple
                    text = sisu.puudulikud_andmed
                    ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
                    return
                                    # Check if the symbol_text contains disallowed characters
                if re.search(r'[<>:"/\\|?*.]', symbol_text):
                    # Display warning message
                    label_symbol.setStyleSheet("border: 1px solid #D32F2F;")
                    pealkiri=Headings.warningSimple
                    text=sisu.korrigeeri_sümbolit
                    ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
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