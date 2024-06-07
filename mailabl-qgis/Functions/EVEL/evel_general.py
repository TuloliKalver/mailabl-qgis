from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi
from ...config.settings import Filepaths
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from .evel_common import EvelGroupLayers, EVEL_Creator
from .evel_easements import LayerFunctions

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
        self.widget_EVEL = loadUi(ui_file_path)  # Use self.widget_EVEL here
        save_button = self.widget_EVEL.pbSave
        cancel_button = self.widget_EVEL.pbCancel

        self.widget_EVEL.show()
        EvelGroupLayers.create_EVEL_group_layer()
        EVELCheckboxes.get_checkbox_info(self.widget_EVEL)
        pushbutton = self.widget_EVEL.pbGenerateVrtLayer
        checkbox = self.widget_EVEL.cbEasements

        # Initial state based on the checkbox
        pushbutton.setEnabled(checkbox.isChecked())

        # Connect checkbox state change to the method
        #checkbox.stateChanged.connect(lambda: EVELTools.update_button_state)

        save_button.clicked.connect(lambda: EVELTools().on_save_button_clicked)
        cancel_button.clicked.connect(lambda: EVELTools().on_cancel_button_clicked)

        # Connect closeEvent method to handle window close event
        self.widget_EVEL.closeEvent = self.closeEvent

    def closeEvent(self, event):
        event.accept()  # Allow the window to close
        self.widgetClosed.emit()

    def on_save_button_clicked(self):
        self.widget_EVEL.accept()
        self.widgetClosed.emit()

    def on_cancel_button_clicked(self):
        self.widget_EVEL.reject()
        self.widgetClosed.emit()

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

        # Define texts for checkboxes
        checkbox_texts = {
            water_checkbox: "Vesi",
            sewage_checkbox: "Reoveekanal",
            rainwater_checkbox: "Sademevesi",
            pumpstation_checkbox: "Reoveepumpla",
            treatment_checkbox: "Reoveepuhasti",
            connectionpoint_checkbox: "Liitumispunktid",
            easement_checkbox: "Servtuudid",
            services_checkbox: "Töökäsud",
            snconstant_checkbox: "SN_CONSTANT",
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
