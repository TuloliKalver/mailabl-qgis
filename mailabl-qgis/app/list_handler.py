
from qgis.core import QgsProject
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QListWidgetItem
from .View_tools import shp_tools
from ..config.settings import SettingsDataSaveAndLoad

class ExpandProcessListsFunctions:
    
    @staticmethod
    def get_county_list(self):      
        field_county_name = 'MK_NIMI'
        expression = ""
        input_layer_name = SettingsDataSaveAndLoad.load_SHP_inputLayer_name(self)
        layers = QgsProject.instance().mapLayersByName(input_layer_name)
        
        # Check if the list of layers is not empty before accessing its elements
        if layers:
            layer = layers[0]
            if layer.isValid():
                # Your existing code to clear data can go here
                layer.setSubsetString(expression)
                layer.triggerRepaint()
                layer.updateExtents()   
                shp_tools.activateLayer_zoomTo(layer)
                
                object_county = self.listWidget_county
                object_county.clear()
                county_items = shp_tools.create_item_list(input_layer_name, field_county_name)
                print(county_items)
                for county in county_items:
                    list_item = QListWidgetItem(county)
                    object_county.addItem(list_item)
                    QCoreApplication.processEvents()

                #list_functions.insert_values_to_listView_object(object_county, county_items)
                #object_county.update()
                item_count = shp_tools.count_items_in_layer(input_layer_name)
                self.lblCount.setText(f"{item_count}")
