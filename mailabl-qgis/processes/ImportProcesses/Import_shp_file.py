import gc
import os

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QFileDialog
from qgis.core import QgsVectorLayer, QgsFeature, QgsLayerTreeGroup, QgsProject, QgsWkbTypes

from ...utils.ProgressHelper import ProgressDialogModern
from ...config.settings import Filepaths, SettingsDataSaveAndLoad, FilesByNames
from ...KeelelisedMuutujad.messages import Headings
from ...utils.messagesHelper import ModernMessageDialog
 
pealkiri = Headings()

import_subgroup_layer_name = 'Imporditavad kinnistud'



class SHPLayerLoader:
    def __init__(self, dialog):
        self.dialog = dialog
        self.label = self.dialog.lblSHPNewItems
    
    def load_shp_layer(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Shapefiles (*.shp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()
            file_path = file_path[0]
            if file_path:
                root = QgsProject.instance().layerTreeRoot()
                imporditavad_group = root.findGroup(import_subgroup_layer_name)

                if imporditavad_group is None:
                    imporditavad_group = QgsLayerTreeGroup(import_subgroup_layer_name)
                    root.insertChildNode(-1, imporditavad_group)
                else:
                    existing_layers = imporditavad_group.findLayers()
                    layer_name = os.path.splitext(os.path.basename(file_path))[0]
                    for existing_layer in existing_layers:
                        if existing_layer.layer().name() == layer_name:
                            QgsProject.instance().removeMapLayer(existing_layer.layer())

                ShapefileImporter.import_shp_file_as_memory_layer(file_path, imporditavad_group)

                text = (f"Andmed on edukalt imporditud ja lisatud\n{import_subgroup_layer_name}\ngrupi kihile")
                heading = pealkiri.infoSimple
                ModernMessageDialog.Info_messages_modern(heading, text)
                
                save_setting = SettingsDataSaveAndLoad()
                save_setting._save_SHP_layer_setting(self.label, layer_name)
                
                self.dialog.frMaaAmetControlls.setVisible(False)
                self.dialog.frPropertiFlowHolder.setVisible(True)
                self.dialog.pbConfirmAction.setEnabled(False)

class ShapefileImporter:
    @staticmethod
    def import_shp_file_as_memory_layer(file_path: str, group_layer: QgsLayerTreeGroup, progress=None):

        shp_layer_name = os.path.splitext(os.path.basename(file_path))[0]
        shapefile_layer = QgsVectorLayer(file_path, "shapefile_import", "ogr")
        if not shapefile_layer.isValid():
            return None

        # Get geometry type from input
        geometry_type = QgsWkbTypes.displayString(shapefile_layer.wkbType()).split()[0]  
        crs = shapefile_layer.crs()

        virtual_layer = QgsVectorLayer(f"{geometry_type}?crs={crs.authid()}", shp_layer_name, "memory")
        if not virtual_layer.isValid():
            return None

        total = shapefile_layer.featureCount()
        progress = ProgressDialogModern( title="Kihi importimine", maximum=total)
        progress.update(text1=f"Kihi {shp_layer_name} impordi edenemine")

        provider = virtual_layer.dataProvider()
        provider.addAttributes(shapefile_layer.fields())
        virtual_layer.updateFields()
        
        quarter, half, three_quarter = total // 4, total // 2, total * 3 // 4
        
        features_to_add = []

        for i, feat in enumerate(shapefile_layer.getFeatures()):
            features_to_add.append(feat)
           
            if i % 1000 == 0 or i in (quarter, half, three_quarter):
                provider.addFeatures(features_to_add)
                features_to_add.clear()
                progress.update(value=i)
            if i == quarter:
                provider.addFeatures(features_to_add)       
                features_to_add.clear()
                progress.update(text2="Nüüd siruta varbaid")
            elif i == half:
                provider.addFeatures(features_to_add)
                features_to_add.clear()
                progress.update(text2="Pool teed läbitud - ära magama jää!")
            elif i == three_quarter:
                provider.addFeatures(features_to_add)
                features_to_add.clear()
                progress.update(text2="Natuke veel minna - jõuad mõned kükid teha")

        provider.addFeatures(features_to_add)
        features_to_add.clear()
        progress.update(value=total)
        QCoreApplication.processEvents()

        progress.update(value=1, maximum=6, text1="Andmete kinnitamine")
        virtual_layer.commitChanges()
        progress.update(value=2)
        virtual_layer.updateExtents()
        progress.update(value=3, text1="Andmete indekseerimine")
        provider.createSpatialIndex()
        progress.update(value=4, text1="Kujundan kaardi")
        # Apply style
        style_path = Filepaths.get_style(FilesByNames().MaaAmet_import)
        virtual_layer.loadNamedStyle(style_path)
        progress.update(value=5)
        if virtual_layer.isValid():
            QgsProject.instance().addMapLayer(virtual_layer, False)
            group_layer.insertLayer(0, virtual_layer)
        progress.update(value=6, text1="Kiht on valmis!")
        progress.close()
        del shapefile_layer, virtual_layer
        gc.collect()
