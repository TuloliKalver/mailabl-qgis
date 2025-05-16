from PyQt5.QtCore import Qt

from .worksHelpers import worksHelpers
from qgis.gui import QgsMapTool, QgsMapToolPan
from qgis.core import QgsPointXY
from qgis.utils import iface
from ...KeelelisedMuutujad.modules import Module
from ...config.settings_new import PluginSettings

from qgis.core import QgsProject
from qgis.core import (
    QgsProject
)

class PointCaptureTool(QgsMapTool):
    def __init__(self, canvas, callback):
        super().__init__(canvas)
        self.canvas = canvas
        self.callback = callback
        self.dialog = self
    def canvasReleaseEvent(self, event):
        if event.button() == 1:  # Left click
            point = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos())
            self.callback(point)

_tool_instance = None  # avoid GC

def start_work_capture(plugin_instance):
    plugin_instance.setWindowState(Qt.WindowMinimized)
    global _tool_instance

    def handle_point_selected(point: QgsPointXY):
        print(f"📍 Point selected in works module: {point}")
        # Restore default pan tool or whatever tool was before
        module = Module.WORKS

        works_layer_name = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.WORKS_LAYER
        )

        works_layer = QgsProject.instance().mapLayersByName(works_layer_name)[0]
        if not works_layer:
            raise ValueError(f"No layer found with the name {works_layer_name}")
        

        worksHelpers.insert_work_feature(point, plugin_instance)        # Now you have the 'tunnus' of the property at that location.
        
        iface.mapCanvas().unsetMapTool(_tool_instance)
        iface.actionPan().trigger()  # activate pan tool again
        # You can now open a dialog, insert feature, etc.

    canvas = iface.mapCanvas()
    _tool_instance = PointCaptureTool(canvas, handle_point_selected)
    canvas.setMapTool(_tool_instance)

