import shutil
import os
import re
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from ...config.settings import SettingsDataSaveAndLoad
from ...queries.python.projects_pandas import TableHeaders
from ...queries.python.DataLoading_classes import GraphQLQueryLoader
from ...queries.python.query_tools import requestBuilder
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, HoiatusTextsAuto
from ...utils.messagesHelper import ModernMessageDialog
def copy_and_rename_folder(table):
    text = "Ettevalmistatud struktuuriga projektikaustade genereerimine on mõeldud eelkõige uutele projektidele.\nEnne jätkamist kontrolli ega samasisulist kausta pole juba loodud.\nOled kindel, et soovid jätkata?"

    overall_confirmation = QMessageBox.question(None, "Confirmation", text,
                                        QMessageBox.Yes | QMessageBox.No)

    if overall_confirmation == QMessageBox.Yes:

        source_folder = SettingsDataSaveAndLoad().load_projcets_copy_folder_path_value()
        target_folder = SettingsDataSaveAndLoad().load_target_Folder_path_value()

        headers = TableHeaders()
        # Get the selected row index
        selected_row_index = table.selectionModel().currentIndex().row()
        # Get the model associated with the table
        model = table.model()
        value_name = headers.header_name
    
        # Find the column index by header name, skipping empty headers
        column_index = None
        for column in range(model.columnCount()):
            header_data = model.headerData(column, QtCore.Qt.Horizontal)
            if header_data and header_data == value_name:
                column_index = column
                break

        value_number = headers.header_number
        column_number_index = None
        for column in range(model.columnCount()):
            header_data = model.headerData(column, QtCore.Qt.Horizontal)
            if header_data and header_data == value_number:
                column_number_index = column
                break



        if column_index is not None:
            # Get the value in the selected row and specified column
            project_name_raw = model.data(model.index(selected_row_index, column_index))

            # Remove unwanted characters from the project name
            project_name = re.sub(r'[<>:"/\\|?*.]', '', project_name_raw)

            project_number = model.data(model.index(selected_row_index, column_number_index))



            if project_name:
                try:
                    # Use the FolderNameGenerator to generate the folder name based on the user-defined order
                    folder_name = FolderNameGenerator().folder_structure_name_order(project_name, project_number)
                    
                    # Check if the target folder with the new name already exists
                    if os.path.exists(os.path.join(os.path.dirname(target_folder), folder_name)):                        
                        text = f"Kaust nimega '{folder_name}' on juba sihtkohas olemas."
                        heading = Headings().warningSimple
                        ModernMessageDialog.Info_messages_modern(heading,text)
                    else:
                        shutil.copytree(source_folder, target_folder)
                        os.rename(target_folder, os.path.join(os.path.dirname(target_folder), folder_name))
                        
                        # Ask the user for confirmation
                        confirmation = QMessageBox.question(None, "Confirmation", "Oled kindel, et soovid genereeritud kausta lingi lisada Mailablis projektile?",
                                                            QMessageBox.Yes | QMessageBox.No)


                        if confirmation == QMessageBox.Yes:
                            # Call the linkUpdater function
                            project_id = model.data(model.index(selected_row_index, 0))
                            print(f"project_id {project_id}")
                            link = os.path.join(os.path.dirname(target_folder), folder_name)
                            Link_updater().update_link(project_id, link)

                        else:
                            print("Operation canceled by the user.")
                
                        # Display success message using modern dialog box
                        heading = Headings().tubli
                        text = (f"Kausta '{source_folder}'\n(k.a kaustas sisalduvad alamkaustad ja failid) dubleerimine õnnestus.")
                        text_2 = f"Sihtkohta on genereeritud kaust nimetusega \n'{folder_name}'."
                        ModernMessageDialog.Info_messages_modern(heading,text, text_2)
                       
                except Exception as e:
                    heading = Headings().warningSimple
                    text = f"An error occurred: {e}"
                    ModernMessageDialog.Info_messages_modern(heading,text)
                    

            else:
                heading = Headings().warningSimple
                text = f"Jätkamiseks vali mõni projekt"
                ModernMessageDialog.Info_messages_modern(heading,text)

        else:
            heading = Headings().warningSimple
            text = HoiatusTexts().error
            ModernMessageDialog.Info_messages_modern(heading,text)
            print(f"Header  not found or empty in the model.")

    else:
        print("Operation canceled by the user.")


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

class FolderNameGenerator:
    def folder_structure_name_order(self, project_name, project_number):
        value = SettingsDataSaveAndLoad.load_projects_prefered_folder_name_structure(self)
        print(f"Value: {value}")

        # Split the value into individual components
        components = value.split(" + ")

        # Initialize an empty list to hold the parts of the folder name
        folder_name_parts = []

        # Iterate through each component and construct the folder name parts
        for component in components:
            # Check if the component contains a symbol in parentheses
            if "(" in component and ")" in component:
                # Extract the symbol from the parentheses
                symbol = component.split("(")[-1].split(")")[0]
                # Remove the symbol part from the component
                component = component.replace(f"({symbol})", "")
            else:
                # If no symbol is specified, set it to an empty string
                symbol = ""

            # Check the component type and add the corresponding part to the folder name
            if component == "Projekti number":
                folder_name_parts.append(project_number)
            elif component == "Sümbol":
                folder_name_parts.append(symbol)
            elif component == "Projekti nimetus":
                folder_name_parts.append(project_name)

        # Construct the final folder name by joining the parts
        folder_name = "".join(folder_name_parts)

        # Print the constructed folder name
        heading = Headings().tubli
        text = HoiatusTextsAuto().strange_usage_folder(folder_name)
        ModernMessageDialog.Info_messages_modern(heading, text)
        #print("Folder name:", folder_name)



class FolderNameGenerator:
    def folder_structure_name_order(self, project_name, project_number):
        value = SettingsDataSaveAndLoad.load_projects_prefered_folder_name_structure(self)
        print(f"Value: {value}")

        # Split the value into individual components
        components = value.split(" + ")

        # Initialize an empty list to hold the parts of the folder name
        folder_name_parts = []

        # Iterate through each component and construct the folder name parts
        for component in components:
            # Check if the component contains a symbol in parentheses
            if "(" in component and ")" in component:
                # Extract the symbol from the parentheses
                symbol = component.split("(")[-1].split(")")[0]
                # Remove the symbol part from the component
                component = component.replace(f"({symbol})", "")
            else:
                # If no symbol is specified, set it to an empty string
                symbol = ""

            # Check the component type and add the corresponding part to the folder name
            if component == "Projekti number":
                folder_name_parts.append(project_number)
            elif component == "Sümbol":
                folder_name_parts.append(symbol)
            elif component == "Projekti nimetus":
                folder_name_parts.append(project_name)

        # Construct the final folder name by joining the parts
        folder_name = "".join(folder_name_parts)

        # Return the constructed folder name
        return folder_name




