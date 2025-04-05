
import processing

from qgis.utils import iface
from qgis.core import QgsProcessingFeatureSourceDefinition, QgsProject, QgsFeature, edit, QgsVectorLayer

from PyQt5.QtCore import QCoreApplication
from ..config.settings import SettingsDataSaveAndLoad, StoredLayers
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
#Provides tools to select elements from map or from tables and show on map

active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        
class properties_selectors:
    @staticmethod
    def show_connected_properties_on_map(values, layer_type):
        if layer_type == "active":
            layer_name =  StoredLayers.users_properties_layer_name()
        #    print(f"layer_name if active = {layer_name}")
        if layer_type == "import":
            layer_name = StoredLayers.import_layer_name()
        #    print(f"layer_name if import = {layer_name}")
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        layer.removeSelection()

        selected_feature_ids = []
        #printt(f"selected feature ids before  {selected_feature_ids}")
        for feature in layer.getFeatures():
            if feature[Katastriyksus.tunnus] in values:
                selected_feature_ids.append(feature.id())
        #print(f"selected_features_ids: {selected_feature_ids}")
        layer.selectByIds(selected_feature_ids)
        QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setCustomProperty("selectedFeatures", selected_feature_ids)
        iface.mapCanvas().zoomToSelected(layer)
        iface.mapCanvas().refresh()
        
        
    @staticmethod
    def show_AND_copy_connected_cadasters_for_sync_process_dev(values, memory_layer_name):
        #print(f"values in 'show_connected_cadasters_for_sync_process': {values}")

        input_layer_name = StoredLayers.import_layer_name()
        #    print(f"layer_name if import = {layer_name}")
        
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
        target_layer = QgsProject.instance().mapLayersByName(memory_layer_name)[0]
        
        QgsProject.instance().layerTreeRoot().findLayer(input_layer.id()).setItemVisibilityChecked(True)
        input_layer.removeSelection()
        selected_feature_ids = []
        #print(f"selected feature ids before  {selected_feature_ids}")
        for feature in input_layer.getFeatures():
            if feature[Katastriyksus.tunnus] in values:
                selected_feature_ids.append(feature.id())
        #print(f"selected_features_ids: {selected_feature_ids}")
        input_layer.selectByIds(selected_feature_ids)
        QgsProject.instance().layerTreeRoot().findLayer(input_layer.id()).setCustomProperty("selectedFeatures", selected_feature_ids)
        #iface.mapCanvas().zoomToSelected(layer)
        iface.mapCanvas().refresh()
        if len(selected_feature_ids)==0:
            print(f"values not found in import process: {values}")
        if input_layer.selectedFeatureCount() > 0:
            # Get the target layer by name or any other means
            #print(f"target_layer: {target_layer}")
            # Start editing on the target layer
            with edit(target_layer):
                # Loop through selected features on the input layer
                selected_features = input_layer.selectedFeatures()
                #print(f"selected features in 'copy_selected_features': {selected_features}")
                for feature in input_layer.selectedFeatures():
                    # Clone the feature to add it to the target layer
                    new_feature = QgsFeature(feature)
                    target_layer.addFeature(new_feature)
            target_layer.commitChanges()
            target_layer.triggerRepaint()  # Refresh the map canvas
            target_layer.updateExtents()
            
            #shp_tools.zoom_to_layer_extent(self, target_layer)
            # Hide the input layer
            #QgsProject.instance().layerTreeRoot().findLayer(input_layer.id()).setItemVisibilityChecked(False)     
            input_layer.removeSelection()
        else:
            print("No features selected on the input layer.")
        

    @staticmethod
    def For_Base_layer_show_connected_cadasters(layer_type, values, selected_feature_ids):
        #print("Started: For_Base_layer_show_connected_cadasters")
        print(f"cadaster values in 'For_Base_layer_show_connected_cadasters' {values}")
        print(f"selected_feature_ids at the begining in 'For_Base_layer_show_connected_cadasters' {selected_feature_ids}")
        if layer_type == "active":
            layer_name = StoredLayers.users_properties_layer_name()
            #print(f"layer_name if active = {layer_name}")
        elif layer_type == "import":
            layer_name = StoredLayers.import_layer_name()
            #print(f"layer_name if import = {layer_name}")
        print(f"layer_name in 'For_Base_layer_show_connected_cadasters' {layer_name}")
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        #layer.removeSelection()
        #import time
        #start_time = time.time()  # Start the timer
        for feature in layer.getFeatures():
            #print(f"feature in get features in 'For_Base_layer_show_connected_cadasters' {feature}")
            if feature[Katastriyksus.tunnus] in values:
                selected_feature_ids.append(feature.id())
                QCoreApplication.processEvents()
        #end_time = time.time()  # End the timer
        #elapsed_time = end_time - start_time
        #print(f"spent time for finding features in layer features from {layer_name}: {elapsed_time} seconds")
        #start_time = time.time()  # Start the timer
        print(f"selected_feature_ids before selecting items in 'For_Base_layer_show_connected_cadasters' {selected_feature_ids}")
        layer.selectByIds(selected_feature_ids)
        QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setCustomProperty("selectedFeatures", selected_feature_ids)
        iface.mapCanvas().refresh()
        iface.mapCanvas().zoomToSelected(layer)
        #end_time = time.time()  # End the timer
        #elapsed_time = end_time - start_time
        #print(f"spent time to select and zoom {layer_name}: {elapsed_time} seconds")
        QCoreApplication.processEvents()
        #selected_feature_ids.clear()
        return layer_name


    def create_mapView_of_county(self, layer_type, selected_county_item_text):
        if layer_type == "active":
            layer_name = StoredLayers.users_properties_layer_name()
            #print(f"layer_name if active = {layer_name}")
        elif layer_type == "import":
            layer_name = StoredLayers.import_layer_name()
            #print(f"layer_name if import = {layer_name}")
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        layer.removeSelection()
        QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        county_name_field = Katastriyksus.mk_nimi #'MK_NIMI'
        #county_restriction = "', '".join(selected_county_item_text)
        expression = f"{county_name_field} IN ('{selected_county_item_text}')"
        print(f"Expression: {expression}")
        layer.setSubsetString(expression)
        layer.triggerRepaint()

        # Zoom to the full extent of the layer
        iface.mapCanvas().setExtent(layer.extent())
        iface.mapCanvas().refresh()
        QCoreApplication.processEvents()
        
        
    def create_mapView_of_state(self, layer_type, selected_state_item_text):
        if layer_type == "active":
            layer_name = StoredLayers.users_properties_layer_name()
            #print(f"layer_name if active = {layer_name}")
        elif layer_type == "import":
            layer_name = StoredLayers.import_layer_name()
            #print(f"layer_name if import = {layer_name}")
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        layer.removeSelection()
        QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        state_name_field = Katastriyksus.ov_nimi
        #county_restriction = "', '".join(selected_county_item_text)
        expression = f"{state_name_field} IN ('{selected_state_item_text}')"
        print(f"Expression: {expression}")
        layer.setSubsetString(expression)
        layer.triggerRepaint()

        # Zoom to the full extent of the layer
        iface.mapCanvas().setExtent(layer.extent())
        iface.mapCanvas().refresh()
        QCoreApplication.processEvents()
        
        
class CadasterSelector:
    def projects_return_cadasters(self, table):
        table_view = table
        selected_item = table_view.selectedIndexes()
        
        if not selected_item:
            return ""
        id_column_index = selected_item[0].sibling(selected_item[0].row(), 5)
        cadasters = table_view.model().data(id_column_index)
        if not cadasters:
            return ""
        cadasters_list = ['"' + value + '"' for value in cadasters.split(", ")]
        cadasters_str = ", ".join(cadasters_list)
        return cadasters_str

class UseQGISNative:
    def select_elements_from_layer(layer, reference_layer, widget):
        # Find and select all features in the input layer
        
        print(f"select elements from '{layer}' layer")
        input_layer = QgsProject.instance().mapLayersByName(layer)
        if not input_layer:
            #print(f"Missing elements from '{input_layer}' layers")
            return

        reference = QgsProject.instance().mapLayersByName(reference_layer)
        if not reference:
            #print(f"Input layer '{reference_layer}' not found")
            return
        
        dial_value = widget.dPuhvriSuurus.value()
        puhver = dial_value / 10
        distance = round(puhver * 2) / 2

        # Run select within distance algorithm
        result = processing.run("native:selectwithindistance", {
            'INPUT': layer,
            'REFERENCE': QgsProcessingFeatureSourceDefinition(reference_layer),
            'DISTANCE': distance,
            'METHOD': 0, # Use planar distance
        })

        # Get selected features
        selected_features = result['OUTPUT']

        return selected_features
 

    @staticmethod
    def get_diameter_and_Z(selected_features):
        diameters = []
        begin_z_coords = []

        for feature in selected_features:
            diameter = feature.attribute('diameter')
            begin_z_coord = feature.attribute('begin_z_coord')

            # Append the attributes to the respective lists
            diameters.append(diameter)
            begin_z_coords.append(begin_z_coord)

        return diameters, begin_z_coords