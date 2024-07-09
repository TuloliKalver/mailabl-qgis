from PyQt5.QtCore import QSize, Qt, QRectF, QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QAbstractButton, QApplication, QFrame, QHBoxLayout, QWidget
from PyQt5.QtGui import QColor, QPainter, QPen, QFont


class ToggleSwitch(QAbstractButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._offset = 0  # Initialize _offset early in the constructor
        self.setCheckable(True)
        self.setChecked(False)
        self.setContentsMargins(7, 10, 10, 7)  # Adjusted margins to be 30% smaller
        self._switch_margin = 1.4  # Adjusted switch margin to be 30% smaller
        self._animation = QPropertyAnimation(self, b"offset")
        self._animation.setDuration(300)
        self._on_color = QColor("#0078d4")
        self._off_color = QColor("#848484")
        self.setFont(QFont("Arial", 8, QFont.Bold))

    @pyqtProperty(float)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.update()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._rect = QRectF(self._switch_margin, self._switch_margin,
                            self.width() - 2 * self._switch_margin,
                            self.height() - 2 * self._switch_margin)
        self._radius = self._rect.height() / 2

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self._draw_background(painter)
        self._draw_foreground(painter)
        self._draw_labels(painter)

    def _draw_background(self, painter):
        if self.isChecked():
            painter.setBrush(self._on_color)
        else:
            painter.setBrush(self._off_color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self._rect, self._radius, self._radius)
        

    def _draw_foreground(self, painter):
        margin = self._switch_margin
        diameter = self._rect.height()
        if self.isChecked():
            x = self._rect.right() - diameter - margin
        else:
            x = self._rect.left() + margin

        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.gray))
        painter.drawEllipse(QRectF(x, self._rect.top() + margin,
                                   diameter, diameter))

    def _draw_labels(self, painter):
        painter.setPen(Qt.white)
        if self.isChecked():
            painter.drawText(self._rect.left() + 9, self._rect.center().y() + 4, "Peida")
        else:
            painter.drawText(self._rect.left() + 23, self._rect.center().y() + 4, "Näita")


    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self._animation.setStartValue(self.offset)
        self._animation.setEndValue(self._rect.width() - self._rect.height())
        self._animation.start()

    def sizeHint(self):
        # 30% smaller than the original size
        return QSize(int(66), int(30 * 0.7))

