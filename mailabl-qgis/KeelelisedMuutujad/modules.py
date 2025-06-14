
class Module:
    CONTRACT = "contract"
    PROJECT = "project"
    TASK = "task"
    COORDINATION = "coordination"
    LETTER = "letter"
    SPECIFICATION = "specification"
    EASEMENT = "easement"
    ORDINANCE = "ordinance"
    SUBMISSION = "submission"
    PROPERTIE = "propertie"
    USER = "me"
    TAGS = "tags"
    STATUSES = "statuses"
    ASBUILT = "task"
    WORKS = "works"

    all_modules = [CONTRACT, PROJECT, TASK, COORDINATION, LETTER,
                    SPECIFICATION, EASEMENT, ORDINANCE, SUBMISSION, ASBUILT]

class ModuleTriggerButtons:
    #TODO module needs development to better understand how user rights are managed
    @staticmethod
    def get_mapped_buttons(dialog):
        return {
            Module.CONTRACT: dialog.pbContracts,
            Module.PROJECT: dialog.pbProjects,
            Module.COORDINATION: dialog.pbCooperations,
            Module.EASEMENT: dialog.pbeasements,
            Module.WORKS: dialog.pbWorksMain
        }

    @staticmethod
    def apply_button_access_control(abilities: dict[str, str], dialog):

        print(f"abilities: {abilities}")
        allowed_modules = set()
        subject_to_actions = {}

        # Collect all actions for each subject
        for role in abilities:
            subjects = role["subject"]
            action = role.get("action")

            if not isinstance(subjects, list):
                subjects = [subjects]

            for subject in subjects:
                subject_lower = subject.lower()
                if subject_lower not in subject_to_actions:
                    subject_to_actions[subject_lower] = set()
                subject_to_actions[subject_lower].add(action)

        # Filter subjects that have at least "read" permission
        for subject, actions in subject_to_actions.items():
            if "read" in actions:
                allowed_modules.add(subject)

        print(f"✅ Allowed modules (with read access): {allowed_modules}")

        for module, button in ModuleTriggerButtons.get_mapped_buttons(dialog).items():
            print(f"{module}: {button}")
            if module not in allowed_roles:
                button.setEnabled(False)
                button.setToolTip("Ligipääs puudub")
            else:
                button.setEnabled(True)
                button.setToolTip("")

class Languages:
    ESTONIA = "et"
    LATVIA = "Latviesu"

class ModuleTranslation:
    translations_plural = {
        Module.CONTRACT: {Languages.ESTONIA: "Lepingud", Languages.LATVIA: "Līgumi"},
        Module.PROJECT: {Languages.ESTONIA: "Projektid", Languages.LATVIA: "Projekti"},
        Module.TASK: {Languages.ESTONIA: "Ülesanded", Languages.LATVIA: "Uzdevumi"},
        Module.COORDINATION: {Languages.ESTONIA: "Kooskõlastused", Languages.LATVIA: "Koordinācija"},
        Module.LETTER: {Languages.ESTONIA: "Kirjad", Languages.LATVIA: "Vēstules"},
        Module.SPECIFICATION: {Languages.ESTONIA: "Tingimused", Languages.LATVIA: "Specifikācijas"},
        Module.EASEMENT: {Languages.ESTONIA: "Servituudid", Languages.LATVIA: "Apgrūtinājumi"},
        Module.ORDINANCE: {Languages.ESTONIA: "Käskkirjad", Languages.LATVIA: "Rīkojumi"},
        Module.SUBMISSION: {Languages.ESTONIA: "Avaldused", Languages.LATVIA: "Iesniegumi"},
        Module.ASBUILT: {Languages.ESTONIA: "Teostusjoonised", Languages.LATVIA: "Asbuilt"},
        "teostusjoonised": {Languages.ESTONIA: "Teostusjoonised", Languages.LATVIA: "Asbuilt"},
        "tegevused": {Languages.ESTONIA: "Tegevused", Languages.LATVIA: "Darbi"}
    }

    translations_singular = {
        Module.CONTRACT: {Languages.ESTONIA: "Lepingu", Languages.LATVIA: "Līgums"},
        Module.PROJECT: {Languages.ESTONIA: "Projekti", Languages.LATVIA: "Projekts"},
        Module.TASK: {Languages.ESTONIA: "Ülesande", Languages.LATVIA: "Uzdevums"},
        Module.COORDINATION: {Languages.ESTONIA: "Kooskõlastuse", Languages.LATVIA: "Koordinācija"},
        Module.LETTER: {Languages.ESTONIA: "Kirja", Languages.LATVIA: "Vēstule"},
        Module.SPECIFICATION: {Languages.ESTONIA: "Tingimuse", Languages.LATVIA: "Specifikācija"},
        Module.EASEMENT: {Languages.ESTONIA: "Servituudi", Languages.LATVIA: "Apgrūtinājums"},
        Module.ORDINANCE: {Languages.ESTONIA: "Käskkirja", Languages.LATVIA: "Rīkojums"},
        Module.SUBMISSION: {Languages.ESTONIA: "Avalduse", Languages.LATVIA: "Iesniegums"},
        Module.ASBUILT: {Languages.ESTONIA: "Teostusjoonis", Languages.LATVIA: "Asbuilt"},
        "teostusjoonised": {Languages.ESTONIA: "Teostusjoonis", Languages.LATVIA: "Asbuilt"},
        "tegevused": {Languages.ESTONIA: "Tegevus", Languages.LATVIA: "Darbi"}
    }

    @staticmethod
    def module_name(module, language, plural=True):
        #print("module:", module)
        if plural:
            return ModuleTranslation.translations_plural.get(module, {}).get(language, "Translation not available")
        else:
            return ModuleTranslation.translations_singular.get(module, {}).get(language, "Translation not available")


    @staticmethod
    def print_examples():        
        language = Languages.ESTONIA
        print(ModuleTranslation.module_name(Module.CONTRACT, language))  # Output: Lepingud
        print(ModuleTranslation.module_name(Module.CONTRACT, language, plural=False))  # Output: Leping