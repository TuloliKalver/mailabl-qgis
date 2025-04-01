from ...KeelelisedMuutujad.modules import Module
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

class SetupConrtacts:
    def load_contract_settings_widget(self):
        module = Module.CONTRACT
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().contracts_setup_ui)
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        widget = loadUi(ui_file_path)
        save_button = widget.pbSave
        cancel_button = widget.pbCancel

        widget.show()

        statuses_combo_box = widget.cmbPreferredContractStatuses
        combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            module=module,
            context=self,
            preferred_items=False
        )

        types_combo_box = widget.cbcb_PreferredContractTypes
        combo_handler.populate_comboBox_smart(
            comboBox=types_combo_box,
            module=module,
            context=self,
            preferred_items=True
        )

        # Connect signals to functions
        save_button.clicked.connect(lambda: SetupConrtacts.on_save_button_clicked(self, widget, statuses_combo_box, types_combo_box))
        cancel_button.clicked.connect(lambda: SetupConrtacts.on_cancel_button_clicked(self, widget))
    def on_save_button_clicked(self, widget, statuses_combo_box, combo_box_checkable):
        # Handle logic when the save button is clicked

        status_value_name = GetValuesFromComboBox._get_selected_status_name_from_combobox(statuses_combo_box)
        status_value_ids = GetValuesFromComboBox._get_selected_status_id_from_combobox(statuses_combo_box)
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
        ModernMessageDialog.Info_messages_modern(heading, text)
        # Additional logic if needed

        widget.accept()  # Close the dialog

    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked

        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        ModernMessageDialog.Info_messages_modern(heading, text)
        widget.reject()  # Close the dialog       