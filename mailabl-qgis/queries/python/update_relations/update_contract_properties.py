
from PyQt5.QtCore import QCoreApplication
from ..DataLoading_classes import GraphqlQueriesContracts
from ..property_data import PropertiesGeneralQueries, GraphQLQueryLoader
from ..query_tools import requestBuilder
from ....config.ui_directories import PathLoaderSimple
from ....Functions.timer import Timer 
from ....utils.messagesHelper import ModernMessageDialog
from PyQt5.uic import loadUi
from ....KeelelisedMuutujad.messages import Headings, InfoTexts
from ....KeelelisedMuutujad.modules import Module

pealkiri = Headings()

on_selection_changed_lambda = None
# Adjust the delay interval and sleep duration according to your requirements
delay_interval = 10
sleep_duration = 2
timer_instance = Timer(delay_interval=delay_interval, sleep_duration=sleep_duration)

class ContractProperties:
    @staticmethod    
    def update_contract_properties(self, contract_id, widget):
        properties_table = widget.tvProperties
        model_properties = properties_table.model()
        
        properties = []
        count = model_properties.rowCount()
        if count == 0:
            heading = pealkiri.warningSimple
            text = "Vali kaardikihil vähemalt üks kinnistu"  
            ModernMessageDialog.Info_messages_modern(heading,text)
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
        returned_ids = PropertiesGeneralQueries._get_properties_MyLabl_ids(self, properties_list=properties)
        
        total_returned_ids = len(returned_ids)
        print(f"returned_ids (total: {total_returned_ids}) when adding properties to project")
        print(returned_ids)
        
        chunk_size = 25
        count = 0
        paus_interval = 25  # Set the interval for the sleep timer
        #sleep_duration = 1  # Set the sleep duration in seconds
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total_returned_ids)
        progress_widget.setWindowTitle("Kinnistutega sidumine")
        progress_widget.show()
        
        for i in range(0, total_returned_ids, chunk_size):
            chunk = returned_ids[i:i+chunk_size]
            

            module = Module.CONTRACT
            query_name =  GraphqlQueriesContracts.UPDATE_CONTRACT_PROPERTIES
            query = GraphQLQueryLoader.load_query_by_module(module, query_name)

            
            variables = {
                        "input": {
                            "id": contract_id,
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

        progress_widget.close()
        return total_returned_ids, total_ids_Table
    


