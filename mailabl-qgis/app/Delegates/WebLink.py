import requests
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from ...config.settings import OpenLink



class WebLinkDelegate(QStyledItemDelegate):
    def __init__(self, id_column_index, parent=None):
        super(WebLinkDelegate, self).__init__(parent)
        self.id_column_index = id_column_index
    
    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                id_value = model.data(model.index(index.row(), self.id_column_index), Qt.DisplayRole)
                self.open_project_in_mailabl(id_value)
                return True
        return super().editorEvent(event, model, option, index)

    def open_project_in_mailabl(self, project_id):
        web_link = OpenLink.web_link_single_projects()
        project_link = f"{web_link}{project_id}"
        try:
            response = requests.get(project_link, timeout=10, verify=False)
            webbrowser.open(response.url)
        except requests.Timeout:
            print("Request timed out.")
        except requests.RequestException as e:
            print(f"Error: {e}")