from PyQt5.QtWidgets import QCheckBox

class CheckboxHelper:
    dialog = None  # Class-level variable to store the dialog reference

    @staticmethod
    def set_dialog(main_dialog):
        """Sets the main dialog reference for ButtonHelper."""
        CheckboxHelper.dialog = main_dialog

    @staticmethod
    def get_checkbox_by_name(element_name):
        element = CheckboxHelper.dialog.findChild(QCheckBox, element_name)
        return element


class CheckBoxes:

    @staticmethod
    def uncheck_checkboxes(widget, checkboxes_info):
        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                checkbox.setChecked(False)

    @staticmethod
    def update_checkboxes(checkboxes_info, table):
        if table:
            model = table.model()
           

        for checkbox, (text, connect_function) in checkboxes_info.items():
            if checkbox:
                current_text = checkbox.text()
                if connect_function is not None:
                    if model is None:
                        checkbox.setEnabled(False)
                    elif model is not  None:
                        item_count = model.rowCount()
                        if item_count == 0:
                            checkbox.setEnabled(False)
                        else:
                            checkbox.setEnabled(True)
                            checkbox.clicked.connect(connect_function)
                else:
                    checkbox.setText(f"{current_text}* ({text}m)")
                    checkbox.setEnabled(False)




