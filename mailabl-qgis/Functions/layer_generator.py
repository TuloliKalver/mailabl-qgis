#layer_generator.py

import os

from qgis.core import QgsVectorLayer, QgsProject, QgsCoordinateReferenceSystem, QgsVectorFileWriter, QgsFeature
from qgis.core import QgsFeature, QgsExpression, QgsExpressionContext, QgsExpressionContextUtils

from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from ..config.settings import Filepaths, FilesByNames, connect_settings_to_layer
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts ,HoiatusTextsAuto, Salvestamisel
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus

pealkiri = Headings()

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))



class LayerCopier():
    def __init__(self):
        super(LayerCopier, self).__init__()
        
    @staticmethod
    def StartSaving_virtual_Layer( memory_layer_name, new_layer_name, group_layer_name):
        #print(f"add memory layer: {memory_layer_name}")
        #print(f"new_layer_name: {new_layer_name}")
        #print(f"group_layer_name: {group_layer_name}")
        
        # User can select a folder to save file!
        selected_folder = LayerCopier.user_folder_location_path()
        #print(f"File will be saved into: {selected_folder}")
        if selected_folder is None:
            # User canceled the folder selection, handle accordingly
            text = HoiatusTexts().kasutaja_peatas_protsessi
            heading = pealkiri.informationSimple
            QMessageBox.information(None, heading, text)
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
                text = HoiatusTextsAuto.deleted_output_file_sucess(output_file_path)
                heading = pealkiri.warningSimple
                QMessageBox.information(None, heading, text)
            except OSError as e:
                heading = Headings().warningCritical
                text = HoiatusTextsAuto.unable_to_delete_output_file(output_file_path, e)
                QMessageBox.critical(None, heading, text)
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
                heading = pealkiri.warningSimple
                text = HoiatusTextsAuto.save_layer_error(error_message)
                QMessageBox.information(None,text,heading)
                
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
                    text = HoiatusTextsAuto.load_layer_error(output_file_path)
                    heading = pealkiri.warningSimple
                    QMessageBox.information(None,heading,text)
            
                #Remove layer if it exists
                if QgsProject.instance().mapLayersByName(memory_layer_name):
                    memory_layer = QgsProject.instance().mapLayersByName(memory_layer_name)
                    if memory_layer:
                        layer_id = memory_layer[0].id()
                        QgsProject.instance().removeMapLayer(layer_id)
                        print(HoiatusTextsAuto.deleted_output_file_sucess(memory_layer_name))
                
                

                
                updated_layer = QgsProject.instance().mapLayersByName(new_layer_name)[0]
                
                QGIS_Layer_style = Filepaths().get_style(FilesByNames().MaaAmet_import)
                updated_layer.loadNamedStyle(QGIS_Layer_style)
                updated_layer.triggerRepaint()
                text = HoiatusTextsAuto.layer_indexing(new_layer_name)
                heading = pealkiri.informationSimple
                QMessageBox.information(None, heading, text)
                updated_layer.dataProvider().createSpatialIndex()
                text = HoiatusTextsAuto.generated_layer_in_subgroup(new_layer_name, group_layer_name)
                heading = pealkiri.informationSimple
                QMessageBox.information(None, heading,text)                
                
            else:
                text = HoiatusTextsAuto.load_gpkg_file_error(output_file_path)
                heading = pealkiri.informationSimple
                QMessageBox.information(None, heading, text)

    @staticmethod
    def copy_virtual_layer_for_properties(new_layer_name, group_name):
        # Get the group layer or create it if it doesn't exist
        root = QgsProject.instance().layerTreeRoot()
        
        group = root.findGroup(group_name)
        if group is None:
            group = root.addGroup(group_name)
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
        style_name = FilesByNames().MaaAmet_temp
        QGIS_Layer_style = Filepaths().get_style(style_name)
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
        selected_folder = file_dialog.getExistingDirectory(None, Salvestamisel().vali_kausta_asukoht, '', QFileDialog.ShowDirsOnly)

        if selected_folder:
            return selected_folder
        else:
            text = HoiatusTexts().laadimine_error
            heading = pealkiri.informationSimple
            QMessageBox.information(None, heading,text)
        return None
    
    
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
            text = HoiatusTexts().kinnistuid_ei_leidnud
            heading = pealkiri.informationSimple
            QMessageBox.warning(self, heading, text)

        count = 1
        progress_widget = loadUi(widgets_path)
        progress_bar = progress_widget.testBar
        progress_widget.setWindowTitle(Headings().lisan_kinnistuid)
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

            # Evaluate and set the 'search_field' value
            context = QgsExpressionContext()
            context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(target_layer))
            context.setFeature(new_feature)


            katastriyksus = Katastriyksus()

            self.search_field = 'search_field'
            # Define a list of field names
            field_names = [
                katastriyksus.tunnus,
                katastriyksus.l_aadress,
                katastriyksus.ay_nimi,
                katastriyksus.ov_nimi,
                katastriyksus.mk_nimi,
            ]

            # Assuming 'field_names' is a list of field names to concatenate for the search field
            virtual_field_expression = " || ' ' || ".join([f"lower({name})" for name in field_names])
            expression = QgsExpression(virtual_field_expression)


            if not expression.hasParserError():
                value = expression.evaluate(context)
                # Update the "search_field" attribute
                new_feature[self.search_field] = value
            else:
                print(f"Error parsing expression: {expression.parserErrorString()}")

            # Add the new feature to the target layer
            target_layer.addFeature(new_feature)
            count +=1
            progress_bar.setValue(count)
            QCoreApplication.processEvents()
        # Commit changes to the target layer for each selected feature
        target_layer.commitChanges()
        #print("Selected features added to the target layer.")
        progress_widget.hide()

class GroupActions:
    def add_layer_to_group (layer, grouplayer_name, style_name=None):
        # Add the layer to the project without adding to the layer tree        
        QgsProject.instance().addMapLayer(layer, False)
        # Get the root of the layer tree
        root = QgsProject.instance().layerTreeRoot()
         # Find or create the sub-group layer within the main group
        sub_group = root.findGroup(grouplayer_name)
        sub_group.insertLayer(0, layer)

        #print(style_name)
        # Load the QGIS layer style
        if style_name is not None:
            style = Filepaths().get_style(style_name)
            print(f"style: {style} for style_name: {style_name}")
        else:
            style = None
            pass
        # Apply the layer style
        if style is not None:
            #print("style not none")
            layer.loadNamedStyle(style)
        layer.triggerRepaint()