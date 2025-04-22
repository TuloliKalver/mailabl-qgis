from ..app.workspace_handler import WorkSpaceHandler
from ..app.MainMenuController import MenuModules

class MainMenuControlls:
    def __init__(self, dialog):
        self.dialog = dialog
        self.pbHome = dialog.pbHome
        self.pbProjects = dialog.pbProjects
        self.pbContracts = dialog.pbContracts
        self.pbeasements = dialog.pbeasements
        self.pbMapThemes = dialog.pbMapThemes
        self.pbAddDrawings = dialog.pbAddDrawings

        # Keep track of last clicked button
        self.active_button = None

        # Map buttons to actions
        self.MenuButtons = {
            self.pbHome: lambda: WorkSpaceHandler.swWorkSpace_Home(self.dialog),
            self.pbProjects: lambda: WorkSpaceHandler.swWorkspace_Projects(self.dialog),
            self.pbContracts: lambda: WorkSpaceHandler.swWorkSpace_Contracts(self.dialog),
            self.pbeasements: lambda: WorkSpaceHandler.swWorkSpace_Easements(self.dialog),
            self.pbMapThemes: lambda: WorkSpaceHandler.swWorkSpace_MapThemes_FrontPage(self.dialog),
            self.pbAddDrawings: lambda: WorkSpaceHandler.swWorkSpace_Controller(self.dialog, module=MenuModules.TEOSTUS)
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
