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

    def has_undefined_labels(self, module_key: str):
        #print(f"Checking module: {module_key}")
        module_widget = self.setup_modules.get(module_key)
        #print(f"Module widget: {module_widget}")
        if not module_widget:
            print(f"❌ Module '{module_key}' not found.")
            return True, []  # Treat as "valid" so it doesn't block others

        no_value_labels = []
        labels = module_widget.findChildren(QLabel)
        #print(f"Found {len(labels)} labels in module.")
        for label in labels:
            if label.text().strip() == "Määramata":
                no_value_labels.append(label)
                #print(f"⚠️ Found undefined value in label: {label.objectName()}")

        return len(no_value_labels) == 0, no_value_labels  # ✅ True if nothing is wrong

    def check_all_modules(self):
        all_valid = True
        undefined_labels_list = []

        for key in self.setup_modules.keys():
            valid, undefined_labels = self.has_undefined_labels(key)
            all_valid &= valid  # Now this works as expected
            undefined_labels_list.extend(undefined_labels)

        for label in undefined_labels_list:
            print(type(label))
            label.setStyleSheet("background-color: red;")

        return all_valid  # If needed