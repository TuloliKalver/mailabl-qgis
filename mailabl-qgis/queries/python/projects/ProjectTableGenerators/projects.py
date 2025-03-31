# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
#from .....config.tetstlogger import log_test_entry
from ...projects_pandas import ProjectModelBuilders
from .....config.settings import MailablWebModules
from .....KeelelisedMuutujad.messages import Headings, HoiatusTexts
from .....KeelelisedMuutujad.modules import Module
from .....utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder


pealkiri = Headings()

class Projects:
    @staticmethod
    #@log_test_entry("load projects by status")
    def load_projects_by_status(table, status_value, language="et"):
        model = ProjectModelBuilders()._model_for_projects_by_statuses(None, status_value, language)
        if model is not None:
            module = Module.PROJECT
            ModuleTableBuilder.setup(table, model, module, language)
        else:
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")

    @staticmethod
    #@log_test_entry("laod projects by number")
    def load_projects_by_number(project_number, table, language="et"):
        model = ProjectModelBuilders()._model_for_projects_search_results(None, project_number, language)

        if model is not None:
            module = MailablWebModules.PROJECTS
            ModuleTableBuilder.setup(table, model, module, language)
        else:
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
