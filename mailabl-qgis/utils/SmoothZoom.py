from qgis.utils import iface
import math

class SmoothZoomManual:
    def __init__(self, start_scale, end_scale, steps=20, easing='ease_out', on_done=None):
        print("🧪 SmoothZoomManual init")
        self.canvas = iface.mapCanvas()
        self.scales = self._generate_scales(start_scale, end_scale, steps, easing)
        self.index = 0
        self.on_done = on_done
        self._connected = False

    def start(self):
        print("🚀 Starting smooth zoom (step-by-step without timer)")
        self._connect()
        self._apply_scale()

    def _apply_scale(self):
        if self.index < len(self.scales):
            target_scale = round(self.scales[self.index])
            current_scale = round(self.canvas.scale())
            print(f"🔍 Step {self.index + 1}/{len(self.scales)} → target: {target_scale} | current: {current_scale}")

            # Prevent reapplying the same scale endlessly
            if target_scale == current_scale:
                print("🔄 Scale unchanged — nudging")
                target_scale += 1

            self.canvas.zoomScale(target_scale)
            self.index += 1
        else:
            self._disconnect()
            print("✅ Zoom complete")
            if self.on_done:
                print("📞 Calling on_done")
                self.on_done()

    def _connect(self):
        if not self._connected:
            self.canvas.scaleChanged.connect(self._apply_scale)
            self._connected = True

    def _disconnect(self):
        if self._connected:
            self.canvas.scaleChanged.disconnect(self._apply_scale)
            self._connected = False

    def _generate_scales(self, start, end, steps, easing):
        t = [i / (steps - 1) for i in range(steps)]
        if easing == 'ease_out':
            ease = [1 - (1 - x)**2 for x in t]
        elif easing == 'ease_in_out':
            ease = [0.5 * (1 - math.cos(math.pi * x)) for x in t]
        else:
            ease = t
        return [start - (start - end) * e for e in ease]
