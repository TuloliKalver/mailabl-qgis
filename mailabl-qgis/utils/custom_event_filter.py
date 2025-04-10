from PyQt5.QtWidgets import QPushButton, QLineEdit, QWidget
from PyQt5.QtCore import Qt, QEvent, QObject
from ..Functions.SearchEngines import ModularSearchEngine
from ..KeelelisedMuutujad.modules import Module


class BlockButtonsToPreferLabelEventFilter(QObject):
    def __init__(self, parent=None):
        super(BlockButtonsToPreferLabelEventFilter, self).__init__(parent)
        self.dialog = parent

    def set_button_focus_policy(self):
        # Iterate through all children and set focus policy for QPushButton
        for child in self.dialog.findChildren(QPushButton):
            child.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() in (Qt.Key_Return, Qt.Key_Enter):
            # Ignore the event to prevent it from being propagated to buttons
            return True
        return super(BlockButtonsToPreferLabelEventFilter, self).eventFilter(obj, event)

class ReturnPressedManager:
    def __init__(self, parent: QWidget):
        self.dialog = parent
        self.mse = ModularSearchEngine(self.dialog)
   

        self.label_callbacks_user = {
            self.dialog.lePassword: self.dialog.save_user_data,
            self.dialog.leUsername: self.dialog.activate_line_edit,
        }


                # Setup connections for existing widgets
        self.label_callbacks = {
            self.dialog.isSelectedCadaster: self.dialog.start_propertie_search,
            self.dialog.le_searchContracts: lambda: self.mse.universalSearch(Module.CONTRACT),
            self.dialog.le_searchProjects: lambda: self.mse.universalSearch(Module.PROJECT),
            self.dialog.leSearcheasements: lambda: self.mse.universalSearch(Module.EASEMENT),
            self.dialog.leText_For_Sync_GreateLayerName: self.dialog.generate_virtual_mapLayer_synced_with_Mailabl
        }

    def setup_connections_to_handle_return(self):

        for label, callback in self.label_callbacks.items():
            if label:
                label.returnPressed.connect(callback)
                label.clear()
                label.setCursorPosition(0)
        for label_user, callback_user in self.label_callbacks_user.items():
            if label_user:
                label_user.returnPressed.connect(callback_user)
                

    def on_label_return_pressed(self):
        # Identify which label sent the signal
        sender = self.dialog.sender()
        if isinstance(sender, QLineEdit):
            self.dialog.start_propertie_search()