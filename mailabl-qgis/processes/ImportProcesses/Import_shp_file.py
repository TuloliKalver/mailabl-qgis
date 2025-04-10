import gc
import os
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QFileDialog
from qgis.core import QgsVectorLayer, QgsFeature, QgsSpatialIndex, QgsLayerTreeGroup, QgsGeometry, QgsProject
from ...utils.ProgressHelper import ProgressDialogModern
from ...config.settings import Filepaths, SettingsDataSaveAndLoad, FilesByNames
from ...KeelelisedMuutujad.messages import Headings
from ...utils.messagesHelper import ModernMessageDialog
 
pealkiri = Headings()

import_subgroup_layer_name = 'Imporditavad kinnistud'


class SpatialIndexCreator:
    @staticmethod
    def create_spatial_index(layer):
        index = QgsSpatialIndex()
        features = layer.getFeatures()
        for feature in features:
            index.addFeature(feature)
            QCoreApplication.processEvents()
        return index


class SHPLayerLoader:
    def __init__(self, dialog):
        self.dialog = dialog
        self.label = self.dialog.lblSHPNewItems
    
    def load_shp_layer(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Shapefiles (*.shp)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                root = QgsProject.instance().layerTreeRoot()
                imporditavad_group = root.findGroup(import_subgroup_layer_name)

                if imporditavad_group is None:
                    imporditavad_group = QgsLayerTreeGroup(import_subgroup_layer_name)
                    root.insertChildNode(-1, imporditavad_group)
                else:
                    existing_layers = imporditavad_group.findLayers()
                    for file_path in selected_files:
                        layer_name = file_path.split('/')[-1].split('.')[0]
                        for existing_layer in existing_layers:
                            if existing_layer.layer().name() == layer_name:
                                QgsProject.instance().removeMapLayer(existing_layer.layer())

                ShapefileImporter.import_shpFile_as_virtual_layer(file_path, imporditavad_group)

                text = (f"Andmed on edukalt imporditud ja lisatud\n{import_subgroup_layer_name}\ngrupi kihile")
                heading = pealkiri.infoSimple
                ModernMessageDialog.Info_messages_modern(heading, text)
                
                save_setting = SettingsDataSaveAndLoad()
                save_setting.save_SHP_layer_setting(self.label, layer_name)
                
                self.dialog.frMaaAmetControlls.setVisible(False)
                self.dialog.frPropertiFlowHolder.setVisible(True)
                self.dialog.pbConfirmAction.setEnabled(False)
    @staticmethod
    def add_spatial_index_to_layer(layer_name):
        layers = QgsProject.instance().mapLayersByName(layer_name)
        if layers:
            layer = layers[0]
            if layer is not None and layer.isValid():
                #progress = ProgressDialogModern(maximum=0)
                #progress.load_progress_dialog(title = f"Indekseerin kihi {layer_name} andmed ")
                layer.dataProvider().createSpatialIndex()
                QCoreApplication.processEvents()
                #progress.close()

class ShapefileImporter:
    @staticmethod
    def import_shpFile_as_virtual_layer(file_path, group_layer):
        gc.collect()
        shp_layer_name = file_path.split('/')[-1].split('.')[0]
        shapefile_layer = QgsVectorLayer(file_path, "shapefile_import", "ogr")
        if not shapefile_layer.isValid():
            return None
        crs = shapefile_layer.crs()
        virtual_layer = QgsVectorLayer("Polygon?crs=" + crs.authid(), shp_layer_name, "memory")
        if not virtual_layer.isValid():
            return None

        total_rows = shapefile_layer.featureCount()

        progress = ProgressDialogModern(title="Kihi importimine", maximum=total_rows)
        progress.update(text1=f"Kihi {shp_layer_name} impordi edenemine")
        QCoreApplication.processEvents()

        fields = shapefile_layer.fields()
        virtual_layer_provider = virtual_layer.dataProvider()
        virtual_layer_provider.addAttributes(fields)
        virtual_layer.updateFields()

        count = 0
        for feature in shapefile_layer.getFeatures():
        
            attrs = feature.attributes()
            geom = feature.geometry()

            new_feature = QgsFeature()
            new_feature.setAttributes(attrs)
            new_feature.setGeometry(QgsGeometry(geom))
            virtual_layer_provider.addFeature(new_feature)

            count += 1
            quarter_point = total_rows // 4
            halfway_point = total_rows // 2
            three_quarter_point = total_rows * 3 // 4
            progress.update(value=count)
            if count == quarter_point:
                progress.update(text2 = "Nüüd siruta varbaid")
            elif count == halfway_point:
                progress.update(text2 ="Pool teed läbitud - ära magama jää!")
            elif count == three_quarter_point:
                progress.update(text2 = "Natuke veel minna - jõuad mõned kükid teha")
        QCoreApplication.processEvents()


        virtual_layer.commitChanges()
        virtual_layer.updateExtents()
        virtual_layer.dataProvider().createSpatialIndex()
        add_style = Filepaths.get_style(FilesByNames().MaaAmet_import)
        virtual_layer.loadNamedStyle(add_style)
        if virtual_layer.isValid():
            QgsProject.instance().addMapLayer(virtual_layer, False)
            group_layer.insertLayer(0, virtual_layer)

        progress.close()

        del shapefile_layer
        del virtual_layer
        gc.collect()

