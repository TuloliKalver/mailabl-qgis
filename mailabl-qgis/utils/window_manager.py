from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class WindowManager:
    def __init__(self, window):
        self.window = window
        self.original_flags = window.windowFlags()

    def toggle_always_on_top(self):
        if self.window.windowFlags() & Qt.WindowStaysOnTopHint:
            self.turn_off_always_on_top()
        else:
            self.turn_on_always_on_top()

    def turn_on_always_on_top(self):
        if not (self.window.windowFlags() & Qt.WindowStaysOnTopHint):
            self.window.setWindowFlags(self.window.windowFlags() | Qt.WindowStaysOnTopHint)
            self.window.show()

    def turn_off_always_on_top(self):
        if self.window.windowFlags() & Qt.WindowStaysOnTopHint:
            self.window.setWindowFlags(self.original_flags)
            self.window.show()


class WindowManagerMinMax:
    def __init__(self, window: QWidget):
        self.window = window
        self.is_maximized = False
        self.is_minimized = False
        self.original_geometry = window.geometry()

    def minimize_window(self):
        if not self.is_minimized:
            self.window.showMinimized()
            self.is_minimized = True
            self.is_maximized = False

    def maximize_window(self):
        if not self.is_maximized:
            self.window.showMaximized()
            self.is_maximized = True
            self.is_minimized = False

    def restore_window(self):
        self.window.setGeometry(self.original_geometry)
        self.window.showNormal()
        self.window.raise_()  # Bring the window to the front
        self.window.activateWindow()  # Focus the window
        self.is_maximized = False
        self.is_minimized = False

    def toggle_maximize(self):
        if self.is_maximized:
            self.restore_window()
        else:
            self.maximize_window()
