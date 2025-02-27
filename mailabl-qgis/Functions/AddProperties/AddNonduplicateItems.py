#AddNonDuplicateItems.py


from PyQt5.QtWidgets import QMessageBox
from qgis.core import QgsProject
from PyQt5.QtCore import QCoreApplication
from ...app.View_tools import MapSelector
from ..Tools import tableFunctions
from ...config.settings import SettingsDataSaveAndLoad
from ...queries.python.property_data import MyLablChecker
from PyQt5.QtGui import QStandardItemModel
from ..QstandardModelTools.QStandardModelHandler import ModelHeadersGenerator, CombineModels, DataExtractors
from ...app.workspace_handler import TabHandler
from PyQt5.QtWidgets import QAbstractItemView
from ...Functions.add_items import Add_Properties_final
from ...Functions.layer_generator import LayerCopier
from ...KeelelisedMuutujad.messages import Headings
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...config.settings import SettingsDataSaveAndLoad
from .AddProperties_dev import AddProperties_dev


pealkiri = Headings()

table_data = tableFunctions
checker = MyLablChecker()
load = SettingsDataSaveAndLoad()


class AddProperties:
    @staticmethod
    def check_for_duplicates_and_add_only_matches(self):
        # Load necessary layers and prepare setup
        #print(f"shp layer: {input_layer_name}")
        #print(f"shp layer: {input_layer_name}")

        button = self.pbConfirm_action
        table_properties = self.tblvResults_Confirm
        table_streets = self.tblvResults_streets_Confirm
        table_target = self.tblNew
        tab_widget = self.tabWidget_Propertie_list
        
        data_properties = table_data.RemoveNonSelectedRowsFromTable(self, table_properties)
        print(f"data_properties: {data_properties}")
        data_streets = table_data.RemoveNonSelectedRowsFromTable(self, table_streets)
        print(f"data_streets: {data_streets}")


        if len(data_properties) == 0 and len(data_streets) == 0:
            text = ("Vali importimiseks vähemalt üks kinnistu")
            heading = pealkiri.warningSimple
            QMessageBox.warning(self,heading,text)
            return
        else:
            button.blockSignals(True)
            model_properties = table_properties.model()
            model_streets = table_streets.model()
            
            header_names = ModelHeadersGenerator.generateHeadersFromExistingModel(model_properties)
            # Get column names from the model

            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(header_names)
            
            # Now that the new model is populated, you can set it to your table view
            table_target.setModel(model)        
            # Insert data into the new model
            CombineModels.TableModelCombiner(model_properties,model_streets,model,header_names)
            model_properties.clear()
            model_streets.clear()

            properties = DataExtractors.ExtractCadastralNrDataFromModel(model,header_names)
            TabHandler.tabViewByState(tab_widget, state=False)
            
            #print(f"Selected properties in table {properties}")
            #print(f"Returned properties: {len(properties)}")
        
            ToBe_imported_properties = checker.process_data_in_batches_with_progress(properties)
            #print(f"To be imported properties: {len(ToBe_imported_properties)}")
            active_layer_name,input_layer_name = AddProperties_dev.load_import_and_activ_layers(self)

            if len(ToBe_imported_properties) == 0:
                text = ("Kõik valitud kinnistud on juba Mailablis")
                heading = pealkiri.informationSimple
                QMessageBox.warning(self,heading,text)
                TabHandler.tabViewByState(tab_widget,True)
                tab_widget.hide()
                model_properties.clear()
                model_streets.clear()
                button.blockSignals(False)
                return
            else:        
                for unit in ToBe_imported_properties:
                    matching_rows = DataExtractors.CadasterMatcher(unit, model, header_names)
                
                    # Select the matching rows
                    for row in matching_rows:
                        table_target.setSelectionMode(QAbstractItemView.MultiSelection)
                        table_target.selectRow(row)
            
                table_data.RemoveNonSelectedRowsFromTable(self, table_target)
                model_final = table_target.model()
            
                properties_final = DataExtractors.ExtractCadastralNrDataFromModel(model_final, header_names) 
                #print(f"Final values: {properties_final}")
                field = Katastriyksus.tunnus #"TUNNUS"

                input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]

                MapSelector.set_MapItemsByItemList_WithZoom(input_layer, properties_final, field)
                QCoreApplication.processEvents()
                    
                Add_Properties_final.insert_selected_items_to_Mailabl(self, table_target, input_layer_name)
                LayerCopier.append_data(self, input_layer_name, active_layer_name)
                model_properties.clear()
                model_streets.clear()
                model_final.clear()
                text = "Andmed on laetud ja kaardikihile kantud"
                heading = pealkiri.tubli
                QMessageBox.information(self, heading, text)
            
        button.blockSignals(False)
