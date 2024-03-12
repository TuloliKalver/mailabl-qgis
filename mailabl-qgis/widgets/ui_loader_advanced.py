import os
from PyQt5.QtGui import  QStandardItemModel
from PyQt5.uic import loadUi

from ..Functions.add_items import DataPreparation
from PyQt5.QtCore import QCoreApplication



model = QStandardItemModel()

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))



class Directories:
    # Declare catalogues and links
    # Main directory
    plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Status bar widget folder
    widgets_folder = "widgets"
    WStatusBar = "WStatusBar.ui"
    WConfirmation = "Confirmation_list.ui"

    # Full paths for the widgets
    WstatusBar_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, WStatusBar))
    WConfirmation_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, WConfirmation))

    # Define widget names
    WIDGET_NAMES = {
        "WStatusBar.ui": WStatusBar,
        "Confirmation_list.ui": WConfirmation
        # Add more widgets as needed
    }
#TODO delete afther developing has ended!!!
    @staticmethod
    def print_paths():
        print(f"plugin_dir: {Directories.plugin_dir}")
        print(f"WstatusBar_path: {Directories.WstatusBar_path}")
        print(f"WConfirmation_path: {Directories.WConfirmation_path}")
        
class loader():
    def load_ui_WConfirmation(self, false_count_properties, true_count_properties,
                            false_count_streets, true_count_streets,
                            false_values,
                            table,
                            RowIndexes_and_cadastralUnits,
                            input_layer_name):
        print(f" Step 6,1: Input items totals!")
        total_false_count = int(false_count_properties) + int(false_count_streets)
        total_true_count = int(true_count_properties) + int(true_count_streets)
        
        print(f"totals total_false_count: {total_false_count}")
        print(f"totals total_true_count: {total_true_count}")
        
        #print(f"totals false_values: {false_values_properties}")
        #print(f"total RowIndexes_and_cadastralUnits: {len(RowIndexes_and_cadastralUnits)}")
        #print(f"input layer_name: {input_layer_name}")
        
        
        # Load the UI file
        widget = loadUi(Directories.WConfirmation_path)
        widget.show()
        if total_false_count <=0:
            widget.f_results.hide()
            widget.f_heading.hide()
            footer_size = widget.f_footer.size()

            buttonBox_size = widget.buttonBox.size()
            padding = 6
            
            total_height = footer_size.height() + buttonBox_size.height() + padding*2
            self.resize(450, total_height)
        
        # Define the column names
        label = widget.lb_results
        lbl_total_toAdd = widget.lbl_Total_toAdd
        tbl_summary_properties = widget.tblW_confirmation
        # Show the loaded widget
        
        label.setText(str(total_false_count)) #here we can add item count together to display total amount of properties to be added!
        lbl_total_toAdd.setText(str(total_true_count))
        
        returned_cadastral_units = DataPreparation.data_structuring(false_values, tbl_summary_properties)
        result = widget.exec_()

        decision = True
        # Check the result after the user interaction (e.g., which button was pressed)
        if result == widget.Accepted:
            print("User pressed OK")
            #return returned_cadastral_units
        
            
            #print(f"total RowIndexes_and_cadastralUnits: {len(RowIndexes_and_cadastralUnits)}")
            #loader.clear_table_from_inMailabl_rows(input_layer_name, table, RowIndexes_and_cadastralUnits, returned_cadastral_units)
            #Add_Properties_final.insert_selected_items_to_Mailabl(self, table)
            return decision, returned_cadastral_units
        else:
            decision = False
            print("User pressed Cancel")
            return decision, returned_cadastral_units

    
    def clear_table_from_inMailabl_rows(input_layer_name, table_1, rowIDs_cadastralData, returned_cadastral_units):
        result = []
        indexes_to_remove = []
        total_rows = len(rowIDs_cadastralData)
        count = 0
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_widget.setWindowTitle("valikust välja jäänud kinnistud eemaldatakse tablesit!")
        progress_bar.setMaximum(total_rows)
        progress_widget.show()
        
        
        print(f"Total_rows '{total_rows}'")
        for item in rowIDs_cadastralData:
            #print(f"item: {item_s1}")
            # Access values for 'index' and 'number'
            number_value = item['number']
            #print(f"index: {index_value}, number: {number_value}")
            print(f"if 'number_value' in 'returned_units'")
            print (f"if {number_value} in {returned_cadastral_units}")
        
            if number_value in returned_cadastral_units:
                print("else append features")
                index_value = item['index']
                indexes_to_remove.append(index_value)

                #pass
            #if number_value in returned_cadastral_units:
                #print("number not in ")
                #print(number_value)
            else:
                print("number in")
                print(number_value)
                #result.append(number_value)
            count +=1
            progress_bar.setValue(count)
            QCoreApplication.processEvents()
            
        model_before = table_1.model()
        indexes_to_remove.sort(reverse=True)
        print(f"indexes to be removed:'{indexes_to_remove}'")

        # Remove rows from the model based on IDs
        for row_id in indexes_to_remove:
            model_before.removeRow(row_id)
            QCoreApplication.processEvents()
            
        # Update the table view
        #table_1.update()
        # Get the model from the table view
#        model_after = table_1.model()

        # Get the data from the first column of the updated model
#        column_data = []

#        count = 0 
        
        #count_selected_rows_before = model_before.rowCount()        
#        count_selected_rows_after = model_after.rowCount()
        #print(f"count_selected_rows_before: '{count_selected_rows_before}'")
        #print(f"count_selected_rows_after: '{count_selected_rows_after}'")
        
#        progress_bar.setMaximum(count_selected_rows_after)
#        progress_bar.setValue(count)
        #progress_widget.setWindowTitle("Appending something somewhere third time!!!")

#        for row_index in range(model_after.rowCount()):
#            # Assuming the first column is at index 0
#            item = model_after.item(row_index, 0)
            
            # Check if the item exists
#            if item is not None:
                # Retrieve the data from the item and add it to the list
#                column_data.append(item.text())
#                count +=1
#                progress_bar.setValue(count)
#                QCoreApplication.processEvents()
        # Now, column_data contains the data from the first column of the updated model
        #print(column_data)
        progress_widget.hide()
