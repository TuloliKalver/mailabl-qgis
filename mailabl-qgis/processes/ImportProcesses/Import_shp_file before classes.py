import os
from qgis.core import QgsVectorLayer
from qgis.core import QgsFeature, QgsSpatialIndex, QgsLayerTreeGroup, QgsGeometry, QgsProject, QgsVectorLayer
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from ...config.settings import Filepaths, SettingsDataSaveAndLoad
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import QgsFeatureRequest
from ...processes.infomessages.messages import Headings
 
heading = Headings()

#declare catalouges and links
#main directory
plugin_dir = os.path.dirname(__file__)

#style setup folder
#style_folder = "QGIS_styles" 
#style_path = os.path.join(style_folder, "Maa_amet_import_2.qml")
style_path = Filepaths().File_maaAmet_style()

#Status bar widget folder
widgets_folder = "widgets"  
widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")

#layer names and other variables
import_subgroup_layerName = 'Imporditavad kinnistud'



# This function creates spatial indexes for a given layer
def create_spatial_index(layer):
    index = QgsSpatialIndex()
    features = layer.getFeatures()
    for feature in features:
        index.addFeature(feature)
        QCoreApplication.processEvents()
    return index


#This is the main function responsible for loading shapefile layers into the QGIS project
def load_shp_layer(label):
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    file_dialog.setNameFilter("Shapefiles (*.shp)")
    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            # Check if the group layer "Imporditavad kinnistud" already exists
            root = QgsProject.instance().layerTreeRoot()
            imporditavad_group = root.findGroup(import_subgroup_layerName)

            if imporditavad_group is None:
                # Create a new group layer named "Imporditavad kinnistud"
                imporditavad_group = QgsLayerTreeGroup(import_subgroup_layerName)
                root.insertChildNode(-1, imporditavad_group)
            else:
                # Remove existing layers with the same name as the layers in "Imporditavad kinnistud"
                existing_layers = imporditavad_group.findLayers()
                for file_path in selected_files:
                    layer_name = file_path.split('/')[-1].split('.')[0] #get layer name from file name
                    for existing_layer in existing_layers:
                        if existing_layer.layer().name() == layer_name:
                            QgsProject.instance().removeMapLayer(existing_layer.layer())

                import_shpFile_AS_virtualLayer(file_path, imporditavad_group)
            text = (f"Andmed on edukalt imporditud ja lisatud\n{import_subgroup_layer_name}\ngrupi kihile")
            heading = "Tehtud"    
            QMessageBox.information(None, heading,text)
        save_setting = SettingsDataSaveAndLoad()
        save_setting.save_SHP_layer_setting(label, layer_name)


            
def add_spatialIndex_to_layer(self, layer_name):
    # Retrieve the layer by name from the QgsProject
    name = "Indekseerin laetud kihti!"
    label_1 = "Ruumiliselt indekseeritud kaardikihid on töökindlamad"
    #print("lae progress_bar")
    progress_widget = loadUi(widgets_path)
    #print("laadisin progress_bari")
    progress_bar = progress_widget.testBar
    progress_widget.label.setText(name)
    progress_widget.label_2.setText(label_1)
    #progress_widget.label_3.setText(label_2)
    
    progress_bar.setMinimum(0)# Set the maximum value of the progress bar
    progress_bar.setMaximum(100)  # Set the maximum value of the progress bar (assuming 0 to 100%)
    progress_widget.show()
    QCoreApplication.processEvents()

    layers = QgsProject.instance().mapLayersByName(layer_name)
    #print(f"layer {layers}")
    if layers:
        layer = layers[0]  # Assuming there's only one layer with this name
        if layer is not None and layer.isValid():
            # Inform the user that indexing is starting
            total_features = layer.featureCount()
            #print(total_features)
            processed_features = 0

            while processed_features < total_features:
                processed_features += 1  # 
                progress_percentage = int((processed_features / total_features) * 100)
                #print(progress_percentage)
                progress_bar.setValue(progress_percentage)
                QCoreApplication.processEvents()
            # Create spatial index for the layer's geometry        
            layer.dataProvider().createSpatialIndex()
            progress_widget.close()



# Imports shapefile data in batches and returns a virtual layer.
def import_shpFile_AS_virtualLayer(file_path, group_layer):  #temporary removed batch_size, for testing purpose
    shp_layer_name = file_path.split('/')[-1].split('.')[0]
    shapefile_layer = QgsVectorLayer(file_path, "shapefile_import", "ogr")
    #print(shapefile_layer)
    if not shapefile_layer.isValid():
        return None
    
    # Get the CRS from the shapefile
    crs = shapefile_layer.crs()

    virtual_layer = QgsVectorLayer("Polygon?crs=" + crs.authid(), shp_layer_name, "memory")
    #print(virtual_layer)
    if not virtual_layer.isValid():
        return None
    
    total_rows = shapefile_layer.featureCount()
    quarter_point = total_rows // 4  # Calculate the quarter point
    halfway_point = total_rows // 2  # Calculate the halfway point
    three_quarter_point = total_rows * 3 // 4  # Calculate the three-quarter point

    virtual_layer_provider = virtual_layer.dataProvider()
    #print(f"virtual_layer_provider = '{virtual_layer_provider}'")

    count = 0
    batch_count = 0

    # Load the custom progress widget from the .ui file
    ui_file_path = widgets_path
    #print(ui_file_path)
    progress_widget = loadUi(ui_file_path)
    progress_bar = progress_widget.testBar
    progress_bar.setMaximum(total_rows)  # Set the maximum value of the progress bar
    progress_widget.show()

    fields = shapefile_layer.fields()

    virtual_layer_provider.addAttributes(fields)  # Add fields to the virtual layer
    virtual_layer.updateFields()  # Update fields in the virtual layer

    for feature in shapefile_layer.getFeatures():
        if count == 0:
            progress_widget.label_2.setText("Kas sa täna kohvi oled juba joonud?")  # Update the label content
            batch_count += 1

        attrs = feature.attributes()
        geom = feature.geometry()

        new_feature = QgsFeature()
        new_feature.setAttributes(attrs)
        new_feature.setGeometry(QgsGeometry(geom))
        virtual_layer_provider.addFeature(new_feature)

        count += 1

        # Update the progress bar value based on the current count
        progress_bar.setValue(count)

        # Update the label content at different progress points
        if count == quarter_point:
            progress_widget.label_2.setText("Nüüd siruta varbaid")
        elif count == halfway_point:
            progress_widget.label_2.setText("Pool teed läbitud - ära magama jää!")
        elif count == three_quarter_point:
            progress_widget.label_2.setText("Natuke veel minna - jõuad mõned kükid teha")

        # Refresh QGIS interface
        QCoreApplication.processEvents()

    # Hide the custom progress widget when done
    
    virtual_layer.commitChanges()
    virtual_layer.updateExtents()
    virtual_layer.dataProvider().createSpatialIndex()
    progress_widget.hide()

    # Load the layer style file
    add_style = os.path.join(plugin_dir, style_path)
    virtual_layer.loadNamedStyle(add_style)
    if virtual_layer.isValid():
        #memory_layer_name = os.path.basename(file_path).split('.')[0]
        QgsProject.instance().addMapLayer(virtual_layer, False)
        group_layer.insertLayer(0, virtual_layer)

    del shapefile_layer
    #del virtual_layer_provider
    del progress_widget
    del virtual_layer




