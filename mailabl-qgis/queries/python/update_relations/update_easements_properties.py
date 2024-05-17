from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox, QWidget
from ..property_data import PropertiesGeneralQueries
from ..query_tools import requestBuilder
from ....config.ui_directories import PathLoaderSimple
from ....Functions.timer import Timer

from PyQt5.uic import loadUi
from ....KeelelisedMuutujad.messages import Headings, InfoTexts

pealkiri = Headings()

on_selection_changed_lambda = None
# Adjust the delay interval and sleep duration according to your requirements
delay_interval = 10
sleep_duration = 2
timer_instance = Timer(delay_interval=delay_interval, sleep_duration=sleep_duration)

class EasementProperties:
    @staticmethod    
    def update_easements_properties(self, easements_id, widget, item_name):
        properties_table = widget.tvProperties
        model_properties = properties_table.model()
        
        properties = []
        count = model_properties.rowCount()
        if count == 0:
            parent_widget = QWidget()
            heading = pealkiri.warningSimple
            text = "Vali kaardikihil vähemalt üks kinnistu"  
            QMessageBox.information(parent_widget, heading, text)
            return
        
        for row in range(model_properties.rowCount()):
            item_column_0 = model_properties.item(row, 0)
            if item_column_0 is not None:
                cadastral_nr = item_column_0.text()
                properties.append(cadastral_nr)
            else:
                print(f"Row {row}, Column 0: No item")

        total_ids_Table = len(properties)
        returned_ids = PropertiesGeneralQueries.get_properties_MyLabl_ids(self, properties_list=properties)
        
        total_returned_ids = len(returned_ids)
        print(f"returned_ids (total: {total_returned_ids}) when adding properties to easement")
        print(returned_ids)
        
        chunk_size = 25
        count = 0
        paus_interval = 25
        widgets_path = PathLoaderSimple.widget_statusBar_path(self)
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total_returned_ids)
        progress_widget.setWindowTitle("Kinnistutega sidumine")
        progress_widget.show()
        
        for i in range(0, total_returned_ids, chunk_size):
            chunk = returned_ids[i:i+chunk_size]
            from ..DataLoading_classes import GraphqlQueriesEasements           
            query_loader = GraphqlQueriesEasements()
            query = query_loader.load_query_for_easements(query_loader.UPDATE_easments_properties)            

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

                print("Variables:")
                print(variables)
                print("Property ID:", property_id)
                
                response = requestBuilder.construct_and_send_request(self, query, variables)
                count += 1
                progress_bar.setValue(count)
                QCoreApplication.processEvents()
                
                if count % paus_interval == 0:
                    timer_instance.pause()

        text = InfoTexts().properties_successfully_added(item_name, total_returned_ids, total_ids_Table)
        heading = Headings().informationSimple
        QMessageBox.information(None, heading, text)
