import subprocess
import webbrowser
import requests
from qgis.core import QgsSettings
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtCore import Qt, QCoreApplication
from .TreeHelper import TreeHelper, StoreValues
from ...utils.ColorHelper import ColorUtils
from ...KeelelisedMuutujad.modules import Module, Languages, ModuleTranslation
from ...queries.python.query_tools import requestBuilder
from ...queries.python.DataLoading_classes import GraphQLQueryLoader, GraphqlProperties
from ...queries.python.responses import HandlePropertiesResponses
from .query_cordinator import PropertiesConnectedElementsQueries

from ...config.ui_directories import PathLoader, plugin_dir_path, UI_multiline_Statusbar

paths = PathLoader(plugin_dir_path, UI_multiline_Statusbar)

class MyTreeHomeView:
    header_number = 'Number'
    header_name = 'Nimetus'
    header_id = 'ID'
    header_file_path = "file_path_button"
    header_statuses = 'status'

    @staticmethod
    def fetch_module_data(module, item):
        #print(f"module name in query: {module} and item: {item}")
        query_name = GraphqlProperties.W_properties_number
        query = GraphQLQueryLoader.load_query_by_module(module, query_name)

        end_cursor = None
        variables = {
            "first": 1,
            "after": end_cursor,
            "where": {
                "column": "CADASTRAL_UNIT_NUMBER",
                "operator": "IN",
                "value": item
            }
        }
        response = requestBuilder().construct_and_send_request(None, query, variables)
        if response.status_code == 200:
            data = HandlePropertiesResponses._response_properties_data_edges(response)
            return data

    @staticmethod
    def update_tree_with_modules(treeView, item):
        print(f"item: {item}")

        langage = Languages.ESTONIA


        # Get the module attributes
        module_attrs = [attr for attr in dir(Module) if not attr.startswith("_") and not callable(getattr(Module, attr))]
        total = len(module_attrs)


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




        response = requestBuilder().construct_and_send_request(None,query, variables)
        #print(f"response {response}")
        #start do use data
        if response.status_code == 200:
            data_id = HandlePropertiesResponses._response_properties_data_edges(response)
            #print(f"returned data: {data_id}")
                # Extract the id value from the returned data
            if data_id and 'node' in data_id[0]:
                property_id = data_id[0]['node'].get('id')
                #print(f"Extracted id: {property_id}")
                StoreValues().save_propertyID(property_id)
            else:
                print("No valid data found to extract id")

   
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([MyTreeHomeView.header_number, MyTreeHomeView.header_name, MyTreeHomeView.header_id, "", MyTreeHomeView.header_file_path, "", MyTreeHomeView.header_statuses])

        child_data = {}
        for index, module_name in enumerate((getattr(Module, attr) for attr in module_attrs), start=1):
            # Update the progress bar
            property_id_str = str(property_id)
            module_data = PropertiesConnectedElementsQueries().fetch_module_data(module_name, property_id_str)
            if module_data:
                for data_list in module_data:
                    for item in data_list:
                        node_data = item.get('node')
                        if node_data:
                            typename = node_data['__typename']
                            if typename not in child_data:
                                child_data[typename] = []
                            child_data[typename].append(node_data)
        QCoreApplication.processEvents()
        print(f"child_data: {child_data}")

        if child_data:
            for typename, items in child_data.items():
                # Create root item (parent row)
                root_item = QStandardItem(ModuleTranslation.module_name(typename.lower() + 's', langage))
                
                # Store module type in UserRole
                root_item.setData("main_item", Qt.UserRole)
                root_item.setData(typename.lower() + 's', Qt.UserRole)

                for child in items:
                    # Prepare all columns as QStandardItems
                    number_item = QStandardItem()
                    title_item = QStandardItem()
                    id_item = QStandardItem()
                    dummy_item = QStandardItem()  # placeholder for column 3 (for icons)
                    file_path_item = QStandardItem()
                    file_dummy_item = QStandardItem()  # placeholder for column 5 (for icons)
                    status_item = QStandardItem()

                    module = typename.lower() + 's'

                    # Fill items based on module type
                    if module == Module.TASK:
                        number_item.setText("")
                        file_path_item.setText("")
                        title_item.setText(child.get("title", ""))
                    else:
                        title_item.setText(child.get("name", ""))
                        number = child.get("number", "")
                        number_item.setText(str(number) if number else "")
                        file_path = child.get("filesPath", "")
                        file_path_item.setText(file_path)
                        file_path_item.setData(file_path, Qt.UserRole)

                    # Set ID
                    id_item.setText(child.get("id", ""))

                    # Set status name and color
                    status = child.get(MyTreeHomeView.header_statuses, {})
                    status_name = status.get("name", "")
                    status_color = status.get("color", "")
                    status_item.setText(status_name)
                    TreeHelper.set_status_color(status_item, status_color)

                    # Optional: Set module type for internal reference (could be used for click handlers)
                    dummy_item.setData(typename, Qt.UserRole)

                    # For TreeView (QStandardItem)
                    TreeHelper.set_clickable_webIcon(dummy_item)
                    TreeHelper.set_clickable_folderIcon(file_path_item, 5)

                    # Add row to root item
                    root_item.appendRow([
                        number_item,
                        title_item,
                        id_item,
                        dummy_item,
                        file_path_item,
                        file_dummy_item,
                        status_item
                    ])

                # Finally, add the root item to the model
                model.appendRow(root_item)

        # Close the progress widget after the loop ends

        delegate = StatusColorDelegate(treeView)
        treeView.setItemDelegate(delegate)

        treeView.expandAll()
        treeView.setColumnHidden(2, True)
        treeView.setColumnHidden(4, True)
        treeView.setColumnWidth(1, 250)
        treeView.setColumnWidth(3, 15)
        treeView.setColumnWidth(5, 15)
        treeView.setColumnWidth(1, 400)

        treeView.clicked.connect(TreeHelper.open_in_web_brauser)
        treeView.clicked.connect(TreeHelper.handle_dok_clicked)
        treeView.setModel(model)

        
class StatusColorDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index = "7"):
        painter.save()

        # Call the base class paint method to draw the default item content
        self.drawBaseContent(painter, option, index)  # Added missing method call


        status_col = MyTreeHomeView.header_statuses.index(MyTreeHomeView.header_statuses)  # or whatever the label is
        if index.column() == status_col:            # Get the status text and color

            status_text = index.data(Qt.DisplayRole)
            status_color_code = index.data(Qt.UserRole + 1)  # Assuming color is stored in UserRole + 1

            if status_color_code:
                try:
                    rgb_color = ColorUtils.hex_to_rgb(status_color_code)
                    background_color = QColor(*rgb_color)
                    painter.setBrush(background_color)
                    painter.drawRect(option.rect)
                    painter.setPen(Qt.black)  # Set foreground color to black
                except Exception as e:
                    print(f"Error in setting color: {e}")

            # Draw the status text with appropriate alignment
            painter.drawText(option.rect, Qt.AlignCenter | Qt.AlignVCenter, status_text)

        painter.restore()

    def drawBaseContent(self, painter, option, index):
        # Implement the logic for drawing the default item content (text, icon)
        # Here's a basic example:
        #  - Get the item text and icon (if available) from the model
        item_text = index.data(Qt.DisplayRole)
        item_icon = index.data(Qt.DecorationRole)

        #  - Draw the icon (if present) using the painter's drawPixmap() method
        if item_icon:
            painter.drawPixmap(option.rect, item_icon.pixmap(option.iconSize))

        #  - Adjust the text rectangle based on icon presence
        text_rect = option.rect
        if item_icon:
            text_rect.adjust(item_icon.pixmap(option.iconSize).width() + 4, 0, 0, 0)

        #  - Draw the text using the painter's drawText() method with appropriate alignment
        painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter, item_text)

