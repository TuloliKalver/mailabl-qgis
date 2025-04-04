# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
import os
from collections import deque
from qgis.utils import iface
from qgis.core import QgsProject, edit, QgsFeatureRequest

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView, QTableView
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QListWidgetItem
from ..config.settings import SettingsDataSaveAndLoad
from ..KeelelisedMuutujad.messages import Headings, HoiatusTextsAuto, HoiatusTexts
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..utils.messagesHelper import ModernMessageDialog

from ..utils.progres_bar_operations import run_with_progress, ProgressBarHandler_Comlex_old       

pealkiri = Headings()

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))

projects_toolsWidget_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "Properties_connector.ui"))
contracts_toolsWidget_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "ContractsPropertiesConnector.ui"))

model = QStandardItemModel()

class ToolsProject:
    def projects_toolWidget(self, Project_name, Project_number):
        projects_ToolsWidget = loadUi(projects_toolsWidget_path)
        projects_ToolsWidget.lblProjectName.setText(Project_name)
        projects_ToolsWidget.lblProjectNumber.setText(Project_number)
        return projects_ToolsWidget    

class ToolsContract:
    def contract_toolWidget(self, Contract_name, Contract_number):
        contract_ToolsWidget = loadUi(contracts_toolsWidget_path)
        contract_ToolsWidget.lblContractName.setText(Contract_name)
        contract_ToolsWidget.lblContractNumber.setText(Contract_number)
        return contract_ToolsWidget    


class tableView_functions():
    def generate_table_view_headers(self, view_item, layer, total):
        ui_file_path = widgets_path
        #print(f"path:  {ui_file_path}") 

        progress_widget = loadUi(ui_file_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
        # Set the window title for the progress_widget
        progress_widget.setWindowTitle("Koostan kinnistute nimekirja!")
        
        progress_widget.show()
        
        quarter_point = total // 4  # Calculate the quarter point
        halfway_point = total // 2  # Calculate the halfway point
        three_quarter_point = total * 3 // 4  # Calculate the three-quarter point


        fields = shp_tools.get_field_names(layer)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(fields)
        view_item.setModel(model)    

        input_layer = QgsProject.instance().mapLayersByName(layer)[0]    
        features = input_layer.getFeatures()
        row = 0
                
        for feature in features:
            row_items = []  # List to hold items for each row
            for field in fields:
                value = feature.attribute(field)

                # Check if the value is a QDate object
                if isinstance(value, QDate):
                    value = value.toString("yyyy-MM-dd")  # Format the date as desired

                item = QStandardItem(str(value))  # Create QStandardItem for the value
                row_items.append(item)  # Add item to the row_items list

            model.appendRow(row_items)  # Add row_items list to the model
            row += 1
            progress_bar.setValue(row)
            
            # Update the label content at different progress points
            if row == quarter_point:
                progress_widget.label_2.setText("Kas teadsid, et:")
                progress_widget.label_3.setText("98% meie kodumaa jõgedest on joogikõlbuliku veega")
                
            elif row == halfway_point:
                progress_widget.label_3.setText("Eestis on 56-s linnatüüpi asulat")
            elif row == three_quarter_point:
                progress_widget.label_3.setText("Inimese keha sisaldab 65% vett.")

            QCoreApplication.processEvents()  # Process events to allow GUI updates
            #print(f"row item: {row_items}")

        progress_widget.close() 



    def generate_table_from_selected_map_items_with_roads(self, layer_name):
        #print("creates table from selected items")
        input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        features = input_layer.selectedFeatures()
        total = len(features)
        
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)
        progress_widget.setWindowTitle("Koostan kinnistute nimekirja!")
        progress_widget.show()

        quarter_point = total // 4
        halfway_point = total // 2
        three_quarter_point = total * 3 // 4

        fields = shp_tools.get_field_names(layer_name)
        model_without_transport = QStandardItemModel()
        model_without_transport.setHorizontalHeaderLabels(fields)
        model_with_transport = QStandardItemModel()
        model_with_transport.setHorizontalHeaderLabels(fields)

        row = 0
        count_without_transport = 0
        count_with_transport = 0
        from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus, Puprpouse

        for feature in features:
            siht1_value = feature.attribute(Katastriyksus.siht1)
            row_items = [QStandardItem(feature.attribute(field).toString("yyyy-MM-dd") if isinstance(feature.attribute(field), QDate) else str(feature.attribute(field))) for field in fields]

            restriction = Puprpouse.transport
            if restriction not in siht1_value:
                model_without_transport.appendRow(row_items)
                count_without_transport += 1
            else: 
                model_with_transport.appendRow(row_items)
                count_with_transport += 1

            row += 1
            progress_bar.setValue(row)

            if row == quarter_point:
                progress_widget.label_2.setText("Kas teadsid, et:")
                progress_widget.label_3.setText("98% meie kodumaa jõgedest on joogikõlbuliku veega")
            elif row == halfway_point:
                progress_widget.label_3.setText("Eestis on 56-s linnatüüpi asulat")
            elif row == three_quarter_point:
                progress_widget.label_3.setText("Inimese keha sisaldab 65% vett.")

            QCoreApplication.processEvents()

        progress_widget.close() 

        #print(f"Items without 'Transpordimaa': {count_without_transport}")
        #print(f"Items with 'Transpordimaa': {count_with_transport}")

        total = count_with_transport + count_without_transport

        return model_without_transport, model_with_transport, total


class listView_functions():
    def __init__(self):
        pass

    @staticmethod
    def toggleListSelection( list_view, state):
        #print("started toggle selection in view_tools.py line 385")
        # state = 2 when checked, 0 when unchecked
        if state == 2:
            list_view.setSelectionMode(QAbstractItemView.MultiSelection)
            list_view.selectAll()
        else:
            list_view.selectionModel().clearSelection()

    @staticmethod
    def onSelectionChangeReturnChanges(selected, deselected, table):
        # Get the model from the QTableView
        model = table.model()
        
        # Find the column index for the header "tunnus"
        column = -1
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Horizontal)
            if header == Katastriyksus.tunnus:
                column = col
                break
        
        # Check if the column index was found
        if column == -1:
            print("Column 'tunnus' not found")
            return None

        # Helper function to gather data from the indexes
        def gather_data(selection):
            data = []
            for index in selection.indexes():
                # Ensure the index is in the correct column
                if index.column() == column:
                    number = index.data()
                    data.append(number)
            return data

        # Gather data from selected and deselected items
        selected_data = gather_data(selected)
        deselected_data = gather_data(deselected)

        print("selected_data:")
        print(selected_data)
        print("deselected_data:")
        print(deselected_data)


    def getAllSelectedRowsData(self, table1, table2):
        # Get the model from the QTableView
        input_layer_name = SettingsDataSaveAndLoad().load_SHP_inputLayer_name()
        layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        model1 = table1.model()
        model2 = table2.model()
        
        field_name = Katastriyksus.tunnus

        # Find the column index for the header "tunnus" in both tables
        column1 = self.getColumnIndex(model1, field_name)
        column2 = self.getColumnIndex(model2, field_name)
        
        # Check if the column index was found in both tables
        if column1 == -1:
            print("Column 'tunnus' not found in table1")
            return None
        if column2 == -1:
            print("Column 'tunnus' not found in table2")
            return None

        # Collect all selected rows' "tunnus" values from both tables
        tunnus_values1 = self.getSelectedRowsValues(table1, model1, column1)
        tunnus_values2 = self.getSelectedRowsValues(table2, model2, column2)

        # Combine the values from both tables
        combined_tunnus_values = set(tunnus_values1 + tunnus_values2)
        
        print("All selected 'tunnus' values from both tables:")
        print(combined_tunnus_values)
        
        # Select features on the layer based on the combined field values
        if layer:
            # Construct the expression with correctly formatted quotes
            tunnus_values_str = ",".join(f"'{v}'" for v in combined_tunnus_values)
            expression = f'"{field_name}" IN ({tunnus_values_str})'
            print("Combined Expression:")
            print(expression)
            features = layer.getFeatures(QgsFeatureRequest().setFilterExpression(expression))
            feature_ids = [feature.id() for feature in features]
            layer.selectByIds(feature_ids)
            #print(f"Layer '{input_layer_name}' selected features with expression: {expression}")
        else:
            print(f"Layer '{input_layer_name}' not found")
    
    def getColumnIndex(self, model, field_name):
        """Helper method to find the column index for a given field name"""
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Horizontal)
            if header == field_name:
                return col
        return -1

    def getSelectedRowsValues(self, table, model, column):
        """Helper method to get selected rows' values for a given column"""
        selection_model = table.selectionModel()
        selected_rows = selection_model.selectedRows()
        
        tunnus_values = []
        for row_index in selected_rows:
            # Get the model index for the column in the selected row
            index = model.index(row_index.row(), column)
            tunnus_value = index.data()
            tunnus_values.append(tunnus_value)
        
        return tunnus_values


    def insert_values_to_listView_object(self, object, data):
        """
        Helper function to insert values into a list view and update the widget.
        """
        object.clear()
        for feature in data:
            list_item = QListWidgetItem(feature)
            object.addItem(list_item)
            QCoreApplication.processEvents()
            object.update() 

        
#Develope later for unversal use
    def get_object_name(self, object):
        object_name = object.objectName()
        return object_name

    def get_unique_county_names(self, data):
        if data is None:
            return []  # Return an empty list if data is None

        unique_county_list = list(set(data))  
        
        #print(f"unique counties {unique_county_list}")
        return list(unique_county_list)  # Convert the set back to a list and return it

    
    def increase_popup_size(self, combo_box, additional_height):
        popup = combo_box.view()
        size = popup.sizeHint()
        size.setHeight(size.height() + additional_height)
        popup.setFixedSize(size)

    def select_all_items(self, combo_box):
        for index in range(combo_box.count()):
            combo_box.setItemData(index, Qt.Checked, Qt.CheckStateRole)

    def deselect_all_items(self, combo_box):
        for index in range(combo_box.count()):
            combo_box.setItemData(index, Qt.Unchecked, Qt.CheckStateRole)
        QCoreApplication.processEvents()
            
    def unload_and_hide_connectedItems(self, object_views, object_tables, buttons, checkboxes):
        #handle views
        empty_model = model
        for object in object_views:
            object.clear()
            object.update() 
        #handle buttons
        for button in buttons:
            button.hide()
        #handle views
        for checkbox in checkboxes:
            checkbox.setChecked(False)
            checkbox.hide()
        
        for table in object_tables:
            table.setModel(empty_model)
        QCoreApplication.processEvents()
    
        
class shp_tools:
    
    @staticmethod
    def clear_table_and_layer (table_view, layer):
        table_view.setModel(None)
        active_layer = QgsProject.instance().mapLayersByName(layer)[0]
        active_layer.removeSelection()
        
    @staticmethod
    def get_field_names(layer):
        input_layer = QgsProject.instance().mapLayersByName(layer)[0]
        # Get the field names from the layer
        fields = [field.name() for field in input_layer.fields()]
        return fields
    
    
    @staticmethod
    def activateLayer_zoomTo(layer):
        #input_layer = QgsProject.instance().mapLayersByName(layer)[0]
        iface.setActiveLayer(layer)
        iface.zoomToActiveLayer()
        QCoreApplication.processEvents()
        
    @staticmethod
    def count_items_in_layer(layer):
        input_layer = QgsProject.instance().mapLayersByName(layer)[0]
        count = input_layer.featureCount()
        return count

        
    def count_selected_items_in_SHPLayer(self):
        input_layer_name = SettingsDataSaveAndLoad.load_SHP_inputLayer_name(self)
        input_layers = QgsProject.instance().mapLayersByName(input_layer_name)
        #print(f"input_layers: {input_layers}")
        if input_layers:
            input_layer = input_layers[0]
            selected_features = input_layer.selectedFeatures()
            count = len(selected_features)
            return count
        else:
            # Handle the case where the layer is not found
            #print("Layer '{}' not found.".format(layer_name))
            return 0
    

    @staticmethod
    def create_item_list(input_layer, field):
        #print(f"input layer {input_layer}")
        input_layer = QgsProject.instance().mapLayersByName(input_layer)[0]
        # Hangi atribuutide unikaalsed väärtused tulbast "field"
        unique_values = input_layer.uniqueValues(input_layer.fields().lookupField(field))
        sorted_values = sorted(unique_values)
        #print(f"sorted_values: {sorted_values}")
        return sorted_values
    
    
    
    @staticmethod
    def create_item_list_with_where(total, restriction, input_layer_name, where_field, field):
        # Get the input layer by name from the QgsProject
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        
        ui_file_path = widgets_path
        progress_widget = loadUi(ui_file_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
        # Set the window title for the progress_widget
        progress_widget.setWindowTitle("Koostan omavalitsuste nimekirja!")
        progress_widget.show()
        
        quarter_point = total // 4  # Calculate the quarter point
        halfway_point = total // 2  # Calculate the halfway point
        three_quarter_point = total * 3 // 4  # Calculate the three-quarter point
        #object_county = self.mCB_County
        filtered_values = []
        row = 0
        # Iterate through features and filter based on where_field and restriction
        for feature in input_layer.getFeatures():
            if feature[where_field] == restriction:
                filtered_values.append(feature[field])
            row += 1
            progress_bar.setValue(row)
            
            if row == quarter_point:
                progress_widget.label_2.setText("päris palju manti sul siin läbitöötlemiseks:")
                progress_widget.label_3.setText("Vähemalt on algus tehtud")
                
            elif row == halfway_point:
                progress_widget.label_3.setText("No kaua võib!")
            elif row == three_quarter_point:
                progress_widget.label_3.setText("ohoo lõpp paistab.")
            QCoreApplication.processEvents()  # Process events to allow GUI updates
        
        sorted_values = sorted(set(filtered_values))
        #print(f"sorted_values: {sorted_values}")
        return sorted_values

    @staticmethod
    def create_item_list_with_MultyWhere(restrictions, layer_name, where_field, field):
        progress_handler = ProgressBarHandler_Comlex_old()
        input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        total = input_layer.featureCount()  # Automatically get the total number of features
        #print(f"Total features in layer '{layer_name}': {total}")

        filtered_values = []
        row = 0

        quarter_point = total // 4
        halfway_point = total // 2
        three_quarter_point = total * 3 // 4

        for feature in input_layer.getFeatures():
            #print(f"Processing feature ID: {feature.id()}, {where_field}: {feature[where_field]}, {field}: {feature[field]}")

            if feature[where_field] in restrictions:
                filtered_values.append(feature[field])
                #print(f"Feature added: {feature[field]}")

            row += 1
            progress_handler.increment_progress(row)

            # Update progress labels
            if row == quarter_point:
                progress_handler.progress_widget.label_2.setText("Uhh kui palju tööd:")
                progress_handler.progress_widget.label_3.setText("Olen juba veerandi läbinud")
            elif row == halfway_point:
                progress_handler.progress_widget.label_3.setText("Ära noki nina!")
            elif row == three_quarter_point:
                progress_handler.progress_widget.label_3.setText("Sain nimekirja kokku.")

        #print(f"Filtered values before sorting: {filtered_values}")
        # Return the sorted unique values
        sorted_filtered_values = sorted(set(filtered_values))
        #print(f"Sorted unique values: {sorted_filtered_values}")
        return sorted_filtered_values

    @staticmethod
    def county_map_simplifier(county_nimi_field, input_layer_name, viewItem_county):
        layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]

        item_county = viewItem_county.currentItem()
        
        county_restriction = item_county.text()
        expression = f"{county_nimi_field} IN ('{county_restriction}')"
        layer.setSubsetString(expression)
    @staticmethod    
    def _builds_universal_query_based_restrictions(
                                county_nimi_field, 
                                state_field,
                                city_field,
                                county_restriction, 
                                state_restrictions, 
                                city_restrictions
                                ):
    
        # Construct the expression based on selected items
        expression = ""

        if county_restriction:
            expression += f"{county_nimi_field} IN ('{county_restriction}')"

        if state_restrictions:
            if expression:
                expression += " AND "
            expression += f"{state_field} IN ('{state_restrictions}')"

        if city_restrictions:
            if expression:
                expression += " AND "
            expression += f"{city_field} IN ('{city_restrictions}')"

        return expression

class TableViewadjuster:
    @staticmethod
    def QTableView_look(table_view):
        custom_row_height = 12  # Adjust this value as needed
        for row in range(model.rowCount()):
            table_view.setRowHeight(row, custom_row_height) 
        table_view.setSortingEnabled(True)
        # Hide the vertical header (row numbers)
        table_view.verticalHeader().setVisible(False)
        # Optional: Hide grid lines
        table_view.setShowGrid(False)
        # Automatically resize columns to fit content
        table_view.resizeColumnsToContents()
        # Block editing for all cells
        table_view.setEditTriggers(QTableView.NoEditTriggers)
        
class MapSelector:
    @staticmethod
    def set_MapItemsByItemList_WithZoom(layer, items:list, field:str):
        properties_final_quoted = [f"'{item_text}'" for item_text in items]
        expression = f"{field} IN ({', '.join(properties_final_quoted)})"
        print(f"Expression is: '{expression}'")
        iface.setActiveLayer(layer)
        layer.blockSignals(False)
        layer.removeSelection()        
        layer.setSubsetString(expression)
        layer.selectAll()
        layer.triggerRepaint()
        layer.updateExtents()
        iface.zoomToActiveLayer()
        QCoreApplication.processEvents()
    
class LayerProcessor:
    @staticmethod
    def process_layer_with_progress(layer_name, filter_function, process_function=None, progress_messages=None):
        """
        A universal function to process layers with progress updates.

        Parameters:
        - layer_name: The name of the layer to process.
        - filter_function: A function defining the filtering condition (returns True/False).
        - process_function: (Optional) A function to process each filtered feature.
        - progress_messages: (Optional) A dictionary for customizing progress messages at different stages.

        Returns:
        - The processed and filtered unique data.
        """

        # Default progress messages
        default_progress_messages = {
            'quarter': "Uhh kui palju tööd:",
            'halfway': "Olen juba veerandi läbinud",
            'three_quarters': "Ära noki nina!"
        }
        progress_messages = progress_messages or default_progress_messages

        def task(progress_handler):
            input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
            processed_data = []
            
            for feature in input_layer.getFeatures():
                if filter_function(feature):
                    if process_function:
                        processed_data.append(process_function(feature))
                    else:
                        processed_data.append(feature)
                progress_handler.increment_progress(1)

            #print(f"Processed data before filtering unique values: {processed_data}")

            # Filter for unique values and sort
            unique_sorted_data = sorted(set(processed_data))
            #print(f"Unique sorted data: {unique_sorted_data}")

            return unique_sorted_data  # Return unique sorted values

        result = run_with_progress(task_function=task, window_title="Processing")
        #print(f"Final result from process_layer_with_progress: {result}")
        return result or []
