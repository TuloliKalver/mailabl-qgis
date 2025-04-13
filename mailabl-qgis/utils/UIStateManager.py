# UIStateManager.py

from qgis.utils import iface
from qgis.core import QgsProject
from PyQt5.QtWidgets import QListView, QTableView, QTableWidget, QCheckBox

from .WidgetHelpers import WidgetAndWievHelpers, ListSelectionHandler
from ..config.settings import SettingsDataSaveAndLoad, StoredLayers
from ..Common.app_state import PropertiesProcessStage, FlowStages
from ..Common.ChaceHelpers import CacheUpdater
from ..utils.ProgressHelper import ProgressDialogModern
from ..utils.LayerHelpers import LayerFilterSetters
from ..app.workspace_handler import CenterMainSliderIndexes, WorkSpaceHandler
from ..app.ui_controllers import WidgetAnimator
from ..widgets.decisionUIs.DecisionMaker import DecisionDialogHelper


class UIStateManager:
    def __init__(self, dialog):
        self.dialog = dialog

        self.check_boxes = [dialog.chkSelectAllSettlements, dialog.chkToggleRoadSelection]
        self.list_views = [dialog.lvCounty, dialog.lvState, dialog.lvSettlement]
        self.frames = [dialog.FrMunicipality, dialog.FrState, dialog.FRCounty,
                       dialog.frResultViewer, dialog.frControllButtons]
        self.table = [dialog.tvSelectedMapItems]

        self.main_frame_buttons = [dialog.pbAddElements, dialog.btnRemoveItems]
        self.action_buttons = [dialog.pbAddElements, dialog.btnRemoveItems,
                               dialog.pbConfirmAction, dialog.pbCancelAction]

        self.slider_ws = dialog.swWorkSpace
        self.lbl_action = dialog.lblPropertieOperations
        self.lbl = dialog.lblActionName
        self.main_buttons = [dialog.pbHome, dialog.pbProjects, dialog.pbContracts, 
                             dialog.pbeasements, dialog.btnMapActions,
                             dialog.pbMainMenu,dialog.pbSettings ]

        self.list_widgets_with_signals = {
            dialog.lvCounty: self.get_connected_signal,
            dialog.lvState: self.get_connected_signal,
            dialog.lvSettlement: self.get_connected_signal
        }

    def connect_list_signals(self):
        for widget, func in self.list_widgets_with_signals.items():
            widget.itemSelectionChanged.connect(func)

    def disconnect_list_signals(self):
        for widget, func in self.list_widgets_with_signals.items():
            try:
                widget.itemSelectionChanged.disconnect(func)
            except TypeError:
                pass

    def get_connected_signal(self):
        for widget in self.list_views:
            widget.setEnabled(False)
        element = self.dialog.sender()
        CacheUpdater.update_slected_items_cache(element)
        self.flow_and_ui_controls()
        for widget in self.list_views:
            widget.setEnabled(True)

    def exit_properties_process_flows(self):
        shp_layer_name = SettingsDataSaveAndLoad().load_SHP_inputLayer_name()
        choice = DecisionDialogHelper.ask_user(
            title="Mõtte koht...",
            message=f"Kas soovid {shp_layer_name} nimelise \n alles jätta või eemaldada?",
            parent=self.dialog
        )

        if choice is False:
            print("cancelled whole thing")
            return

        if choice is None:
            print(f"user pressed cancel")
            return  # ❌ User closed dialog — cancel exit entirely

        if choice is True:  # ✅ Only delete if explicitly confirmed
            layer_shp = QgsProject.instance().mapLayersByName(shp_layer_name)
            if layer_shp:
                layer_s = layer_shp[0]
                if layer_s and layer_s.isValid():
                    QgsProject.instance().removeMapLayer(layer_s)

        # Reset state regardless of choice
        WorkSpaceHandler.swWorkSpace_Properties(self.dialog)
        for button in self.main_buttons:
            button.setEnabled(True)
        WidgetAnimator.toggle_Frame_height_for_settings(self.dialog, self.dialog.pbSettings_SliderFrame)

        # Refresh layer
        layer_name = StoredLayers.users_properties_layer_name()
        LayerFilterSetters._reset_layer(layer_name)
        layers = QgsProject.instance().mapLayersByName(layer_name)
        if layers:
            iface.setActiveLayer(layers[0])


    def start_properti_flow_main(self):
        self.slider_ws.setCurrentIndex(CenterMainSliderIndexes.PROPERTIES_OPERATIONS)
        self.lbl_action.setText("Andmete laadimine")

        layer_name = SettingsDataSaveAndLoad().load_SHP_inputLayer_name()
        layer = QgsProject.instance().mapLayersByName(layer_name)

        lv_county = self.dialog.lvCounty
        lv_state = self.dialog.lvState
        lv_municipality = self.dialog.lvSettlement
        cb_municipality = self.dialog.chkSelectAllSettlements
        cb_roads = self.dialog.chkToggleRoadSelection

        all_checkboxes = self.check_boxes + [cb_municipality, cb_roads]
        all_tables = self.table
        all_controls = all_checkboxes + all_tables

        for button in self.main_buttons:
            button.setEnabled(False)

        if not layer:
            self.dialog.frMaaAmetControlls.setVisible(True)
            self.dialog.frPropertiFlowHolder.setVisible(False)
            UIActions.hide(self.frames)
            WidgetAndWievHelpers.reset_and_set_data(lv_county, data=[], state=True)
            WidgetAndWievHelpers.reset_and_set_data([lv_municipality, lv_state], data=[], state=False)
            WidgetAndWievHelpers.reset_and_set_data(all_controls, data=[], state=False)
            self.lbl.setText('Aluskaart on laadimata, lae eelnevalt aluskaart')
            return

        self.dialog.frMaaAmetControlls.setVisible(False)
        self.dialog.frPropertiFlowHolder.setVisible(True)
        self.lbl.setText('Vali mida sa kinnistutega teha tahad')
        UIActions.hide(self.frames)
        WidgetAndWievHelpers.reset_and_set_data(lv_county, data=[], state=True)
        WidgetAndWievHelpers.reset_and_set_data([lv_municipality, lv_state], data=[], state=False)
        WidgetAndWievHelpers.reset_and_set_data(all_controls, data=[], state=False)

    def flow_and_ui_controls(self):
        lv_county, lv_state, lv_municipality = self.list_views
        cb_municipality, cb_roads = self.check_boxes
        all_views = self.list_views
        all_checkboxes = self.check_boxes + [cb_municipality, cb_roads]
        all_tables = self.table
        all_controls = all_checkboxes + all_tables

        state = PropertiesProcessStage.current_flow_stage
        progress = ProgressDialogModern(title="Andmete laadimine...", value=0)

        if state == FlowStages.COUNTY:
            progress.update(text1="Palun oota...", maximum=4)
            WidgetAndWievHelpers.reset_and_set_data(lv_county, data=[], state=True)
            UIActions.disable_and_clear(all_checkboxes)
            progress.update(1)
            WidgetAndWievHelpers.reset_and_set_data([lv_municipality, lv_state], data=[], state=False)
            progress.update(2)
            WidgetAndWievHelpers.reset_and_set_data(all_controls, data=[], state=False)
            progress.update(3)
            FlowStages.forward_stage()
            progress.close()

        elif state == FlowStages.PRE_STATE:
            progress.update(text1="Palun oota...", maximum=3)
            UIActions.disable_and_clear(all_checkboxes)
            WidgetAndWievHelpers.reset_and_set_data([lv_state, lv_municipality], data=[], state=True)
            progress.update(1)
            ListSelectionHandler.handle_selection()
            progress.update(2)
            WidgetAndWievHelpers.update_map_with_expression(lv_state, refresh=True, zoom_to=True)
            progress.update(3)
            progress.close()

        elif state == FlowStages.PRE_MUNICIPALITY:
            UIActions.enable(all_checkboxes)
            progress.update(text1="Palun oota...", maximum=3)
            WidgetAndWievHelpers.reset_and_set_data([lv_municipality], data=[], state=True)
            progress.update(1)
            ListSelectionHandler.handle_selection()
            progress.update(2)
            WidgetAndWievHelpers.update_map_with_expression(lv_municipality, refresh=True, zoom_to=True)
            progress.update(3)
            progress.close()

        elif state == FlowStages.PREVIEW:
            progress.update(text1="Palun oota...", maximum=4)
            progress.update(1)
            ListSelectionHandler.handle_selection()
            progress.update(2)
            WidgetAndWievHelpers.update_map_with_expression(lv_municipality, refresh=True, zoom_to=True)
            progress.update(3)
            FlowStages.forward_stage()
            progress.update(4)
            progress.close()

        elif state == FlowStages.COMPLETE:
            WidgetAndWievHelpers.reset_and_set_data(all_controls + all_views, data=None, state=False)
            progress.close()


class UIActions:
    @classmethod
    def hide(cls, elements):
        for element in elements:
            element.hide()

    @classmethod
    def show(cls, elements):
        for element in elements:
            element.show()

    @classmethod
    def enable(cls, elements):
        for element in elements:
            element.setEnabled(True)

    @classmethod
    def disable_and_clear(cls, elements):
        for element in elements:
            element.setEnabled(False)
            if isinstance(element, QCheckBox):
                element.setChecked(False)
            elif isinstance(element, QListView):
                model = element.model()
                if hasattr(model, 'clear'):
                    model.clear()
                elif hasattr(model, 'setRowCount'):
                    model.setRowCount(0)
            elif isinstance(element, QTableWidget):
                element.clearContents()
                element.setRowCount(0)
            elif isinstance(element, QTableView):
                model = element.model()
                if hasattr(model, 'clear'):
                    model.clear()
                elif hasattr(model, 'setRowCount'):
                    model.setRowCount(0)
