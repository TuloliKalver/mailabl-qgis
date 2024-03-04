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
from ...config.ui_directories import PathLoader, plugin_dir_path, UI_multiline_Statusbar
from ...Functions.tableViewAdjust import ColumnResizer
from ...processes.infomessages.messages import Headings
 
heading = Headings()

paths = PathLoader(plugin_dir_path, UI_multiline_Statusbar)

tunnus_AND_address = ['TUNNUS', 'MK_NIMI', 'OV_NIMI', 'AY_NIMI', 'L_AADRESS']


class PropertiesLayerFunctions:
    def generate_table_from_selected_map_items(self, view_item, layer_name):
        input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]    
        features = input_layer.selectedFeatures()
        
        total = len(features)
        
        widget = paths.UI_multiline_Statusbar
        widget_path = paths.get_widgets_path(widget)
        progress_widget = loadUi(widget_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
        progress_widget.setWindowTitle("Koostan kinnistute nimekirja!")
        progress_widget.show()
                        
        quarter_point = total // 4  # Calculate the quarter point
        halfway_point = total // 2  # Calculate the halfway point
        three_quarter_point = total * 3 // 4  # Calculate the three-quarter point

        # Get only the desired fields from the layer
        fields = TableGenerator.get_desired_field_names(layer_name, tunnus_AND_address)
        # Generate the table model
        #model = TableGenerator.generate_table_model(features, fields)
        model = QStandardItemModel()

        # Set the horizontal header labels
        model.setHorizontalHeaderLabels(fields)
        # Add a new 'Address' column
        model.setHorizontalHeaderItem(len(fields), QStandardItem('Address'))

        # Set the model for the view
        view_item.setModel(model)
        # Set the row height to 20 pixels
        view_item.verticalHeader().setDefaultSectionSize(20)
          # Define the columns to hide
        resizer = ColumnResizer(view_item)
        
        columns = [1, 5]
        column_widths = [125,400]
        resizer.setColumnWidths(view_item, columns, column_widths)
        
        columns_to_hide = [1, 2, 3, 4]
        # Hide the specified columns
        for column_index in columns_to_hide:
            view_item.hideColumn(column_index)

        view_item.verticalHeader().setVisible(False)
        
        view_item.update()  # Refresh the view
        
        # Populate the model with data
        row = 0  # Initialize row index
        main_row = 0
        for feature in features:
            # Concatenate 'MK_NIMI', 'OV_NIMI', 'AY_NIMI', 'L_AADRESS' into a single 'Address' column
            address_value = f"{feature['MK_NIMI']} {feature['OV_NIMI']} {feature['AY_NIMI']} {feature['L_AADRESS']}"

            # Add data to the model
            for idx, field in enumerate(fields):
                item = QStandardItem(str(feature[field]))
                model.setItem(row, idx, item)

            # Add the concatenated 'Address' value to the model
            address_item = QStandardItem(address_value)
            model.setItem(row, len(fields), address_item)
            row += 1

            main_row += 1
            progress_bar.setValue(main_row)
            
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
        pass


class TableGenerator:
    @staticmethod
    def get_desired_field_names(layer_name, desired_columns):
        input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        
        # Get all field names from the layer
        all_fields = [field.name() for field in input_layer.fields()]

        # Filter out only the desired fields
        desired_fields = [field for field in all_fields if field in desired_columns]

        return desired_fields

    @staticmethod
    def generate_propertiesListModelForTable(features, fields):
        model = QStandardItemModel()

        # Set the horizontal header labels
        model.setHorizontalHeaderLabels(fields)

        # Add a new 'Address' column
        model.setHorizontalHeaderItem(len(fields), QStandardItem('Address'))

        # Populate the model with data
        for feature in features:
            # Concatenate 'MK_NIMI', 'OV_NIMI', 'AY_NIMI', 'L_AADRESS' into a single 'Address' column
            address_value = f"{feature['MK_NIMI']} {feature['OV_NIMI']} {feature['AY_NIMI']} {feature['L_AADRESS']}"

            # Add data to the model
            for idx, field in enumerate(fields):
                item = QStandardItem(str(feature[field]))
                model.setItem(0, idx, item)

            # Add the concatenated 'Address' value to the model
            address_item = QStandardItem(address_value)
            model.setItem(0, len(fields), address_item)
        return model

