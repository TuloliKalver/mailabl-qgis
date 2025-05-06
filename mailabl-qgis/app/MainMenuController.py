from PyQt5.QtWidgets import QLabel

from enum import Enum

class ModuleKey(str, Enum):
    ID = "idforDisplay"
    WIDGET = "hWidget"
    TITLE = "title"
    LABELS = "settingLabels"
    CHECKBOXES = "settingsCheckboxes"
    SETTINGS_BUTTON = "settingsDialogButton"
    VISIBLE = "visible"
    STARTPAGE = "startPage"
    USERS = "users"

    


class MenuModules():
    EASEMENTS = 0
    CADASTRALMOVES = 1
    CONTRACTS = 2
    TEOSTUS = 3
    SETTINGS = 4
    HOMEPAGE = 5
    PROPERTIES = 6
    PROJECTS = 7
    ARCHIVE_HELP_PROPERTIES = 8
    PROPERTIES_OPERATIONS = 9
    USERS = 10
    COOPERATION = 11


class SetupController:
    def __init__(self, dialog):
        self.dialog = dialog
        self.setup_modules = {
            MenuModules.TEOSTUS: {
                ModuleKey.ID: MenuModules.TEOSTUS,
                ModuleKey.WIDGET: dialog.qwSU_Teostus,
                ModuleKey.TITLE: "Teostus",
                ModuleKey.LABELS: [
                    dialog.lblTeostusMapLayerValue,
                    dialog.lblTeostusPreferredStatusesValue,
                    dialog.lblTesotusActionsValue,
                    dialog.lblTeostusFolderNameValue 
                ],
                ModuleKey.CHECKBOXES: [dialog.cbPartOfProject],
                ModuleKey.SETTINGS_BUTTON: dialog.pbTeostusSettings,
                ModuleKey.VISIBLE: True,
            },
            MenuModules.CONTRACTS: {
                ModuleKey.ID: MenuModules.CONTRACTS,
                ModuleKey.WIDGET: dialog.qwSU_Mailabl_Contracts_Main,
                ModuleKey.TITLE: "Lepingud",
                ModuleKey.LABELS: [
                    dialog.lblPreferredContractStatusValue,
                    dialog.lblPreferredContractsTypesValue
                ],
                ModuleKey.CHECKBOXES: [],
                ModuleKey.SETTINGS_BUTTON: None,
                ModuleKey.VISIBLE: True,
            },
            MenuModules.EASEMENTS: {
                ModuleKey.ID: MenuModules.EASEMENTS,
                ModuleKey.WIDGET: dialog.qwSU_Mailabl_Easements_Main,
                ModuleKey.TITLE: "Servituudid",
                ModuleKey.LABELS: [
                    dialog.lblPreferredEasementsStatusValue,
                    dialog.lblPreferredEasementsTypesValue,
                    dialog.lblWaterPipesValue,
                    dialog.lblSewerPipesValue,
                    dialog.lblDrainagePipesValue
                ],
                ModuleKey.CHECKBOXES: [],
                ModuleKey.SETTINGS_BUTTON: None,
                ModuleKey.VISIBLE: True,
            },
            MenuModules.PROJECTS: {
                ModuleKey.ID: MenuModules.PROJECTS,
                ModuleKey.WIDGET: dialog.qwSU_Mailabl_Projects,
                ModuleKey.TITLE: "Projektid",
                ModuleKey.LABELS: [
                    dialog.lblLayerProjectsValue,
                    dialog.lblLayerProjectsBaseValue,
                    dialog.lblPreferredProjectStatusValue,
                    dialog.lblProjectsFolderValue,
                    dialog.lblProjectsTargetFolderValue,
                    dialog.lblPreferredFolderNameValue,
                    dialog.lblPhotosValue
                    ],
                ModuleKey.CHECKBOXES: [],
                ModuleKey.SETTINGS_BUTTON: None,
                ModuleKey.VISIBLE: True,
            },
            MenuModules.PROPERTIES: {
                ModuleKey.ID: MenuModules.PROPERTIES,
                ModuleKey.WIDGET: dialog.qwSU_Layers,
                ModuleKey.TITLE: "Kinnistud",
                ModuleKey.LABELS: [
                    dialog.lblSHPLayerValue,
                    dialog.lblMainLayerValue,
                    dialog.lblMainTargetLayerValue
                ],
                ModuleKey.CHECKBOXES: [],
                ModuleKey.SETTINGS_BUTTON: None,
                ModuleKey.VISIBLE: True,

            },
            MenuModules.USERS: {
                ModuleKey.ID: MenuModules.USERS, # No specific ID needed here as it's a special case
                ModuleKey.WIDGET: dialog.qwSU_Mailabl_Users,
                ModuleKey.TITLE: "Kasutajad",
                ModuleKey.LABELS: [
                    dialog.lblNUserSurenameValue,
                    dialog.lbNuserNameValue,
                    dialog.lblUserRolesValue,
                    dialog.lblSPreferedHomeValue
                ],
                ModuleKey.CHECKBOXES: [],
                ModuleKey.SETTINGS_BUTTON: None,
                ModuleKey.VISIBLE: True
            },
            MenuModules.ARCHIVE_HELP_PROPERTIES: {
                ModuleKey.ID: MenuModules.ARCHIVE_HELP_PROPERTIES,
                ModuleKey.WIDGET: None,
                ModuleKey.TITLE: "Arhiivitavate kinnistuste seaded",
                ModuleKey.LABELS: [],
                ModuleKey.CHECKBOXES: [],
                ModuleKey.SETTINGS_BUTTON: None,
                ModuleKey.VISIBLE: True
            },
            MenuModules.COOPERATION: {
                ModuleKey.ID: MenuModules.COOPERATION,
                ModuleKey.WIDGET: dialog.gwSU_Mailabl_Coordinations,
                ModuleKey.TITLE: "Kooskõlastused",
                ModuleKey.LABELS: [
                    dialog.lblCoordinationsActionsValue,
                    dialog.lblCoordinationsPreferredStatusesValue,
                    dialog.lblCoordinationsMapLayerValue,
                ],
                ModuleKey.CHECKBOXES: [],
                ModuleKey.SETTINGS_BUTTON: None,
                ModuleKey.VISIBLE: True
            },

        }

    def has_undefined_labels(self, module_key: str):
        module = self.setup_modules.get(module_key)
        if not module or ModuleKey.WIDGET not in module:
            print(f"❌ Module '{module_key}' not found or misconfigured.")
            return True, []  # 🔁 Always return a (bool, list) tuple

        widget = module[ModuleKey.WIDGET]
        if widget is None:
            print(f"⚠️ No widget defined for module '{module_key}'.")
            return True, []

        all_labels = widget.findChildren(QLabel)
        no_value_labels = [label for label in all_labels if label.text().strip() == "Määramata"]

        return len(no_value_labels) == 0, no_value_labels
    def check_all_modules(self):
        all_valid = True
        #print("🔍 Modules registered in SetupController:")

        for key, module in self.setup_modules.items():
            #print(f" - {key} ({type(key)}): {module.get(ModuleKey.TITLE)}")

            widget = module.get(ModuleKey.WIDGET)
            if widget is None:
                print(f"⚠️ Skipping module '{key}' due to missing widget.")
                continue

            all_labels = widget.findChildren(QLabel)
            invalid_labels = []

            for label in all_labels:
                text = label.text().strip()
                name = label.objectName()
                if text == "Määramata":
                    invalid_labels.append(label)
                    # 🟥 Soft translucent warning red (matching green vibe)
                    label.setStyleSheet("background-color: rgba(255, 90, 90, 0.25); "
                    "border: 1px solid rgba(9, 144, 143, 0.4);" \
                    "color: #c5c5d2;" \
                    "transition: all 150ms ease-in-out;" \
                    "border-radius: 3px;"
                    "padding: 2px;")

                else:
                    if name.endswith("Value"):
                        label.setStyleSheet(
                            "background-color: rgba(9, 144, 143, 0.15);"
                            "border: 1px solid rgba(9, 144, 143, 0.4);"
                            "color: #c5c5d2;"
                            "transition: all 150ms ease-in-out;"
                            "border-radius: 3px;"
                            "padding: 2px;"
                        )

            if invalid_labels:
                #print(f"⚠️ {module.get(ModuleKey.TITLE, key)} has {len(invalid_labels)} undefined labels.")
                all_valid = False

        return all_valid
