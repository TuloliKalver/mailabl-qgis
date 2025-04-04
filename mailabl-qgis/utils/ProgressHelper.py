from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QLabel, QProgressBar
from typing import Optional
from PyQt5.QtWidgets import QFrame


class ProgressDialogModern:
    active_instance = None  # Class-level tracker
    _open_dialogs = set()
    def __init__(self, value=0, maximum=100, title="Andmete laadimine...", stay_on_top=True, **kwargs):
        self.dialog, self.bar = ProgressDialogModern.load_progress_dialog(
            value=value,
            maximum=maximum,
            title=title,
            stay_on_top=stay_on_top,
            **kwargs
        )
        if not self.dialog:
            print("⚠️ Progress dialog could not be loaded.")
            return  # or raise Exception("Failed to load progress dialog")

        drag_frame = self.dialog.findChild(QFrame, "dragFrame")  # if it's a QFrame
        if drag_frame is not None:
            # Pass `self` to static methods using lambda
            drag_frame.mousePressEvent = lambda event, s=ProgressDialogModern.active_instance: s.start_drag(event)
            drag_frame.mouseMoveEvent = lambda event, s=ProgressDialogModern.active_instance: s.do_drag(event)

        else:
            print("⚠️ dragFrame not found in UI.")

        ProgressDialogModern._open_dialogs.add(self)

        self.dialog.show()

    @staticmethod
    def load_progress_dialog(value: int, maximum: Optional[int] = None, title: str = "Andmete laadimine...", stay_on_top=True):
        from ..config.settings import Filepaths, FilesByNames
        widget_name = Filepaths._get_widget_name(FilesByNames().statusbar_widget)
        widget = Filepaths.load_ui_file(widget_name)

        if not widget:
            print(f"⚠️ Could not load {widget_name} file.")
            return None, None

        flags = Qt.FramelessWindowHint | Qt.Tool
        if stay_on_top:
            flags |= Qt.WindowStaysOnTopHint
        widget.setWindowFlags(flags)

        widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.setAttribute(Qt.WA_DeleteOnClose)

        # Set title (fixed on load)
        title_label = widget.findChild(QLabel, "lblTitle", Qt.FindChildrenRecursively)
        if title_label:
            title_label.setText(str(title))

        # Hide all optional content initially
        for name in ["lblMain", "text_1", "text_2"]:
            label = widget.findChild(QLabel, name, Qt.FindChildrenRecursively)
            if label:
                label.hide()



        progress_bar = widget.findChild(QProgressBar, "bar", Qt.FindChildrenRecursively)
        if progress_bar:
            if maximum is not None:
                progress_bar.setMaximum(maximum)
            progress_bar.setValue(value)


        return widget, progress_bar

    def update(self, value: int = None, purpouse: str = None, text1: str = None, text2: str = None, maximum: Optional[int] = None):
        if self.bar:
            if value is not None:
                self.bar.setValue(value)
            if maximum is not None:
                self.bar.setMaximum(maximum)


        label1 = self.dialog.text_1
        if text1 is not None:
            label1.show()
            label1.setText(text1)

        label2 = self.dialog.text_2
        if text2 is not None:
            label2.show()
            label2.setText(text2)

        lbl_main = self.dialog.lblMain
        if purpouse is not None:
            lbl_main.show()
            lbl_main.setText(purpouse)

        QCoreApplication.processEvents()

    def close(self):
        if self.dialog:

            self.dialog.hide()
            ProgressDialogModern._open_dialogs.discard(self)
            self.dialog.setParent(None)  # Detach from QGIS window tree
            self.dialog.deleteLater()
            self.dialog = None  # Important to prevent double-close

        QCoreApplication.processEvents()  # 💡 Force UI refresh

    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.dialog.frameGeometry().topLeft()
            event.accept()

    def do_drag(self, event):
        if event.buttons() & Qt.LeftButton:
            self.dialog.move(event.globalPos() - self.dragPos)
            event.accept()

    @staticmethod
    def force_close(dialog_instance: "ProgressDialogModern"):
        if dialog_instance:
            print("🧹 Closing specific progress dialog")
            dialog_instance.close()

    @staticmethod
    def close_all():
        for dlg in list(ProgressDialogModern._open_dialogs):
            dlg.close()