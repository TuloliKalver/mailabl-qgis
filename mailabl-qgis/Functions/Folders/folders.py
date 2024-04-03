import shutil
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import SettingsDataSaveAndLoad
from ...queries.python.projects_pandas import TableHeaders
from ...queries.python.DataLoading_classes import GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder

def copy_and_rename_folder(table):
    source_folder = SettingsDataSaveAndLoad().load_projcets_copy_folder_path_value()
    target_folder = SettingsDataSaveAndLoad().load_target_Folder_path_value()

    #source_folder = r"C:\Users\Kalver\Desktop\Copydev\Copy_me"
    #target_folder = r"C:\Users\Kalver\Desktop\Copydev\Copy_Done"


    headers = TableHeaders()
    # Get the selected row index
    selected_row_index = table.selectionModel().currentIndex().row()
       # Get the model associated with the table
    model = table.model()
    value = headers.header_name
 

    # Find the column index by header name, skipping empty headers
    column_index = None
    for column in range(model.columnCount()):
        header_data = model.headerData(column, QtCore.Qt.Horizontal)
        if header_data and header_data == value:
            column_index = column
            break

    if column_index is not None:
        print(f"Column index of header '{value}': {column_index}")
        
        # Get the value in the selected row and specified column
        project_name = model.data(model.index(selected_row_index, column_index))
        print(f"Selected value in column '{value}' for the selected row: {project_name}")
        project_id = model.data(model.index(selected_row_index, 0))    
        if project_name is not None or '':
            try:
                # Check if the target folder with the new name already exists
                if os.path.exists(os.path.join(os.path.dirname(target_folder),project_name)):
                    QMessageBox.information(None, "Error", f"A folder with the name '{project_name}' already exists in the target location.")
                else:
                    shutil.copytree(source_folder, target_folder)
                    os.rename(target_folder, os.path.join(os.path.dirname(target_folder), project_name))
                    link = os.path.join(os.path.dirname(target_folder), project_name)
                    
                    Link_updater().update_link(project_id, link)
                    QMessageBox.information(None, "Success", f"Folder '{source_folder}' copied to '{target_folder}' and renamed to '{project_name}' successfully.")
           
            except Exception as e:
                QMessageBox.critical(None, "Error", f"An error occurred: {e}")
        
        else:
            QMessageBox.error(None, 'Error', f"Jätkamiseks vali mõni projekt")    
    
    else:
        print(f"Header '{value}' not found or empty in the model.")

class Link_updater:
    def update_link(self, project_id, link):
            query_loader = GraphQLQueryLoader() 
            query = query_loader.load_query_for_projects(query_loader.UPDATE_project_properties)
            
            variables = {
                        "input": {
                            "id": project_id,
                            "filesPath": link
                             
                        }
                        }
            
            response = requestBuilder.construct_and_send_request(self, query, variables)
            print(response)


