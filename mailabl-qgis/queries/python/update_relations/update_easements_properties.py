from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import  QWidget
from ..property_data import PropertiesGeneralQueries
from ..query_tools import requestBuilder
from ....Functions.timer import Timer
from ....utils.messagesHelper import ModernMessageDialog
from ....KeelelisedMuutujad.messages import Headings, InfoTexts
from ....KeelelisedMuutujad.modules import Module
from ....utils.ProgressHelper import ProgressDialogModern
from ..DataLoading_classes import GraphqlEasements, GraphQLQueryLoader, GraphqlContracts




pealkiri = Headings()

on_selection_changed_lambda = None
# Adjust the delay interval and sleep duration according to your requirements
delay_interval = 10
sleep_duration = 2
timer_instance = Timer(delay_interval=delay_interval, sleep_duration=sleep_duration)

class EasementProperties:
    @staticmethod    
    def update_easements_properties(self, easements_id, widget):
        properties_table = widget.tvProperties
        model_properties = properties_table.model()
        
        properties = []
        count = model_properties.rowCount()
        if count == 0:
            parent_widget = QWidget()
            heading = pealkiri.warningSimple
            text = "Vali kaardikihil vähemalt üks kinnistu"  
            ModernMessageDialog.Info_messages_modern(heading,text)
            return
        
        for row in range(model_properties.rowCount()):
            item_column_0 = model_properties.item(row, 0)
            if item_column_0 is not None:
                cadastral_nr = item_column_0.text()
                properties.append(cadastral_nr)
            else:
                print(f"Row {row}, Column 0: No item")

        total_ids_Table = len(properties)
        returned_ids = PropertiesGeneralQueries._get_properties_MyLabl_ids(self, properties_list=properties)
        
        total_returned_ids = len(returned_ids)
        
        chunk_size = 25
        count = 0
        paus_interval = 25
        progress = ProgressDialogModern(maximum=total_returned_ids)
        
        for i in range(0, total_returned_ids, chunk_size):
            chunk = returned_ids[i:i+chunk_size]

            module = Module.EASEMENT

            query_name = GraphqlEasements.UPDATE_EASEMENTS_PROPERTIES
            query = GraphQLQueryLoader.load_query_by_module(module, query_name)  

            for property_id in chunk:
                variables = {
                    "input": {
                        "id": easements_id,
                        "properties": {
                            "associate": [
                                {
                                    "id": property_id
                                }
                            ]
                        }
                    }
                }
                
                response = requestBuilder.construct_and_send_request(self, query, variables)
                count += 1
                progress.update(count)
                QCoreApplication.processEvents()
                
                if count % paus_interval == 0:
                    timer_instance.pause()

        progress.close()
        return total_returned_ids, total_ids_Table
    


    @staticmethod    
    def _add_properties_to_module_item(self, easements_id, widget, module):

        if Module.PROJECT:
            query_loader = GraphQLQueryLoader() 
            query = query_loader.load_query_for_projects(query_loader.UPDATE_project_properties)

        if Module.CONTRACT:
            query_name =  GraphqlContracts.UPDATE_CONTRACT_PROPERTIES
            query = GraphQLQueryLoader.load_query_by_module(module, query_name)

        if Module.EASEMENT:
            query_name = GraphqlEasements.UPDATE_EASEMENTS_PROPERTIES
            query = GraphQLQueryLoader.load_query_by_module(module,query_name)            

        properties_table = widget.tvProperties
        model_properties = properties_table.model()
        
        properties = []
        count = model_properties.rowCount()
        if count == 0:
            heading = pealkiri.warningSimple
            text = "Vali kaardikihil vähemalt üks kinnistu"  
            ModernMessageDialog.Info_messages_modern(heading, text)
            return
        
        for row in range(model_properties.rowCount()):
            item_column_0 = model_properties.item(row, 0)
            if item_column_0 is not None:
                cadastral_nr = item_column_0.text()
                properties.append(cadastral_nr)
            else:
                print(f"Row {row}, Column 0: No item")

        total_ids_Table = len(properties)
        returned_ids = PropertiesGeneralQueries._get_properties_MyLabl_ids(self, properties_list=properties)
        
        total_returned_ids = len(returned_ids)
        
        chunk_size = 25
        count = 0
        paus_interval = 25
        progress = ProgressDialogModern(maximum=total_returned_ids)
        
        for i in range(0, total_returned_ids, chunk_size):
            chunk = returned_ids[i:i+chunk_size]
            
            for property_id in chunk:
                variables = {
                    "input": {
                        "id": easements_id,
                        "properties": {
                            "associate": [
                                {
                                    "id": property_id
                                }
                            ]
                        }
                    }
                }
                
                response = requestBuilder.construct_and_send_request(self, query, variables)
                count += 1
                progress.update(count)
                QCoreApplication.processEvents()
                
                if count % paus_interval == 0:
                    timer_instance.pause()

        progress.close()
        return total_returned_ids, total_ids_Table
    