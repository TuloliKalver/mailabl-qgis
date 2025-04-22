from ...config.QGISSettingPaths import SettingsLoader, UserSettings
from ...config.mainwidget import WidgetInfo
from ...config.settings import Filepaths, FilesByNames, SettingsDataSaveAndLoad
from ...utils.ComboboxHelper import GetValuesFromComboBox
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog

from PyQt5.uic import loadUi


pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()


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

        page_name = GetValuesFromComboBox._get_selected_status_name_from_combobox(combobox)
        selected_index = WidgetInfo.get_selected_index(combobox)

        SettingsDataSaveAndLoad.save_user_prefered_startpage(self,selected_index, page_name)
        print(f"Nimetus: {page_name}")
        print(f"selected_index: {selected_index}")
        label = self.lblSPreferedHomeValue

        label.setText(page_name)

        text = edu.salvestatud
        heading = pealkiri.tubli
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
        # Additional logic if needed
        print("saved")
        widget.accept()  # Close the dialog
    def on_cancel_button_clicked(self, widget):
        # Handle logic when the cancel button is clicked

        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
        widget.reject()  # Close the dialog       