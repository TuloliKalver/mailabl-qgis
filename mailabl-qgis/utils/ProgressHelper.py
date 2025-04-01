
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QFrame
from typing import Optional

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QProgressBar


class ProgressHelper:
    dialog = None  # Class-level variable to store the dialog reference

    @staticmethod
    def set_dialog(main_dialog):
        if main_dialog is None:
            print("Warning: Attempting to set dialog with None")
        ProgressHelper.dialog = main_dialog
    @staticmethod
    def updat_progress_on_main_dialog(value: int, maximum: Optional[int] = None):
        """
        Update the progress bar with a new value and optionally set a new maximum.
        
        Args:
            progressBar (QProgressBar): The progress bar widget.
            value (int): The new value to set.
            maximum (int, optional): If provided, update the maximum value of the progress bar.
        """

        progressBar = ProgressHelper.dialog.findChild(QProgressBar, 'progressBar_Projects')

        if progressBar:
            if maximum is not None:
                progressBar.setMaximum(maximum)
            progressBar.setValue(value)
            progressBar.show()
            QCoreApplication.processEvents()  # Keep the UI responsive

        return progressBar
    
    @staticmethod
    def update_progressbar_by_current_index(current_index):
        """
        Update the progress bar during feature processing.

        This function increments the progress bar for every tenth feature processed, ensuring
        that the UI remains responsive by processing pending events.

        Args:
            progressBar (QProgressBar): The progress bar widget used to display progress.
            current_index (int): The index of the current feature being processed.
        """
        if current_index % 100 == 0:
            ProgressHelper.updat_progress_on_main_dialog(value=current_index)
            QCoreApplication.processEvents()


class ProgressDialogModern:
    def __init__(self, value=0, maximum=100, **kwargs):
        self.dialog, self.bar = ProgressDialogModern.load_progress_dialog(value=value, maximum=maximum, **kwargs)
        self.dialog.show()

    @staticmethod
    def load_progress_dialog(value:int, maximum:Optional[int]=None, purpouse:str="", title:str="Andmete laadimine...", text:str ="", text_2:str="", Show=True):
        """
        Load the progress dialog with an initial value and maximum.

        Args:
            value (int): Initial value for the progress bar.
            maximum (int, optional): Maximum value for the progress bar. Defaults to None.
            title (str, optional): Title of the progress dialog window. Defaults to "Andmete laadimine...".
            text (str, optional): Text displayed in the first line of the status bar. Defaults to None.
            text_2 (str, optional): Text displayed in the second line of the status bar. Defaults to None.
            Show(bool,optional): Whether or not show dialog on screen
        """
        
        from ..config.settings import Filepaths, FilesByNames
        widget_name = Filepaths._get_widget_name(FilesByNames().statusbar_widget)
        widget = Filepaths.load_ui_file(widget_name)
        if not widget:
            print(f"Could not load {widget_name} file.")
            return
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.setAttribute(Qt.WA_DeleteOnClose)
    
        title_label = widget.findChild(QLabel, "lblTitle", Qt.FindChildrenRecursively)
        title_label.setText(str(title))

        main_label = widget.findChild(QLabel, "lblMain", Qt.FindChildrenRecursively)
        label_1 = widget.findChild(QLabel, "text_1", Qt.FindChildrenRecursively)
        label_2 = widget.findChild(QLabel, "text_2", Qt.FindChildrenRecursively)
        progressBar = widget.findChild(QProgressBar, "bar", Qt.FindChildrenRecursively)
        
        label_1.hide()
        label_2.hide()
        main_label.hide()

        if purpouse != "" :
            main_label.show()
            main_label.setText(purpouse)
        if text != "" :
            label_1.show()
            label_1.setText(text)
        if text_2 != "" :
            label_2.show()
            label_2.setText(text_2) 
        if maximum  is not None:
            progressBar.setMaximum(maximum)
        progressBar.setValue(value)

        return widget, progressBar
    

    def update(self, value, label=None):
        self.bar.setValue(value)
        if label:
            lbl = self.dialog.findChild(QLabel, "text_1", Qt.FindChildrenRecursively)
            if lbl:
                lbl.setText(label)
        QCoreApplication.processEvents()

    def close(self):
        self.dialog.close()
