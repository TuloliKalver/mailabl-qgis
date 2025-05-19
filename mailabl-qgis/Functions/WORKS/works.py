from PyQt5.QtCore import Qt
from qgis.gui import QgsMapTool
from qgis.core import (
    QgsProject,
    QgsPointXY,
    QgsRectangle,
    QgsFeatureRequest,
    QgsGeometry,
    QgsVectorLayer,
    edit
)
from qgis.utils import iface

from .worksHelpers import worksHelpers
from ...KeelelisedMuutujad.modules import Module
from ...config.settings_new import PluginSettings
class PointCaptureTool(QgsMapTool):
    def __init__(self, canvas, callback, cancel_callback=None):
        super().__init__(canvas)
        self.canvas = canvas
        self.callback = callback
        self.cancel_callback = cancel_callback
        self.setCursor(Qt.CrossCursor)
    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos())
            self.callback(point)
        elif event.button() == Qt.RightButton:
            print("❌ Reposition cancelled via right click")
            if self.cancel_callback:
                self.cancel_callback()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print("❌ Reposition cancelled via ESC")
            if self.cancel_callback:
                self.cancel_callback()

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


# ----------------------------
# FeatureSelectTool – click to select a feature by geometry
# ----------------------------
class FeatureSelectTool(QgsMapTool):
    def __init__(self, canvas, layer: QgsVectorLayer, callback):
        super().__init__(canvas)
        self.canvas = canvas
        self.layer = layer
        self.callback = callback

    def canvasReleaseEvent(self, event):
        print("canvasReleaseEvent")
        if event.button() == Qt.LeftButton:
            point = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos())
            feature_id = self._identify_feature(point)
            if feature_id is not None:
                self.callback(feature_id)


    def _identify_feature(self, point: QgsPointXY):
        print("_identify_feature")
        search_rect = QgsRectangle(
            point.x() - 5, point.y() - 5,
            point.x() + 5, point.y() + 5
        )
        print("search_rect", search_rect)
        request = QgsFeatureRequest().setFilterRect(search_rect)

        closest_feature = None
        closest_distance = float("inf")

        for feature in self.layer.getFeatures(request):
            geom = feature.geometry()
            if not geom:
                continue
            dist = geom.distance(QgsGeometry.fromPointXY(point))
            if dist < 5 and dist < closest_distance:
                closest_feature = feature
                closest_distance = dist

        if closest_feature:
            feature_id = closest_feature.id()
            print(f"✅ Closest feature found with ID: {feature_id}, distance: {closest_distance}")

            # Highlight (select) it on the layer
            self.layer.removeSelection()
            self.layer.selectByIds([feature_id])

            return feature_id

        print("❌ No nearby point feature found.")
        return None


    @staticmethod
    def start_feature_select(layer: QgsVectorLayer, on_selected_callback):
        print("start_feature_select")
        global _tool_instance
        canvas = iface.mapCanvas()
        _tool_instance = FeatureSelectTool(canvas, layer, on_selected_callback)
        canvas.setMapTool(_tool_instance)



class WorksManipulator:
    @staticmethod
    def reposition_feature(layer: QgsVectorLayer, feature_id: int, new_point: QgsPointXY) -> bool:
        if not layer.isEditable():
            layer.startEditing()

        feature = next(layer.getFeatures(QgsFeatureRequest(feature_id)), None)
        if not feature:
            print(f"❌ Feature with ID {feature_id} not found.")
            return False

        new_geom = QgsGeometry.fromPointXY(new_point)
        success = layer.changeGeometry(feature_id, new_geom)

        if success:
            print(f"✅ Moved feature {feature_id} to {new_point}")
        else:
            print(f"❌ Failed to move feature {feature_id}")
        return success

    
class WorkMapHelper:
    @staticmethod
    def begin_reposition_work_feature():
        module = Module.WORKS
        works_layer_name = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.WORKS_LAYER
        )
        layer = QgsProject.instance().mapLayersByName(works_layer_name)[0]
        print("layer", layer)
        def on_feature_selected(fid):
            print(f"🟢 Feature selected: {fid}")

            def on_new_location_chosen(new_point: QgsPointXY):
                WorksManipulator.reposition_feature(layer, fid, new_point)
                layer.commitChanges()
                iface.mapCanvas().unsetMapTool(_tool_instance)
                iface.actionPan().trigger()

            def on_cancel_reposition():
                layer.removeSelection()
                iface.mapCanvas().unsetMapTool(_tool_instance)
                iface.actionPan().trigger()

            WorkMapHelper.start_point_capture_for_reposition(on_new_location_chosen, on_cancel_reposition)


        FeatureSelectTool.start_feature_select(layer, on_feature_selected)



    @staticmethod
    def start_point_capture_for_reposition(callback, cancel_callback=None):
        global _tool_instance
        canvas = iface.mapCanvas()
        _tool_instance = PointCaptureTool(canvas, callback, cancel_callback)
        canvas.setMapTool(_tool_instance)