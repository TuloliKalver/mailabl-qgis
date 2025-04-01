
from ..Functions.item_selector_tools import properties_selectors
from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from .Contracts.Contracts import ContractsMain
from .Easements.Easements import EasementssMain
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..KeelelisedMuutujad.modules import Module
from ..utils.messagesHelper import ModernMessageDialog

class searchGeneral:
    @staticmethod
    def search_cadastral_items_by_values(self):
        layer_type = "import"
        self.tabWidget_Propertie_list.setCurrentIndex(0)
        self.cbChooseAllAdd_properties.setChecked(False)
        self.cbChooseAllAdd__street_properties.setChecked(False)
        search_items = self.leSearch_Add.displayText()
        items_list = [item.strip() for item in search_items.split(',')]
        items_str = ', '.join('"{}"'.format(item) for item in items_list)
        properties_selectors.show_connected_properties_on_map(items_str, layer_type)


class ModularSearchEngine:
    def __init__(self):
        # Define the mapping between module names and their respective search functions
        self.search_functions = {
            Module.PROJECT: Projects.load_projects_by_number,
            Module.CONTRACT: ContractsMain.load_contracts_by_query,
            Module.EASEMENT: EasementssMain.load_easemenets_by_number
        }

    def universalSearch(self,instance, module_name):
        # Get the corresponding line edit and table based on the module name
        line_edits = {
            Module.PROJECT: instance.le_searchProjects,
            Module.CONTRACT: instance.le_searchContracts,
            Module.EASEMENT: instance.leSearcheasements
        }

        tables = {
            Module.PROJECT: instance.tblMailabl_projects,
            Module.CONTRACT: instance.ContractView,
            Module.EASEMENT: instance.tweasementView
        }

        lineEdit = line_edits[module_name]
        table = tables[module_name]
        search_items = lineEdit.displayText()
        item = search_items.strip()

        if item == '':
            # Frame the label with a red border
            lineEdit.setStyleSheet("border: 1px solid #D32F2F;")
            # Display warning message
            ModernMessageDialog.Info_messages_modern(Headings().warningSimple, HoiatusTexts().otsing_puudu)
            return
        else:
            lineEdit.setStyleSheet("border: None")
            # Call the appropriate search function based on the module name
            self.search_functions[module_name](item, table)