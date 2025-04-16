from PyQt5.QtWidgets import QLabel




class MenuModules():
    EASEMENTS = 0
    CADASTRALMOVES = 1
    CONTRACTS = 2
    TEOSTUS = 3
    SETTINGS = 4
    HOMEPAGE = 5
    PROPERTIES = 6
    PROJECTS = 7
    REMOVEPROPERTIES = 8
    PROPERTIES_OPERATIONS = 9

    def swWorkSpace(self, index):
        # This is a placeholder method to demonstrate how you might use the MyClassWithIndexes().
        print(f"Switching to workspace index: {index}")
        # Implement your actual workspace switching logic here


class SetupController:
    def __init__(self, dialog):
        self.dialog = dialog

        self.setup_modules = {
            MenuModules.TEOSTUS: dialog.qwSU_Teostus,
            MenuModules.CONTRACTS: dialog.qwSU_Mailabl_Contracts_Main,
            MenuModules.EASEMENTS: dialog.qwSU_Mailabl_Easements_Main,
            MenuModules.PROJECTS: dialog.qwSU_Mailabl_Projects,
            MenuModules.PROPERTIES: dialog.qwSU_Layers,
            "users": dialog.qwSU_Mailabl_Users
        }

    def has_undefined_labels(self, module_key: str) -> bool:
        print(f"Checking module: {module_key}")
        module_widget = self.setup_modules.get(module_key)
        print(f"Module widget: {module_widget}")
        if not module_widget:
            print(f"❌ Module '{module_key}' not found.")
            return False

        labels = module_widget.findChildren(QLabel)
        print(f"Found {len(labels)} labels in module.")
        for label in labels:
            if label.text().strip() == "Määramata":
                print(f"⚠️ Found undefined value in label: {label.objectName()}")
                return True

        return False