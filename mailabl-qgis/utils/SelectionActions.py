import gc

from .LayerSetups import LayerSetups
from .LayerHelpers import LayerProcessHandlers
from .WidgetHelpers import WidgetAndWievHelpers
from .MapHelpers import MapDataFlowHelper
from ..Common.app_state import PropertiesProcessStage, Expressions,  Processes, FlowStages, Layers_NEED_CENTRALIZING
from ..Functions.FlowPropertiesAdd import AddProperties
from ..Functions.RemoveProperties.RemoveSelectedProperties import ReomoveProcessController
from ..utils.UIStateManager import UIStateManager
from ..utils.TableUtilys.TableHelpers import TableHelper
from ..utils.ProgressHelper import ProgressDialogModern
from ..utils.MessagesHelpers import MessageLoaders
from ..utils.messagesHelper import ModernMessageDialog
from ..utils.LayerHelpers import LayerFilterSetters
from ..config.settings import StoredLayers

class SelectionActions:
    """Class responsible for handling user selections and executing actions.""" 
    @classmethod
    def __init__(self, dialog):
        """Initialize UI label for updates."""
        self.dialog = dialog
        self.label = self.dialog.lblActionName 
        self.frButtons = self.dialog.frPropertiFlowHolder
        self.table_view = self.dialog.tvSelectedMapItems
        self.confirm_button = self.dialog.pbConfirmAction

    @staticmethod
    def show_message(title, text):
        """
        Display a message.
        In your main project, replace this stub with your preferred message display.
        """
        print(f"{title}: {text}")



    @classmethod
    def cancel_selection(cls):
        """Handle process cancellation and cleanup."""
        UI = UIStateManager(cls.dialog)
        UI.disconnect_list_signals()

        if PropertiesProcessStage.active_process:
            process = PropertiesProcessStage.active_process.get("process")
            button = PropertiesProcessStage.active_process.get("button")
            frames = [cls.dialog.FrMunicipality,cls.dialog.FrState,
                            cls.dialog.FRCounty, cls.dialog.frResultViewer,
                            cls.dialog.frControllButtons]
            for frame in frames:
                frame.hide()
            cls.dialog.frPropertiFlowHolder.show()
            if button:
                button.setEnabled(True)
        PropertiesProcessStage.current_flow_stage = FlowStages.COMPLETE

        PropertiesProcessStage.clear_all_app_states()
        cls.dialog.lblActionName.setText('Vali mida sa kinnistutega teha tahad')
        layer_name =  StoredLayers.users_properties_layer_name()
        LayerFilterSetters._reset_layer(layer_name)
        shape_layer_name = StoredLayers.import_layer_name()
        print(f"shape_layer_name: {shape_layer_name}")
        LayerFilterSetters._reset_layer(shape_layer_name)

        



    @classmethod
    def _reset_previous_process(self):
        """Cancel any active process and re-enable its button."""
        gc.collect()  # Force garbage collection
        self.confirm_button.setEnabled(False)
        TableHelper.reset_and_set_tableView(self.table_view)
        if PropertiesProcessStage.active_process:
            prev_button = PropertiesProcessStage.active_process.get("button")
            prev_process = PropertiesProcessStage.active_process.get("process")
            if prev_button:
                prev_button.setEnabled(True)
                self.show_message("Process Canceled", f"Canceled previous {prev_process} process.")
                PropertiesProcessStage.active_process = None
                PropertiesProcessStage.current_flow_stage = None





    @classmethod
    def main_process_control(self, planned_process, selected_button):
        """
        Main entry point for process selection.
        Cancels any existing process, sets UI state, and loads required layers.
        """

        gc.collect()
        # Define the total number of steps for progress tracking.
        #print("going through main process controll")
        AddProperties.set_buttons_in_dev()
        self.frButtons.hide()
        progres_steps = 5  # Steps: 1-reset/initial, 2-flow controls, 3-layer load, 4-map elements, 5-final UI update
        
        # Initialize the progress bar using the helper.
        progress = ProgressDialogModern(title="Laen andmeid", value=0, maximum=progres_steps)
        progress.update(text1="Palun oota...")

        # Step 1: Reset previous process and update basic UI state.
        #self._reset_previous_process()
        selected_button.setEnabled(False)
        frames = [self.dialog.FrMunicipality,self.dialog.FrState,
                        self.dialog.FRCounty, self.dialog.frResultViewer,
                        self.dialog.frControllButtons]
        for frame in frames:
            frame.show()

        PropertiesProcessStage.active_process = {"process": planned_process, "button": selected_button}
        self.label.setText(planned_process)
        if PropertiesProcessStage.current_flow_stage is None:
            PropertiesProcessStage.current_flow_stage = FlowStages.COUNTY
        progress.update(value=1, maximum=progres_steps)

        # Determine required layers for the process.
        add = Processes.ADD
        edit = Processes.EDIT
        remove = Processes.REMOVE

        ui_state = UIStateManager(self.dialog)

        if planned_process in [add, edit]:
            ui_state.flow_and_ui_controls()
            ui_state.connect_list_signals()

            layers_config = [
                {"name": Layers_NEED_CENTRALIZING.IMPORT_LAYER_NAME, "activated": True, "cleanup": True},
                {"name": Layers_NEED_CENTRALIZING.USER_LAYER_NAME, "activated": False, "cleanup": False}
            ]


            print (f"layers config is {layers_config}")
        elif planned_process == remove:
            ui_state.connect_list_signals()
            ui_state.flow_and_ui_controls()
            layers_config = [
                {"name": Layers_NEED_CENTRALIZING.USER_LAYER_NAME, "activated": True, "cleanup": True}
            ]


        else:
            progress.close()
            self.show_message("Error", f"Unknown process: {planned_process}")
            selected_button.setEnabled(True)
            PropertiesProcessStage.active_process = None
            return
        progress.update(value=2, maximum=progres_steps)
        # Step 3: Load layers.
        if not LayerProcessHandlers._load_and_handle_layers(layers_config):
            selected_button.setEnabled(True)
            PropertiesProcessStage.active_process = None
            progress.close()
            return
        progress.update(value=3, maximum=progres_steps)
        
        # Step 4: Set active layer and update map element selection.
        if planned_process in [add, edit, remove]:
            # For this example the expression is empty – adjust as needed.
            expression = ""
            #print(f"atributes are: {expression}")
            field = Expressions.get_mapped_field()
            if not field:
                selected_button.setEnabled(True)
                PropertiesProcessStage.active_process = None
                progress.close()
                return
            #print(f"field is {field}")
            map_item_list = MapDataFlowHelper.get_sorted_unique_values_from_filtered_layer(
                                                                                    field=field,
                                                                                    expression=expression,
                                                                                    zoom_to=False,
                                                                                    select=False)
            WidgetAndWievHelpers.reset_and_set_data(elements=self.dialog.lvCounty, data=map_item_list)
            
        progress.update(value=5, maximum=progres_steps)
        # Finally, hide the progress bar.
        progress.close()
        gc.collect()
        print("Final cleanup — progress should now be closed")
        print(f"progress.dialog: {progress.dialog}, active_instance: {ProgressDialogModern.active_instance}")


        

    @classmethod
    def execute_action(self):
        """Execute the selected action and perform cleanup."""
        if PropertiesProcessStage.active_process:
            process = PropertiesProcessStage.active_process.get("process")
            button = PropertiesProcessStage.active_process.get("button")
            #print(f"process on execution {process} and button on process {button}")
            if process == Processes.ADD:
                if button:
                    button.setEnabled(False)
                result = AddProperties.add_properties_final_flow_controller()
                print(f"result is {result}")
                if result == False:
                    ModernMessageDialog.Info_messages_modern("Result", f"Nothing to update or to archive")
                    return
                if result == True:

                    ModernMessageDialog.Info_messages_modern("Result", f"All updatin processes handled succesfully")
                    SelectionActions.cancel_selection()

                    return
                else:
                    ModernMessageDialog.Info_messages_modern("Error", f"Something went wrong during {process} process")
                    return
            if process == Processes.EDIT:
                ModernMessageDialog.Info_messages_modern("Executing", f"Executing {process.capitalize()} Process...")
                return
            if process == Processes.REMOVE:
                if button:
                    button.setEnabled(False)
                    result = ReomoveProcessController.reomve_process_controller(delete_anyway=True)
                    if result == False:
                        ModernMessageDialog.Info_messages_modern("Result", f"Nothing to delete")
                        return
                    if result == True:
                        ModernMessageDialog.Info_messages_modern("Result", f"All deletion processes handled succesfully")
                        SelectionActions.cancel_selection()
                    else:
                        ModernMessageDialog.Info_messages_modern("Error", f"Something went wrong during {process} process")
                return
        else:
            MessageLoaders.show_message("Error", "No action selected!")
            #self.cleanup_map_and_functions()

