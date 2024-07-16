from PyQt5.QtWidgets import QPushButton, QLineEdit, QWidget
from PyQt5.QtCore import Qt, QEvent, QObject


class BlockButtonsToPreferLabelEventFilter(QObject):
    def __init__(self, parent=None):
        super(BlockButtonsToPreferLabelEventFilter, self).__init__(parent)
        self.parent = parent

    def set_button_focus_policy(self):
        # Iterate through all children and set focus policy for QPushButton
        for child in self.parent.findChildren(QPushButton):
            child.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() in (Qt.Key_Return, Qt.Key_Enter):
            # Ignore the event to prevent it from being propagated to buttons
            return True
        return super(BlockButtonsToPreferLabelEventFilter, self).eventFilter(obj, event)

class ReturnPressedManager:
    def __init__(self, parent: QWidget):
        self.parent = parent

    def setup_connections(self, label_callbacks):
        for label_name, callback in label_callbacks.items():
            label = self.parent.findChild(QLineEdit, label_name)
            if label:
                label.returnPressed.connect(callback)
    
    def on_label_return_pressed(self):
        # Identify which label sent the signal
        sender = self.parent.sender()
        if isinstance(sender, QLineEdit):
            self.parent.start_propertie_search()