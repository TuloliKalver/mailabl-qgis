# FlagIconHelper.py

from PyQt5.QtGui import QPixmap, QIcon, QPainter
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtSvg import QSvgRenderer

class FlagIconHelper:
    _svg_template = """
    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24">
    <path fill="currentColor" d="M12.36 6H7v6h7.24l.4 2H18V8h-5.24z" opacity="0.3"/>
    <path fill="currentColor" d="M14.4 6L14 4H5v17h2v-7h5.6l.4 2h7V6zm3.6 8h-3.36l-.4-2H7V6h5.36l.4 2H18z"/>
    </svg>
    """

    @staticmethod
    def generate_icon(priority: str = None, size: int = 24) -> QIcon:
        color = FlagIconHelper.get_priority_color(priority)
        svg_colored = FlagIconHelper._svg_template.replace('currentColor', color)
        svg_data = QByteArray(svg_colored.encode('utf-8'))

        renderer = QSvgRenderer(svg_data)
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        return QIcon(pixmap)

    @staticmethod
    def get_priority_color(priority: str) -> str:
        """
        Map priority values to colors.
        """
        priority = (priority or "").lower()  # Safe handling
        mapping = {
            "urgent": "#FF0000",   # Red
            "high": "#FF8000",     # Orange
            "medium": "#FFD700",   # Gold / Yellow
            "low": "#00CC00",      # Green
        }
        return mapping.get(priority, "#CCCCCC")  # Default gray if unknown
