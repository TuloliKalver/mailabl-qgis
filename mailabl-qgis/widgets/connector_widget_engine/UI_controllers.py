
from PyQt5.uic import loadUi
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from ...utils.table_utilys import TableExtractor
from ...queries.python.projects_pandas import TableHeaders
from ...config.settings import Filepaths, SettingsDataSaveAndLoad, FilesByNames
from ...processes.infomessages.messages import Headings, HoiatusTexts, EdukuseTexts


class PropertiesConnector(QObject):
    ConnectorWidgetClosed = pyqtSignal()

    def __init__(self, table):
        super().__init__()  # Call the __init__ method of the QObject superclass
        self.table = table
        self.widget = None
        self.SelectionTools = None


    def load_propertiesconnector_widget_ui(self, module):
        widget_file = FilesByNames().add_properties_to_module_ui
        ui_file_path = Filepaths.get_widget(widget_file)
        widget = loadUi(ui_file_path)
        widget.show()
        self.widget = widget
        #button_save = widget.pbSave
        #button_cancel = widget.pbCancel
        widget.show()
        PropertiesConnector.button_controller(self, widget)

        widget.closeEvent = self.closeEvent

    def closeEvent(self, event):
        self.widget.close()
        event.accept()  # Allow the window to close
        self.ConnectorWidgetClosed.emit()

    def on_cancel_button_clicked(self, widget):
        if widget is not None:
            widget.reject()
            self.ConnectorWidgetClosed.emit()

    def on_save_button_clicked(self, widget):
        if widget is not None:
            widget.accept()
            self.ConnectorWidgetClosed.emit()



    def button_controller(self, widget):

        button_save = getattr(widget, 'pbSave', None)
        button_cancel = getattr(widget, 'pbCancel', None)
        button_clear_model_data = getattr(widget, 'pbClear_list', None)

        # Define lambdas to connect buttons to functions
        button_functions = {
            button_save: lambda: PropertiesConnector.on_save_button_clicked(self, widget),
            button_cancel: lambda: PropertiesConnector.on_cancel_button_clicked(self, widget),
            button_clear_model_data: None
        }
        
       # Connect buttons to functions
        for button, function in button_functions.items():
            PropertiesConnector.connect_button(button, function)

    @staticmethod
    def connect_button(button, function):
        # Check if button and function are assigned
        if button is not None and function is not None:
            # Connect button to function
            button.clicked.connect(function)
        elif button is not None:
            # Disable button if no function assigned
            button.setEnabled(False)


class WidgetLabels:
    def widget_elements(widget):
        label_descripton = widget.lblDescription
        lable_element_name = widget.lblElementName
        label_element_number = widget.lblElementNumber


class ConnectorFunctions:

    def ConnectProperties(id_value):
    
            #table_view = widget.tvProperties
        #button_clear_model_data = widget.pbClear_list
        #label_descripton = widget.lblDescription
        #lable_element_name = widget.lblElementName
        #label_element_number = widget.lblElementNumber
        #label_element_number.hide()
        #use if needed 
        #label_element_number.show()
        
        #input_headers = TableExtractor.table_header_extractor(self.table)
        #module_headers = TableHeaders()
        #id_column_index = input_headers.index(module_headers.header_id)
        #name_colum_index = input_headers.index(module_headers.header_name)
        #number_column_index = input_headers.index(module_headers.header_number)

        #indexes = [number_column_index, name_colum_index]
        #object_heading = TableExtractor.values_from_selected_row_by_columns(self.table, indexes)
        #lable_element_name.setText(object_heading)
        #id_value = TableExtractor.value_from_selected_row_by_column(self.table, 0)


        pass


