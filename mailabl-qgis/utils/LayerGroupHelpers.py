from qgis.core import ( # type: ignore
    QgsProject,
    QgsVectorLayer,
)

from ..config.settings import Filepaths


class LayerGroupHelper:

    @staticmethod
    def add_layer_to_projct_in_given_group(layer: QgsVectorLayer, group_name: str = None) -> QgsVectorLayer:
    
        QgsProject.instance().addMapLayer(layer, False)
        # Get the layer tree root
        root = QgsProject.instance().layerTreeRoot()
        # Try to find the group by its name (e.g., "My Group")
        group = root.findGroup(group_name)
        # If the group doesn't exist, create it
        if group is None:
            group = root.insertGroup(0, group_name)
        # Add the layer to the group
        group.addLayer(layer)           
    
        return layer
    
    def _add_layer_to_group (layer, grouplayer_name, style_name=None):
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



    @staticmethod
    def get_or_create_group(group_name):
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
