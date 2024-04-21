from qgis.utils import iface
from qgis.core import QgsProject, QgsLayoutExporter

class PrintEasement:
    def print_selected_items(layer_name, layout_name):
        # Get the layer
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        if layer is None:
            print(f"Layer '{layer_name}' not found.")
            return
        else:
            layer.selectAll()

        layout = QgsProject.instance().layoutManager().layoutByName(layout_name)
        if layout is None:
            print(f"Layout '{layout_name}' not found.")
            return


        # Open the layout manager for manual selection of layout form
        layout_manager = iface.openLayoutDesigner(layout)
        if layout_manager is None:
            print("Layout manager not available.")
            return

        # Find the "Map 1" item in the layout
        map_item = layout.itemById("Map 1")

        if map_item is None:
            print("Map item 'Map 1' not found in selected layout.")
            return

        # Adjust the extent of the map item to focus on the selected features
        if layer.selectedFeatureCount() > 0:
            # Get the extent of the selected features
            extent = layer.selectedFeaturesBounds()

            # Set the extent of the map item to the extent of the selected features
            map_item.zoomToExtent(extent)

            # Refresh the layout to reflect the changes
            layout.refresh()
        else:
            print("No features selected in the layer.")

        '''
        # Export the selected layout to a PDF file
        if layout_manager.selectedLayout():
            layout = layout_manager.selectedLayout()
            #export_path = "output.pdf"  # Replace with your desired output path
            #exporter = QgsLayoutExporter(layout)
            #exporter.exportToPdf(export_path)
            #print(f"PDF exported to: {export_path}")
        else:
            print("No layout selected.")

        '''