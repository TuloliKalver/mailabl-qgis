import subprocess
import webbrowser
import requests


from PyQt5.QtGui import QColor, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtCore import Qt
from ...Functions.tableViewAdjust import Colors
from ...KeelelisedMuutujad.modules import Modules
from ...config.settings import Filepaths, IconsByName
from ...config.iconHandler import iconHandler
from ...queries.python.query_tools import requestBuilder
from ...queries.python.DataLoading_classes import GraphQLQueryLoader, Graphql_properties
from ...queries.python.responses import handleResponse
from .query_cordinator import PropertiesConnectedElementsQueries
from ...config.settings import MailablWebModules, OpenLink

class MyTreeHomeView:
    header_number = 'Number'
    header_name = 'Nimetus'
    header_id = 'ID'
    header_file_path = "file_path_button"
    header_statuses = 'Staatus'

    @staticmethod
    def fetch_module_data(module_name, item):
        print(f"module name in query: {module_name} and item: {item}")
        query_loader = Graphql_properties()
        query = GraphQLQueryLoader().load_query_properties(query_loader.W_properties_number)
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
            data = handleResponse.response_properties_data_edges(response)
            return data

    @staticmethod
    def update_tree_with_modules(treeView, item):
        print(f"item: {item}")

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([MyTreeHomeView.header_number, MyTreeHomeView.header_name, MyTreeHomeView.header_id, "", MyTreeHomeView.header_file_path, "", MyTreeHomeView.header_statuses])

        child_data = {}
        for module_name in (getattr(Modules, attr) for attr in dir(Modules) if not attr.startswith("_") and not callable(getattr(Modules, attr))):
            something = PropertiesConnectedElementsQueries()
            module_data = something.fetch_module_data(module_name, item)
            if module_data:
                for data_list in module_data:
                    for item in data_list:
                        node_data = item.get('node')
                        if node_data:
                            typename = node_data['__typename']
                            if typename not in child_data:
                                child_data[typename] = []
                            child_data[typename].append(node_data)
        print(f"child_data: {child_data}")

        if child_data:
            for typename, items in child_data.items():
                root_item = QStandardItem(typename)
                for child in items:
                    child_item = QStandardItem()
                    child_item.setText(child["number"])
                    name_item = QStandardItem()
                    name_item.setText(child["name"])
                    id_item = QStandardItem()
                    id_item.setText(child["id"])
                    file_path_item = QStandardItem()
                    file_path_item.setText(child.get("dok", ""))
                    status_item = QStandardItem()
                    status_name = child["status"]['name']
                    status_color = child["status"]['color']
                    status_item.setText(status_name)
                    MyTreeHomeView.set_status_color(status_item, status_color)
                    # Create a custom delegate for coloring status items

                    root_item.appendRow([child_item, name_item, id_item, QStandardItem(), file_path_item, QStandardItem(), status_item])

                model.appendRow(root_item)
                treeView.setModel(model)

        delegate = StatusColorDelegate(treeView)
        treeView.setItemDelegate(delegate)

        treeView.expandAll()
        treeView.setColumnHidden(2, True)
        treeView.setColumnHidden(4, True)
        treeView.setColumnWidth(1, 250)
        treeView.setColumnWidth(3, 15)
        treeView.setColumnWidth(5, 15)
        treeView.setColumnWidth(1, 400)

        treeView.clicked.connect(MyTreeHomeView.open_in_web_browser)
        treeView.clicked.connect(MyTreeHomeView.handle_dok_clicked)

    @staticmethod
    def set_status_color(status_item, color_code):
        if color_code:
            try:                    
                rgb_color = Colors.hex_to_rgb(color_code)
                background_color = QColor(*rgb_color)
                foreground_color = QColor(Qt.black)  # Set foreground color to black
                status_item.setBackground(background_color)
                status_item.setForeground(foreground_color)
                status_item.setTextAlignment(Qt.AlignCenter)
            except Exception as e:
                print(f"Error in setting color: {e}")

    @staticmethod
    def open_in_web_browser(index):
        if index.column() == 3:
            item = index.model().itemFromIndex(index)
            module = item.data(Qt.UserRole)
            if module:
                module = module.lower() + 's'
            print(f"Module in column head: {module}")
            link_id = item.text(2)
            web_module = MailablWebModules().get_web_link(module)
            print(f"web_module: {web_module}")
            web_link = OpenLink.weblink_by_module(web_module)
            print(f"web_link: {web_link}")
            link = f"{web_link}{link_id}"
            response = requests.get(link, verify=False)
            webbrowser.open(response.url)

    @staticmethod
    def handle_dok_clicked(index):
        if index.column() == 5:
            item = index.model().itemFromIndex(index)
            dok_path = item.text(4)
            print(f"dok_path: {dok_path}")
            subprocess.Popen(['explorer', dok_path.replace('/', '\\')], shell=True)

# Note: Make sure to adapt any other functions that interact with the items to handle the new QTreeView's model-based system.

class StatusColorDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index = "7"):
        painter.save()

        # Call the base class paint method to draw the default item content
        self.drawBaseContent(painter, option, index)  # Added missing method call

        if index.column() == MyTreeHomeView.header_statuses.index(index):            # Get the status text and color
            status_text = index.data(Qt.DisplayRole)
            status_color_code = index.data(Qt.UserRole + 1)  # Assuming color is stored in UserRole + 1

            if status_color_code:
                try:
                    rgb_color = Colors.hex_to_rgb(status_color_code)
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
