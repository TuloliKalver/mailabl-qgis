# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module

from typing import List
from PyQt5.QtWidgets import QMessageBox
from ...MapTools.selector import visibleSelector
from ...projects_pandas import ProjectModelBuilders
from .....config.settings import SettingsDataSaveAndLoad, MailablWebModules
from .....KeelelisedMuutujad.messages import Headings, HoiatusTexts
from .....utils.TableUtilys.MainModuleTaibleBiulder import ModuleTableBuilder


pealkiri = Headings()

class Projects:
    #@staticmethod
    def load_projects_by_status(table, status_value, language = "et"):
        
        model = ProjectModelBuilders()._model_for_projects_by_statuses(None,status_value, language)
        if model is not None:
            module = MailablWebModules.PROJECTS
            ModuleTableBuilder.setup(table, model, module, language)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")


    @staticmethod
    def load_Mailabl_projects_list_with_zoomed_map_elements(table, language = "et"):
        layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        selected_features = visibleSelector.get_visible_features(layer_name)

        if len(selected_features) >= 500:
            text = "Ala on projektide laadimiseks liiga suur\nZoomi lähemale"
            heading = pealkiri.warningSimple
            QMessageBox.warning(None, heading, text)
            return

        model = ProjectModelBuilders()._model_for_projects_zoomed_map_properties(None,selected_features, language)

        if model is not None:
            module = MailablWebModules.PROJECTS
            ModuleTableBuilder.setup(table, model, module, language)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")

    @staticmethod
    def load_projects_by_number(project_number, table, language = "et"):

        model = ProjectModelBuilders()._model_for_projects_search_results(None,project_number, language)

        if model is not None:
            module = MailablWebModules.PROJECTS
            ModuleTableBuilder.setup(table, model, module, language)
        else:            
            text = HoiatusTexts().ostingu_tulemused_puuduvad
            heading = Headings().warningSimple
            print(f"{heading}, {text}")
