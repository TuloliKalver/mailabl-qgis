
from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from .Contracts.Contracts import ContractsMain
from .Easements.Easements import EasementssMain
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts
from ..KeelelisedMuutujad.modules import Module
from ..utils.messagesHelper import ModernMessageDialog



class ModularSearchEngine:
    def __init__(self, dialog):
        self.dialog =dialog

        # Define the mapping between module names and their respective search functions
        self.search_functions = {
            Module.PROJECT: Projects.load_projects_by_number,
            Module.CONTRACT: ContractsMain.load_contracts_by_query,
            Module.EASEMENT: EasementssMain.load_easemenets_by_number
        }

    def universalSearch(self, module_name):
        # Get the corresponding line edit and table based on the module name
        line_edits = {
            Module.PROJECT: self.dialog.le_searchProjects,
            Module.CONTRACT: self.dialog.le_searchContracts,
            Module.EASEMENT: self.dialog.leSearcheasements
        }

        tables = {
            Module.PROJECT: self.dialog.tblMailabl_projects,
            Module.CONTRACT: self.dialog.ContractView,
            Module.EASEMENT: self.dialog.tweasementView
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