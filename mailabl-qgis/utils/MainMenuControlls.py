from ..app.workspace_handler import WorkSpaceHandler
from ..app.MainMenuController import MenuModules
from ..KeelelisedMuutujad.modules import Module
class MainMenuControlls:
    def __init__(self, dialog):
        self.dialog = dialog
        self.pbHome = dialog.pbHome
        self.pbProjects = dialog.pbProjects
        self.pbContracts = dialog.pbContracts
        self.pbeasements = dialog.pbeasements
        self.pbMapThemes = dialog.pbMapThemes
        self.pbAddDrawings = dialog.pbAddDrawings
        self.pbArchiveHelper = dialog.pbArchiveHelper
        self.pbCooperations = dialog.pbCooperations

        # Keep track of last clicked button
        self.active_button = None

        # Map buttons to actions
        self.MenuButtons = {
            self.pbHome: lambda: WorkSpaceHandler.swWorkSpace_Properties(self.dialog),
            self.pbProjects: lambda: WorkSpaceHandler.swWorkspace_Projects(self.dialog),
            self.pbContracts: lambda: WorkSpaceHandler.swWorkSpace_Contracts(self.dialog),
            self.pbeasements: lambda: WorkSpaceHandler.swWorkSpace_Easements(self.dialog),
            self.pbMapThemes: lambda: WorkSpaceHandler.swWorkSpace_MapThemes_FrontPage(self.dialog),
            self.pbAddDrawings: lambda: WorkSpaceHandler.swWorkSpace_Controller(self.dialog, menu_module=MenuModules.TEOSTUS, module=Module.ASBUILT),
            self.pbCooperations: lambda: WorkSpaceHandler.swWorkSpace_Coordinations(self.dialog,menu_module=MenuModules.COORDINATIONS, module=Module.COORDINATION),
            self.pbArchiveHelper: lambda: WorkSpaceHandler.swWorkspace_arhive_helper(self.dialog,MenuModules.ARCHIVE_HELP_PROPERTIES)
        }

        # Connect each button to a wrapper that handles activation
        for button, handler in self.MenuButtons.items():
            button.clicked.connect(lambda checked, b=button, h=handler: self._activate_menu_button(b, h))

    def _activate_menu_button(self, button, handler):
        # Re-enable previously active button
        if self.active_button and self.active_button != button:
            self.active_button.setEnabled(True)

        # Disable current one
        button.setEnabled(False)
        self.active_button = button

        # Call the handler
        handler()
