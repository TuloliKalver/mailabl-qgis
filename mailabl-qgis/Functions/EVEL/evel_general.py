from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi
from ...config.settings import Filepaths
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...KeelelisedMuutujad.EVEL_lang_module import EvelGroupLayersNames
from .evel_common import EvelGroupLayers, EVEL_Creator, EVELCancel
from .LayerVariables.evel_easements import LayerFunctions

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()

class EVELTools(QObject):
    widgetClosed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.widget_EVEL = None

    def load_widget(self):
        ui_file_path = Filepaths.get_EVEL_tools()
        print(f"File path {ui_file_path}")
        widget_EVEL = loadUi(ui_file_path)  # Use self.widget_EVEL here
        save_button = widget_EVEL.pbSave
        cancel_button = widget_EVEL.pbCancel

        widget_EVEL.show()
        EvelGroupLayers.create_EVEL_group_layer()
        EVELCheckboxes.get_checkbox_info(widget_EVEL)
        pushbutton = widget_EVEL.pbGenerateVrtLayer
        checkbox = widget_EVEL.cbEasements

        # Initial state based on the checkbox
        pushbutton.setEnabled(checkbox.isChecked())

        # Connect checkbox state change to the method
        #checkbox.stateChanged.connect(lambda: EVELTools.update_button_state)

        save_button.clicked.connect(lambda: EVELTools.on_save_button_clicked(self, widget_EVEL))
        cancel_button.clicked.connect(lambda: EVELTools.on_cancel_button_clicked(self, widget_EVEL))

        # Connect closeEvent method to handle window close event
        widget_EVEL.closeEvent = self.closeEvent

    def closeEvent(self, event):
        group_layer = EvelGroupLayersNames.EVEL_MAIN
        EVELCancel.remove_group_and_contents(group_layer)
        event.accept()  # Allow the window to close
        
    def on_save_button_clicked(self, widget_EVEL):
        widget_EVEL.accept()
        
    def on_cancel_button_clicked(self, widget_EVEL):
        print("cancel button clicked")
        group_layer = EvelGroupLayersNames.EVEL_MAIN
        EVELCancel.remove_group_and_contents(group_layer)
        widget_EVEL.reject()
        

class EVELCheckboxes:
    def get_checkbox_info(widget):
        water_checkbox = getattr(widget, 'cbWater', None)
        sewage_checkbox = getattr(widget, 'cbSewage', None)
        rainwater_checkbox = getattr(widget, 'cbRainwater', None)
        pumpstation_checkbox = getattr(widget, 'cbPumpstation', None)
        treatment_checkbox = getattr(widget, 'cbSewTreatment', None)
        connectionpoint_checkbox = getattr(widget, 'cbConnectionPoints', None)
        easement_checkbox = getattr(widget, 'cbEasements', None)
        services_checkbox = getattr(widget, 'cbServices', None)
        snconstant_checkbox = getattr(widget, 'cbSNConstant', None)

        from ...KeelelisedMuutujad.EVEL_lang_module import UICheckboxes
        # Define texts for checkboxes

        checkbox_texts = {
            water_checkbox: UICheckboxes.water_checkbox,
            sewage_checkbox: UICheckboxes.sewage_checkbox,
            rainwater_checkbox: UICheckboxes.rainwater_checkbox,
            pumpstation_checkbox: UICheckboxes.pumpstation_checkbox,
            treatment_checkbox: UICheckboxes.treatment_checkbox,
            connectionpoint_checkbox: UICheckboxes.connectionpoint_checkbox,
            easement_checkbox: UICheckboxes.easement_checkbox,
            services_checkbox: UICheckboxes.services_checkbox,
            snconstant_checkbox: UICheckboxes.snconstant_checkbox,
        }

        from ...config.settings import FilesByNames
        easment_style_name = FilesByNames().easement_evelLayer
        from .evel_common import EvelGroupLayers, EvelLayerNames



        # Define lambdas to connect checkboxes to functions (to be implemented)
        checkbox_functions = {
            water_checkbox: None,  # lambda: widget.cbMapSelectors.selectWater_pipes(widget, water_checkbox),
            sewage_checkbox: None,
            rainwater_checkbox: None,
            pumpstation_checkbox: None,
            treatment_checkbox: None,
            connectionpoint_checkbox: None,
            easement_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(easement_checkbox,EvelGroupLayers.EASEMENT ,EvelLayerNames().EASEMENT, easment_style_name),
            services_checkbox: lambda: EVEL_Creator.generate_EVEL_model_layer(services_checkbox,EvelGroupLayers.SERVICES ,EvelLayerNames().SERVICES, easment_style_name),
            snconstant_checkbox: None,
        }

        # Create checkboxes_info dictionary
        checkboxes_info = {}
        for checkbox, text in checkbox_texts.items():
            if checkbox:
                checkboxes_info[checkbox] = (text, checkbox_functions.get(checkbox))
        EVELCheckboxes.update_checkboxes(checkboxes_info)
        return checkboxes_info

    @staticmethod
    def update_checkboxes(checkboxes_info):
        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                checkbox.setText(text)
                if connect_function is None:
                    checkbox.setEnabled(False)
                else:
                    checkbox.setEnabled(True)
                    checkbox.clicked.connect(connect_function)
