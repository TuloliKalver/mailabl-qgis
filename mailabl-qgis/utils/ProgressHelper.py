
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

    @staticmethod
    def load_progress_dialog(value:int, maximum:Optional[int]=None, title:str="Andmete laadimine...", text:str =None, text_2:str=None, Show=True):
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
        print(f"widget name: {widget_name}")
        widget = Filepaths.load_ui_file(widget_name)
        if not widget:
            print(f"Could not load {widget_name} file.")
            return
        for child in widget.children():
            print(child.objectName())
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.setAttribute(Qt.WA_DeleteOnClose)
    
        drag_frame = widget.findChildren(QFrame, "dragFrame")
        frame = widget.findChildren(QFrame, "frame")

        title_label = drag_frame.findChild(QLabel, "lblTitle", Qt.FindChildrenRecursively)
        if not title_label:
            print("⚠️ Could not find QLabel 'lblMainTitle' in progress dialog UI")
        main_label = frame.findChild(QLabel, "lblMain", Qt.FindChildrenRecursively)
        if not main_label:
            print("⚠️ Could not find QLabel 'lblMain' in progress dialog UI")
        label_1 = frame.findChild(QLabel, "text_1", Qt.FindChildrenRecursively)
        if not label_1:
            print("⚠️ Could not find QLabel 'text_1' in progress dialog UI")
        label_2 = frame.findChild(QLabel, "text_2", Qt.FindChildrenRecursively)
        if not label_2:
            print("⚠️ Could not find QLabel 'text_2' in progress dialog UI")
        progressBar = frame.findChild(QProgressBar, "bar", Qt.FindChildrenRecursively)
        if not progressBar:
            print("⚠️ Could not find QProgressBar 'bar' in progress dialog UI")

        if title is not None:
            main_label.setText(title)
        if text is not None:
            label_1.setText(text)
        if text_2 is not None:
            label_2.setText(text_2) 
        if maximum  is not None:
            progressBar.setMaximum(maximum)
        progressBar.setValue(value)

        if Show:
            widget.show()
        else:
            widget.hide()