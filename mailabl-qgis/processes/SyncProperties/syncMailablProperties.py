import time
from PyQt5.QtCore import QObject, pyqtSignal
from qgis.core import QgsApplication, QgsTask, QgsMessageLog
from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, edit
from ...queries.python.property_data import WhereProperties
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QIcon
from ...Functions.item_selector_tools import properties_selectors
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import connect_settings_to_layer
from ...app.View_tools import shp_tools
from...Functions.layer_generator import LayerCopier
from ...processes.infomessages.messages import Headings
 
pealkiri = Headings()

class MapView(QObject):
    mapLayerUpdated = pyqtSignal()

    def create_MapView(self, layer_name):
        # Simulate the creation of the map view for the given layer
        print(f"Map view created for layer: {layer_name}")

        # Introduce a 2-second pause
        time.sleep(2)

        # Emit the signal
        self.mapLayerUpdated.emit()

class MapTask(QgsTask):
    def __init__(self, layer_name):
        QgsTask.__init__(self, "MapTask")
        self.layer_name = layer_name

    def run(self):
        
        # Simulate the creation of the map view for the given layer
        print(f"Map view created for layer: {self.layer_name}")

        # Introduce a 2-second pause
        time.sleep(2)

        return True  # Indicate that the task is complete

class PropertiesBaseMap:
    def __init__(self,lblFor_Sync_GreatLayerName, frSync_Cadastrals_Main, county_list_widget,
                state_list_widget, city_list_widget, pBar_County_list, pBar_State_list,
                pBar_City_list, pBar_City_items, lblSync_General, lblSync_General_aditional,
                lblFor_pBar_County_list, lblFor_pBar_State_list, lblFor_pBar_City_list,
                lblFor_pBar_City_items, Sync_Cadastrals, frSync_Overview_Main, frSync_Tools, a, b, c, d):
        self.map_view = MapView()
        self.map_view.mapLayerUpdated.connect(self.continueToCityLoop)
        
        self.lblFor_Sync_GreatLayerName = lblFor_Sync_GreatLayerName
        self.frSync_Cadastrals_Main = frSync_Cadastrals_Main
        self.county_list_widget = county_list_widget
        self.state_list_widget = state_list_widget
        self.city_list_widget = city_list_widget
        self.pBar_County_list = pBar_County_list
        self.pBar_State_list = pBar_State_list
        self.pBar_City_list = pBar_City_list
        self.pBar_City_items = pBar_City_items
        self.lblSync_General = lblSync_General
        self.lblSync_General_aditional = lblSync_General_aditional
        self.lblFor_pBar_County_list = lblFor_pBar_County_list
        self.lblFor_pBar_State_list = lblFor_pBar_State_list
        self.lblFor_pBar_City_list = lblFor_pBar_City_list
        self.lblFor_pBar_City_items = lblFor_pBar_City_items
        self.Sync_Cadastrals = Sync_Cadastrals
        self.frSync_Overview_Main = frSync_Overview_Main
        self.frSync_Tools = frSync_Tools
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        

    def prepare_items_for_base_map(self):
        #print("Click signal received")
        lblFor_Sync_GreatLayerName = self.lblFor_Sync_GreatLayerName
        frSync_Cadastrals_Main = self.frSync_Cadastrals_Main
        county_list_widget = self.county_list_widget
        state_list_widget = self.state_list_widget
        city_list_widget = self.city_list_widget
        pBar_County_list = self.pBar_County_list
        pBar_State_list = self.pBar_State_list
        pBar_City_list = self.pBar_City_list
        pBar_City_items = self.pBar_City_items
        lblSync_General = self.lblSync_General
        lblSync_General_aditional = self.lblSync_General_aditional
        lblFor_pBar_County_list = self.lblFor_pBar_County_list
        lblFor_pBar_State_list = self.lblFor_pBar_State_list
        lblFor_pBar_City_list = self.lblFor_pBar_City_list
        lblFor_pBar_City_items = self.lblFor_pBar_City_items
        Sync_Cadastrals = self.Sync_Cadastrals
        frSync_Overview_Main = self.frSync_Overview_Main
        frSync_Tools = self.frSync_Tools

        input_layer_name =  connect_settings_to_layer.Import_Layer_name()
        future_layer_name_text = lblFor_Sync_GreatLayerName.text()
        if not future_layer_name_text or len(future_layer_name_text) < 3:
            text = ("Nimetus on vigane või lisamata")    
            heading = pealkiri.warningSimple
            QMessageBox.warning(self.frSync_Cadastrals_Main, heading, text)
            # Set red background color for the label
            border = ("border: 1px solid #D32F2F; border-radius: 5px;")
            #background_red = "background-color: #D32F2F"
            #lblFor_Sync_GreatLayerName.setStyleSheet(background_red)
            lblFor_Sync_GreatLayerName.setStyleSheet(border)
            lblFor_Sync_GreatLayerName.clear()
            return

        county_list_widget.clear()
        state_list_widget.clear()
        city_list_widget.clear()
        
        Sync_Cadastrals.show()
        frSync_Cadastrals_Main.show()
        frSync_Overview_Main.show()
                
        frSync_Tools.hide()
        lblFor_pBar_State_list.hide()
        lblFor_pBar_City_list.hide()
        lblFor_pBar_City_items.hide()
        
        done_icon_path = ":/qt-project.org/styles/commonstyle/images/standardbutton-apply-16.png"
        icon = QIcon(done_icon_path)  
        
        lblSync_General_text = (f"kaardikihi ettevalmistamine.")
        lblSync_General_aditional_text = (f"{future_layer_name_text}")
        lblSync_General.setText(lblSync_General_text)
        lblSync_General_aditional.setText(lblSync_General_aditional_text)
        
        
        layer_creator = True
        if layer_creator:
            memory_layer_name = LayerCopier.copy_virtual_layer_for_properties(future_layer_name_text)
            layer_creator = False
            print(f"Created memory_layer_name at 'start': {memory_layer_name}")
        
    # Step 1: Query counties 
        county_items = self.query_counties_and_add_to_listView()

        total_items = county_list_widget.count()
        pBar_State_list.setMaximum(total_items+1)
        pBar_State_list.setValue(1)
    
        county_index = 0
        for county_item in county_items:
            county_list_widget.setCurrentRow(county_index)
            selected_county_items = county_list_widget.selectedItems()
            selected_county_item = selected_county_items[0]
            if selected_county_item:
                selected_county_item_text = selected_county_item.text()
                lblFor_pBar_State_list.show()
                lblFor_pBar_State_list.setText(f"Töötlen {selected_county_item_text} andmeid")
                #print(f"Valmistan ette aluskaarti: {selected_county_item_text}")        
            
# Step 2: Query states for the selected county and load the first state item
                if county_index == 0:
                    state_index = 0
                else:
                    state_index = state_list_widget.count()          
                state_items = self.query_states_for_county_and_add_to_stateListView(selected_county_item_text)     
                
# Step 3: Load city items for the selected state
            city_items_counter = 0
            total_states = len(state_items)
            pBar_State_list.setMaximum(total_states)
            for state_item in state_items:
                pBar_State_list.setValue(city_items_counter+1)
                #print(f"state_index {state_index}")
                state_list_widget.setCurrentRow(state_index)
                current_state_item = state_list_widget.item(state_index)
                selected_state_items = state_list_widget.selectedItems()
                selected_state_item = selected_state_items[0]
                if selected_state_item:
                    selected_state_item_text = selected_state_item.text()
                    
                    layer_type = "import"
                    properties_selectors.create_mapView_of_state(self, layer_type, selected_state_item_text)
                    city_items = self.load_city_items_for_state(state_item = selected_state_item_text,
                                                                state_index=state_index, 
                                                                icon=icon, 
                                                                future_layer_name_text=future_layer_name_text,
                                                                memory_layer_name=memory_layer_name)
                else:
                    print("No 'State' selected")
                    return
                current_state_item.setIcon(icon)
                state_index += 1
                
                city_index = 0
                list_widget_city_total_count = city_list_widget.count()
                
                while list_widget_city_total_count > city_index:
                    city_list_widget.setCurrentRow(city_index)
                    current_city_item = city_list_widget.item(city_index)
                    selected_city_items = city_list_widget.selectedItems()
                    selected_city_item = selected_city_items[0]
                    if selected_city_item:
                        selected_city_item_text = selected_city_item.text()
                        city_cadastrals, total_out = PropertiesBaseMap.process_selected_City_item(self, selected_city_item_text, pBar_City_items, state_item) 
                        #print("city_cadastrals")
                        #print(city_cadastrals)
                        properties_selectors.show_AND_copy_connected_cadasters_for_sync_process_dev(city_cadastrals, memory_layer_name)
                        #PropertiesBaseMap.select_on_map_and_import_to_layer(self, city_cadastrals, memory_layer_name, input_layer_name)

                        selected_city_item.setIcon(icon)
                        QCoreApplication.processEvents()
                        city_index +=1
                
                
                
                current_city_item.setIcon(icon)
                
                city_list_widget.clear()
                City_items_in_loop = len(city_items)
                total_cites = city_items_counter + City_items_in_loop
                
                # Step 5: Continue to the next state item
                print("Step 5: Continue to the next state item")
                # Simulate a delay where processing may take some time
                #time.sleep(0.5)

    # Simulate the need for QCoreApplication.processEvents()
            selected_county_item.setIcon(icon)
            county_index +=1
            county_progressValue = county_index+1
            pBar_State_list.setValue(county_progressValue)
            # Step 6: Continue to the next county item
            print("Step 6: Continue to the next county item")

        print("Step 7: copy memory layer to the file designated file!")
        group_layer_name = 'Uued kinnistud'
        QTimer.singleShot(500, lambda: LayerCopier.StartSaving_virtual_Layer(self, memory_layer_name, future_layer_name_text, group_layer_name))


        lblSync_General.setText(f" kaardikiht on koostatud. Laetud on:")
        lblFor_pBar_County_list.setText(f"{county_index} maakonda")
        lblFor_pBar_State_list.setText(f"{state_index} omavalitsust")
        lblFor_pBar_City_list.setText(f"{total_cites} linna linna/küla")
        ##lblFor_pBar_City_items.hide()
        lblFor_pBar_City_items.setText(f"kinnistute koguarv: 'xxxx arv'")
        pBar_County_list.hide()
        pBar_State_list.hide()
        pBar_City_list.hide()
        pBar_City_items.hide()
        self.a.hide()
        self.b.hide()
        self.c.hide()
        self.d.hide()
        
        
        # Simulate a delay where processing may take some time
        #time.sleep(0.5)
        layer_creator = False
        #print(f"The end: Layer_creator = {layer_creator}")
            
    def continueToCityLoop(self):
        # This method will be called once the map layer has been updated
        print("Continuing to the city loop")

        # Simulate a delay where processing may take some time
        time.sleep(0.5)

        # Simulate the need for QCoreApplication.processEvents()

    # Implement the following methods based on your actual data retrieval and processing logic
    def query_counties_and_add_to_listView(self):
        county_list_widget = self.county_list_widget
        pBar_County_list = self.pBar_County_list
        lblFor_pBar_County_list = self.lblFor_pBar_County_list

        county_label_text =  "Kontollin maakondi"
        lblFor_pBar_County_list.setText(county_label_text)

        pBar_County_list.setMaximum(100)
        pBar_County_list.setValue(0)
        pBar_County_list.show()

        #Too Maakonnad
        county_items = []
        has_next_page = True
        county_loop_count = 0
        #print("started county loop")
        while has_next_page is True:#county_last_page is None or county_last_page:
            new_county_items, has_next_page, total_new_county= WhereProperties.Return_Mailabl_County_list_with_where_COUNTY_NOT_IN(self, county_items)  
            county_items.extend(new_county_items)
            #print(f"Combined:{county_items}")

            if county_loop_count == 0:
                county_max = total_new_county
                pBar_County_list.setMaximum(county_max)
                remaining_value = 1
            else:
                remaining_value = (total_new_county - county_max)*-1
                #print(f"{remaining_value}=({max}-{total_new})*-1")
            pBar_County_list.setValue(remaining_value)
                # Calculate the remaining value for the progress bar
            county_loop_count += 1            
            QCoreApplication.processEvents()
        for county in county_items:
            list_item = QListWidgetItem(county)
            self.county_list_widget.addItem(list_item)
            QCoreApplication.processEvents()
        
        #county_items_count = county_list_widget.count()   
        #county_label_text =  (f"Maakondi on kokku {county_items_count}")
        county_label_text =  (f"Maakondade nimekiri on alla laaditud. Järgneb iga maakonna eraldi töötlemine.")
        lblFor_pBar_County_list.setText(county_label_text)
        #print("County ended")
        pBar_County_list.setValue(1)
        pBar_County_list.hide()
        self.b.hide()
        return county_items
    
    def query_states_for_county_and_add_to_stateListView(self, county_item):
        state_list_widget = self.state_list_widget
        state_items = []
        state_item_count = 0
        state_has_next_page = True
        end_cursor = None
        while state_has_next_page is True: #clear limitation of or state_item <1 for productions         use 
            #print(f"variable county item in query_states_for_county: '{county_item}")
            #print(f"variable state_last_page item in query_states_for_county: '{state_has_next_page}")
            #print(f"variable end_cursor in query_states_for_county: '{end_cursor}")
            new_state_item, state_has_next_page, end_cursor = WhereProperties.Return_Mailabl_State_list_Where_county_IN(self, county_item, state_items, end_cursor)
            #print(f"new_state_item {new_state_item}")
            if new_state_item != "":
                state_items.append(new_state_item)
                state_item = new_state_item
                print(f"appended and cleaned new_state_item is '{new_state_item}'")
                #print(f"appended new_state_items are '{state_items}'")
            #for state_item in state_items:
                state_list_item = QListWidgetItem(state_item)
                state_list_widget.addItem(state_list_item)
                state_item_count +=1
                QCoreApplication.processEvents()
                
        return state_items

    def load_city_items_for_state(self, state_item, state_index, icon, future_layer_name_text, memory_layer_name):
        city_list_widget = self.city_list_widget
        pBar_City_list = self.pBar_City_list
        pBar_City_items = self.pBar_City_items
        lblFor_pBar_State_list = self.lblFor_pBar_State_list
        lblFor_pBar_City_list = self.lblFor_pBar_City_list
        lblFor_pBar_City_items = self.lblFor_pBar_City_items


        city_items = []
        city_has_next_page = True
        city_end_cursor = None
        city_loop_count = 1
        city_Dev_item = 0
        city_loop_max = 10
        #initialize statusbar for the first time!
        pBar_City_list.show()
        pBar_City_list.setMaximum(city_loop_max)
        pBar_City_list.setValue(1)
        while city_has_next_page is True: #or city_Dev_item < 3: 
            if city_loop_count == 1:
                city_loop_max = state_index
                #print(f"max = {max} total_new = {total_new}")
                pBar_City_list.setMaximum(city_loop_max)
                remaining_value = 1
            else:
                remaining_value = (total_new - city_loop_max)*-1
            
                # Calculate the remaining value for the progress bar
            lblFor_pBar_City_list.show()
            lblFor_pBar_City_list.setText(f"Töötlen {state_item} linnasid ja külasid")
            new_city_item, city_has_next_page, total_new, count, city_end_cursor = WhereProperties.Return_Mailabl_City_list_Where_State_IN(self, state_item, city_items)  
            print(f"new_city_item for '{state_item}' is '{new_city_item}'")
            if new_city_item != "":
                city_items.extend([new_city_item])
                #print(city_items)
                city_Dev_item +=1
                city_list_item = QListWidgetItem(new_city_item)
                #print(city_list_item)
                city_list_widget.addItem(city_list_item)
                #print("added city item")
                city_loop_count += 1
                pBar_City_list.setValue(remaining_value)
                # Step 4: Query data for each city item and create a map layer using QgsTask
                #layer_name = f"Copying layer data for '{state_item}_{new_city_item}"
                QCoreApplication.processEvents()
                
        # Simulate loading city items for the given state and return a list of city items
        return city_items

    @staticmethod
    def process_selected_City_item(self, selected_item_text, pBar_City_items, selected_state_item_text):
        
        city_cadastralNrs = []  # Initialize with a default value
        total = 0
        city_items_max = 10
        pBar_City_items.setMaximum(city_items_max)
        pBar_City_items.setValue(1)
        cityItems_loop_count = 1
        end_cursor = None
        hasNextPage = True
        total_count = 0
        while hasNextPage is True:
            time.sleep(0.3)
            city_cadastral_units, hasNextPage, totalCityItems, count, end_cursor = WhereProperties.Return_Mailabl_Properties_Where_City_IN(self, city_item= selected_item_text, next_page=end_cursor,state_item=selected_state_item_text) 
            city_cadastralNrs.extend(city_cadastral_units)
            if cityItems_loop_count == 1:
                maxCitys = totalCityItems
                #print(f"max = {max} total_new = {total_new}")
                pBar_City_items.setMaximum(maxCitys)
                remaining_value = maxCitys
                end_total = total_count + count
                #lblFor_pBar_City_Items.setText(f"{selected_item_text} on {city_items_max} kinnistut")
                #QCoreApplication.processEvents()
            else:
                end_total = total_count + count
                remaining_value = (end_total - maxCitys)*-1
                #lblFor_pBar_City_Items.setText(f"{selected_item_text} on ette valmistatud {end_total}/{city_items_max} kinnistut")
                #print(f"{remaining_value}=({max}-{total_new})*-1")
            cityItems_loop_count +=1
            pBar_City_items.setValue(remaining_value)
            QCoreApplication.processEvents()

        return city_cadastralNrs, total
    
        
class SyncProcess_LayerHandling:
    @staticmethod
    def copy_selected_features(self, memory_layer_name, input_layer_name):
        #
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        # Check if there is a selection on the input layer
        feature_count = input_layer.selectedFeatureCount()
        # Example: Display a message box with a Cancel button
        if feature_count ==0:
            print(f"Error!!!: Feature count in 'copy_selected_features': {feature_count}")
            return  False# Return from the method, stopping further execution
        
        
        #print(f"feature count in 'copy_selected_features': {feature_count}")
        if input_layer.selectedFeatureCount() > 0:
            # Get the target layer by name or any other means
            target_layer = QgsProject.instance().mapLayersByName(memory_layer_name)[0]
            #print(f"target_layer: {target_layer}")
            # Start editing on the target layer
            with edit(target_layer):
                # Loop through selected features on the input layer
                selected_features = input_layer.selectedFeatures()
                #print(f"selected features in 'copy_selected_features': {selected_features}")
                for feature in input_layer.selectedFeatures():
                    # Clone the feature to add it to the target layer
                    new_feature = QgsFeature(feature)
                    target_layer.addFeature(new_feature)
            target_layer.commitChanges()
            target_layer.triggerRepaint()  # Refresh the map canvas
            target_layer.updateExtents()
            
            #shp_tools.zoom_to_layer_extent(self, target_layer)
            # Hide the input layer
            #QgsProject.instance().layerTreeRoot().findLayer(input_layer.id()).setItemVisibilityChecked(False)     
            input_layer.removeSelection()
        else:
            print("No features selected on the input layer.")
