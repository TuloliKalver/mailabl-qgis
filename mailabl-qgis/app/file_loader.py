import subprocess

from qgis.PyQt.QtWidgets import QFileDialog


class FileLoader:
    def __init__(self):
        pass


    def load_shp_layer(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Shapefiles (*.shp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()
            file_path = file_path[0]
            layer_name = os.path.splitext(os.path.basename(file_path))[0]


    @staticmethod
    def open_with_default_application(file_path):
        try:
            subprocess.Popen(["xdg-open", file_path])  # Linux
        except Exception:
            try:
                subprocess.Popen(["open", file_path])  # macOS
            except Exception:
                subprocess.Popen(["start", "", file_path], shell=True)
                
    def get_layer_name_from_path(file_path):
        return file_path.split('/')[-1].split('.')[0]

    @staticmethod
    def load_shp_layer(label):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Shapefiles (*.shp)")
#        if file_dialog.exec_():
#            selected_files = file_dialog.selectedFiles()
    
    @staticmethod
    def load_csv(label):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("CSV files (*.csv)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                # Open the CSV file with the default application
                FileLoader.open_with_default_application(file_path)
    
    @staticmethod
    def load_folder(label):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly, True)
        if folder_dialog.exec_():
            selected_folder = folder_dialog.selectedFiles()[0]
            # Open the folder with the default file manager
            FileLoader.open_with_default_application(selected_folder)
            # You can return the folder path or any relevant information



