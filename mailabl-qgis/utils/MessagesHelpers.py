#Message.Helpers.py
from PyQt5.QtWidgets import QMessageBox


class MessageLoaders:
    @staticmethod
    def show_message(title, text):
        """Display a message box."""
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()

    @staticmethod
    def layername_error(layer_name):
        """Return a formatted error message for missing layers."""
        MessageLoaders.show_message(TitleMessages.error, f"Layer '{layer_name}' is missing, process aborted.")

    @staticmethod
    def ask_append_or_replace(new_layer_name):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(TitleMessages.layer_exists)
        msgBox.setText(
            f"Sinu algses failis on juba '{new_layer_name}' nimeline kiht olemas .\n"
            "kas sa soovid andmeid asendada  ja lisada täiesti uued andmed .\n"
            "või lisada need olemasolevate andmetele lisaks. \n"
            "või tühistan tegevuse?"
        )
        appendButton = msgBox.addButton("Lisa", QMessageBox.AcceptRole)
        replaceButton = msgBox.addButton("Asenda", QMessageBox.DestructiveRole)
        cancelButton = msgBox.addButton("Tühista", QMessageBox.RejectRole)
        msgBox.exec_()
        # Return the clicked button and the button references so you can compare later
        return msgBox.clickedButton(), appendButton, replaceButton, cancelButton



class TitleMessages:
    layer_exists = "Leitud kaardikiht"
    title_example = 'write something here'
    error = "Error"
    process_selected = "Process Selected"

class TextMessages:
    text_example = 'write something here'
    no_layer_provided = "No layer provided for unloading!"



        
