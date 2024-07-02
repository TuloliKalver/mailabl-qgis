import subprocess
import webbrowser  # For opening links in browser
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtGui import QIcon, QColor, QBrush
from PyQt5.QtCore import Qt
from ...KeelelisedMuutujad.modules import Modules
from ...config.settings import Filepaths, IconsByName
from ...config.iconHandler import iconHandler

class MyTreeHome:
    def fetch_module_data(module_name):
        # Sample data structure (replace with actual data source)
        module_data = {
            Modules.MODULE_CONTRACTS: [
                {"nr": 1, "name": "Sample Contract 1", "link": "https://kohevpesa.mailabl.io/tasks/42", "dok": r"C:/Users/Kalver/Desktop/GIS/Arendus"},
                {"nr": 2, "name": "Sample Contract 2", "link": "https://kohevpesa.mailabl.io/tasks/42", "dok": r"C:/Users/Kalver/Desktop/Konfidentsiaalsusleping Kalver Tammik.asice"},
            ],
            Modules.MODULE_PROJECTS: [
                {"nr": 1, "name": "Sample Project 1", "link": "https://kohevpesa.mailabl.io/tasks/42", "dok": r"C:/Users/Kalver/Desktop/Konfidentsiaalsusleping Kalver Tammik.pdf"},
                {"nr": 2, "name": "Sample Project 2", "link": "https://kohevpesa.mailabl.io/tasks/42", "dok": r"C:/Users/Kalver/Desktop/kalver (Töö) - Chrome.lnk"},
            ],
        }
        # Simulate data availability based on module_name
        return module_data.get(module_name, [])  # Return empty list if no data for the module


    def update_tree_with_modules(workspace, treeWidget):
        workspace.setCurrentIndex(6)

        treeWidget.clear()  # Clear existing items (optional)
        treeWidget.setHeaderLabel("Seotud tulemusi")
        treeWidget.setHeaderLabels(["Nr", "Nimetus", "Link_text", "", "Dok_text", ""])

        for module_name in (getattr(Modules, attr) for attr in dir(Modules)
                            if not attr.startswith("_") and not callable(getattr(Modules, attr))):
            child_data = MyTreeHome.fetch_module_data(module_name)
            if child_data:  # Only add module if data is returned
                root_item = QTreeWidgetItem(treeWidget)
                root_item.setText(0, module_name)


                for child in child_data:
                    child_item = QTreeWidgetItem(root_item)
                    child_item.setText(0, str(child["nr"]))
                    child_item.setText(1, child["name"])
                    child_item.setText(2, child["link"])  # Store the link in column 2
                    child_item.setText(4, child["dok"])

                      # Hide columns 2 and 4 after setting text
                    treeWidget.hideColumn(2)
                    treeWidget.hideColumn(4)
                    
                    # Set clickable icon for the link (replace with your icon logic)
                    
                    MyTreeHome.set_clickable_webIcon(child_item, 3)  # Column 2 for link
                    MyTreeHome.set_clickable_folderIcon(child_item, 5)

        # Connect the treeWidget's itemClicked signal to a handler
        treeWidget.itemClicked.connect(MyTreeHome.handle_icon_clicked_single)
        treeWidget.itemClicked.connect(MyTreeHome.handle_dok_clicked)
        treeWidget.setColumnWidth(3, 10)
        treeWidget.setColumnWidth(5, 10)
        treeWidget.setColumnWidth(1, 250)
        # Expand all items to make sure they are visible
        treeWidget.expandAll()

    def set_clickable_webIcon(tree_item, column):
        # Replace with your logic to get the icon path based on link type or preference
        icon_path = Filepaths.get_icon(IconsByName().Mailabl_icon_name)
        icon = QIcon(icon_path)

        # Set the icon and make the text empty (invisible)
        tree_item.setIcon(column, icon)
        tree_item.setText(column, "")  # Set empty text for the link column

        # Make the entire item clickable, not just the icon (optional)
        tree_item.setFlags(tree_item.flags() | Qt.ItemIsSelectable)
        


    def set_clickable_folderIcon(tree_item, column):
        dokLink = tree_item.text(4)
        icon_path = iconHandler.set_document_icon_based_on_item(dokLink)
        icon = QIcon(icon_path)

        tree_item.setIcon(column, icon)
        # Make the entire item clickable, not just the icon (optional)
        tree_item.setFlags(tree_item.flags() | Qt.ItemIsSelectable)

    def handle_icon_clicked_single(item, column):
        if column == 3:  # Check for link column
            link_url = item.text(2)  # Extract link URL from data (column 2)
            webbrowser.open(link_url)  # Open link in browser

    def handle_icon_clicked(item, column):
        if column in (3, 5):  # Check for both link columns (2 and 3)
            if column == 3:
                link_url = item.text(2)  # Extract link URL from column 2
            else:
                link_url = item.text(4)  # Extract link URL from column 3 (assuming column 3)
            webbrowser.open(link_url)  # Open link in browser

    def handle_dok_clicked(item, column):
        if column == 5:
            dok_path = item.text(4)
            print(f"dok_path: {dok_path}")
            subprocess.Popen(['explorer', dok_path.replace('/', '\\')], shell=True)



    