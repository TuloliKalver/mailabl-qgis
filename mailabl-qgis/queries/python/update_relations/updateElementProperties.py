from PyQt5.QtCore import QCoreApplication
from ..property_data import PropertiesGeneralQueries
from ..query_tools import requestBuilder
from ....Functions.timer import Timer
from ....utils.messagesHelper import ModernMessageDialog
from ....KeelelisedMuutujad.messages import Headings, InfoTexts
from ....KeelelisedMuutujad.modules import Module
from ....utils.ProgressHelper import ProgressDialogModern
from ..FileLoaderHelper import GraphqlEasements, GraphQLQueryLoader, GraphqlContracts, GraphqlProjects, GraphqlTasks, GraphqlCoordinations




pealkiri = Headings()

on_selection_changed_lambda = None
# Adjust the delay interval and sleep duration according to your requirements
delay_interval = 10
sleep_duration = 2
timer_instance = Timer(delay_interval=delay_interval, sleep_duration=sleep_duration)

class ConnectElementWithPropertysties:
    
    @staticmethod
    def _add_properties_to_module_item(item_id, widget, module):
       
        if module == Module.PROJECT:
            query_name = GraphqlProjects.UPDATE_project_properties
        elif module == Module.CONTRACT:
            query_name = GraphqlContracts.UPDATE_CONTRACT_PROPERTIES
        elif module == Module.EASEMENT:
            query_name = GraphqlEasements.UPDATE_EASEMENTS_PROPERTIES
        elif module == Module.ASBUILT:
            query_name = GraphqlTasks.UPDATE_TASK_PROPERTIES
        elif module == Module.COORDINATION:
            query_name = GraphqlCoordinations.UPDATE_PROPERTIES
        else:
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER("Viga", "Moodulile {module}")
            return

        query = GraphQLQueryLoader.load_query_by_module(module, query_name)

        properties_table = widget.tvProperties
        model_properties = properties_table.model()
        
        properties = []
        count = model_properties.rowCount()
        if count == 0:
            heading = pealkiri.warningSimple
            text = "Vali kaardikihil vähemalt üks kinnistu"  
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
            return

        for row in range(count):
            item_column_0 = model_properties.item(row, 0)
            if item_column_0 is not None:
                cadastral_nr = item_column_0.text()
                properties.append(cadastral_nr)

        total_ids_Table = len(properties)
        returned_ids = PropertiesGeneralQueries._get_properties_MyLabl_ids(properties_list=properties)
        total_returned_ids = len(returned_ids)

        chunk_size = 25
        count = 0
        paus_interval = 25
        progress = ProgressDialogModern(maximum=total_returned_ids)

        for i in range(0, total_returned_ids, chunk_size):
            chunk = returned_ids[i:i+chunk_size]
            for property_id in chunk:
                associate = ConnectElementWithPropertysties.build_associate_payload(module, property_id)
                variables = {
                    "input": {
                        "id": item_id,
                        "properties": {
                            "associate": associate
                        }
                    }
                }

                response = requestBuilder.construct_and_send_request(query, variables)
                count += 1
                progress.update(count)
                QCoreApplication.processEvents()

                if count % paus_interval == 0:
                    timer_instance.pause()

        progress.close()
        return total_returned_ids, total_ids_Table

    @staticmethod
    def build_associate_payload(module, property_id):
        if module == Module.EASEMENT:
            # If area/pricePerAreaUnit is needed dynamically, update here
            return [{
                "id": property_id,
                    }]
        elif module in (Module.PROJECT, Module.CONTRACT, Module.ASBUILT, Module.COORDINATION):
            return [property_id]
        else:
            raise ValueError(f"Unsupported module type: {module}")

    