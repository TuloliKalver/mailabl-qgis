
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
        widget.show()
        table_view = widget.tvProperties
    
        input_headers, module_headers = WidgetLabels.widget_label_elements(widget, self.table, module)
        PropertiesConnector.button_controller(self, widget)
 
        id_column_index = input_headers.index(module_headers.header_id)
        id_value = TableExtractor.value_from_selected_row_by_column(self.table, id_column_index)

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
    def widget_label_elements(widget, table, module):
        label_descripton = widget.lblDescription
        lable_element_name = widget.lblElementName
        label_element_number = widget.lblElementNumber
        line_element_number = widget.leElementNumber
        line_element_name = widget.leElementName

        input_headers = TableExtractor.table_header_extractor(table)
        module_headers = TableHeaders()
        
        name_colum_index = input_headers.index(module_headers.header_name)
        number_column_index = input_headers.index(module_headers.header_number)

        object_number = TableExtractor.value_from_selected_row_by_column(table, number_column_index)
        object_name = TableExtractor.value_from_selected_row_by_column(table, name_colum_index)
        lable_element_name.setText(object_name)
        label_element_number.setText(object_number)
        line_element_name.setText(object_name)
        line_element_number.setText(object_number)

        module_text = f"{module}i Nr. ja nimetus"
        label_descripton.setText(module_text)


        return input_headers, module_headers

class ConnectorFunctions:

    def ConnectProperties(id_value):
    


        pass


