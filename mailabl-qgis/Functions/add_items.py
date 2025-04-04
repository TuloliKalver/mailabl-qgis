import os
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QTableWidgetItem
from ..Functions.Tools import tableFunctions, propertyUsages
from ..queries.python.property_data import add_properties
from ..config.settings import SettingsDataSaveAndLoad
from ..utils.ProgressHelper import ProgressDialogModern

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets" 
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))

load = SettingsDataSaveAndLoad()

class DataPreparation:
    @staticmethod
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
        progress = ProgressDialogModern(title="Katastri laadimine", value=0)
        progress.update(1, purpouse="Projektide laadimine", text1="Palun oota...")
        
        for index in selected_indexes:

            each_data = tableFunctions.extract_property_data(self,index, table)
            if each_data:
                data.add(f'{each_data}')
            
            property_id = add_properties.add_single_property_item(self, each_data)
            #print(f"property_id in 'input item to Mailabl loop {property_id}")
            intended_usages = propertyUsages.extract_intendedUse_data(self, index, table)
            #print(f"intended_usages in 'input item to Mailabl loop {intended_usages}")
            
            add_properties.add_additional_property_data(self, property_id, intended_usages)
            
            #count += 1
            #progress_bar.setValue(total_fetched)
            QCoreApplication.processEvents()
            if count % paus_interval == 0:
                progress.update(value=count, purpouse=f"{count}/{count_selected_rows}", text1="Palun oota...")
                # Sleep for 0.5 seconds after every delete_interval items
                time.sleep(sleep_duration)