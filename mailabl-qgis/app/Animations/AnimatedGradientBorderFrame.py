from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QConicalGradient, QPainter, QPen
from PyQt5.QtWidgets import QFrame

class AnimatedGradientBorderFrame(QFrame):
    WARNING = "warning"
    WHITE = "white"
    MODERN = "modern"
    INSPIRE = "inspire"

    def __init__(self, parent=None,  style=WARNING):
        super().__init__(parent)
        self._angle = 0
        self._style = style

        self.setObjectName("glowFrame")
        self.setMinimumSize(100, 100)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._rotate_gradient)
        self._timer.start(10)

    def _rotate_gradient(self):
        self._angle = (self._angle + 2) % 360
        self.update()

    def _get_gradient(self, center):
        gradient = QConicalGradient(center, self._angle)

        if self._style == AnimatedGradientBorderFrame.WARNING:
            gradient.setColorAt(0.0, QColor(255, 60, 60, 255))
            gradient.setColorAt(0.5, QColor(255, 60, 60, 100))
            gradient.setColorAt(1.0, QColor(255, 60, 60, 255))
        elif self._style == AnimatedGradientBorderFrame.WHITE:
            gradient.setColorAt(0.0, QColor(255, 255, 255, 200))
            gradient.setColorAt(0.5, QColor(180, 180, 180, 80))
            gradient.setColorAt(1.0, QColor(255, 255, 255, 200))
        elif self._style == AnimatedGradientBorderFrame.MODERN:
            gradient.setColorAt(0.0, QColor(0, 255, 200, 255))
            gradient.setColorAt(0.5, QColor(255, 0, 150, 100))
            gradient.setColorAt(1.0, QColor(0, 255, 200, 255))
        elif self._style == AnimatedGradientBorderFrame.INSPIRE:
            gradient.setColorAt(0.0, QColor(9, 144, 143, 255))
            gradient.setColorAt(0.25, QColor(255, 128, 64, 160))
            gradient.setColorAt(0.5, QColor(46, 47, 56, 60))
            gradient.setColorAt(0.75, QColor(255, 105, 180, 160))
            gradient.setColorAt(1.0, QColor(9, 144, 143, 255))
        else:
            gradient.setColorAt(0.0, QColor(100, 100, 100, 120))
            gradient.setColorAt(1.0, QColor(100, 100, 100, 120))

        return gradient

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect().adjusted(2, 2, -2, -2)
        center = rect.center()

        pen = QPen()
        pen.setWidth(2)
        pen.setBrush(self._get_gradient(center))
        painter.setPen(pen)
        painter.setBrush(Qt.transparent)

        painter.drawRoundedRect(rect, 9, 9)
