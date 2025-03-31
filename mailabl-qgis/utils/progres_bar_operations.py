

#progres_bar_operations.py

import os
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Status bar widget folder
widgets_folder = "widgets"  
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))

class ProgressBarHandler(QWidget):
    def __init__(self, window_title="Progress", max_value=100):
        super().__init__()
        self.window_title = window_title
        self.max_value = max_value
        self.init_ui()

    def init_ui(self):
        # Load the UI with the progress bar
        self.progress_widget = loadUi(widgets_path)
        self.progress_bar = self.progress_widget.testBar  # Ensure 'testBar' matches the object name in UI
        self.progress_widget.setWindowTitle(self.window_title)
        self.progress_bar.setMaximum(self.max_value)

    def run_indeterminate_progress(self, task_function):
        """
        Runs an indeterminate progress bar (busy indicator) while executing the provided task.
        """
        self.progress_widget.show()
        self.progress_bar.setRange(0, 0)  # Indeterminate mode
        QCoreApplication.processEvents()

        # Pass `self` as argument to the task function
        result = task_function(self)  

        # After task completes, stop the busy indicator
        self.progress_bar.setRange(0, self.max_value)
        self.progress_bar.setValue(self.max_value)
        self.progress_widget.hide()
        #print(f"Task '{self.window_title}' completed successfully!")

        return result  # Return the result!


    def run_dynamic_progress(self, task_function, total_steps=100):
        """
        Runs a dynamic progress bar, updating based on task steps while executing the provided task.
        """
        self.progress_widget.show()
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(total_steps)

        # Execute the provided task and capture the result
        result = task_function(self)

        self.progress_widget.hide()
        #print(f"Task '{self.window_title}' completed successfully!")

        return result  # Make sure to return the result!

    def increment_progress(self, step, throttle=10):
        """
        Increments the progress bar dynamically.
        Throttles UI updates for large datasets to improve performance.
        """
        if step % throttle == 0 or step == self.max_value:
            self.progress_bar.setValue(step)
            QCoreApplication.processEvents()


# Wrapper function for universal use
@staticmethod
def run_with_progress(task_function, window_title="Processing", total_steps=None):
    """
    Universal wrapper function to run any task with a progress bar.

    Parameters:
    - task_function: The function to execute. It should accept `progress_handler` as an argument.
    - window_title: Title for the progress bar window.
    - total_steps: Total steps for dynamic progress. If None, runs in indeterminate mode.

    Returns:
    - The result of the task function.
    """
    #print(f"[run_with_progress] Initializing progress bar with title: {window_title}")
    progress_handler = ProgressBarHandler(window_title=window_title, max_value=total_steps or 100)

    if total_steps:
        #print("[run_with_progress] Running dynamic progress task...")
        result = progress_handler.run_dynamic_progress(task_function, total_steps)
    else:
        #print("[run_with_progress] Running indeterminate progress task...")
        result = progress_handler.run_indeterminate_progress(task_function)

    #print(f"[run_with_progress] Task completed. Result: {result}")
    return result  # Ensure the result from the task is returned



