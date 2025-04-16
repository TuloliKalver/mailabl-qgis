# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
#from .....config.tetstlogger import log_test_entry
from ...projects_pandas import ProjectModelBuilders
from .....config.settings import MailablWebModules
from .....KeelelisedMuutujad.messages import Headings, HoiatusTexts
from .....KeelelisedMuutujad.modules import Module
from .....utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder
from .....utils.ProgressHelper import ProgressDialogModern

pealkiri = Headings()

class Projects:
    @staticmethod
    #@log_test_entry("load projects by status")
    def load_projects_by_status(table, status_value, language="et"):
        
        progress = ProgressDialogModern(title="Katastri laadimine", value=0)
        progress.update(1, purpouse="Projektide laadimine", text1="Palun oota...")
        
        model = ProjectModelBuilders()._model_for_projects_by_statuses(None, status_value, language)
        if model == None:
            text = "probleem projektide laadimisel"
            heading = pealkiri.warningSimple
            print(f"{heading}, {text}")
            progress.close()
            return
        
        progress.update(50)
        if model is not None:
            module = Module.PROJECT
            ModuleTableBuilder.setup(table, model, module, language)
        else:
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")

        progress.update(98)
        progress.close()
    @staticmethod
    #@log_test_entry("laod projects by number")
    def load_projects_by_number(project_number, table, language="et"):
        progress = ProgressDialogModern(title="Katastri laadimine", value=0)
        progress.update(1, purpouse="Projektide laadimine", text1="Palun oota...")
        
        model = ProjectModelBuilders()._model_for_projects_search_results(None, project_number, language)
        progress.update(50)

        if model is not None:
            module = MailablWebModules.PROJECTS
            ModuleTableBuilder.setup(table, model, module, language)
        else:
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
        progress.update(98)
        progress.close()