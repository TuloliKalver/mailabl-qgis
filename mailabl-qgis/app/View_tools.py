import os
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from qgis.core import (QgsFeature,
                       QgsGeometry, QgsLayerTreeGroup,
                       QgsMapLayer, QgsProject, QgsVectorLayer, edit)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView, QTableView
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QDate
from qgis.utils import iface
from collections import deque
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QListWidgetItem
from ..config.settings import DataSettings, SettingsDataSaveAndLoad


#declare catalouges and links
#main directory
#plugin_dir = os.path.dirname(__file__)
# Get the parent directory of the directory containing the script
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

class progress:
        def progress_bar_load(total):
            progress_widget = loadUi(widgets_path)
            progress_bar = progress_widget.testBar
            progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
            #QCoreApplication.processEvents()  # Process events to allow GUI updates
            return progress_bar


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


        fields = shp_tools.get_field_names(self, layer)
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

        fields = shp_tools.get_field_names(self, layer_name)
        model_without_transport = QStandardItemModel()
        model_without_transport.setHorizontalHeaderLabels(fields)
        model_with_transport = QStandardItemModel()
        model_with_transport.setHorizontalHeaderLabels(fields)

        row = 0
        count_without_transport = 0
        count_with_transport = 0

        for feature in features:
            siht1_value = feature.attribute('SIHT1')
            row_items = [QStandardItem(feature.attribute(field).toString("yyyy-MM-dd") if isinstance(feature.attribute(field), QDate) else str(feature.attribute(field))) for field in fields]

            if 'Transpordimaa' not in siht1_value:
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

        print(f"Items without 'Transpordimaa': {count_without_transport}")
        print(f"Items with 'Transpordimaa': {count_with_transport}")

        total = count_with_transport + count_without_transport

        return model_without_transport, model_with_transport, total


class listView_functions():
    def __init__(self):
        pass


    def toggleListSelection(self, list_view, state):
        print("started toggle selection in view_tools.py line 385")
        # state = 2 when checked, 0 when unchecked
        if state == 2:
            list_view.setSelectionMode(QAbstractItemView.MultiSelection)
            list_view.selectAll()
        else:
            list_view.selectionModel().clearSelection()
            

    def insert_values_to_listView_object(self, object, data):
        #object_name = object.objectName() - if testing or printing is needed
        object.clear()
        for feature in data:
            list_item = QListWidgetItem(feature)
            object.addItem(list_item)
            QCoreApplication.processEvents()
            

        
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
    
    
    def clear_table_and_layer (table_view, layer):
        table_view.setModel(None)
        active_layer = QgsProject.instance().mapLayersByName(layer)[0]
        active_layer.removeSelection()
        
    
    def get_field_names(self, layer):
        input_layer = QgsProject.instance().mapLayersByName(layer)[0]
        # Get the field names from the layer
        fields = [field.name() for field in input_layer.fields()]
        return fields
    
    def getLayerFieldItemsBasedonColumn(self, layer_name: str, desired_columns):
        input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]        
        # Get all field names from the layer
        all_fields = [field.name() for field in input_layer.fields()]
        # Filter out only the desired fields
        desired_fields = [field for field in all_fields if field in desired_columns]
        return desired_fields
    
    def activateLayer_zoomTo(self, layer):
        #input_layer = QgsProject.instance().mapLayersByName(layer)[0]
        iface.setActiveLayer(layer)
        iface.zoomToActiveLayer()
        QCoreApplication.processEvents()
    
    def count_items_in_layer(self,layer):
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
    

    
    def create_item_list(self, input_layer, field):
        #print(f"input layer {input_layer}")
        input_layer = QgsProject.instance().mapLayersByName(input_layer)[0]
        # Hangi atribuutide unikaalsed väärtused tulbast "MK_NIMI"
        unique_values = input_layer.uniqueValues(input_layer.fields().lookupField(field))
        sorted_values = sorted(unique_values)
        #print(f"sorted_values: {sorted_values}")
        return sorted_values
    
    
    
    
    def create_item_list_with_where(self,view_item, total, restriction, input_layer_name, where_field, field):
        import time
        start = time.perf_counter()        
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
            #print(f"row item: {row}")
        # Get unique values from the filtered list
        #unique_values = list(set(filtered_values))

        # Sort and return the unique values
        #sorted_values = sorted(unique_values)
        
        sorted_values = sorted(set(filtered_values))
        #print(f"sorted_values: {sorted_values}")
        return sorted_values


    def create_item_list_with_MultyWhere(self, total, restrictions, input_layer_name, where_field, field):
        # Get the input layer by name from the QgsProject
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        
        ui_file_path = widgets_path
        progress_widget = loadUi(ui_file_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
        # Set the window title for the progress_widget
        progress_widget.setWindowTitle("Koostan linnade/külade nimekirja!")
        progress_widget.show()
        
        quarter_point = total // 4  # Calculate the quarter point
        halfway_point = total // 2  # Calculate the halfway point
        three_quarter_point = total * 3 // 4  # Calculate the three-quarter point
        
        #filtered_values = QStandardItemModel()
        filtered_values = []
        row = 0
        # Iterate through features and filter based on where_field and restrictions
        for feature in input_layer.getFeatures():
            if feature[where_field] in restrictions:
            
                filtered_values.append(feature[field])
            row += 1
            progress_bar.setValue(row)
            
            # Update the label content at different progress points
            if row == quarter_point:
                progress_widget.label_2.setText("Uhh kui palju tööd:")
                progress_widget.label_3.setText("Olen juba veerandi läbinud")
                
            elif row == halfway_point:
                progress_widget.label_3.setText("Ära noki nina!")
            elif row == three_quarter_point:
                progress_widget.label_3.setText("Sain nimekirja kokku.")
            
            QCoreApplication.processEvents()  # Process events to allow GUI updates
        # Get unique values from the filtered list
        unique_values = list(set(filtered_values))

        # Sort and return the unique values
        sorted_values = sorted(unique_values)
        #print(f"sorted_values: {sorted_values}")
        return sorted_values
    
    
    def county_map_simplifier(self, county_nimi_field, input_layer_name, viewItem_county,viewItem_state, viewItem_city):
        try:
            layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        except IndexError:
            #print(f"Layer '{input_layer_name}' not found.")
            heading = "Hoiatus"
            text = (f"Oi, laetavate kinnistute kiht {input_layer_name} on puudu.\nJätkamiseks lae algandmed")
            QMessageBox.warning(self, heading,text)
            #print("No items selected")
            return
        item_county = viewItem_county.currentItem()
        item_state = viewItem_state.currentItem()
        item_city = viewItem_city.currentItem()
        
        county_restriction = item_county.text()
        expression = f"{county_nimi_field} IN ('{county_restriction}')"
        layer.setSubsetString(expression)
        
    def universal_map_simplifier(self, 
                                input_layer_name,
                                county_nimi_field, 
                                state_field,
                                city_field,
                                county_restriction, 
                                state_restrictions, 
                                city_restrictions
                                ):
        try:
            layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        except IndexError:
            #print(f"Layer '{input_layer_name}' not found.")
            text = (f"Oi, laetavate kinnistute kiht {input_layer_name} on puudu. \n jätkamiseks lae algandmed")
            heading = "Oi Oi Oi"
            QMessageBox.warning(self, heading, text)
            #print("No items selected")
            return
    
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

    def delete_selected_map_elements (layer):
            selected_features = layer.selectedFeatures()

            # Delete each selected feature
            with edit(layer):
                for feature in selected_features:
                    layer.deleteFeature(feature.id())


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
        
class finder_deque_method:
    def create_item_list_for_cities(self, total, restrictions, input_layer_name, where_field, field):
        print(f"restrictions: {restrictions}")
        print(f"where field: {where_field}")
        print(f"field: {field}")
        
        # Get the input layer by name from the QgsProject
        print(f"input_layer_name: {input_layer_name}")
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        print(f"input_layer: {input_layer}")
        ui_file_path = widgets_path
        progress_widget = loadUi(ui_file_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
            # Set the window title for the progress_widget
        progress_widget.setWindowTitle("Koostan linnade/külade nimekirja!")
        progress_widget.show()
        
        quarter_point = total // 4  # Calculate the quarter point
        halfway_point = total // 2  # Calculate the halfway point
        three_quarter_point = total * 3 // 4  # Calculate the three-quarter point
        

        # Instead of using a list, use a deque
        filtered_values = deque()
        row = 0

        # Iterate through features and filter based on where_field and restrictions
        for feature in input_layer.getFeatures():
            #print(feature)
            if feature[where_field] in restrictions:
                filtered_values.append(feature[field])
            row += 1
            progress_bar.setValue(row)

            # Update the label content at different progress points
            if row == quarter_point:
                progress_widget.label_2.setText("Uhh kui palju tööd:")
                progress_widget.label_3.setText("Olen juba veerandi läbinud")
            elif row == halfway_point:
                progress_widget.label_3.setText("Ära noki nina!")
            elif row == three_quarter_point:
                progress_widget.label_3.setText("Sain nimekirja kokku.")

            QCoreApplication.processEvents()  # Process events to allow GUI updates

        # Get unique values from the filtered deque
        unique_values = list(set(filtered_values))

        # Sort and return the unique values
        sorted_values = sorted(unique_values)
        return sorted_values

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
    
    @staticmethod
    def set_MapItemsByItemList_NoZoom(layer, items:list, filed:str):
        properties_final_quoted = [f"'{item_text}'" for item_text in items]
        expression = f"{filed} IN ({', '.join(properties_final_quoted)})"
        print(f"Expression is: '{expression}'")
        iface.setActiveLayer(layer)
        layer.blockSignals(False)
        layer.removeSelection()        
        layer.setSubsetString(expression)
        layer.selectAll()
        layer.triggerRepaint()
        layer.updateExtents()
        QCoreApplication.processEvents()
        
    @staticmethod
    def select_MapItemsByItem_NoZoom(layer, item:str, field:str):
        expression = f"{field} IN ('{item}')"
        print(f"Expression is: '{expression}'")
        iface.setActiveLayer(layer)
        layer.removeSelection()
        layer.selectByExpression(expression)
        layer.triggerRepaint()
        layer.updateExtents()
        QCoreApplication.processEvents()
    

    