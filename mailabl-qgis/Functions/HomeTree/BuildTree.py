import subprocess
import webbrowser  # For opening links in browser
import requests
from qgis.core import QgsSettings
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtGui import QIcon, QBrush
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QColor
from ...utils.ColorHelper import ColorUtils
from ...KeelelisedMuutujad.modules import Module, Languages, ModuleTranslation
from ...config.settings import Filepaths, IconsByName
from ...config.iconHandler import iconHandler
from ...queries.python.query_tools import requestBuilder
from ...queries.python.DataLoading_classes import GraphQLQueryLoader, Graphql_properties
from ...queries.python.responses import HandlePropertiesResponses
from .query_cordinator import PropertiesConnectedElementsQueries
from ...config.settings import MailablWebModules, OpenLink
from ...config.ui_directories import PathLoader, plugin_dir_path, UI_multiline_Statusbar
from ...utils.ProgressHelper import ProgressDialogModern

paths = PathLoader(plugin_dir_path, UI_multiline_Statusbar)

class MyTreeHome:
    header_id = 'ID'
    header_number = 'Number'
    header_name = 'Nimetus'
    header_deadline = 'Tähtaeg'
    header_color = 'Color'
    header_creator = 'Looja'
    header_property_number = 'Kataster'
    header_properties_icon ='propertiesIcon'
    header_parent_id = 'Parent_id'
    header_webLinkButton = 'web_link_button'
    header_Documents = 'Dokumendid'
    header_file_path = "file_path_button"
    header_statuses = 'Staatus'

    @staticmethod
    def update_tree_with_modules(treeWidget, item):
        #print(f"item: {item}")
        language = Languages.ESTONIA

        treeWidget.clear()  # Clear existing items (optional)
        treeWidget.setHeaderLabel("Seotud tulemusi")
        treeWidget.setHeaderLabels([MyTreeHome.header_number, MyTreeHome.header_name, MyTreeHome.header_id, "", MyTreeHome.header_file_path, "", MyTreeHome.header_statuses])
            # Initialize child_data to combine results from all modules

        # Get the module attributes
        module_attrs = Module().all_modules# [attr for attr in dir(Module) if not attr.startswith("_") and not callable(getattr(Module, attr))]
        total = len(module_attrs)

        # Initialize the progress dialog
        progress = ProgressDialogModern(title="Katastri laadimine", value=0, maximum=total)

        progress.update(1, purpouse="Katastri laadimine", text1="Palun oota...")

        #end_cursor_id = None  # Initialize end_cursor before the loop
        first = 1
        after = None
        # Extract the single item from the list and convert to string
        item_str = str(item[0]) if isinstance(item, list) and len(item) == 1 else str(item)
        
        variables_id =  {
            "first": first,
            "after": after,
            "search": item_str
        }

        query_id = Graphql_properties().load_query_for_properties_WHERE(Graphql_properties().W_properties_number_improwed)

        response_id = requestBuilder().construct_and_send_request(None,query_id, variables_id)
        #print(f"response {response}")
        #start do use data
        if response_id.status_code == 200:
            data_id = HandlePropertiesResponses._response_properties_data_edges(response_id)
            QCoreApplication.processEvents()

            #print(f"returned data: {data_id}")
                # Extract the id value from the returned data
            if data_id and 'node' in data_id[0]:
                property_id = data_id[0]['node'].get('id')
                #print(f"Extracted id: {property_id}")
                StoreValues().save_propertyID(property_id)
            else:
                print("No valid data found to extract id")
        progress.update(value=10)
        #print(f"property_id: {property_id}")
        # Continue with your function implementation
        child_data = {}
        for index, module_name in enumerate(Module().all_modules, start=1):
            # Update the progress bar
            property_id_str = str(property_id)
            module_data = PropertiesConnectedElementsQueries().fetch_module_data(module_name, property_id_str)
            progress.update(value=25)
            QCoreApplication.processEvents()
            #print(f"module_data: {module_data}")
            # Check if module_data is not empty before updating child_data
            if module_data:
                for data_list in module_data:
                    for item in data_list:
                        node_data = item.get('node')
                        if node_data:
                            typename = node_data['__typename']
                            if typename not in child_data:
                                child_data[typename] = []
                                # Remove the last character from typename
                            child_data[typename].append(node_data)
            QCoreApplication.processEvents()

        #print(f"child_data: {child_data}")
        #print(f"child data: {child_data}")
 
        length = len(child_data.keys())
        progress.update(50, "uuesti")
        if child_data:  # Only add module if data is returned
            #print(f"length: {length}")
            for typename, items in child_data.items():  # Iterate over child_data correctly
                root_item = QTreeWidgetItem(treeWidget)
                # Set custom property for main item
                root_item.setData(0, QtCore.Qt.UserRole, "main_item")

                # Use lowe bechase typename has capital letters at start
                module = typename.lower() 
                # Store the module information in the item's data
                root_item.setData(0, Qt.UserRole, module)

                # Translate the module name using ModuleTranslation
                moduel_str = ModuleTranslation.module_name(module, language)
                root_item.setText(0, moduel_str)
                progress.update(index, text2=f"Alustan moodulite laadimist")
                for child in items:  # Iterate over each item in the list
                    child_item = QTreeWidgetItem(root_item)
                    child_item.setText(2, child["id"])  # Store the link in column 2
                    # Assuming 'dok' is a key that may or may not exist in each child dictionary
                    #print(f"typename: {typename}")
                    if module == Module.TASK:
                        child_item.setText(0, "")
                        child_item.setText(4, "")
                        child_item.setText(1, child.get("title",""))
                    else:
                        child_item.setText(1, child.get("name",""))
                        number = child.get("number", "")  # Get the number, default to empty string
                        if number == None:
                            number = ""
                        child_item.setText(0, str(number))
                        path = child.get("filesPath", "")
                        #print(f"insert path: {path}")
                        child_item.setData(5, Qt.UserRole, path)
                    
                    # Display statuses in a format that makes sense for your application
                    status = child["status"]
                    status_name = status['name']

                    child_item.setText(6,status_name)  # Assuming 6 is the index of the column to display statuses

                    # Store the module information in the item's data
                    child_item.setData(3, Qt.UserRole, typename)
                    # Set clickable icon for the link (replace with your icon logic)

                    MyTreeHome.set_clickable_webIcon(child_item, 3) 
                    MyTreeHome.set_clickable_folderIcon(child_item, 5)
                    length = length+1
                    progress.update(length, text2="Laen Mooduleid")
            
                QCoreApplication.processEvents()
        # Step 2
        progress.update(100, text1="Valmis!")
        progress.close()
        # Hide the second column (index 1)
        treeWidget.setColumnHidden(2, True)
        treeWidget.setColumnHidden(4, True)
        
        # Connect the treeWidget's itemClicked signal to a handler
        treeWidget.itemClicked.connect(MyTreeHome.open_in_web_brauser)
        treeWidget.itemClicked.connect(MyTreeHome.handle_dok_clicked)

        treeWidget.setColumnWidth(0, 150)
        treeWidget.setColumnWidth(1, 350)
        treeWidget.setColumnWidth(3, 30)
        treeWidget.setColumnWidth(5, 30)

        # Expand all items to make sure they are visible
        treeWidget.expandAll()
        QCoreApplication.processEvents()



    def set_clickable_webIcon(tree_item, column):
        # Replace with your logic to get the icon path based on link type or preference
        icon_path = Filepaths.get_icon(IconsByName().Mailabl_icon_name)
        icon = QIcon(icon_path)

        # Set the icon and make the text empty (invisible)
        tree_item.setIcon(column, icon)
        tree_item.setText(column, "")  # Set empty text for the link column

        # Make the entire item clickable, not just the icon (optional)
        tree_item.setFlags(tree_item.flags() | Qt.ItemIsSelectable)
        
    def open_in_web_brauser(item, column):
        if column == 3:  # Check for link column
            module = item.data(column, Qt.UserRole)  # Retrieve the stored module information
            if module:
                # Convert to lowercase and add "s" (handle potential None value)
                module = module.lower() + 's'
            #print(f"Module in column head: {module}")
            link_id = item.text(2)
            web_module = MailablWebModules().get_web_link(module)
            #print(f"web_module: {web_module}")
            web_link = OpenLink.weblink_by_module(web_module)
            #print(f"web_link: {web_link}")
            link = f"{web_link}{link_id}"
            response = requests.get(link, verify=False)
            webbrowser.open(response.url)

    def set_clickable_folderIcon(tree_item, column):
        dok_path = tree_item.data(column, Qt.UserRole)  # Retrieve the stored module informatio
        if dok_path:
            icon_path = iconHandler.set_document_icon_based_on_item(dok_path)
            icon = QIcon(icon_path)
            tree_item.setIcon(column, icon)
            # Make the entire item clickable, not just the icon (optional)
            tree_item.setFlags(tree_item.flags() | Qt.ItemIsSelectable)
        else:
            pass

    def handle_dok_clicked(item, column):
        if column == 5:
            dok_path = item.data(column, Qt.UserRole)  # Retrieve the stored module information
            #print(f"dok_path: {dok_path}")
            subprocess.Popen(['explorer', dok_path.replace('/', '\\')], shell=True)

    @staticmethod
    def open_property():
        link_id = StoreValues().return_properties_id()
        module = Module.PROPRETIE
        web_module = MailablWebModules().get_web_link(module)
        web_link = OpenLink.weblink_by_module(web_module)
        link = f"{web_link}{link_id}"
        response = requests.get(link, verify=False)
        webbrowser.open(response.url)

class StoreValues:
    def __init__(self) -> None:
        self.propertyID_location = 'MailablProperty_id/stores_id'

    def return_properties_id(self):
        settings_address = self.propertyID_location
        settings = QgsSettings()
        value = settings.value(settings_address, '', type=str)
        return value
    

    def load_propertieID_from_memory (self):
        value = self.propertyID_location
        return value
    
    def save_propertyID(self, input_value):
        settings = QgsSettings()
        target_settings_address = self.propertyID_location
        settings.setValue(target_settings_address, input_value)

