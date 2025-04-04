import os
from PyQt5.QtGui import  QStandardItemModel
from ..Functions.add_items import DataPreparation
from ..config.settings import Filepaths, FilesByNames
        
model = QStandardItemModel()

class ConfirmationUIwithTableView():
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
        
        
        widget_name = Filepaths._get_widget_name(FilesByNames().WConfirmation)
        widget = Filepaths.load_ui_file(widget_name)
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

