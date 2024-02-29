import os
from qgis.core import QgsVectorLayer, QgsFeature, QgsSpatialIndex, QgsLayerTreeGroup, QgsGeometry, QgsProject
from PyQt5.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from ...config.settings import Filepaths, SettingsDataSaveAndLoad

# Declare catalogs and links
# Main directory
plugin_dir = os.path.dirname(__file__)

# Style setup folder
style_path = Filepaths().File_maaAmet_style()

# Status bar widget folder
widgets_folder = "widgets"
widgets_path = os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui")

# Layer names and other variables
import_subgroup_layerName = 'Imporditavad kinnistud'


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
    @staticmethod
    def load_shp_layer(label):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Shapefiles (*.shp)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                root = QgsProject.instance().layerTreeRoot()
                imporditavad_group = root.findGroup(import_subgroup_layerName)

                if imporditavad_group is None:
                    imporditavad_group = QgsLayerTreeGroup(import_subgroup_layerName)
                    root.insertChildNode(-1, imporditavad_group)
                else:
                    existing_layers = imporditavad_group.findLayers()
                    for file_path in selected_files:
                        layer_name = file_path.split('/')[-1].split('.')[0]
                        for existing_layer in existing_layers:
                            if existing_layer.layer().name() == layer_name:
                                QgsProject.instance().removeMapLayer(existing_layer.layer())

                ShapefileImporter.import_shpFile_as_virtual_layer(file_path, imporditavad_group)
                text = (f"Andmed on edukalt imporditud ja lisatud '{import_subgroup_layerName}' grupi kihile")
                heading = "Import on lõppenud"
                QMessageBox.information(None, heading, text)
                save_setting = SettingsDataSaveAndLoad()
                save_setting.save_SHP_layer_setting(label, layer_name)

    @staticmethod
    def add_spatial_index_to_layer(layer_name):
        layers = QgsProject.instance().mapLayersByName(layer_name)
        if layers:
            layer = layers[0]
            if layer is not None and layer.isValid():
                total_features = layer.featureCount()
                progress_widget = UtilityFunctions.create_progress_widget()
                progress_bar = progress_widget.testBar
                progress_bar.setMinimum(0)
                progress_bar.setMaximum(100)
                progress_widget.show()
                QCoreApplication.processEvents()

                count = 0
                for processed_features in range(1, total_features + 1):
                    progress_percentage = int((processed_features / total_features) * 100)
                    progress_bar.setValue(progress_percentage)
                    QCoreApplication.processEvents()

                layer.dataProvider().createSpatialIndex()
                progress_widget.close()

    @staticmethod
    def create_progress_widget(name, label_1):
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_widget.label.setText(name)
        progress_widget.label_2.setText(label_1)
        return progress_widget


class ShapefileImporter:
    @staticmethod
    def import_shpFile_as_virtual_layer(file_path, group_layer):
        shp_layer_name = file_path.split('/')[-1].split('.')[0]
        shapefile_layer = QgsVectorLayer(file_path, "shapefile_import", "ogr")
        if not shapefile_layer.isValid():
            return None

        crs = shapefile_layer.crs()
        virtual_layer = QgsVectorLayer("Polygon?crs=" + crs.authid(), shp_layer_name, "memory")
        if not virtual_layer.isValid():
            return None

        total_rows = shapefile_layer.featureCount()

        progress_widget = SHPLayerLoader.create_progress_widget("Kihi importimine", "Kihi impordi edenemine")
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total_rows)
        progress_widget.show()
        QCoreApplication.processEvents()

        fields = shapefile_layer.fields()
        virtual_layer_provider = virtual_layer.dataProvider()
        virtual_layer_provider.addAttributes(fields)
        virtual_layer.updateFields()

        count = 0
        for feature in shapefile_layer.getFeatures():
            count += 1
            progress_bar.setValue(count)

            attrs = feature.attributes()
            geom = feature.geometry()

            new_feature = QgsFeature()
            new_feature.setAttributes(attrs)
            new_feature.setGeometry(QgsGeometry(geom))
            virtual_layer_provider.addFeature(new_feature)

            UtilityFunctions.update_progress_label(progress_widget, count, total_rows)

            QCoreApplication.processEvents()

        virtual_layer.commitChanges()
        virtual_layer.updateExtents()
        virtual_layer.dataProvider().createSpatialIndex()
        progress_widget.hide()

        add_style = os.path.join(plugin_dir, style_path)
        virtual_layer.loadNamedStyle(add_style)
        if virtual_layer.isValid():
            QgsProject.instance().addMapLayer(virtual_layer, False)
            group_layer.insertLayer(0, virtual_layer)

        del shapefile_layer
        del progress_widget
        del virtual_layer


class UtilityFunctions:
    @staticmethod
    def create_progress_widget():
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_widget.label.setText("Indekseerin laetud kihti!")
        progress_widget.label_2.setText("Ruumiliselt indekseeritud kaardikihid on töökindlamad")
        return progress_widget

    @staticmethod
    def update_progress_label(progress_widget, current_count, total_rows):
        quarter_point = total_rows // 4
        halfway_point = total_rows // 2
        three_quarter_point = total_rows * 3 // 4

        if current_count == quarter_point:
            progress_widget.label_2.setText("Nüüd siruta varbaid")
        elif current_count == halfway_point:
            progress_widget.label_2.setText("Pool teed läbitud - ära magama jää!")
        elif current_count == three_quarter_point:
            progress_widget.label_2.setText("Natuke veel minna - jõuad mõned kükid teha")

        QCoreApplication.processEvents()