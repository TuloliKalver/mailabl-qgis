import processing
from qgis.core import QgsProcessingFeatureSourceDefinition, QgsProject

class TempIntersectLayerName:
    intersect_water_name = 'Ajutine_intersect_V'
    intersect_sewer_name = 'Ajutine_intersect_K'
    intersect_prSewer_name = 'Ajutine_intersect_KS'
    intersect_drainage_name = 'Ajutine_intersect_D'
    intesect_road = 'Ajutine_intersect_Tee'
    intersect_layers = [intersect_water_name, intersect_sewer_name, intersect_prSewer_name, intersect_drainage_name, intesect_road]


class Intersect:
    @staticmethod
    def intersect_two_layers(input_layer_name, overlay_layer_name, intersect_buffer):
        print("intersect buffer in intersect_two layers")
        print(intersect_buffer)
        # Remove existing intersection layer if it exists
        existing_layer = QgsProject.instance().mapLayersByName(intersect_buffer)
        if existing_layer:
            QgsProject.instance().removeMapLayer(existing_layer[0])
        else:
            #print("No existing layer to remove")
            pass

        # Find and select all features in the overlay layer
        overlay_layer = QgsProject.instance().mapLayersByName(overlay_layer_name)
        if not overlay_layer:
            #print(f"Overlay layer '{overlay_layer_name}' not found")
            return
        overlay_layer = overlay_layer[0]
        #overlay_layer.selectAll()

        # Find and select all features in the input layer
        input_layer = QgsProject.instance().mapLayersByName(input_layer_name)
        if not input_layer:
            #print(f"Input layer '{input_layer_name}' not found")
            return
        input_layer = input_layer[0]
        input_layer.selectAll()

        # Intersect input layer with overlay layer
        result = processing.run("native:intersection", {
            'INPUT': QgsProcessingFeatureSourceDefinition(input_layer.source(), True),
            'OVERLAY': QgsProcessingFeatureSourceDefinition(overlay_layer.source(), True),
            'INPUT_FIELDS': ['mslink'],
            'OVERLAY_FIELDS': ['mslink'],
            'OVERLAY_FIELDS_PREFIX': 'overlay',
            'OUTPUT': 'memory:',
            'OUTPUT_FIELDS': 'keep_all'
        })

        # Add intersected layers to the project
        intersection = result['OUTPUT']
        #print(f"Intersected buffer layer: {intersect_buffer}")
        intersection.setName(intersect_buffer)
        QgsProject.instance().addMapLayer(intersection)


        return intersect_buffer