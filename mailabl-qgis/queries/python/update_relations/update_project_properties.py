from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import  QWidget
from ..DataLoading_classes import GraphQLQueryLoader, Graphql_project
from ..property_data import PropertiesGeneralQueries
from ..query_tools import requestBuilder
from ....config.ui_directories import PathLoaderSimple
from ....Functions.timer import Timer 
from ....KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ....KeelelisedMuutujad.modules import Module
from ....utils.messagesHelper import ModernMessageDialog

pealkiri = Headings()

# Adjust the delay interval and sleep duration according to your requirements
delay_interval = 10
sleep_duration = 2
timer_instance = Timer(delay_interval=delay_interval, sleep_duration=sleep_duration)

class ProjectsProperties:
    @staticmethod    
    def update_projects_properties(self, project_id, widget):
        properties_table = widget.tvProperties
        model_properties = properties_table.model()
        properties = []
        count = model_properties.rowCount()
        if count == 0:
            parent_widget = QWidget()
            heading = Headings().warningSimple
            text = HoiatusTexts().kihil_kinnistu_valik
            ModernMessageDialog.Info_messages_modern(heading,text)
            
        for row in range(model_properties.rowCount()):
            item_column_0 = model_properties.item(row, 0)
            if item_column_0 is not None:
                #print(f"Row {row}, Column 0: {item_column_0.text()}")
                cadastral_nr = item_column_0.text()
                properties.append(cadastral_nr)
            else:
                return False 

        total_ids_Table = len(properties)
        #print(f"properties {properties}")        
        returned_ids = PropertiesGeneralQueries._get_properties_MyLabl_ids(self, properties_list=properties)
        total_returned_ids = len(returned_ids)        
        chunk_size = 25
        count = 0
        paus_interval = 25  # Set the interval for the sleep timer
        #sleep_duration = 1  # Set the sleep duration in seconds
       

        for i in range(0, total_returned_ids, chunk_size):
            chunk = returned_ids[i:i+chunk_size]
            
            module = Module.PROJECT
            query_name = Graphql_project.UPDATE_project_properties
            query = GraphQLQueryLoader.load_query_by_module(module, query_name)

            variables = {
                        "input": {
                            "id": project_id,
                            "properties":
                                {
                                "associate": chunk
                            }
                        }
                        }
            #print(variables)
            requestBuilder.construct_and_send_request(self, query, variables)

            count += paus_interval
            QCoreApplication.processEvents()
             
            if count % paus_interval == 0:
                timer_instance.pause()

        return total_returned_ids, total_ids_Table
    
