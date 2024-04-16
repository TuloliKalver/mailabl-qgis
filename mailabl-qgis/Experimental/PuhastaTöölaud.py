# import necessary QGIS modules
from qgis.core import QgsProject

# get the current project
project = QgsProject.instance()

# check if layer with name "Ajutine_servituut" exists in the project
if project.mapLayersByName("Ajutine_servituut"):
    # if layer exists, remove it from the project
    project.removeMapLayer(project.mapLayersByName("Ajutine_servituut")[0])
