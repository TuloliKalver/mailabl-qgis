import os
from qgis.core import edit
from qgis.core import QgsFeature, QgsLayerTreeGroup, QgsProject, QgsVectorLayer

from ..app.View_tools import listView_functions, shp_tools, finder_deque_method
from ..Functions.Tools import tableFunctions, propertyUsages
from PyQt5.uic import loadUi
from ..queries.python.property_data import add_properties
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableWidgetItem
from ..config.settings import DataSettings, Filepaths, SettingsDataSaveAndLoad

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))
#ui_file_path = f"C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\kataster\app\widgets\WStatusBar.ui"

graph_tools = shp_tools()
list_functions = listView_functions()
deque_methods = finder_deque_method()
load = SettingsDataSaveAndLoad()

class DataPreparation:
    def data_structuring(data, table):
        #print(f"in data_structuring 'data' is: {data}")
        headers = ['Katastri tunnus', 'Mailabl link']
        table.setColumnCount(len(headers))  # Set the number of columns
        for col, header_text in enumerate(headers):
            header_item = QTableWidgetItem(header_text)
            table.setHorizontalHeaderItem(col, header_item)

        # Hide the vertical header (row numbers)
        table.verticalHeader().setVisible(False)
        # Optional: Hide grid lines
        table.setShowGrid(False)

        custom_row_height = 20
        prepared_data = []
        for index, item in enumerate(data):
            #immovable_number = QStandardItem(item.get('immovableNumber', '').replace('NULL', ''))
            cadastral_unit_pure = item['cadastralUnit'].get('number', '').replace('NULL', '')
            cadastral_unit = QTableWidgetItem(cadastral_unit_pure)             
            link_value ="Link Mailabli on arendamisel!"
            link = QTableWidgetItem(link_value)
            # set items in the table
            table.setRowCount(index + 1)  # increase row count so each item is set to new row!
            table.setItem(index, 0, cadastral_unit)
            table.setItem(index, 1, link)
            table.setRowHeight(index, custom_row_height) 

            #make list to for data comparison
            prepared_data.append(cadastral_unit_pure)
            QCoreApplication.processEvents()
        # Automatically resize columns to fit content
        table.resizeColumnsToContents()
        # Block editing for all cells

        return  prepared_data   #model,


class Add_Properties_final:
    def insert_selected_items_to_Mailabl(self,table, new_layer_name):  #Remove 2 if not needed 
        selected_indexes = table.selectionModel().selectedRows()
        count_selected_rows = len(selected_indexes)
        # Set to store data
        data = set()
        import time
        count = 0 
        paus_interval = 10  # Set the interval for the sleep timer
        sleep_duration = 2  # Set the sleep duration in seconds
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_widget.setWindowTitle("Lisan kinnistuid")
        progress_bar.setMaximum(count_selected_rows)
        progress_bar.setValue(count)
        
        progress_widget.show()
        for index in selected_indexes:

            each_data = tableFunctions.extract_property_data(self,index, table)
            if each_data:
                data.add(f'{each_data}')
            
            property_id = add_properties.add_single_property_item(self, each_data)
            #print(f"property_id in 'input item to Mailabl loop {property_id}")
            intended_usages = propertyUsages.extract_intendedUse_data(self, index, table)
            #print(f"intended_usages in 'input item to Mailabl loop {intended_usages}")
            
            #for intended_use in intended_usages:   
            #print(f"fintended use: {intended_use}")  
            add_properties.add_additional_property_data(self, property_id, intended_usages)
            
            count += 1
            progress_bar.setValue(count)
            #progress_bar.setValue(total_fetched)
            QCoreApplication.processEvents()
            if count % paus_interval == 0:
                # Sleep for 0.5 seconds after every delete_interval items
                time.sleep(sleep_duration)
                
        
        #target_layer_name_2 = load.load_target_cadastral_name()
        '''
        target_layer_name = new_layer_name
        input_layer_name = load.load_SHP_inputLayer_name()
        #print("Layers before map conversion:")
        #print(f"target_layer_name: '{target_layer_name}'")
        #print(f"input_layer_name: '{input_layer_name}'")
        target_layer = QgsProject.instance().mapLayersByName(target_layer_name)[0]
        QgsProject.instance().layerTreeRoot().findLayer(target_layer.id()).setItemVisibilityChecked(True)
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        QgsProject.instance().layerTreeRoot().findLayer(input_layer.id()).setItemVisibilityChecked(True)
        #target_layer_2 = QgsProject.instance().mapLayersByName(target_layer_name_2)[0]
        with edit(target_layer):
            counter = 1
            progress_bar.setValue(counter)
            # Loop through selected features on the input layer
            counted_features = input_layer.selectedFeatureCount()
            progress_bar.setMaximum(counted_features)
            progress_widget.setWindowTitle("Kopeerin kaardiandmeid")
            print(f"counted features: {counted_features}")
            if input_layer.selectedFeatureCount() > 0:
                #print(f"entering loop to copy map features")
                for feature in input_layer.selectedFeatures():
                    #print(f"Feature: '{feature}'")

                    #new_feature = QgsFeature(feature)
                    #print(f"new_feature: {new_feature}")
                    #target_layer.addFeature(new_feature)
                    target_layer.addFeature(feature)
                    counter +=1
                    progress_bar.setValue(counter)
                    QCoreApplication.processEvents()
        # Commit changes to the target layer
        target_layer.commitChanges()
        target_layer.triggerRepaint()  # Refresh the map canvas
        target_layer.updateExtents()
        '''
    