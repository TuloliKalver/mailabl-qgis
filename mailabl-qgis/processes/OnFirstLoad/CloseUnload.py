from ...queries.python.access_credentials import clear_UC_data



class Unload:

    def handle_dialog_closed():
        #clear_UC_data()
        
        # This method will be called when the dialog is about to be closed
        # Perform any necessary cleanup and resource management here
        # Reset the plugin's state and variables here
        
        pass

    def closeEvent(self, event):
        # This method will be called when the user tries to close the dialog
        # Perform cleanup and reset operations here before closing the dialog
        self.handle_dialog_closed()
        event.accept()  # Accept the close event