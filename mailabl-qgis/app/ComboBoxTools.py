class ComboBoxTools: 
   # Retrieving the selected item's value
    def get_selected_item_name(comboBox):
        selected_index = comboBox.currentIndex()
        if selected_index != -1:
            selected_text = comboBox.currentText()
            return selected_text
        return None