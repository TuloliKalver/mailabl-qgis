
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
    PROPRETIE = "propertie"



class Languages:
    ESTONIA = "Eesti"
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
        Module.SUBMISSION: {Languages.ESTONIA: "Avaldused", Languages.LATVIA: "Iesniegumi"}
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
        Module.SUBMISSION: {Languages.ESTONIA: "Avalduse", Languages.LATVIA: "Iesniegums"}
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
        print(ModuleTranslation.module_name(Module.CONTRACT, language))  # Output: Lepingud
        print(ModuleTranslation.module_name(Module.CONTRACT, language, plural=False))  # Output: Leping