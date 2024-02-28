import subprocess
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate


class FileDelegate(QStyledItemDelegate):
    def __init__(self, file_column_index, parent=None):
        super(FileDelegate, self).__init__(parent)
        self.file_column_index = file_column_index
    
    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                file_value = model.data(model.index(index.row(), self.file_column_index), Qt.DisplayRole)
                self.open_folder_in_local_file_browser(file_value)
                return True
        return super().editorEvent(event, model, option, index)

    def open_folder_in_local_file_browser(self, file_id):
        #print(f"file_id: {file_id}")
        # Use subprocess to open the local file explorer
        subprocess.Popen(['explorer', file_id.replace('/', '\\')], shell=True)