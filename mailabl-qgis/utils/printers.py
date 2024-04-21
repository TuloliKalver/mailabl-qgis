from qgis.utils import iface
from qgis.core import QgsProject, QgsLayoutExporter

class PrintEasement:
    def print_selected_items(layer_name, layout_name, layout_map_item):
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
        map_item = layout.itemById(layout_map_item)
        label_item = layout.itemById("easement_nr")

        if label_item is None:
            print("Label item 'easement_nr' not found in selected layout.")
        else:
            # Set the text of the label item
            label_item.setText("See on test")

        if map_item is None:
            print("Map item 'Map 1' not found in selected layout.")
            return

        # Get the extent of the selected features
        selected_features = layer.selectedFeatures()
        if selected_features:
            # Adjust the extent of the map item to focus on the selected features
            if layer.selectedFeatureCount() > 0:   
                extent = selected_features[0].geometry().boundingBox()
                for feature in selected_features[1:]:
                    extent.combineExtentWith(feature.geometry().boundingBox())

                # Set the extent of the map item
                map_item.setExtent(extent)
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