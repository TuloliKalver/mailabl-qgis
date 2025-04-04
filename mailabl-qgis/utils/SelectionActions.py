import gc
from .LayerHelpers import LayerSetups, LayerProcessHandlers
from .WidgetHelpers import WidgetAndWievHelpers
from .MapHelpers import MapDataFlowHelper
from ..Common.app_state import PropertiesProcessStage, Expressions,  Processes, FlowStages, Layers_NEED_CENTRALIZING
from ..Functions.FlowPropertiesAdd import AddProperties
from ..utils.UIStateManager import UIStateManager
from ..utils.TableUtilys.TableHelpers import TableHelper
from ..utils.ProgressHelper import ProgressDialogModern
from ..utils.MessagesHelpers import MessageLoaders




class SelectionActions:
    """Class responsible for handling user selections and executing actions.""" 
    @classmethod
    def initialize(self, dialog, label, button_frame, confirm_button, table_view):
        """Initialize UI label for updates."""
        self.dialog = dialog
        self.label = label
        self.frButtons = button_frame
        self.table_view = table_view
        self.confirm_button = confirm_button

    @staticmethod
    def show_message(title, text):
        """
        Display a message.
        In your main project, replace this stub with your preferred message display.
        """
        print(f"{title}: {text}")

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
    def cleanup_map_and_functions(self):
        """
        Unload all layers that were flagged for cleanup,
        reset the active process, and clear UI state.
        """
        ui_state = UIStateManager(self.dialog)
        #print(f"active layer is {AppState.active_layer}")
        LayerSetups.unload_layer_usage(PropertiesProcessStage.active_layer)
        PropertiesProcessStage.loaded_layers = {}  # Clear the loaded layers dictionary.
        PropertiesProcessStage.active_layer = None
        ui_state.flow_and_ui_controls()
        PropertiesProcessStage.clear_flow_and_processes()
        gc.collect()  # Force garbage collection
        self.label.setText("")


    @classmethod
    def main_process_control(self, planned_process, selected_button):
        """
        Main entry point for process selection.
        Cancels any existing process, sets UI state, and loads required layers.
        """


        # Define the total number of steps for progress tracking.
        #print("going through main process controll")
        AddProperties.set_buttons_in_dev()
        self.frButtons.hide()
        progres_steps = 5  # Steps: 1-reset/initial, 2-flow controls, 3-layer load, 4-map elements, 5-final UI update
        start_value = 0

        # Initialize the progress bar using the helper.
        progress = ProgressDialogModern(title="Laen andmeid", value=0, maximum=progres_steps)
        progress.update(text1="Palun oota...")

        # Step 1: Reset previous process and update basic UI state.
        self._reset_previous_process()
        selected_button.setEnabled(False)
        frames = [self.dialog.FrMunicipality,self.dialog.FrState,
                        self.dialog.FRCounty, self.dialog.frResultViewer,
                        self.dialog.frControllButtons,]
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
            
            layers_config = [
                {"name": Layers_NEED_CENTRALIZING.IMPORT_LAYER_NAME, "activated": True, "cleanup": True},
                {"name": Layers_NEED_CENTRALIZING.USER_LAYER_NAME, "activated": False, "cleanup": False}
            ]
            print (f"layers config is {layers_config}")
        elif planned_process == remove:
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
        if not LayerProcessHandlers.load_and_handle_layers(layers_config):
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
                                                                                    zoom_to=True)
            WidgetAndWievHelpers.reset_and_set_data(elements=self.dialog.lvCounty, data=map_item_list)
            
        progress.update(value=5, maximum=progres_steps)
        # Finally, hide the progress bar.
        progress.close()
        gc.collect()
        print("Final cleanup — progress should now be closed")
        print(f"progress.dialog: {progress.dialog}, active_instance: {ProgressDialogModern.active_instance}")

    @classmethod
    def cancel_selection(self):
        """Handle process cancellation and cleanup."""
        if PropertiesProcessStage.active_process:
            process = PropertiesProcessStage.active_process.get("process")
            button = PropertiesProcessStage.active_process.get("button")
            self.show_message("Action", f"Canceled {process} process.")
            frames = UIStateManager.frames()
            print(f"frames are {frames}")
            if button:
                button.setEnabled(True)
            from .UIStateManager import UIActions
            UIActions.hide(frames)
            
        self.frButtons.show()
        self.cleanup_map_and_functions()


    @classmethod
    def execute_action(self):
        """Execute the selected action and perform cleanup."""
        if PropertiesProcessStage.active_process:
            process = PropertiesProcessStage.active_process.get("process")
            button = PropertiesProcessStage.active_process.get("button")
            #print(f"process on execution {process} and button on process {button}")
            if process == Processes.ADD:
                if button:
                    button.setEnabled(True)
                result = AddProperties.add_properties_final_flow_controller()
                if result == False:
                    MessageLoaders.show_message("Result", f"Nothing to update or to archive")
                if result == True:
                    MessageLoaders.show_message("Result", f"All updatin processes handled succesfully")

            if process == Processes.EDIT:
                MessageLoaders.show_message("Executing", f"Executing {process.capitalize()} Process...")
                return
            if process == Processes.REMOVE:
                MessageLoaders.show_message("Executing", f"Executing {process.capitalize()} Process...")
                return
            
            #self.cleanup_map_and_functions()
        else:
            MessageLoaders.show_message("Error", "No action selected!")
            #self.cleanup_map_and_functions()
