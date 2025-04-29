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
from ...config.settings_new import PluginSettings

from ...config.iconHandler import iconHandler

from ...queries.python.query_tools import requestBuilder
from ...queries.python.FileLoaderHelper import GraphQLQueryLoader, GraphqlProperties
from ...queries.python.responses import HandlePropertiesResponses
from .query_cordinator import PropertiesConnectedElementsQueries
from ...config.settings import MailablWebModules, OpenLink
from ...config.ui_directories import PathLoader, plugin_dir_path, UI_multiline_Statusbar
from ...utils.ProgressHelper import ProgressDialogModern
from ...KeelelisedMuutujad.messages import Headings
from ...widgets.decisionUIs.DecisionMaker import DecisionDialogHelper
from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame

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
    def update_tree_with_modules(self, treeWidget, item):
        #print(f"item: {item}")
        language = Languages.ESTONIA
        treeWidget.clear()  # Clear existing items (optional)

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
        
        variables =  {
            "first": first,
            "after": after,
            "search": item_str
        }

        
        module = Module.PROPRETIE

        file =  GraphqlProperties.W_properties_number_improwed
        query = GraphQLQueryLoader.load_query_by_module(module, file)


        response = requestBuilder().construct_and_send_request(query, variables)
        #print(f"response {response}")
        #start do use data
        if response.status_code == 200:
            data_id = HandlePropertiesResponses._response_properties_data_edges(response)
            QCoreApplication.processEvents()

            #test = True
            #print(f"returned data: {data_id}")
                # Extract the id value from the returned data
            if data_id and 'node' in data_id[0]:
                property_id = data_id[0]['node'].get('id')
                #print(f"Extracted id: {property_id}")
                StoreValues().save_propertyID(property_id)
            #if test == True:
            else:
                buttons = {"keep": "Edasi",}
                DecisionDialogHelper.ask_user(
                title=Headings.WARNING_CRITICAL,
                message="Antud kinnistut ei leitud Mailabli keskkonnas,\nPalun pöördu probleemi lahendamisega \nkinnistutega tegeleva isiku poole",
                options=buttons,
                parent=self,
                type= AnimatedGradientBorderFrame.WARNING
                    )
                no_value = [0]
                StoreValues().save_propertyID(no_value)

                #print("No valid data found to extract id")

        progress.update(value=10)
        #print(f"property_id: {property_id}")
        # Continue with your function implementation
        child_data = {}
        #print(f"All modules: {Module().all_modules}")
            
        for index, module_name in enumerate(Module().all_modules, start=1):
            #print(f"indexes by module name: {index}, {module_name}")
            

            # Update the progress bar
            property_id_str = str(property_id)
            module_data = PropertiesConnectedElementsQueries().fetch_module_data(module_name, property_id_str, index)
            #print(f"module_data: {module_data}")
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
                            if index == 10:
                                typename = "Teostusjoonised"
                            if index == 3:
                                typename = "Tegevused"
                            if typename not in child_data:
                                child_data[typename] = []
                                # Remove the last character from typename
                            child_data[typename].append(node_data)
            QCoreApplication.processEvents()

        #print(f"child_data: {child_data}")
        #print(f"child data: {child_data}")
 
        length = len(child_data.keys())
        progress.update(50, "uuesti")

        # Pre-load AsBuilt types only once
        Asbuilttypes = PluginSettings.load_setting(
            module=Module.ASBUILT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
        )
        print(f"Loaded Asbuilttypes: {Asbuilttypes}")
        if isinstance(Asbuilttypes, str):
            import ast
            try:
                Asbuilttypes = ast.literal_eval(Asbuilttypes)
            except Exception:
                Asbuilttypes = []

        Asbuilttypes = [str(t).strip() for t in Asbuilttypes]  # sanitize
        print (f"Asbuilttypes: {Asbuilttypes}")
        #print (f"child_data: {child_data}")
        if child_data:
            for typename, items in child_data.items():
                module = typename.lower()

                # Load translated name once
                module_str = ModuleTranslation.module_name(module, language)

                # Define filter rule
                def should_include(child):
                    child_type = child.get("type", {}).get("name", "")
                    if typename == "Tegevused":
                        return child_type not in Asbuilttypes
                    elif typename == "Teostusjoonised":
                        return child_type in Asbuilttypes
                    else:
                        return True  # Easement or any other group

                # Filtered list of children
                allowed_children = [child for child in items if should_include(child)]

                if not allowed_children:
                    continue  # Don't create empty root

                # Create root item
                root_item = QTreeWidgetItem(treeWidget)
                root_item.setData(0, QtCore.Qt.UserRole, "main_item")
                root_item.setData(0, Qt.UserRole, module)
                root_item.setText(0, module_str)

                for child in allowed_children:
                    child_item = QTreeWidgetItem(root_item)
                    child_type = child.get("type", {}).get("name", "")
                    child_id = child.get("id", "")
                    status = child.get("status", {}).get("name", "")

                    child_item.setText(2, child_id)
                    child_item.setText(6, status)

                    if typename in ["Tegevused", "Teostusjoonised"]:
                        # Task-like entry
                        child_item.setText(0, child_type)
                        child_item.setText(4, "")
                        child_item.setText(1, child.get("title", ""))
                    else:
                        # Easement-like entry
                        child_item.setText(1, child.get("name", ""))
                        number = child.get("number", "") or ""
                        child_item.setText(0, str(number))
                        path = child.get("filesPath", "")
                        child_item.setData(5, Qt.UserRole, path)

                    child_item.setData(3, Qt.UserRole, typename)

                    # Set icons
                    MyTreeHome.set_clickable_webIcon(child_item, 3)
                    MyTreeHome.set_clickable_folderIcon(child_item, 5)

                    length += 1
                    progress.update(length, text2="Laen Mooduleid")

                QCoreApplication.processEvents()



        progress.update(100, text1="Valmis!")
        progress.close()

        treeWidget.setHeaderLabel("Seotud tulemusi")
        treeWidget.setHeaderLabels([MyTreeHome.header_number, MyTreeHome.header_name, MyTreeHome.header_id, "", MyTreeHome.header_file_path, "", MyTreeHome.header_statuses])
        

        # Hide the second column (index 1)
        treeWidget.setColumnHidden(2, True)
        treeWidget.setColumnHidden(4, True)
        
        # Connect the treeWidget's itemClicked signal to a handler
        treeWidget.itemClicked.connect(MyTreeHome.open_in_web_brauser)
        treeWidget.itemClicked.connect(MyTreeHome.handle_dok_clicked)

        treeWidget.setColumnWidth(0, 165)
        treeWidget.setColumnWidth(1, 350)
        treeWidget.setColumnWidth(3, 20)
        treeWidget.setColumnWidth(5, 20)

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
                #print(f"module name in column: {module}")
                module = module.lower()
                if module == "tegevused":
                    module = Module.TASK
                if module == "teostusjoonised":
                    module = Module.TASK
                else:
                    module = module
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
    def open_property(self):
        link_id = StoreValues().return_properties_id()
        #print(f"link_id: {link_id}")
        if link_id[0] == "0":
            buttons={"keep": "Edasi",}
            DecisionDialogHelper.ask_user(
                title=Headings.inFO_SIMPLE,
                message="Antud kinnistut ei leitud Mailabli keskkonnas,\nPalun pöördu probleemi lahendamisega \nkinnistutega tegeleva isiku poole",
                options=buttons,
                parent=self,
                type= AnimatedGradientBorderFrame.WARNING
                    )
            return
        else:    
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

