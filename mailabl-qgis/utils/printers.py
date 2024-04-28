from qgis.utils import iface
from qgis.core import QgsProject, QgsRectangle, QgsGeometry

Label_1 = "EasementNr"
lblScale = "Scale"
lblArea = "Area"
lblPropertie = "Propertie"


class PrintEasement:
    @staticmethod
    def print_selected_items(layer_name, layout_name, layout_map_item, scale_text, value_string):
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
        label_nr = layout.itemById(Label_1)


    
        if label_nr is None:
            print("Label item 'easement_nr' not found in selected layout.")
        else:
            # Set the text of the label item
            label_nr.setText("See on test")

        if map_item is None:
            print("Map item 'Map 1' not found in selected layout.")
            return

        label_area = layout.itemById(lblArea)
        if label_area is None:
            print(f"area field is missing")
            pass
        else:
            # Get the extent of the selected features
            selected_features = layer.selectedFeatures()
            total_area = 0
            for feature in selected_features:
                geometry = feature.geometry()
                if geometry:
                    area = geometry.area()
                    total_area += area
            print("Total area of selected features:", total_area)

            # Format the total area with two decimal places
            formatted_area = "{:.2f}".format(total_area)
            
            # Set the label text with the formatted area
            label_area.setText(f"Pindala kokku: {formatted_area} m²")

        label_properties = layout.itemById(lblPropertie)
        if label_properties:
            label_properties.setText(value_string)

        scale_factor = PrintEasement.center_items_in_map(selected_features, map_item, layout, scale_text)

        label_scale = layout.itemById(lblScale)
        if label_scale is None:
            print("Label item 'easement_nr' not found in selected layout.")
        else:
            # Set the text of the label item
            label_scale.setText(f"Mõõtkava: {scale_factor}")



    @staticmethod
    def center_items_in_map(selected_features, map_item, layout, scale_text):
        if selected_features:
            # Calculate the combined extent of all selected features
            combined_extent = QgsGeometry().boundingBox()
            for feature in selected_features:
                combined_extent.combineExtentWith(feature.geometry().boundingBox())

            # Calculate the center of the combined extent
            center = combined_extent.center()

            # Get the extent of the map item
            map_extent = map_item.extent()

            # Calculate the difference in coordinates between the center of the original extent and the combined extent
            dx = center.x() - map_extent.center().x()
            dy = center.y() - map_extent.center().y()

            # Shift the original extent by the calculated difference
            new_extent = QgsRectangle(map_extent.xMinimum() + dx, map_extent.yMinimum() + dy,
                                    map_extent.xMaximum() + dx, map_extent.yMaximum() + dy)

            # Set the extent of the map item
            map_item.setExtent(new_extent)
            # Apply the best scale factor to adjust the scale of the map item

            scale = int(scale_text) 
            map_item.setScale(scale)

            # Refresh the layout to reflect the changes
            layout.refresh()
            return scale
        else:
            print("no selected items found")

    @staticmethod
    def expand_layout_to_fit_items (selected_features, layer, map_item, layout):
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


    @staticmethod
    def adjust_scale_to_fit(selected_features, map_item, layout):
        if selected_features:
            # Get the extent of the map item
            map_extent = map_item.extent()
            print("Map extent:", map_extent)

            while True:
                # Calculate the size of the selected features
                combined_extent = QgsGeometry().boundingBox()
                for feature in selected_features:
                    combined_extent.combineExtentWith(feature.geometry().boundingBox())

                # Calculate the size of the map extent
                map_size = map_extent.width() * map_extent.height()
                print("Map size:", map_size)

                # Calculate the size of the selected features extent
                feature_size = combined_extent.width() * combined_extent.height()
                print("Selected features size:", feature_size)

                # Check if the size of the selected features fits within the size of the map extent
                if feature_size <= map_size:
                    break

                # Calculate the scale factor needed to fit the selected features
                scale_factor_x = map_extent.width() / combined_extent.width()
                scale_factor_y = map_extent.height() / combined_extent.height()
                scale_factor = min(scale_factor_x, scale_factor_y) * 1000
                print("Calculated scale factor:", scale_factor)

                # Choose the best scale factor from the given options that ensures the selected features fit within the map extent
                available_scale_factors = [100, 250, 500, 750, 1000, 5000]
                best_scale_factor = available_scale_factors[0]
                for factor in available_scale_factors:
                    if factor >= scale_factor:
                        print(f"Evaluating scale factor {factor}...")
                        best_scale_factor = factor
                        break

                print("Chosen scale factor:", best_scale_factor)

                # Apply the best scale factor to adjust the scale of the map item
                map_item.setScale(best_scale_factor)

                # Refresh the layout to reflect the changes
                layout.refresh()
                return best_scale_factor
        else:
            print("No selected items found")
