#layer_generator.py
import gc
import os
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsVectorFileWriter,
    QgsFeature,
    QgsField,
    QgsWkbTypes,
    QgsCoordinateReferenceSystem,
    QgsExpression,
    QgsExpressionContext,
    QgsExpressionContextUtils,
    QgsLayerTreeGroup,
)

from typing import Tuple, Optional, List

from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication, QVariant
from PyQt5.QtWidgets import QFileDialog

from ..utils.LayerSetups import LayerSetups
from ..config.settings import Filepaths, FilesByNames, StoredLayers
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts ,HoiatusTextsAuto, Salvestamisel
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..KeelelisedMuutujad.FolderHelper import MailablGroupFolders
from ..utils.messagesHelper import ModernMessageDialog
from ..utils.LayerHelpers import fidOperations
from ..utils.LayerGroupHelpers import LayerGroupHelper
from ..utils.Logging.Logger import TracebackLogger
from .LayerGeneratorHelper import ArchiveOptionBuilder






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
            heading = pealkiri.infoSimple
            ModernMessageDialog.Info_messages_modern(heading,text)
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
                ModernMessageDialog.Info_messages_modern(heading,text)
            except OSError as e:
                heading = Headings().warningCritical
                text = HoiatusTextsAuto.unable_to_delete_output_file(output_file_path, e)
                ModernMessageDialog.Info_messages_modern(heading,text)
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
                pass

            else:
                heading = pealkiri.warningSimple
                text = HoiatusTextsAuto.save_layer_error(error_message)
                ModernMessageDialog.Info_messages_modern(heading,text)
                
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
                    ModernMessageDialog.Info_messages_modern(heading,text)
            
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
                heading = pealkiri.infoSimple
                ModernMessageDialog.Info_messages_modern(heading,text)
                updated_layer.dataProvider().createSpatialIndex()
    
                text = HoiatusTextsAuto.generated_layer_in_subgroup(new_layer_name, group_layer_name)
                heading = pealkiri.infoSimple
                ModernMessageDialog.Info_messages_modern(heading,text)              
                
            else:
                text = HoiatusTextsAuto.load_gpkg_file_error(output_file_path)
                heading = pealkiri.infoSimple
                ModernMessageDialog.Info_messages_modern(heading,text)

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

        layer_name = StoredLayers.import_layer_name()
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
            heading = pealkiri.infoSimple
            ModernMessageDialog.Info_messages_modern(heading,text)
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
            heading = pealkiri.infoSimple
            ModernMessageDialog.Info_messages_modern(heading,text)

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

class LayerManager:
    """
    A class that provides helper methods to create and manage layers within a specific group
    in a QGIS project.
    """

    @staticmethod
    def get_or_create_group(group_name: str) -> QgsLayerTreeGroup:
        """
        Retrieve the group by name from the project's layer tree.
        If the group doesn't exist, create it.
        """
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        group = root.findGroup(group_name)
        if group is None:
            group = root.addGroup(group_name)
        return group

    @staticmethod
    def remove_existing_layer(layer_name: str) -> bool:
        """
        Remove an existing layer with the specified name from the project.

        Parameters:
            layer_name (str): The name of the layer to remove.

        Returns:
            bool: True if the layer was successfully removed, False otherwise.
        """
        project = QgsProject.instance()
        layers = project.mapLayersByName(layer_name)
        if layers:
            layer = layers[0]
            project.removeMapLayer(layer.id())
            # Verify if the layer is still present after removal.
            if not project.mapLayersByName(layer_name):
                #print(f"Layer '{layer_name}' removed successfully.")
                gc.collect()
                ret = LayerSetups.unregister_layer_configuration(layer_name=layer_name)
                if ret:
                    gc.collect()
                    return True
                else:
                    gc.collect()
                
                    #message = "Unable to unload layers settings from layers usages"
                    #TracebackLogger.log_traceback(custom_message=message)
                    return False
            else:
                message = f"Layer '{layer_name}' removal failed."
                TracebackLogger.log_traceback(custom_message=message)
                gc.collect()
                return False
        else:

            message=f"Layer '{layer_name}' not found."
            TracebackLogger.log_traceback(custom_message=message)
            gc.collect()
            return False
        
    @staticmethod
    def check_layer_existance_by_name(layer_name: str)-> Optional[QgsVectorLayer]:
        layers = QgsProject.instance().mapLayersByName(layer_name)
        if layers:
            if len(layers) > 1:
                print(f"Warning: More than one layer exists with the name '{layer_name}'. Using the first one.")
            return layers[0]
        return None 
        

    @staticmethod
    def create_memory_layer_by_coping_original_layer(new_layer_name: str, base_layer: QgsVectorLayer, is_archive=False) -> QgsVectorLayer: 
   
        # Now, base_layer should be a QgsVectorLayer. Continue with layer creation.
        crs_auth_id = base_layer.crs().authid()
        memory_layer_name = f"{new_layer_name}"

        # Detect the geometry type from the base layer.
        geometry_type_str = QgsWkbTypes.displayString(base_layer.wkbType())
        
        # Create the memory layer with the detected geometry type.
        memory_layer = QgsVectorLayer(f'{geometry_type_str}?crs={crs_auth_id}', memory_layer_name, 'memory')
        memory_layer.dataProvider().addAttributes(base_layer.fields())
        memory_layer.updateFields()

        if is_archive:        
            if memory_layer.fields().indexOf("backup_date") == -1:
                memory_layer.dataProvider().addAttributes([QgsField("backup_date", QVariant.String)])
                memory_layer.updateFields()

        memory_layer.setExtent(base_layer.extent())
        memory_layer.setCrs(base_layer.crs())

        nex_id=fidOperations.get_next_fid(target_layer=memory_layer)
        LayerSetups.register_layer_configuration(memory_layer,max_fid=nex_id)
        
        return memory_layer

    @staticmethod
    def add_layer_to_sandbox_group(layer: QgsVectorLayer, group=None):
        """
        Add the given layer to the specified group in the QGIS project.
        IF Group Layer is not provided it is automaticaly generated in MAilabl -> Temporary layer group.
        The group parameter can be either a QGIS group object or a string representing the group name.
        """
        if group == None:
            group = MailablGroupFolders.SANDBOXING
        project = QgsProject.instance()
        # If group is provided as a string, retrieve or create the group.
        if isinstance(group, str):
            group = LayerManager.get_or_create_group(group)

        # Add the layer to the project without automatically updating the layer tree.
        project.addMapLayer(layer, False)
        # Insert the layer at the top of the group.
        group.insertLayer(0, layer)


    @staticmethod
    def store_memory_layer_to_geopackage(memory_layer: QgsVectorLayer, target_layer_for_file: QgsVectorLayer, new_layer_name: str) -> Tuple[bool, Optional[List]]:
        """
        Stores a memory layer into an existing GeoPackage file as a new layer,
        then loads the new layer, adds it to a group (using LayerGroups.ARCHIVE),
        and sets it visible.

        If the layer already exists in the GeoPackage, asks the user whether to
        append data (which will add/update a 'backup_date' field with the current timestamp)
        or replace the existing layer.

        :param memory_layer: QgsVectorLayer representing the in-memory layer to save.
        :param target_layer_for_file: QgsVectorLayer whose data source provides the GeoPackage file location.
        """
        uri = target_layer_for_file.dataProvider().dataSourceUri()
        gpkg_path = uri.split("|")[0]
        layer_uri = f"{gpkg_path}|layername={new_layer_name}"
        # Check if the layer already exists in the GeoPackage
        existing_layer = QgsVectorLayer(layer_uri, new_layer_name, "ogr")
        #print(f"Existing layer: {existing_layer}")
        if existing_layer.isValid():
            layers = QgsProject.instance().mapLayersByName(new_layer_name)
            if layers:
                layer = layers[0]  # Use the first matching layer
            else:
                layer = None            
            if layer is None:
                layer = LayerGroupHelper.add_layer_to_projct_in_given_group(layer=existing_layer, group_name=MailablGroupFolders.ARCHIVED_PROPERTIES)
                if layer is not None:
                    res, features = LayerManager._commit_to_archive(memory_layer=memory_layer, layer=layer)
                    return True, features
                else:
                    TracebackLogger.log_traceback(custom_message="Failed to add layer to group.")
                return True,[]
            else:
                res, features = LayerManager._commit_to_archive(memory_layer=memory_layer, layer=layer)
                return True, features
        else:
            TracebackLogger.log_traceback(custom_message="Failed to append features to geopackage.")
            return False, []


    @staticmethod
    def _commit_to_archive(memory_layer: QgsVectorLayer, layer: QgsVectorLayer) -> Tuple[bool, Optional[List]]:
        '''
        Commits features from a temporary memory layer to a permanent archive target layer.

        This method finalizes the archival process by:
        - Appending features from the memory layer into the target layer.
        - Registering the updated layer configuration, including the current maximum feature ID.
        - Updating the target layer's spatial extents to incorporate the newly added features.

        Parameters:
            memory_layer (QgsVectorLayer): The source layer containing features pending archival.
            layer (QgsVectorLayer): The target layer where the features are to be permanently stored.

        Returns:
            Tuple[bool, Optional[List]]:
                - A boolean indicating if the archival operation was successful.
                - A list of feature IDs that were appended if successful; otherwise, an empty list.

        Side Effects:
            - Updates the target layer's extents via layer.updateExtents().
            - Registers the target layer's configuration with the current maximum feature ID.
            - Logs a traceback message if the archival process fails.

        Usage Example:
            success, feature_ids = YourClass._commit_to_archive(memory_layer, target_layer)
            if success:
                print("Features archived successfully:", feature_ids)
            else:
                print("Archiving failed.")
        '''
        success, returned_features = ArchiveOptionBuilder.append_archive_items_to_layer(
            memory_layer=memory_layer, 
            target_layer=layer
        )
        
        LayerSetups.register_layer_configuration(
            layer, 
            max_fid=fidOperations.get_current_max_fid(target_layer=layer)
        )
        
        # Check if the archiving (append) process was successful.
        if success:
            # Update the spatial extents of the target layer to include the newly added features.
            layer.updateExtents()
            
            return True, returned_features
        else:
            # Log a traceback message indicating the failure to append features to the geopackage.
            TracebackLogger.log_traceback(custom_message="Failed to append features to geopackage.")
            
            # Return a tuple indicating failure and an empty list since no features were appended.
            return False, []
