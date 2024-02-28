from PyQt5.QtCore import Qt
from qgis.core import (QgsFeature,
                       QgsGeometry, QgsLayerTreeGroup,
                       QgsMapLayer, QgsProject, QgsVectorLayer)
from PyQt5.QtWidgets import QComboBox


class ComboBox_functions():
    def __init__(self):
        #Selectable comboboxes on Delete items page
        self.combo_box_county = 'mCB_County'
        self.combo_box_state =  'mCB_State'
        self.combo_box_City = 'mCB_City'        

    def insert_values_to_combobox(self,combo_box, data):
        print(f"Combobox to insert value {combo_box}")
        combo_box.clear()
        combo_box.addItems(data)


#Develope later for unversal use
    def selected_combobox_name(self,combo_box):
        combobox_name = combo_box.objectName()
        return combobox_name
    
    def get_combobox_by_name(self, combobox_name, parent_widget):
        # Find and return the combobox object based on its name
        combobox = parent_widget.findChild(QComboBox, combobox_name)
        return combobox

    def get_unique_county_names(self, data):
        if data is None:
            return []  # Return an empty list if data is None

        unique_county_list = list(set(data))  
        
        print(f"unique counties {unique_county_list}")
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
            


class ComboBoxMapTools:
            
    def create_item_list(input_layer, field):
        print("item list from selectable_combobox.py")
        input_layer = QgsProject.instance().mapLayersByName(input_layer)

        # Get the first layer from the list
        input_layer = input_layer[0]
    # Hangi atribuutide unikaalsed väärtused tulbast "MK_NIMI"
        unique_values = input_layer.uniqueValues(input_layer.fields().lookupField(field))
        sorted_values = sorted(unique_values)
        print(f"sorted_values: {sorted_values}")
        return sorted_values
    
    def create_item_list_with_where(self, combobox, input_layer_name, where_field, field):
        # Get the input layer by name from the QgsProject
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        #print(f"input layer name {input_layer}")
        # Get the selected value from the combobox
        #print(combobox)
        restriction = combobox.currentText()
        #print(f"restriction {restriction}")
        # Create a list to store filtered values
        filtered_values = []

        # Iterate through features and filter based on where_field and restriction
        for feature in input_layer.getFeatures():
            if feature[where_field] == restriction:
                filtered_values.append(feature[field])

        #print(f"Filtererd values: {filtered_values}")
        # Get unique values from the filtered list
        unique_values = list(set(filtered_values))

        # Sort and return the unique values
        sorted_values = sorted(unique_values)
        #print(f"sorted_values: {sorted_values}")
        return sorted_values