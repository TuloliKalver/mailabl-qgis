
from ..queries.python.projects.ProjectTableGenerators.projects import Projects
from .Contracts.Contracts import ContractsMain
from .Easements.Easements import EasementssMain
from ..Functions.AsBuilt.ASBuilt import AsBuiltMain
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
            Module.EASEMENT: EasementssMain.load_easemenets_by_number,
            Module.ASBUILT: AsBuiltMain.load_asBuilt_by_query,
            Module.WORKS: AsBuiltMain.load_asBuilt_by_query
        }

    def universalSearch(self, module_name):
        # Get the corresponding line edit and table based on the module name
        line_edits = {
            Module.PROJECT: self.dialog.le_searchProjects,
            Module.CONTRACT: self.dialog.le_searchContracts,
            Module.EASEMENT: self.dialog.leSearcheasements,
            Module.ASBUILT: self.dialog.le_searchTeostus,
            Module.WORKS: self.dialog.leWorksSearch
        }

        tables = {
            Module.PROJECT: self.dialog.tblMailabl_projects,
            Module.CONTRACT: self.dialog.ContractView,
            Module.EASEMENT: self.dialog.tweasementView,
            Module.ASBUILT: self.dialog.tblAsBuilt,
            Module.WORKS: self.dialog.tblWorks
        }

        lineEdit = line_edits[module_name]
        table = tables[module_name]
        search_items = lineEdit.displayText()
        item = search_items.strip()

        if item == '':
            # Frame the label with a red border
            lineEdit.setStyleSheet("border: 1px solid #D32F2F;")
            # Display warning message
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(Headings().warningSimple, HoiatusTexts().otsing_puudu)
            return
        else:
            lineEdit.setStyleSheet("border: None")
            # Call the appropriate search function based on the module name
            self.search_functions[module_name](item, table)