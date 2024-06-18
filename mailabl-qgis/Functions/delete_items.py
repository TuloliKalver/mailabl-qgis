import os
from qgis.utils import iface
from qgis.core import QgsProject, edit
from ..app.View_tools import listView_functions, shp_tools, finder_deque_method
from PyQt5.QtWidgets import QListView, QMessageBox, QTableView
from ..queries.python.property_data import deleteProperty, MyLablChecker
from ..Functions.Tools import tableFunctions
from ..config.settings import SettingsDataSaveAndLoad
from ..KeelelisedMuutujad.messages import Headings
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
 
pealkiri = Headings()

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))

list_functions = listView_functions()
deque_methods = finder_deque_method()
load = SettingsDataSaveAndLoad()


class Delete_Main_Process():
    
    def Delete_process_view_on_load(self):
        delete_buttons.buttons_on_load(self)
        delete_checkboxes.checkboxes_on_load(self)
        delete_tables.tables_on_load(self)
        delete_frames.frames_on_load(self)
        delete_listViews.clear_all_views(self)
        delete_listViews.selection_model_views_on_load(self)
        DeletingProcesses.get_county_list_delete(self)

        

    
    def Delete_process_view_on_countyListView_click(self):
        delete_buttons.buttons_on_load(self)
        delete_checkboxes.checkboxes_on_load(self)
        delete_tables.tables_on_load(self)
        delete_frames.frames_on_load(self)
        delete_listViews.clear_after_county(self)

    #County views
    def Delete_process_view_after_county(self):
        delete_buttons.buttons_show_after_county(self)
        delete_checkboxes.checkboxes_on_after_county(self)
        delete_frames.frames_on_load(self)
        

    def Delete_process_view_after_unsuccessful_county(self):
        delete_buttons.buttons_on_load(self)
        delete_checkboxes.checkboxes_on_load(self)
        delete_frames.frames_on_load(self)

    #state views
    def Delete_process_view_after_state(self):
        delete_buttons.buttons_show_after_state(self)
        delete_checkboxes.checkboxes_on_after_state(self)
        delete_frames.frames_on_load(self)
        delete_tables.tables_on_load(self)

        
    def Delete_process_view_after_unsuccessful_state(self):
        delete_buttons.buttons_show_after_county(self)
        delete_checkboxes.checkboxes_on_after_county(self)
        delete_frames.frames_on_load(self)
        
    #city views
    def Delete_process_view_after_city(self):
        delete_buttons.buttons_show_after_city(self)
        delete_checkboxes.checkboxes_on_after_city(self)
        delete_frames.frames_after_city(self)
        delete_tables.table_after_city(self)

    def Delete_process_view_after_unsuccessful_city(self):
        delete_buttons.buttons_show_after_state(self)
        delete_checkboxes.checkboxes_on_after_state(self)
        delete_frames.frames_on_load(self)
        delete_tables.table_after_unsuccessful_city(self)
    
class actions:

    def hider(self, elements):
        for element in elements:
            element.hide()

    def shower(self, elements):
        for element in elements:
            element.show()
    
    def cleaner (self, elements):
        for element in elements:
            element.clear()
            
    def selection_extended(self, elements):
        for element in elements:
            element.setSelectionMode(QListView.ExtendedSelection)

    def check_box_states_False(self, elements):
        for element in elements:
            element.setChecked(False)
    
    
    def check_box_states_True(self, elements):
        for element in elements:
            element.setChecked(True)
            
    
    def block_signals_False(self, elements):
        for element in elements:
            element.blockSignals(False)
    
    def block_signals_True(self, elements):
        for element in elements:
            element.blockSignals(True)


class delete_buttons():
    def __init__(self, pbDel_State, pbDel_City, pbDel_PreConfirm):
        self.pbDel_State = pbDel_State
        self.pbDel_City = pbDel_City
        self.pbDel_PreConfirm = pbDel_PreConfirm


    def buttons_on_load(self):
        hide_buttons = [
            self.pbDel_State,
            self.pbDel_City,
            self.pbDel_PreConfirm,
        ]
        actions.hider(self,elements=hide_buttons)

    def buttons_show_after_county(self):
        show_buttons = [
            self.pbDel_State
        ]
        actions.shower(self, elements=show_buttons)
        self.pbDel_City.hide()
        
        


    def buttons_show_after_state(self):
        show_buttons = [
            self.pbDel_City
            ]
        actions.shower(self, elements=show_buttons)
        


    def buttons_show_after_city(self):
        show_buttons = [
            self.pbDel_PreConfirm
        ]
        actions.shower(self, elements=show_buttons)



    def delete_buttons_signal_blocked(self):
        buttons = [
            self.pbDel_State,
            self.pbDel_City,
            self.pbDel_PreConfirm,

        ]
        buttons.blockSignals(True)
    
    def delete_buttons_signal_reactivated(self):
        buttons = [
            self.pbDel_State,
            self.pbDel_City,
            self.pbDel_PreConfirm,
        ]
        buttons.blockSignals(False)
    


class delete_listViews():
    def __init__(self,lwDel_State_Names,lwDelete_Cities_Names, lwDelete_County_Names):
        self.lwDel_State_Names = lwDel_State_Names
        self.lwDelete_Cities_Names = lwDelete_Cities_Names
        self.lwDelete_County_Names = lwDelete_County_Names

    def clear_all_views(self):
        items= [self.lwDel_State_Names,
                self.lwDelete_Cities_Names,
                self.lwDelete_County_Names
                ]
        actions.cleaner(self, items)
       
    def clear_after_county(self):
        items= [self.lwDel_State_Names,
                self.lwDelete_Cities_Names
                ]
        actions.cleaner(self, items)
    
    def clear_after_state(self):
        items= [
                self.lwDelete_Cities_Names
                ]
        actions.cleaner(self, items)
    
    
    def selection_model_views_on_load(self):
        items= [self.lwDel_State_Names,
                self.lwDelete_Cities_Names,
                ]
        actions.selection_extended(self, items)

    def listViews_on_load(self):        
        list_views = [self.lwDel_State_Names,
                    self.lwDelete_Cities_Names]
        actions.hider(self, elements=list_views)
        
        
class delete_checkboxes():
    def __init__(self, cbDel_ChooseAll_Data_properties, cbDel_ChooseAll_Data_include_Allroads, cbDel_ChooseAll_Data_transport, cbDel_ChooseAll_States, cbDel_ChooseAll_Cities):
        self.cbDel_ChooseAll_Data_properties = cbDel_ChooseAll_Data_properties
        self.cbDel_ChooseAll_Data_include_Allroads = cbDel_ChooseAll_Data_include_Allroads
        self.cbDel_ChooseAll_Data_transport = cbDel_ChooseAll_Data_transport
        self.cbDel_ChooseAll_States = cbDel_ChooseAll_States
        self.cbDel_ChooseAll_Cities = cbDel_ChooseAll_Cities
        
    def checkboxes_on_load(self):
        checkboxes = [self.cbDel_ChooseAll_Data_properties,
                        self.cbDel_ChooseAll_Data_include_Allroads,
                        self.cbDel_ChooseAll_Data_transport, 
                        self.cbDel_ChooseAll_States,
                        self.cbDel_ChooseAll_Cities]
        actions.hider(self, checkboxes)
        actions.block_signals_True(self, checkboxes)
        actions.check_box_states_False(self, checkboxes)
        actions.block_signals_False(self, checkboxes)

    def checkboxes_on_after_county(self):
        checkboxes = [ 
                self.cbDel_ChooseAll_States
                ]
        actions.shower(self, elements=checkboxes)
        
        
    
    def checkboxes_on_after_state(self):
        checkboxes = [ 
                self.cbDel_ChooseAll_Cities
                ]
        actions.shower(self, elements=checkboxes)
        self.cbDel_ChooseAll_Cities.hide()
        
    def checkboxes_on_after_city(self):
        checkboxes = [ 
                self.cbDel_ChooseAll_Data_properties,
                self.cbDel_ChooseAll_Data_include_Allroads,
                self.cbDel_ChooseAll_Data_transport
                ]
        actions.shower(self, elements=checkboxes)
        #actions.block_signals_True(self, checkboxes)
        actions.check_box_states_True(self, checkboxes)
        #actions.check_box_states_False(self, checkboxes)
        
class delete_tables():
    def __init__(self,tbl_Delete_streets, tbl_Delete_properties):
        self.tbl_Delete_streets = tbl_Delete_streets
        self.tbl_Delete_properties = tbl_Delete_properties
        
    def tables_on_load(self):
        object_tables = [self.tbl_Delete_streets,
                        self.tbl_Delete_properties]
        actions.hider(self,elements=object_tables)
        
        

    def table_after_city(self):
        object_tables = [self.tbl_Delete_streets,
                        self.tbl_Delete_properties]
        actions.shower(self,elements=object_tables)
            

    def insert_data_to_tables(self, DelModel_streets, DelModel_properties, total, lbl):
        lbl.setText(str(total))
        table_view_1 = self.tbl_Delete_streets
        table_view_2 = self.tbl_Delete_properties
        
        table_view_1.setModel(DelModel_streets)
        table_view_2.setModel(DelModel_properties)
        #TODO if function sets to work 
        #TableViewadjuster.QTableView_look(table_view_1)
        #TableViewadjuster.QTableView_look(table_view_2)
        custom_row_height = 20  # Adjust this value as needed
        for row in range(DelModel_streets.rowCount()):
            table_view_1.setRowHeight(row, custom_row_height) 
            table_view_2.setRowHeight(row, custom_row_height) 
        
        table_view_1.setSortingEnabled(True)
        table_view_2.setSortingEnabled(True)
        
        # Hide the vertical header (row numbers)
        table_view_1.verticalHeader().setVisible(False)
        table_view_2.verticalHeader().setVisible(False)
        
        # Optional: Hide grid lines
        table_view_1.setShowGrid(False)
        table_view_2.setShowGrid(False)
        
        # Automatically resize columns to fit content
        table_view_1.resizeColumnsToContents()
        table_view_2.resizeColumnsToContents()
        
        # Block editing for all cells
        table_view_1.setEditTriggers(QTableView.NoEditTriggers)
        table_view_2.setEditTriggers(QTableView.NoEditTriggers)
        
        table_view_1.selectAll()
        table_view_2.selectAll()



class delete_frames():
    def __init__(self,frDel_Main_Selected_Data_Overview, fr_Del_bottom):
        self.frDel_Main_Selected_Data_Overview = frDel_Main_Selected_Data_Overview
        self.fr_Del_bottom = fr_Del_bottom
        
    def frames_on_load(self):
        frame_tables = [self.fr_Del_bottom,
                        self.frDel_Main_Selected_Data_Overview
                        ]
        actions.hider(self, elements = frame_tables)
        
    def frames_after_city(self):
        frame_tables = [self.fr_Del_bottom,
                        self.frDel_Main_Selected_Data_Overview
                        ]
        actions.shower(self, elements = frame_tables)
        
    

class DeletingProcesses:

    def get_county_list_delete(self):#, county_field, lw_county, lbl): 
        county_field = Katastriyksus.mk_nimi #"MK_NIMI"
        lw_county = self.lwDelete_County_Names 
        lbl = self.lblDel_Amount     
        layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        expression = ""
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        if layer.isValid():
            # Your existing code to clear data can go here
            layer.setSubsetString(expression)
            layer.triggerRepaint()
            layer.updateExtents()   
            shp_tools.activateLayer_zoomTo(layer)
            data = shp_tools.create_item_list(layer_name, county_field)
            list_functions.insert_values_to_listView_object(lw_county, data)
            lw_county.update()
            item_count = shp_tools.count_items_in_layer(layer_name)
            lbl.setText(f"{item_count}")
        else:
            print(f"layer {layer} not found")
                
    def DeleteProcess_get_state_list(self,  button, layer_name, state_field, 
                                            county_field, city_field,
                                            lwDel_County_Names, lwDel_State_names,
                                            lwDel_City_Names, lbl
                                            ):
        button.blockSignals(True)
        
        item_county = lwDel_County_Names.currentItem()
        item_state = lwDel_State_names.selectedItems()
        item_city = lwDel_City_Names.selectedItems()
        
        try:
            layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        except IndexError:
            #print(f"Layer '{input_layer_name}' not found.")
            text = (f"Laetavate kinnistute kiht {layer_name} on puudu.\n Jätkamiseks lae algandmed")
            heading = pealkiri.warningSimple
            QMessageBox.warning(self, heading, text)
            #print("No items selected")
            return
        
            
        
        county_restriction = item_county.text() if item_county is not None else ""
        #print(f"county restriction {county_restriction}")
        state_restrictions = "', '".join([item.text() for item in item_state]) if item_state else ""
        #print(f"Selected items state: {state_restrictions}")
        city_restrictions_before = ""
        city_restrictions = "', '".join([item.text() for item in item_city]) if item_city else ""
        #print(f"Selected items city: {city_restrictions}")
        
        #print(f"Restriction: {restriction}")
        item_count_before = shp_tools.count_items_in_layer(layer_name)
        sorted_values = shp_tools().create_item_list_with_where(lwDel_State_names, item_count_before, 
                                                                county_restriction, layer_name, 
                                                                county_field, state_field)
        list_functions.insert_values_to_listView_object(lwDel_State_names,sorted_values) 
        #viewItem_state.addItems(sorted_values)
        lwDel_State_names.update()
        
        expression = shp_tools.universal_map_simplifier(
                            layer_name,
                            county_field, 
                            state_field,
                            city_field,
                            county_restriction, 
                            state_restrictions, 
                            city_restrictions_before
                            )
        
        layer.setSubsetString(expression)
        layer.triggerRepaint()
        layer.updateExtents()
        shp_tools.activateLayer_zoomTo(layer)
        item_count = shp_tools.count_items_in_layer(layer_name)
        lbl.setText(f"{item_count}")
        
        button.blockSignals(False)  
        
                    
    def DeleteProcess_get_city_list(self,  button, layer_name, state_field, 
                                            county_field, city_field,
                                            lwDel_County_Names, lwDel_State_names,
                                            lwDel_City_Names, lbl
                                            ):
        button.blockSignals(True)
        
        item_county = lwDel_County_Names.currentItem()
        item_state = lwDel_State_names.selectedItems()
        item_city = lwDel_City_Names.selectedItems()
        
        try:
            layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        except IndexError:
            #print(f"Layer '{input_layer_name}' not found.")
            text = (f"Laetavate kinnistute kiht {layer_name} on puudu. \nJätkamiseks lae algandmed")
            heading = pealkiri.warningSimple
            QMessageBox.warning(self, heading, text)
            #print("No items selected")
            return
        
        county_restriction = item_county.text() if item_county is not None else ""
        print(f"county restriction {county_restriction}")
        state_restrictions = "', '".join([item.text() for item in item_state]) if item_state else ""
        print(f"Selected items state: {state_restrictions}")
        city_restrictions_before = ""
        city_restrictions = "', '".join([item.text() for item in item_city]) if item_city else ""
        print(f"Selected items city: {city_restrictions}")
        
        #print(f"Restriction: {restriction}")
        item_count_before = shp_tools.count_items_in_layer(layer_name)
        #testing method diferences
        #list method
        import time
        start = time.perf_counter()
        sorted_values = shp_tools().create_item_list_with_MultyWhere(item_count_before, state_restrictions, layer_name, state_field, city_field)
        print(f"sorted values: {sorted_values}")
        stop = time.perf_counter()
        result = stop-start
        print(f"list method performance: {result}")
        #deque method
        
        list_functions.insert_values_to_listView_object(lwDel_City_Names,sorted_values) 
        #viewItem_state.addItems(sorted_values)
        lwDel_City_Names.update()
        
        expression = shp_tools.universal_map_simplifier(
                            layer_name,
                            county_field, 
                            state_field,
                            city_field,
                            county_restriction, 
                            state_restrictions, 
                            city_restrictions_before
                            )
        
        layer.setSubsetString(expression)
        layer.triggerRepaint()
        layer.updateExtents()
        shp_tools.activateLayer_zoomTo(layer)
        item_count = shp_tools.count_items_in_layer(layer_name)
        lbl.setText(f"{item_count}")
        
        button.blockSignals(False)  
    
class Delete_finalProcess:
    def delete_selected_items_from_mylabl(self):
        DeletActions.delete_selected_items_from_mylabl(self)
    
    def delete_selected_items_from_mylabl_old(self, tbl_Delete_properties, tbl_Delete_streets):
        
        data_from_properties_table = tableFunctions.RemoveNonSelectedRowsFromTable(self, tbl_Delete_properties,)
        data_from_streets_table = tableFunctions.RemoveNonSelectedRowsFromTable(self, tbl_Delete_streets)

        
        #Extract from table data and recombine
        CadastralUnits_Properties = tableFunctions.for_deleting_extract_table_indexes_and_cadasters_from_data(data_from_properties_table)
        CadastralUnits_Streets = tableFunctions.for_deleting_extract_table_indexes_and_cadasters_from_data(data_from_streets_table)
        
        print(f"CadastralUnits_Properties: {CadastralUnits_Properties}")
        print(f"CadastralUnits_Streets: {CadastralUnits_Streets}")
        ##print(f"RowIndexes_and_cadastralUnits_1 : {RowIndexes_and_cadastralUnits_1}")
        #print(f"RowIndexes_and_cadastralUnits_2: {RowIndexes_and_cadastralUnits_2}")
        
        returned_combined_properties_ids = MyLablChecker.DeleteProcess_Data_preparation(self, CadastralUnits_Properties)
        #print("returned_combined_ids - properties:")
        #print(returned_combined_properties_ids)
        #print(f"total {len(returned_combined_properties_ids)}")
        returned_combined_streets_ids = MyLablChecker.DeleteProcess_Data_preparation(self, CadastralUnits_Streets)
        #print("returned_combined_ids - streets:")
        #print(returned_combined_streets_ids)
        #print(f"total {len(returned_combined_streets_ids)}")
        
        # Combine the two lists using extend
        combined_ids = returned_combined_properties_ids.copy()  # Make a copy to avoid modifying the original list
        combined_ids.extend(returned_combined_streets_ids)
        
        deleteProperty.delete_multiple_items(self, combined_ids)

    def clear_layer_from_deleted_items(self, layer):
        print(f"layer_name in 'delete from map': {layer}")
        # Get the input layer by name
        input_layer = QgsProject.instance().mapLayersByName(layer)[0]

        # Check if there is a selection on the input layer
        if input_layer.selectedFeatureCount() > 0:
            # Get the selected feature IDs
            selected_feature_ids = [feature.id() for feature in input_layer.selectedFeatures()]

            # Start editing on the input layer
            with edit(input_layer):
                # Delete the selected features from the input layer
                input_layer.deleteFeatures(selected_feature_ids)

            # Commit changes to the input layer
            input_layer.commitChanges()
            input_layer.triggerRepaint()  # Refresh the map canvas
            input_layer.updateExtents()

        else:
            print("No features selected on the input layer.")