import time
from qgis.core import  QgsProject, QgsMapLayer
from qgis.utils import iface
from PyQt5.QtCore import QCoreApplication
from ..DataLoading_classes import GraphQLQueryLoader
from PyQt5.QtWidgets import  QMessageBox, QWidget
from ....config.settings import  connect_settings_to_layer, flags
from ..property_data import PropertiesGeneralQueries
from ....Functions.propertie_layer.properties_layer_data import PropertiesLayerFunctions
from ..query_tools import requestBuilder
from ....config.ui_directories import PathLoaderSimple
from ....Functions.timer import Timer 

from PyQt5.uic import loadUi


on_selection_changed_lambda = None
# Adjust the delay interval and sleep duration according to your requirements
delay_interval = 10
sleep_duration = 2
timer_instance = Timer(delay_interval=delay_interval, sleep_duration=sleep_duration)



class map_selectors:    
    def activate_layer_and_use_selectTool_on_first_load(self, widget):
        global on_selection_changed_lambda
        print("started with activated layer")
        active_layer_name = connect_settings_to_layer.ActiveMailablPropertiesLayer_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if not isinstance(active_layer, QgsMapLayer):
            #print(f"Ei leidnud kinnistute kihti '{layer}'")
            return
        iface.setActiveLayer(active_layer)
        iface.actionSelect().trigger()
        #print("start selecting stuff")
        #Hide the main window
        flag = flags.active_properties_layer_flag
        print(f"Flag status befor if statement {flag}")
        
        if active_layer and active_layer.selectedFeatureCount() > 0:
            # Show the widget when there are selected features
            table_view = widget.tvProperties_AddTo_Projects

            help = PropertiesLayerFunctions()
            help.generate_table_from_selected_map_items(table_view, active_layer_name)
            table_view.update()
            widget.showNormal()

        if flag:
            print("Flag is true in activate_layer function")
            
            on_selection_changed_lambda = lambda: map_selectors.on_selection_changed(widget)
            print(f"lambda value {on_selection_changed_lambda}")
            active_layer.selectionChanged.connect(on_selection_changed_lambda)
            
        else:
           print("Flag is false")
           pass

    def activate_layer_and_use_selectTool(self, widget):
        global on_selection_changed_lambda
        #print("started with activated layer")
        active_layer_name = connect_settings_to_layer.ActiveMailablPropertiesLayer_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        if not isinstance(active_layer, QgsMapLayer):
            #print(f"Ei leidnud kinnistute kihti '{layer}'")
            return
        iface.setActiveLayer(active_layer)
        iface.actionSelect().trigger()
        #print("start selecting stuff")
        #Hide the main window
        flag = flags.active_properties_layer_flag
        #print(f"Flag status befor if statement {flag}")
        
        if active_layer and active_layer.selectedFeatureCount() > 0:
            # Show the widget when there are selected features
            table_view = widget.tvProperties_AddTo_Projects

            help = PropertiesLayerFunctions()
            help.generate_table_from_selected_map_items(table_view, active_layer_name)
            table_view.update()
            widget.showNormal()

        if flag:
            #print("Flag is true in activate_layer function")
            on_selection_changed_lambda = lambda: map_selectors.on_selection_changed(widget)
            #print(f"lambda value {on_selection_changed_lambda}")
            widget.showMinimized()
            active_layer.selectionChanged.connect(on_selection_changed_lambda)
            
        else:
            print("Flag is false")
            pass
        
    @staticmethod
    def on_selection_changed(widget):
        active_layer_name = connect_settings_to_layer.ActiveMailablPropertiesLayer_name()
#        print("on_selection_changed")
        if flags.active_properties_layer_flag:
            # If the flag is true, execute the function
#            print("Flag is true in selection change")
#            print(f"And active_properties_layer flag is {flags.active_properties_layer_flag}")
            active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]

            if active_layer and active_layer.selectedFeatureCount() > 0:
                # Show the widget when there are selected features
                table_view = widget.tvProperties_AddTo_Projects

                help = PropertiesLayerFunctions()
                help.generate_table_from_selected_map_items(table_view, active_layer_name)
                table_view.update()
                widget.showNormal()

        else:
            # If the flag is false, do nothing
            print("Flag is false")
        


class ProjectsProperties:
    def on_cancel_button_clicked(widget):
        active_layer_name = connect_settings_to_layer.ActiveMailablPropertiesLayer_name()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        parent_widget = QWidget()
        titleText = "Info"
        infoText = "Kinnistute seostamine tühistatud"
        #active_layer.selectionChanged.disconnect()  
        QMessageBox.information(parent_widget, titleText, infoText)
        #import lamda here
        active_layer.selectionChanged.disconnect(on_selection_changed_lambda)

        flag = flags.active_properties_layer_flag 
        flag = False            
        flags.active_properties_layer_flag = flag

    @staticmethod    
    def update_projects_properties(self, project_id, widget, project_name):
        active_layer_name = connect_settings_to_layer.ActiveMailablPropertiesLayer_name()
        properties_table = widget.tvProperties_AddTo_Projects
        model_properties = properties_table.model()
        
        properties = []
        count = model_properties.rowCount()
        if count == 0:
            parent_widget = QWidget()
            titleText = "Oioioi"
            infoText = "Vali kaardikihilt mõni kinnistu"  
            QMessageBox.information(parent_widget, titleText, infoText)
            pass
        for row in range(model_properties.rowCount()):
            item_column_0 = model_properties.item(row, 0)
            if item_column_0 is not None:
                #print(f"Row {row}, Column 0: {item_column_0.text()}")
                cadastral_nr = item_column_0.text()
                properties.append(cadastral_nr)
            else:
                print(f"Row {row}, Column 0: No item")

        total_ids_Table = len(properties)
        #print(f"properties {properties}")
        
        returned_ids = PropertiesGeneralQueries.get_properties_MyLabl_ids(self, properties_list=properties)
        
        total_returned_ids = len(returned_ids)
        #print(f"returned_ids (total: {total_returned_ids}) when adding properties to project")
        #print(returned_ids)
        
        chunk_size = 25
        count = 0
        paus_interval = 25  # Set the interval for the sleep timer
        #sleep_duration = 1  # Set the sleep duration in seconds
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total_returned_ids)
        progress_widget.setWindowTitle("Seostan projekte kinnistutega")
        progress_widget.show()
        
        for i in range(0, total_returned_ids, chunk_size):
            chunk = returned_ids[i:i+chunk_size]
            
            query_loader = GraphQLQueryLoader() 
            query = query_loader.load_query_for_projects(query_loader.UPDATE_project_properties)
            
            variables = {
                        "input": {
                            "id": project_id,
                            "properties":
                                {
                                "associate": chunk
                            }
                        }
                        }
            
            response = requestBuilder.construct_and_send_request(self, query, variables)
            #print(f"Response: {response.status_code}")
            #print(response.text)
            count += paus_interval
            progress_bar.setValue(count)
            QCoreApplication.processEvents()
            
            
            if count % paus_interval == 0:
                timer_instance.pause()

                    
        QMessageBox.information(self, "Info", f"Projektile {project_name} lisatud {total_returned_ids}/{total_ids_Table}")
        #print("Project updated successfully:")
        #print(updated_project)
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)[0]
        active_layer.selectionChanged.disconnect(on_selection_changed_lambda)
            
        flag = flags.active_properties_layer_flag 
        flag = False        
        flags.active_properties_layer_flag = flag


