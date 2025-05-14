from qgis.utils import iface
from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtCore import QObject, pyqtSignal
from ...utils.TableUtilys.TableHelpers import TableExtractor
from ...Functions.propertie_layer.InsertPropertiesToMailabl import PropertiesLayerFunctions
from ...queries.python.projects_pandas import TableHeaders
from ...config.settings import Filepaths, SettingsDataSaveAndLoad, Flags, FilesByNames
from ...KeelelisedMuutujad.messages import LabelsTexts
from ...KeelelisedMuutujad.modules import Module, ModuleTranslation, Languages
from ...KeelelisedMuutujad.messages import InfoTexts, Headings
from ...utils.messagesHelper import ModernMessageDialog
from ...queries.python.update_relations.updateElementProperties import ConnectElementWithPropertysties
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...utils.TableUtilys.TableHEaderIndexMap import HeaderIndexMap, AsBuiltHeaderIndexMap, CoordinationsIndexMap

language = Languages.ESTONIA

class PropertiesConnector(QObject):
    ConnectorWidgetClosed = pyqtSignal()

    def __init__(self, table):
        super().__init__()  # Call the __init__ method of the QObject superclass
        self.table = table
        self.widget = None
        self.SelectionTools = None
        self.module = None

    def load_propertiesconnector_widget_ui(self, module):
        if self.widget is not None:
            try:
                self.widget.close()  # Triggers closeEvent and cleanup
            except Exception:
                pass
        self.widget = None

        global selection_monitor

        widget_file = FilesByNames().add_properties_to_module_ui
        ui_file_path = Filepaths._get_widget_name(widget_file)

        widget = loadUi(ui_file_path)
        
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.setAttribute(Qt.WA_DeleteOnClose)


        drag_frame = widget.findChild(QFrame, "dragFrame")  # if it's a QFrame
        if drag_frame is not None:
            drag_frame.mousePressEvent = self.start_drag
            drag_frame.mouseMoveEvent = self.do_drag
        else:
            print("⚠️ dragFrame not found in UI.")

        widget.show()

        self.widget = widget
        table_view = widget.tvProperties

        if module is not None:
            if module == Module.PROJECT:
                self.module = Module.PROJECT
                module_text = ModuleTranslation.module_name(module, language, plural=False)
            if module == Module.CONTRACT:
                self.module = Module.CONTRACT
                module_text = ModuleTranslation.module_name(module, language, plural=False)
            if module == Module.EASEMENT:
                self.module = Module.CONTRACT
                module_text = ModuleTranslation.module_name(module,language, plural=False)
            if module == Module.ASBUILT:
                self.module = Module.ASBUILT
                module_text = ModuleTranslation.module_name(module, language, plural=False)
            if module == Module.COORDINATION:
                self.module = Module.COORDINATION
                module_text = ModuleTranslation.module_name(module, language, plural=False)

        selection_monitor = None
        flag = True
        Flags.active_properties_layer_flag = flag

        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if not isinstance(active_layer, QgsMapLayer):
            return

        if flag:
            iface.setActiveLayer(active_layer)
            iface.actionSelect().trigger()                            
            if active_layer and active_layer.selectedFeatureCount() > 0:

                WidgetTools.load_tool_and_fill_table(self, widget, table_view, active_layer_name)
                selection_monitor = lambda: WidgetTools.on_selection_changed(widget)
                active_layer.selectionChanged.connect(selection_monitor)
                widget.showNormal()
            else: 
                selection_monitor = lambda: WidgetTools.on_selection_changed(widget)
                active_layer.selectionChanged.connect(selection_monitor)
                widget.showNormal()
                #widget.showMinimized()  


        object_name, object_id = WidgetLabels.widget_label_elements(widget, self.table, module, language="et")
    
        PropertiesConnector.button_controller(self, widget, module, object_id, object_name)
                                             
        widget.closeEvent = self.closeEvent
    def closeEvent(self, event):
        try:
            iface.actionPan().trigger()  # Trigger pan tool
            global selection_monitor
            if selection_monitor:
                active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
                active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
                if active_layer:
                    active_layer.selectionChanged.disconnect(selection_monitor)
                    active_layer.removeSelection()
                    selection_monitor = None
            flag = False
            Flags.active_properties_layer_flag = flag
        
        except Exception as e:
            #print("Error occurred during disconnection:", e)
            pass
        # Close the widget
        if self.widget:
            self.widget.close()
        event.accept()  # Allow the window to close
        self.ConnectorWidgetClosed.emit()

    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.widget.frameGeometry().topLeft()
            event.accept()
    def do_drag(self, event):
        if event.buttons() & Qt.LeftButton:
            self.widget.move(event.globalPos() - self.dragPos)
            event.accept()

    def on_cancel_button_clicked(self, widget):
        if widget is not None:
            self.unset_widget_actions(widget)
            widget.accept()
            self.ConnectorWidgetClosed.emit()
    def on_save_button_clicked(self, widget, module, element_id, element_name):
        result = ConnectorFunctions.add_properties_to_module(widget, module, element_id)
        if result:
            if widget is not None:
                self.unset_widget_actions(widget)
                widget.accept()
                self.ConnectorWidgetClosed.emit()
                total_returned_ids, total_ids_Table = result
                text = InfoTexts().properties_successfully_added(element_name, total_returned_ids, total_ids_Table)
                heading = Headings().infoSimple      
                ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)
        else:
            if widget is not None:
                self.unset_widget_actions(widget)
                widget.accept()
                self.ConnectorWidgetClosed.emit()
                text = InfoTexts().error_adding_properties(element_name)
                heading = Headings().infoSimple
                ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading,text)

    def unset_widget_actions(self, widget):
        iface.actionPan().trigger()
        global selection_monitor
        if selection_monitor:
            #print("Selection monitor true")
            active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
            active_layer.selectionChanged.disconnect(selection_monitor)
            if active_layer:
                active_layer.removeSelection()
        else:
            # print(f"layer '{layer_name}' not found.")
            pass
            selection_monitor = None
        flag = False
        Flags.active_properties_layer_flag = flag
        
    def button_controller(self, widget, module, element_id, element_name):
        button_save = getattr(widget, 'pbSave', None)
        button_cancel = getattr(widget, 'pbCancel', None)
        button_clear_model_data = getattr(widget, 'pbClear_list', None)

        # Define lambdas to connect buttons to functions
        button_functions = {
            button_save: lambda: PropertiesConnector.on_save_button_clicked(self, widget, module, element_id, element_name),
            button_cancel: lambda: PropertiesConnector.on_cancel_button_clicked(self, widget),
            button_clear_model_data: lambda: PropertiesConnector.clear_table_and_map(widget)
        }
        
       # Connect buttons to functions
        for button, function in button_functions.items():
            PropertiesConnector.connect_button(button, function)
        
    @staticmethod
    def clear_table_and_map(widget):
        model = widget.tvProperties.model()
        if model is not None:
            model.clear()
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if active_layer:
            active_layer.removeSelection()
            
    @staticmethod
    def connect_button(button, function):
        if button is not None and function is not None:
            # Connect button to function
            button.clicked.connect(function)
        elif button is not None:
            # Disable button if no function assigned
            button.setEnabled(False)

class WidgetTools:
    def load_tool_and_fill_table(self, widget, table_view, active_layer_name):        
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if active_layer and active_layer.selectedFeatureCount() > 0:
            # Show the widget when there are selected features
            layer_functions = PropertiesLayerFunctions()

            layer_functions.generate_table_from_selected_map_items(table_view, active_layer_name)
            table_view.update()
            widget.showNormal()
        

    @staticmethod
    def on_selection_changed(widget):
        active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()

        if Flags.active_properties_layer_flag:
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
            if active_layer and active_layer.selectedFeatureCount() > 0:
                table_view = widget.tvProperties
                help = PropertiesLayerFunctions()
                help.generate_table_from_selected_map_items(table_view, active_layer_name)
                table_view.update()
                widget.showNormal()                        # Restore from minimized
                widget.raise_()                            # Bring it above sibling widgets
                widget.activateWindow()                    # Request focus
                widget.setWindowState(widget.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)

class WidgetLabels:
    def widget_label_elements(widget, table, module, language="et"):
        
        label_descripton = widget.lblDescription
        line_element_number = widget.leElementNumber
        line_element_name = widget.leElementName

        input_headers = TableExtractor._table_header_extractor(table)
        TableHeaders_new(language)
        
        if module == Module.ASBUILT:
            line_element_number.setVisible(False)

            index_map = AsBuiltHeaderIndexMap(input_headers, language=language)

            object_name = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_TYPE])
            line_element_name.setText(object_name)

            object_id = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_ID])


        elif module == Module.COORDINATION:
            line_element_number.setVisible(True)

            index_map = CoordinationsIndexMap(input_headers, language=language)
            
            object_name = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_JOB_NAME])
            line_element_name.setText(object_name)
            print(object_name)
            object_number = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_JOB_NUMBER])
            line_element_number.setText(object_number)
            print(object_number)
            
            object_id = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_ID])



        else: 
            line_element_number.setVisible(True)

            index_map = HeaderIndexMap(input_headers, language=language)
            
            object_name = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_NAME])
            line_element_name.setText(object_name)
        
            object_number = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_NUMBER])
            line_element_number.setText(object_number)

            object_id = TableExtractor._value_from_selected_row_by_column(table, index_map[HeaderKeys.HEADER_ID])

        module_name = ModuleTranslation.module_name(module, language, plural=False)
        text = LabelsTexts.name_number_by_module(module_name)
        label_descripton.setText(text)

        return object_name, object_id

class ConnectorFunctions:
    @staticmethod
    def add_properties_to_module(widget, module:str, element_id: str):
        if module == Module.PROJECT:
            result = ConnectElementWithPropertysties._add_properties_to_module_item( element_id, widget, module)
            return result
        if module == Module.CONTRACT:
            result = ConnectElementWithPropertysties._add_properties_to_module_item( element_id, widget, module)
            return result
        if module == Module.EASEMENT:
            result = ConnectElementWithPropertysties._add_properties_to_module_item( element_id, widget, module)
            return result
        if module == Module.ASBUILT:
            result = ConnectElementWithPropertysties._add_properties_to_module_item( element_id, widget, module)
            return result
        if module == Module.COORDINATION:
            result = ConnectElementWithPropertysties._add_properties_to_module_item( element_id, widget, module)
            return result