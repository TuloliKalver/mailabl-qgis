import shutil
import os
from PyQt5.QtWidgets import QMessageBox

def copy_and_rename_folder(source_folder, target_folder, new_name):
    try:
        # Check if the target folder with the new name already exists
        if os.path.exists(os.path.join(os.path.dirname(target_folder), new_name)):
            QMessageBox.information(None, "Error", f"A folder with the name '{new_name}' already exists in the target location.")
        else:
            shutil.copytree(source_folder, target_folder)
            os.rename(target_folder, os.path.join(os.path.dirname(target_folder), new_name))
            QMessageBox.information(None, "Success", f"Folder '{source_folder}' copied to '{target_folder}' and renamed to '{new_name}' successfully.")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred: {e}")