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
    def update_progress(value: int, maximum: Optional[int] = None):
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
            ProgressHelper.update_progress(value=current_index)
            QCoreApplication.processEvents()