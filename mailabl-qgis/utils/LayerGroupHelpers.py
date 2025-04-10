from qgis.core import ( # type: ignore
    QgsProject,
    QgsVectorLayer,
)
from typing import Optional



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
