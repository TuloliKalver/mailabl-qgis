
class Modules:
    MODULE_CONTRACTS = "contracts"
    MODULE_PROJECTS = "projects"
    MODULE_TASKS = "tasks"
    MODULE_COORDINATION = "coordinations"
    MODULE_LETTER = "letters"
    MODULE_SPECIFICATIONS = "specifications"
    MODULE_EASEMENTS = "easements"
    MODULE_ORDINANCES = "ordinances"
    MODULE_SUBMISSIONS = "submissions"

class Languages:
    ESTONIA = "Eesti"
    LATVIA = "Latviesu"

class ModuleTranslation:
    translations_plural = {
        Modules.MODULE_CONTRACTS: {Languages.ESTONIA: "Lepingud", Languages.LATVIA: "Līgumi"},
        Modules.MODULE_PROJECTS: {Languages.ESTONIA: "Projektid", Languages.LATVIA: "Projekti"},
        Modules.MODULE_TASKS: {Languages.ESTONIA: "Ülesanded", Languages.LATVIA: "Uzdevumi"},
        Modules.MODULE_COORDINATION: {Languages.ESTONIA: "Koordineerimised", Languages.LATVIA: "Koordinācija"},
        Modules.MODULE_LETTER: {Languages.ESTONIA: "Kirjad", Languages.LATVIA: "Vēstules"},
        Modules.MODULE_SPECIFICATIONS: {Languages.ESTONIA: "Spetsifikatsioonid", Languages.LATVIA: "Specifikācijas"},
        Modules.MODULE_EASEMENTS: {Languages.ESTONIA: "Teenusõigused", Languages.LATVIA: "Apgrūtinājumi"},
        Modules.MODULE_ORDINANCES: {Languages.ESTONIA: "Määrused", Languages.LATVIA: "Rīkojumi"},
        Modules.MODULE_SUBMISSIONS: {Languages.ESTONIA: "Esitused", Languages.LATVIA: "Iesniegumi"}
    }

    translations_singular = {
        Modules.MODULE_CONTRACTS: {Languages.ESTONIA: "Lepingu", Languages.LATVIA: "Līgums"},
        Modules.MODULE_PROJECTS: {Languages.ESTONIA: "Projekti", Languages.LATVIA: "Projekts"},
        Modules.MODULE_TASKS: {Languages.ESTONIA: "Ülesande", Languages.LATVIA: "Uzdevums"},
        Modules.MODULE_COORDINATION: {Languages.ESTONIA: "Koordineerimine", Languages.LATVIA: "Koordinācija"},
        Modules.MODULE_LETTER: {Languages.ESTONIA: "Kirja", Languages.LATVIA: "Vēstule"},
        Modules.MODULE_SPECIFICATIONS: {Languages.ESTONIA: "Tingimuse", Languages.LATVIA: "Specifikācija"},
        Modules.MODULE_EASEMENTS: {Languages.ESTONIA: "Servituudi", Languages.LATVIA: "Apgrūtinājums"},
        Modules.MODULE_ORDINANCES: {Languages.ESTONIA: "Käskkirja", Languages.LATVIA: "Rīkojums"},
        Modules.MODULE_SUBMISSIONS: {Languages.ESTONIA: "Esitus", Languages.LATVIA: "Iesniegums"}
    }

    @staticmethod
    def module_name(module, language, plural=True):
        if plural:
            return ModuleTranslation.translations_plural.get(module, {}).get(language, "Translation not available")
        else:
            return ModuleTranslation.translations_singular.get(module, {}).get(language, "Translation not available")


    @staticmethod
    def print_examples():        
        language = Languages.ESTONIA
        print(ModuleTranslation.module_name(Modules.MODULE_CONTRACTS, language))  # Output: Lepingud
        print(ModuleTranslation.module_name(Modules.MODULE_CONTRACTS, language, plural=False))  # Output: Leping