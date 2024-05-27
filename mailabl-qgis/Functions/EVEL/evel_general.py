from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5.uic import loadUi
from ...config.settings import Filepaths
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
#from .evel_easements import LayerFunctions

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()


class EvelLayerNames:
    EASEMENT = "evel_Servituut"
    WATER = "evel_Vesi"
    SEWAGE = "evel_Kanal"

class EvelGroupLayers:
    EVEL_MAIN = 'EVEL_Mudel'
    EASEMENT = 'Servituut'

    @staticmethod
    def create_EVEL_group_layer(sub_group_layer_name=None):
        from qgis.core import QgsProject
        # Get the main group layer name and sub-group layer name
        main_group_layer_name = EvelGroupLayers.EVEL_MAIN
        # Get the root of the layer tree
        root = QgsProject.instance().layerTreeRoot()
        # Find or create the main group layer and insert it at the top
        main_group = root.findGroup(main_group_layer_name)
        if main_group is None:
            main_group = root.insertGroup(0, main_group_layer_name)
        else:
            pass
        # Find or create the sub-group layer within the main group
        if sub_group_layer_name is None:
            return
        sub_group = main_group.findGroup(sub_group_layer_name)
        if sub_group is None:
            main_group.addGroup(sub_group_layer_name)


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
        pushbutton = self.widget_EVEL.pbGenerateVrtLayer
        checkbox = self.widget_EVEL.cbEasements
                # Initial state based on the checkbox
        pushbutton.setEnabled(checkbox.isChecked())

        # Connect checkbox state change to the method
        checkbox.stateChanged.connect(lambda: EVELTools.update_button_state)
        
            

        save_button.clicked.connect(lambda:EVELTools().on_save_button_clicked)
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

    def update_button_state(self):
        checkbox = self.widget_EVEL.cbEasements
        pushbutton = self.widget_EVEL.pbGenerateLayers
        pushbutton.setEnabled(checkbox.isChecked())


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
            water_checkbox: None,
            sewage_checkbox: None,
            rainwater_checkbox: None,
            pumpstation_checkbox: None,
            treatment_checkbox: None,
            connectionpoint_checkbox: None,
            easement_checkbox: None,
            services_checkbox: None,
            snconstant_checkbox: None,
            }

        # Define lambdas to connect checkboxes to functions (to be implemented)
        checkbox_functions = {
            water_checkbox: lambda: cbMapSelectors.selectWater_pipes(widget, water_checkbox),
            sewage_checkbox: None,
            rainwater_checkbox: None,
            pumpstation_checkbox: None,
            treatment_checkbox: None,
            connectionpoint_checkbox: None,
            easement_checkbox: None,
            services_checkbox: None,
            snconstant_checkbox: None,
        }

        # Create checkboxes_info dictionary
        checkboxes_info = {}
        for checkbox, text in checkbox_texts.items():
            if checkbox:
                checkboxes_info[checkbox] = (text, checkbox_functions.get(checkbox))

        return checkboxes_info