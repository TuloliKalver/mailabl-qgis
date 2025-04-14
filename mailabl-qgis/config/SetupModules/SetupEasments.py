from ...KeelelisedMuutujad.modules import Module
from ...app.ComboBoxTools import ComboBoxTools
from ...config.QGISSettingPaths import LayerSettings, SettingsLoader
from ...config.SetupModules.SetupMainLayers import QGIS_items
from ...config.settings import Filepaths, FilesByNames, SettingsDataSaveAndLoad
from ...utils.ComboboxHelper import GetValuesFromComboBox
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()


class SetupEasments:
    def load_easements_settings_widget(self):

        ui_file_path = Filepaths.get_conf_widget(FilesByNames().easements_setup_ui)
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel

        widget.show()

        module = Module.EASEMENT
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

        # Populate the combo boxes using the populate_comboBox_smart method for statuses
        statuses_combo_box = widget.cmbPreferredEasementStatuses
        combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            module=module,
            context=self,
            preferred_items=False
        )

        # Populate the combo boxes using the populate_comboBox_smart method for types
        types_combo_box = widget.cbcb_PreferredEasementTypes
        combo_handler.populate_comboBox_smart(
            comboBox=types_combo_box,
            module=module,
            context=self,
            preferred_items=True
        )

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


        status_value_name = GetValuesFromComboBox._get_selected_status_name_from_combobox(statuses_combo_box)
        status_value_ids = GetValuesFromComboBox._get_selected_status_id_from_combobox(statuses_combo_box)
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
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)

        # Additional logic if needed
        print("saved")

        widget.accept()  # Close the dialog
    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked

        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
        widget.reject()  # Close the dialog       