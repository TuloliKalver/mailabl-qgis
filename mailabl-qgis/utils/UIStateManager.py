#UIStateManager.py
from ..Common.app_state import PropertiesProcessStage, FlowStages
from PyQt5.QtWidgets import QListView, QTableView, QTableWidget, QCheckBox
from .WidgetHelpers import WidgetAndWievHelpers, ListSelectionHandler
from ..utils.ProgressHelper import ProgressDialogModern
from ..app.workspace_handler import CenterMainSliderIndexes



class UIStateManager:
    buttons = {}
    check_boxes = []
    list_views = []
    frames = []


    def __init__(self, dialog):
        self.dialog =dialog

        self.check_boxes = [self.dialog.chkSelectAllSettlements,self.dialog.chkToggleRoadSelection]
        self.list_views = [self.dialog.lvCounty, self.dialog.lvState,self.dialog.lvSettlement]

        self.frames = [self.dialog.FrMunicipality,self.dialog.FrState,
                        self.dialog.FRCounty, self.dialog.frResultViewer,
                        self.dialog.frControllButtons,]
            
        self.table = [self.dialog.tvSelectedMapItems]
        
        self.main_frame_buttons = [self.dialog.btnAddElements, self.dialog.btnUpdateData,
                            self.dialog.btnRemoveItems]
        
        self.action_buttons = [self.dialog.btnAddElements, self.dialog.btnUpdateData, 
                            self.dialog.btnRemoveItems, self.dialog.btnConfirmAction, 
                            self.dialog.btnCancelAction, self.dialog.pbAction]

        self.slider_ws = self.dialog.swWorkSpace
        self.slider_m = self.dialog.swCadastral_sub_processes
        self.slider_h = self.dialog.sw_HM
        self.lbl_action = self.dialog.lblPropertieOperations
        self.lbl = self.dialog.lblActionName

    def start_properti_flow_main(self):
        #print("started properties flow")
        """
        Set the flow state to 'county' so that only the county list view (first view)
        remains active while the others are disabled and hidden.
        """
        self.slider_ws.setCurrentIndex(CenterMainSliderIndexes.PROPERTIES_OPERATIONS)
        self.slider_h.setCurrentIndex(8)
        self.lbl_action.setText("Andmete laadimine")


        from ..config.settings import SettingsDataSaveAndLoad
        load = SettingsDataSaveAndLoad()
        layer_name = load.load_SHP_inputLayer_name()
        print(f"loaded layer name {layer_name}")
        from qgis.core import  QgsProject
        layer = QgsProject.instance().mapLayersByName(layer_name)

        lv_county, lv_state, lv_municipality = self.list_views[:3]
        cb_municipality, cb_roads = self.check_boxes[:2]
        all_checkboxes = self.check_boxes + [cb_municipality, cb_roads]
        all_tables = self.table
        all_controls = all_checkboxes + all_tables

        if not layer:
            print("layer not loaded")
            self.dialog.frMaaAmetControlls.setVisible(True)
            self.dialog.frPropertiFlowHolder.setVisible(False)
            UIActions.hide(self.frames)
            WidgetAndWievHelpers.reset_and_set_data(lv_county, data=[], state=True)  # Enable county list
            WidgetAndWievHelpers.reset_and_set_data([lv_municipality, lv_state], data=[], state=False)
            WidgetAndWievHelpers.reset_and_set_data(all_controls + all_checkboxes, data=[], state=False)  # Disable everything else
            WidgetAndWievHelpers.reset_and_set_data(all_tables, data=[], state=False)
            self.lbl.setText('Aluskaart on laadimata, lae eelnevalt aluskaart')
            return

        if not self.list_views or len(self.list_views) < 3:

            return
        self.dialog.frMaaAmetControlls.setVisible(False)
        self.dialog.frPropertiFlowHolder.setVisible(True)
        self.lbl.setText('Vali mida sa kinnistutega teha tahad')
        UIActions.hide(self.frames)
        WidgetAndWievHelpers.reset_and_set_data(lv_county, data=[], state=True)  # Enable county list
        WidgetAndWievHelpers.reset_and_set_data([lv_municipality, lv_state], data=[], state=False)
        WidgetAndWievHelpers.reset_and_set_data(all_controls + all_checkboxes, data=[], state=False)  # Disable everything else
        WidgetAndWievHelpers.reset_and_set_data(all_tables, data=[], state=False)

    def enable_after_process_selection(self, selected_button):
        """
        Enable all UI elements (buttons, check_boxes, list views) and then disable the selected button.
        """
        UIActions.show(self.frames)
        selected_button.setEnabled(False)

    @classmethod
    def enable_elements(cls, elements):
        """Enable (show) specific UI elements."""
        UIActions.show(elements)

    @classmethod
    def disable_elements(cls, elements):
        """Disable (hide) specific UI elements."""
        UIActions.hide(elements)


    def flow_and_ui_controls(self):
        """
        Adjust the visibility and enabled state of list views based on the selection flow state.
        Expected states: "county", "state", "municipality", "complete"

        """


        lv_county, lv_state, lv_municipality = self.list_views[:3]
        cb_municipality, cb_roads = self.check_boxes[:2]
        #pbConCounty, pbConState, pbConMunicipality, bbForward, pbBack = cls.flow_buttons [:5]
        
        all_views = [lv_county, lv_state, lv_municipality ]
        #all_buttons = [pbConCounty, pbConState, pbConMunicipality]
        all_checkboxes = self.check_boxes + [cb_municipality, cb_roads]
        all_tables = self.table
        all_controls = all_checkboxes + all_tables

        state = PropertiesProcessStage.current_flow_stage
        # ** Define UI Elements **

        start_value = 0
        progress = ProgressDialogModern(title="Andmete laadimine", value=start_value)

        # Define state-specific UI actions
        if state == FlowStages.COUNTY:
            progres_steps = 5
            progress.update(text1="Palun oota...", maximum=progres_steps)
            WidgetAndWievHelpers.reset_and_set_data(lv_county, data=[], state=True)  # Enable county list
            UIActions.disable_and_clear(all_checkboxes)
            progress.update(1)
            WidgetAndWievHelpers.reset_and_set_data([lv_municipality, lv_state], data=[], state=False)
            progress.update(2)
            WidgetAndWievHelpers.reset_and_set_data(all_controls + all_checkboxes, data=[], state=False)  # Disable everything else
            progress.update(3)
            WidgetAndWievHelpers.reset_and_set_data(all_tables, data=[], state=False)
            progress.update(4)
            FlowStages.forward_stage()
            progress.close()

        elif state == FlowStages.PRE_STATE:
            progres_steps = 3
            progress.update(text1="Palun oota...", maximum=progres_steps)
            UIActions.disable_and_clear(all_checkboxes)
            WidgetAndWievHelpers.reset_and_set_data([lv_state, lv_municipality], data=[], state=True)
            progress.update(1)
            ListSelectionHandler.handle_selection()
            progress.update(2)
            WidgetAndWievHelpers.update_map_with_expression(lv_state, refresh=True, zoom_to=True)
            progress.update(3)
            progress.close()
    

        elif state == FlowStages.STATE:
            print("Ooops ... kuidas sa siia sattusid")
            return

        elif state == FlowStages.PRE_MUNICIPALITY:
            
            progres_steps = 3
            UIActions.enable(all_checkboxes)
            WidgetAndWievHelpers.reset_and_set_data([lv_municipality], data=[], state=True)
            progress.update(1)
            ListSelectionHandler.handle_selection()
            progress.update(2)
            WidgetAndWievHelpers.update_map_with_expression(lv_municipality, refresh=True, zoom_to=True)
            progress.update(3)
            progress.close()
    
        elif state == FlowStages.MUNICIPALITY:
            print("Ooops ... kuidas sa siia sattusid")
            return

        elif state == FlowStages.PREVIEW:
            progres_steps = 4
            progress.update(text1="Palun oota...", maximum=progres_steps)
            progress.update(1)
            ListSelectionHandler.handle_selection()
            progress.update(2)
            WidgetAndWievHelpers.update_map_with_expression(lv_municipality, refresh=True, zoom_to=True)   
            progress.update(3)
            FlowStages.forward_stage()
            progress.update(4)
            progress.close()

        elif state == FlowStages.COMPLETE:
            progres_steps = 0
            progress.update(text1="Palun oota...", maximum=progres_steps)
            WidgetAndWievHelpers.reset_and_set_data(all_controls + all_views, data=None, state=False)  # Disable everything
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
        """
        Enable (set enabled state to True) the given UI elements.
        This makes them interactive while still remaining visible.
        """
        for element in elements:
            element.setEnabled(True)



    @classmethod
    def disable_and_clear(cls, elements):
        """
        Disable (set enabled state to False) the given UI elements.
        Additionally, if an element is a QListView or QTableView/QTableWidget,
        its contents are cleared. If it's a QCheckBox, it's unchecked.
        """
        for element in elements:
            element.setEnabled(False)
            
            # Clear QCheckBox state.
            if isinstance(element, QCheckBox):
                element.setChecked(False)
            
            # Clear contents for QListView.
            elif isinstance(element, QListView):
                model = element.model()
                if model is not None:
                    # Use clear() if availabel.
                    if hasattr(model, 'clear'):
                        model.clear()
                    # If not, try to reset row count if it's a QStandardItemModel or similar.
                    elif hasattr(model, 'setRowCount'):
                        model.setRowCount(0)
                    else:
                        print("Warning: The model for QListView does not support clearing.")
            
            # Clear contents for QTableWidget.
            elif isinstance(element, QTableWidget):
                element.clearContents()
                element.setRowCount(0)
            
            # Clear contents for QTableView.
            elif isinstance(element, QTableView):
                model = element.model()
                if model is not None:
                    if hasattr(model, 'clear'):
                        model.clear()
                    elif hasattr(model, 'setRowCount'):
                        model.setRowCount(0)
                    else:
                        print("Warning: The model for QTableView does not support clearing.")




