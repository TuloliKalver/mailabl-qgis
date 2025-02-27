import os
import time
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget

# Assuming widgets_path is correctly set to the UI file with the progress bar

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))

class ProgressBarTester(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load the UI with the progress bar
        self.progress_widget = loadUi(widgets_path)
        self.progress_bar = self.progress_widget.testBar  # Ensure 'testBar' is the correct object name in your UI
        self.progress_widget.setWindowTitle("Testing Progress Bar")
        self.progress_bar.setMaximum(100)

    def run_test_task(self):
        self.progress_widget.show()
        
        for i in range(1, 101):  # Simulate a task with 100 steps
            time.sleep(0.05)  # Sleep for 50ms, total ~5 seconds for 100 steps
            self.progress_bar.setValue(i)
            
            # Only update the UI every 10 steps to improve performance
            if i % 10 == 0:
                QCoreApplication.processEvents()

        self.progress_widget.hide()
        print("Task completed successfully!")

# integrating into Mailabl plugin
if __name__ == "__main__":
    tester = ProgressBarTester()
    tester.run_test_task()