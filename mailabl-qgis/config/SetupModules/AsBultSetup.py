
from..confWidgets.AsBuitSettings import Ui_ConsturctionDrawings, TesotusChace
from...app.MainMenuController import ModuleKey, SetupController

class SetupASBuilt:

    def __init__(self, parent):
        self.dialog = parent  # Make sure this is a QWidget-based parent!
    
    def load_settings_widget(self):
        res = Ui_ConsturctionDrawings.ConstructionDrawingsSetup(parent=self.dialog)
        
        if not res:
            return  # User canceled

        else:

            self.dialog.lblTeostusMapLayerValue.setText(TesotusChace.TeostusLayer)
            self.dialog.lblTeostusPreferredStatusesValue.setText(TesotusChace.TeostusStatus)
            self.dialog.lblTesotusActionsValue.setText(TesotusChace.TeostusTypes)
            self.dialog.lblTeostusFolderNameValue.setText(TesotusChace.locatioNameValue)
            
            self.dialog.cbPartOfProject.setEnabled(True)
            self.dialog.cbPartOfProject.setChecked(TesotusChace.checkBox)
            self.dialog.cbPartOfProject.setEnabled(False)

            loader = SetupController(self.dialog)
            loader.check_all_modules()