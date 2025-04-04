from qgis.core import QgsProject, edit
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import  QMessageBox, QAbstractItemView
from PyQt5.QtCore import QCoreApplication
from ...app.View_tools import MapSelector, TableViewadjuster
from ...app.workspace_handler import TabHandler
from ..Tools import tableFunctions
from ..QstandardModelTools.QStandardModelHandler import ModelHeadersGenerator, CombineModels, DataExtractors
from ..DeletProcessUIActions import DeletProcessUIActions #Delete_finalProcess, 
from ...queries.python.property_data import PropertiesGeneralQueries, deleteProperty
from ...config.settings import SettingsDataSaveAndLoad
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...utils.messagesHelper import ModernMessageDialog


pealkiri = Headings()
class DeleteActions:
    
    def delete_selected_items_from_mylabl(self):
        active_cadastral_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        #print(active_cadastral_layer_name)
        active_layer = QgsProject.instance().mapLayersByName(active_cadastral_layer_name)[0]
        
        button = self.pbDel_PreConfirm
        table_properties = self.tbl_Delete_properties
        table_streets = self.tbl_Delete_streets
        table_target = self.tblvAllDeletable
        tab_widget = self.tabW_Delete_list
        field = Katastriyksus.tunnus
        
        data = tableFunctions.RemoveNonSelectedRowsFromTable(self, table_properties)
        data2 = tableFunctions.RemoveNonSelectedRowsFromTable(self, table_streets)
        
        if len(data) == 0 and len(data2) == 0:
            text = HoiatusTexts().kihil_kinnistu_valik
            heading = Headings().warningSimple
            ModernMessageDialog.Info_messages_modern(heading, text)
            return
        else:
            button.blockSignals(True)

            # Assuming table_properties and table_streets are QStandardItemModel objects
            model_properties = table_properties.model()
            model_streets = table_streets.model()

            header_names = ModelHeadersGenerator.generateHeadersFromExistingModel(model_properties)
            #print(f"headers created: {header_names}")
            # Get column names from the model

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(header_names)
            
            TabHandler.tabViewByState(tab_widget, state=False)        
            #print("tabView state")
            # Now that the new model is populated, you can set it to your table view
            table_target.setModel(model)
            TableViewadjuster.QTableView_look(table_target)
            # Insert data into the new model
            CombineModels.TableModelCombiner(model_properties,model_streets,model,header_names)
            #print("tables combined")
            model_properties.clear()
            model_streets.clear()
            #print("models cleared!")
            properties = DataExtractors.ExtractCadastralNrDataFromModel(model,header_names)
            print(f"Returned properties {properties}")
            ToBe_deleted_properties, cadasters = PropertiesGeneralQueries.get_properties_MyLabl_idsAndCadastrals(self, properties)
            print(f"To be deleted properties: {len(ToBe_deleted_properties)}")
            print(f"To be deleted properties: {len(cadasters)}")
            

        if len(cadasters) == 0:
            text = HoiatusTexts().kinnistuid_ei_leidnud
            heading = Headings().warningSimple
            ModernMessageDialog.Info_messages_modern(heading, text)
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
            MapSelector.set_MapItemsByItemList_WithZoom(active_layer, properties_final, field)
            QCoreApplication.processEvents()
            
            deleteProperty.delete_multiple_items(self, ToBe_deleted_properties)
            Delete_finalProcess.clear_layer_from_deleted_items(self, active_cadastral_layer_name)
            text = (f"Valitud kinnitsud eemaldati edukalt Mailablist ja kihilt:\n{active_cadastral_layer_name}")
            heading = pealkiri.infoSimple
            ModernMessageDialog.Info_messages_modern(heading,text)
            DeletProcessUIActions.Delete_process_view_on_load(self)

            button.blockSignals(False)


class Delete_finalProcess:
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