import os
from qgis.core import QgsVectorLayer, QgsProject, QgsCoordinateReferenceSystem, QgsVectorFileWriter
from qgis.core import QgsVectorLayer, QgsProject, QgsFeature
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from..config.settings import Filepaths
from ..config.settings import connect_settings_to_layer
from PyQt5.uic import loadUi
from ..config.settings import Filepaths
from PyQt5.QtCore import QCoreApplication

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))



class LayerCopier():

    def __init__(self):
        super(LayerCopier, self).__init__()
        
    @staticmethod
    def StartSaving_virtual_Layer(self, memory_layer_name, new_layer_name, group_layer_name):
        print(f"add memory layer: {memory_layer_name}")
        print(f"new_layer_name: {new_layer_name}")
        print(f"group_layer_name: {group_layer_name}")
        #layer names and other variables
        #TODO add layer storing fixed location

        # User can select a folder to save file!
        selected_folder = LayerCopier.user_folder_location_path()
        #print(f"File will be saved into: {selected_folder}")
        if selected_folder is None:
            # User canceled the folder selection, handle accordingly
            QMessageBox.information(None, "Tähelepanu!", "User canceled the folder selection. Process canceled.")
            return  # or raise an exception or perform other actions as needed
        input_layer = QgsProject.instance().mapLayersByName(memory_layer_name)[0]
        #iface.activeLayer(input_layer)
        
        
        # Specify the output GeoPackage file path
        output_file_name = (f"{new_layer_name}.gpkg")
        output_file_path = os.path.join(selected_folder, output_file_name)
        #print(f"File '{output_file_path}' path is set.")

        # Check if the GeoPackage file already exists
        if os.path.exists(output_file_path):
            # File already exists, delete it
            try:
                os.remove(output_file_path)
                QMessageBox.information(None, "Tähelepanu!", f"Varasem samanimeline fail kustutati: '{output_file_path}'")
            except OSError as e:
                QMessageBox.critical(None, "Viga!!!", f"Ei saa faili '{output_file_path}' kustutada: {e}")
                # Handle the error as needed
        else:
            #print("started generating file")
            driver_name = 'GPKG'
            file_encoding = 'UTF-8'
            source_crs = input_layer.crs()
            dest_crs = QgsCoordinateReferenceSystem(source_crs)
            # Use QgsVectorFileWriter.writeAsVectorFormat to save the layer to GeoPackage
            result, error_message = QgsVectorFileWriter.writeAsVectorFormat(
                input_layer,
                output_file_path,
                file_encoding,
                dest_crs,
                driver_name,
                onlySelected=False,  # Set to True if you want to save only selected features
                skipAttributeCreation=False,  # Set to True if you only want to write geometries
            )
            # Check the result and print the error message if any
            if result == QgsVectorFileWriter.NoError:
                pass #QMessageBox.information(None, "Information","Layer saved successfully!")

            else:
                QMessageBox.information(None, "Tähelepanu!",f"Kihi salvestamine ebaõnnestus: {error_message}")
                
            # Check if the GeoPackage file exists
            if os.path.exists(output_file_path):
                # Create a QgsVectorLayer from the GeoPackage file
                new_layer = QgsVectorLayer(output_file_path, new_layer_name, 'ogr')
                # Check if the layer was successfully loaded
                if new_layer.isValid():
                    # Get the group layer or create it if it doesn't exist
                    root = QgsProject.instance().layerTreeRoot()
                    group = root.findGroup(group_layer_name)
                    if group is None:
                        group = root.addGroup(group_layer_name)
                    
                    QgsProject.instance().addMapLayer(new_layer, False)
                    group.insertLayer(0, new_layer)

                else:
                    QMessageBox.information(None, "Tähelepanu!",f"Error loading the new layer from '{output_file_path}'")
            
                #Remove layer if it exists
                if QgsProject.instance().mapLayersByName(memory_layer_name):
                    memory_layer = QgsProject.instance().mapLayersByName(memory_layer_name)
                    if memory_layer:
                        layer_id = memory_layer[0].id()
                        QgsProject.instance().removeMapLayer(layer_id)
                        print(f"Memory layer '{memory_layer_name}' removed successfully.")
                
            
                QGIS_Layer_style = Filepaths().File_maaAmet_style()
                updated_layer = QgsProject.instance().mapLayersByName(new_layer_name)[0]
                updated_layer.loadNamedStyle(QGIS_Layer_style)
                updated_layer.triggerRepaint()
                QMessageBox.information(None, "Tähelepanu!", f"Paremaks toimimiseks toimub kihi '{new_layer.name()}' indekseerimine.")
                updated_layer.dataProvider().createSpatialIndex()

                QMessageBox.information(None, "Tähelepanu!",f"Kaardikiht on lisatud kaardikihtide alamgruppi 'Mailabl settings/Uued kinnistud/{new_layer.name()}'.")                
                
            else:
                QMessageBox.information(None, "Tähelepanu!", f"'GPKG' tüüpi faili asukohas '{output_file_path}' ei leitud.")

    @staticmethod
    def copy_virtual_layer_for_properties(new_layer_name):
        # Get the group layer or create it if it doesn't exist
        root = QgsProject.instance().layerTreeRoot()
        group_layer_name = 'Uued kinnistud'
        group = root.findGroup(group_layer_name)
        if group is None:
            group = root.addGroup(group_layer_name)
        memory_layer_name = f"{new_layer_name}-memory"
        if QgsProject.instance().mapLayersByName(memory_layer_name):
            memory_layer = QgsProject.instance().mapLayersByName(memory_layer_name)
            if memory_layer:
                layer_id = memory_layer[0].id()
                QgsProject.instance().removeMapLayer(layer_id)
                print(f"Memory layer '{memory_layer_name}' removed successfully.")

        layer_name = connect_settings_to_layer.Import_Layer_name()
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]

        # Create the memory layer
        new_layer = QgsVectorLayer('Polygon?crs=' + layer.crs().authid(), f"{new_layer_name}-memory", 'memory')
        new_layer.dataProvider().addAttributes(layer.fields())
        new_layer.updateFields()
        new_layer.setExtent(layer.extent())
        new_layer.setCrs(layer.crs())
        QGIS_Layer_style = Filepaths().File_MaaAmet_temporary_style()
        new_layer.loadNamedStyle(QGIS_Layer_style)
        new_layer.triggerRepaint()

        # Add the memory layer to the group
        QgsProject.instance().addMapLayer(new_layer, False)  # Add without prompting
        group.insertLayer(0, new_layer)
    
        return f"{new_layer_name}-memory"
    
    
    @staticmethod
    def user_folder_location_path():
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.Directory)

        ## Open the file dialog and get the selected folder
        selected_folder = file_dialog.getExistingDirectory(None, "Valik asukoht kuhu aluskaardi fail salvestatakse!", '', QFileDialog.ShowDirsOnly)

        if selected_folder:
            return selected_folder
        else:
            QMessageBox.information(None, "Tähelepanu!","Laadimisprotsess katkestatud.")
            return None
        
    # This function creates spatial indexes for a given layer
    #TODO add spatial index functionality


    
    def generate_data_from_source(source_layer):
        # Get the source layer
        source_layer = QgsProject.instance().mapLayersByName(source_layer)[0]

        # Check if the source layer is valid
        if not source_layer:
            print("Invalid source layer specified.")
            return

        # Get a sample feature from the source layer (you can modify this as needed)
        sample_feature = next(source_layer.getFeatures())

        # Create a dictionary to store generated data
        generated_data = {}

        # Generate data for each field based on the sample feature
        for field in source_layer.fields():
            field_name = field.name()

            # Use the sample feature's value for the first feature found in the source layer
            generated_data[field_name] = sample_feature[field_name]

            # You can modify this part to generate different data if needed

        return generated_data


    def append_data(self,source_layer_name, target_layer_name):
        # Get the source and target layers
        #print(f"input layer: {source_layer_name}")
        #print(f"target layer: {target_layer_name}")
        
        source_layer = QgsProject.instance().mapLayersByName(source_layer_name)[0]
        target_layer = QgsProject.instance().mapLayersByName(target_layer_name)[0]
        # Check if the layers are valid
        if not source_layer or not target_layer:
            print("Invalid layers specified.")
            return
        # Start editing the target layer
        target_layer.startEditing()
        # Select all features in the layer
        source_layer.selectAll()
        # Get selected features from the source layer
        selected_features = source_layer.selectedFeatures()
        #print(f"in 'append data' Total features: {len(selected_features)}")
        
        
        if selected_features == 0:
            QMessageBox.warning(self, "errorr", "Ühtegi kinnistut ei leitud")

        count = 1
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_widget.setWindowTitle("Lisan kinnistuid")
        progress_bar.setMaximum(len(selected_features))
        progress_bar.setValue(count)
        progress_widget.show()

        for source_feature in selected_features:
            # Create a new feature for the target layer
            #print(f"Loop {loop}")
            new_feature = QgsFeature(target_layer.fields())

            # Set data for each field from the source feature to the target feature
            for field in target_layer.fields():
                field_name = field.name()
                # Check if the field exists in the source feature
                if field_name in source_feature.fields().names():
                    new_feature[field_name] = source_feature[field_name]

            # Set geometry for the target feature
            new_feature.setGeometry(source_feature.geometry())

            # Add the new feature to the target layer
            target_layer.addFeature(new_feature)

            count +=1
            progress_bar.setValue(count)
            QCoreApplication.processEvents()
        # Commit changes to the target layer for each selected feature
        target_layer.commitChanges()
        #print("Selected features added to the target layer.")
        progress_widget.hide()
        