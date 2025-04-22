from PyQt5.QtCore import QEasingCurve, QVariantAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame


class PulsingBorderFrame(QFrame):
    def __init__(self, parent=None, base_color=QColor(255, 255, 255), min_alpha=60, max_alpha=200, duration=1000):
        super().__init__(parent)
        self._color = base_color
        self._min_alpha = min_alpha
        self._max_alpha = max_alpha

        self.setObjectName("pulsingFrame")  # Ensure you give it a name to match stylesheet selector

        self._pulse_anim = QVariantAnimation(self)
        self._pulse_anim.setDuration(duration)
        self._pulse_anim.setLoopCount(-1)
        self._pulse_anim.setEasingCurve(QEasingCurve.InOutQuad)

        # 💡 Smooth loop: fade in and out (min → max → min)
        self._pulse_anim.setKeyValues([
            (0.0, self._min_alpha),
            (0.5, self._max_alpha),
            (1.0, self._min_alpha)
        ])

        self._pulse_anim.valueChanged.connect(self._update_border)
        self._pulse_anim.start()

        self.setStyleSheet(self._generate_stylesheet(self._min_alpha))

    def _update_border(self, alpha):
        self.setStyleSheet(self._generate_stylesheet(int(alpha)))

    def _generate_stylesheet(self, alpha):
        rgba = f"rgba(255, 255, 255, {alpha})"  # brighter white

        return f"""
            QFrame#{self.objectName()} {{
                border: 2px solid {rgba};
                border-radius: 7px;
                background-color: rgba(29, 37, 43, 0.7);  /* subtle base bg */
            }}
        """