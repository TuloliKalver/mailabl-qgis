import subprocess
import requests
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from ..config.settings import  OpenLink, MailablWebModules
#from ..queries.python.contractsBySingleItem import getContractsWhere
from ..queries.python.ContractWhere import getContractsWhere
from ..queries.python.projects_pandas import GetProjectsWhere
from .item_selector_tools import properties_selectors

class ModuleButtonDelegate(QStyledItemDelegate):
    def __init__(self, id_column_index, parent=None, module = None):
        super(ModuleButtonDelegate, self).__init__(parent)
        self.id_column_index = id_column_index
        self.module = module

    
    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                id_value = model.data(model.index(index.row(), self.id_column_index), Qt.DisplayRole)
                self.open_contract_in_mailabl(id_value)
                return True
        return super().editorEvent(event, model, option, index)
    
    def open_contract_in_mailabl(self, id):
        web_link = OpenLink.weblink_by_module(self.module)
        project_link = f"{web_link}{id}"
        response = requests.get(project_link, verify=False)
        webbrowser.open(response.url)        
        

class FileDelegate(QStyledItemDelegate):
    def __init__(self, file_column_index, parent=None):
        super(FileDelegate, self).__init__(parent)
        self.file_column_index = file_column_index
    
    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the path value from the model
                file_value = model.data(model.index(index.row(), self.file_column_index), Qt.DisplayRole)
                print(f"File value: {file_value}")
                self.open_folder_in_local_file_browser(file_value)
                return True
        return super().editorEvent(event, model, option, index)

    def open_folder_in_local_file_browser(self, file_id):
        subprocess.Popen(['explorer', file_id.replace('/', '\\')], shell=True)
        

class SelectByModuleElementsOnMapDelegate(QStyledItemDelegate):
    def __init__(self, ID_column_index, parent=None, module=None):
        super(SelectByModuleElementsOnMapDelegate, self).__init__(parent)
        self.ID_column_index = ID_column_index
        self.module = module

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                id_value = str(model.data(model.index(index.row(), self.ID_column_index), Qt.DisplayRole))
                # Access the appropriate query based on the module
                if self.module == MailablWebModules().projects:
                    print("load project properties")
                    values = GetProjectsWhere.query_projects_related_properties(self, id_value)
                elif self.module == MailablWebModules().contracts:
                    values = getContractsWhere.QueryContracts_relatedProperties(self, id_value)
                elif self.module == MailablWebModules().easements:
                    print("load easment properties")
                    #values = getEasementsWhere.QueryEasements_relatedProperties(self, id_value)
                else:
                    # Handle unknown module
                    return False
                total = len(values)
                layer_type = "active"
                properties_selectors.show_connected_cadasters(values, layer_type)
                return True
        return super().editorEvent(event, model, option, index)