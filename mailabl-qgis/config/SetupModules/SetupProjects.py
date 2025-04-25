import re
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.uic import loadUi
from types import MethodType
from PyQt5.QtWidgets import (
    QDialog, QFrame
    )
from PyQt5.QtGui import QIcon



from ...KeelelisedMuutujad.modules import Module
from ...config.SetupModules.SetupMainLayers import QGIS_items
from ...config.settings import Filepaths, FilesByNames, SettingsDataSaveAndLoad, StartupSettingsLoader
from ...utils.ComboboxHelper import GetValuesFromComboBox
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog
from ...app.MainMenuController import SetupController
from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...config.settings_new import PluginSettings


pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()


class SetupProjects:
    def __init__(self, parent) -> None:
        self.dialog = parent
    def load_project_settings_widget(self):
        module = Module.PROJECT
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().projects_setup_ui)
        widget = loadUi(ui_file_path)

        widget.lblTitle.setText("Servituutide mooduli seadistamine...")

        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)

        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        SetupProjects.replace_frame(
            widget, 
            "FrameMain", 
            lambda parent: AnimatedGradientBorderFrame(parent,
                                                        style=AnimatedGradientBorderFrame.MODERN)
        )

        # 🔄 Promote dragFrame to custom draggable logic
        drag_frame = widget.dragFrame
        if drag_frame:
            # Inject drag behavior via method patching
            drag_frame.mousePressEvent = MethodType(DraggableFrame.mousePressEvent, drag_frame)
            drag_frame.mouseMoveEvent = MethodType(DraggableFrame.mouseMoveEvent, drag_frame)
            drag_frame._drag_pos = None
            drag_frame.setCursor(Qt.OpenHandCursor)

        save_button = widget.pbSave
        cancel_button = widget.pbCancel
        lblProjectsFolderValue = widget.leProjectsFolder_location
        lblProjectsTargetFolderValue = widget.leProjectsTargetFolder_location

        widget.lblPhtoslabel.setEnabled(False)
        widget.lePhotos.setEnabled(False)


        projects_layer_name = PluginSettings.load_setting(
            module=Module.PROJECT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.PROJECTS_LAYER
        )

        cmb_layers  = widget.cmbProjects_Layer
        QGIS_items.clear_and_add_layerNames_selected(cmb_layers, projects_layer_name)


        statuses_combo_box = widget.cmbPreferred_Project_status
        combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            module=module,
            context=self,
            preferred_items=False
        )

        copy_folder_path = SettingsDataSaveAndLoad.load_projcets_copy_folder_path_value(self)
        if copy_folder_path:
            lblProjectsFolderValue.setText(copy_folder_path)

        target_folder_path = SettingsDataSaveAndLoad.load_target_Folder_path_value(self)
        if target_folder_path:
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
        save_button.clicked.connect(lambda: SetupProjects._handle_save(widget))
        cancel_button.clicked.connect(lambda: SetupProjects._handle_cancel(widget))

        result = widget.exec_()
        if result == QDialog.Accepted:


            status_ids = GetValuesFromComboBox._get_selected_id_from_combobox(statuses_combo_box)
            status_name = GetValuesFromComboBox._get_selected_name_from_combobox(statuses_combo_box)
            layer_name = GetValuesFromComboBox._get_selected_name_from_combobox(cmb_layers)

            prefered_folder_name_structure = widget.lblPreferedFolderNamStructure.text()
            SettingsDataSaveAndLoad.save_projects_folder_preferred_name_structure(self, prefered_folder_name_structure)
            #lblPreferredFolderNameValue.setText(prefered_folder_name_structure)
            
            copy_folder = widget.leProjectsFolder_location.text()
            target_folder = widget.leProjectsTargetFolder_location.text()
            
            SettingsDataSaveAndLoad.save_FolderValues(self,lblProjectsFolderValue, lblProjectsTargetFolderValue, copy_folder, target_folder)

            
            self.save_projects_settings(
                        status_name,
                        status_ids,
                        layer_name
                        )
            
            controller = SetupController(self.dialog)
            controller.check_all_modules()

            widget.setAttribute(Qt.WA_DeleteOnClose)
            text = edu.salvestatud
            heading = pealkiri.tubli
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
            # Additional logic if needed

            return True
        else:
            widget.setAttribute(Qt.WA_DeleteOnClose)
            return None

            
            
            
            
            
            


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



    def save_projects_settings(self,
                        status_name,
                        status_ids,
                        layer_name
                        ):
        module = Module.PROJECT
        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_IDs,
            value = status_ids
            )

        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            value = status_name
            )

        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.PROJECTS_LAYER,
            value = layer_name
        )

        StartupSettingsLoader.startup_label_loader(self)




    @staticmethod
    def replace_frame(widget, old_name: str, new_frame_cls: type, *args, **kwargs) -> QFrame:
        old = widget.findChild(QFrame, old_name)
        if old is None:
            raise ValueError(f"Could not find frame named '{old_name}'.")

        layout = old.parentWidget().layout()
        index = layout.indexOf(old)
        layout.removeWidget(old)
        old.deleteLater()

        new_frame = new_frame_cls(widget, *args, **kwargs)
        new_frame.setObjectName(old_name)
        new_frame.setLayout(old.layout())  # reuse inner layout if needed
        layout.insertWidget(index, new_frame)
        return new_frame



    @staticmethod
    def _handle_save(dialog):
        dialog.accept()

    @staticmethod
    def _handle_cancel(dialog):
        dialog.reject()


class DraggableFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._drag_pos = None
        self.setCursor(Qt.OpenHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self._drag_pos:
            self.window().move(event.globalPos() - self._drag_pos)
            event.accept()