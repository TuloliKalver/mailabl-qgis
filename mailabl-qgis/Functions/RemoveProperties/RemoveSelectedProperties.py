from qgis.core import QgsProject
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import  QMessageBox, QAbstractItemView
from PyQt5.QtCore import QCoreApplication
from ...app.View_tools import MapSelector, TableViewadjuster
from ...app.workspace_handler import TabHandler
from ..Tools import tableFunctions
from ..QstandardModelTools.QStandardModelHandler import ModelHeadersGenerator, CombineModels, DataExtractors
from ..delete_items import Delete_finalProcess, Delete_Main_Process
from ...queries.python.property_data import PropertiesGeneralQueries, deleteProperty
from ...config.settings import SettingsDataSaveAndLoad

class DeleteActions:
    @staticmethod
    def delete_selected_items_from_mylabl(self):
        load = SettingsDataSaveAndLoad()
        active_cadastral_layer_name = load.load_target_cadastral_name()
        active_layer = QgsProject.instance().mapLayersByName(active_cadastral_layer_name)[0]
        
        button = self.pbDel_PreConfirm
        table_properties = self.tbl_Delete_properties
        table_streets = self.tbl_Delete_streets
        table_target = self.tblvAllDeletable        
        tab_widget = self.tabW_Delete_list
        field = "TUNNUS"
        
        data = tableFunctions.RemoveNonSelectedRowsFromTable(self, table_properties)
        data2 = tableFunctions.RemoveNonSelectedRowsFromTable(self, table_streets)
        
        if len(data) == 0 and len(data2) == 0:
            QMessageBox.warning(self,"Oops","Vali importimiseks vähemalt üks kinnistu!")
            return
        else:
            button.blockSignals(True)

            # Assuming table_properties and table_streets are QStandardItemModel objects
            model_properties = table_properties.model()
            model_streets = table_streets.model()        

            header_names = ModelHeadersGenerator.generateHeadersFromExistingModel(model_properties)
            # Get column names from the model

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(header_names)
            
            TabHandler.tabViewByState(tab_widget, state=False)        
            
            # Now that the new model is populated, you can set it to your table view
            table_target.setModel(model)
            TableViewadjuster.QTableView_look(table_target)
            # Insert data into the new model
            CombineModels.TableModelCombiner(model_properties,model_streets,model,header_names)

            model_properties.clear()
            model_streets.clear()

            properties = DataExtractors.ExtractCadastralNrDataFromModel(model,header_names)
            
            ToBe_deleted_properties, cadasters = PropertiesGeneralQueries.get_properties_MyLabl_idsAndCadastrals(self, properties)
            #print(f"To be deleted properties: {len(ToBe_deleted_properties)}")
            #print(f"To be deleted properties: {len(cadasters)}")
            
            if len(cadasters) == 0:
                QMessageBox.warning(self,"Oops","Valitud kinnistuid Mailablis ei ole!")
                TabHandler.tabViewByState(tab_widget,True)
                tab_widget.hide()
                model_properties.clear()
                model_streets.clear()
                button.blockSignals(False)
                return
            else:        
                for unit in cadasters:
                    matching_rows = DataExtractors.CadasterMatcher(unit, model, header_names)
                
                    # Select the matching rows
                    for row in matching_rows:
                        table_target.setSelectionMode(QAbstractItemView.MultiSelection)
                        table_target.selectRow(row)
            
                tableFunctions.RemoveNonSelectedRowsFromTable(self, table_target)
                model_final = table_target.model()
            
                properties_final = DataExtractors.ExtractCadastralNrDataFromModel(model_final, header_names) 
                #print(f"Final values: {properties_final}")
                MapSelector.set_MapItemsByItemList_WithZoom(active_layer, properties_final, field)
                QCoreApplication.processEvents()
                
                deleteProperty.delete_multiple_items(self, ToBe_deleted_properties)
                Delete_finalProcess.clear_layer_from_deleted_items(self, active_cadastral_layer_name)
                text = f"Valitud kinnitsud eemaldati Mailablist ja kihilt {active_cadastral_layer_name} edukalt" 
                QMessageBox.information(self, "Tehtud", text)
                Delete_Main_Process.Delete_process_view_on_load(self)

                button.blockSignals(False)
                