from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class WindowPositionHelper:
    def __init__(self, window):
        self.window = window
        self.original_flags = window.windowFlags()

    def _toggle_always_on_top(self):
        if self.window.windowFlags() & Qt.WindowStaysOnTopHint:
            self._turn_off_always_on_top()
        else:
            self._turn_on_always_on_top()

    def _turn_on_always_on_top(self):
        if not (self.window.windowFlags() & Qt.WindowStaysOnTopHint):
            self.window.setWindowFlags(self.window.windowFlags() | Qt.WindowStaysOnTopHint)
            self.window.show()

    def _turn_off_always_on_top(self):
        if self.window.windowFlags() & Qt.WindowStaysOnTopHint:
            self.window.setWindowFlags(self.original_flags)
            self.window.show()


class WindowManagerMinMax:
    def __init__(self, window: QWidget):
        self.window = window
        self.is_maximized = False
        self.is_minimized = False
        self.original_geometry = window.geometry()

    def _minimize_window(self):
        if not self.is_minimized:
            self.window.showMinimized()
            self.is_minimized = True
            self.is_maximized = False

    def _maximize_window(self):
        if not self.is_maximized:
            self.window.showMaximized()
            self.is_maximized = True
            self.is_minimized = False

    def _restore_window(self):
        self.window.setGeometry(self.original_geometry)
        self.window.showNormal()
        self.window.raise_()  # Bring the window to the front
        self.window.activateWindow()  # Focus the window
        self.is_maximized = False
        self.is_minimized = False

    def _toggle_maximize(self):
        if self.is_maximized:
            self._restore_window()
        else:
            self._maximize_window()
