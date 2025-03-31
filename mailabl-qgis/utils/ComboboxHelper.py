from PyQt5.QtWidgets import QListView, QMessageBox, QComboBox, QPushButton
from typing import Any
from ..KeelelisedMuutujad.messages import Headings
from ..core.module.TypeManager import TypeManager


class ComboBoxHelper:
    """
    A utility class to handle context-aware population of QComboBoxes 
    based on module-specific data such as types or statuses.

    This class uses the centralized TypeManager to dynamically load:
    - Type lists (with or without preferred defaults)
    - Status lists with pre-selected status IDs
    - Raw data fills for simple one-off usage

    Usage:
        helper = ComboBoxHelper()
        helper.add_module_types_to_comboBox_set_prefed_type(...)
    """

    def __init__(self):
        """Initialize the helper with a fresh instance of TypeManager."""
        self.type_manager = TypeManager()

    def populate_comboBox_smart(self, module: str =None, context: Any =None, button: QPushButton =None, comboBox: QComboBox=None, preferred_items: bool=False, simple_fill: bool=True):
        test = False
        if test== True:
            print("Test mode enabled.")
            print("Populating combo box...")
            print(f"Module: {module}, Context: {context}")
        
        """
        Populate a QComboBox based on the given module and context.

        Supports three modes:
        1. Simple fill with raw context data (simple_fill=False)
        2. Type list + preferred type selection (preferred_items=True)
        3. Fallback to status list with pre-selected status (default)

        Args:
            module (str): Module identifier (e.g. Modules.MODULE_EASEMENTS)
            context (Any): The parent or context object (often 'self')
            button (QPushButton): Button triggering the combo logic, used for error handling
            comboBox (QComboBox): The combobox to populate
            preferred_items (bool): Whether to apply preferred type selections
            simple_fill (bool): If False, context is used directly to populate items
        """
        comboBox.clear()

        # --- Case 1: Simple fill ---
        if not simple_fill:
            for item_text, item_id in context:
                if test == True:
                    print(f"Adding item: {item_text} ({item_id})")
                comboBox.addItem(item_text)
                comboBox.setItemData(comboBox.count() - 1, item_id)
            comboBox.setView(QListView())
            return None  # or [] if you prefer consistency

        # --- Case 2: Preferred types (multi-check combo) ---

        if preferred_items:
            types = self.type_manager._get_types_for_module(
                module, 
                context)
            if test == True:
                print(f"Types from {module}: ", types)
            
            if not types:
                QMessageBox.warning(None, Headings().warningSimple, "Jätkamiseks seadista eelistatud liigid")
                button.blockSignals(False)
                return None

            for item_text, item_id in types:
                comboBox.addItem(item_text)
                comboBox.setItemData(comboBox.count() - 1, item_id)
            comboBox.setView(QListView())

            preferred_items_raw = self.type_manager._get_preferred_item_ids(module)
            selected_types = []
            for line in preferred_items_raw.split('\n'):
                selected_types.extend(item.strip() for item in line.split(',') if item.strip())

            comboBox.setCheckedItems(selected_types)
            return selected_types  # 🔥 Return list of selected IDs

        # --- Case 3: Status mode (single select) ---
        preferred_statuses = self.type_manager._get_preferred_statuses_for_module(module)
        if test ==True:
            print("Prefered statuses:", preferred_statuses)
            print("Preferred statuses:", preferred_statuses)
        preferred_id = preferred_statuses[0] if preferred_statuses else None
        if test == True:
            print("Selected ID:", preferred_id)
        statuses = self.type_manager._get_all_statuses_for_module(module)
        if test == True:
            print("All statuses:", statuses)
        for item_text, item_id in statuses:
            comboBox.addItem(item_text)
            comboBox.setItemData(comboBox.count() - 1, item_id)
        comboBox.setView(QListView())

        if preferred_id:
            for index in range(comboBox.count()):
                if comboBox.itemData(index) == preferred_id:
                    comboBox.setCurrentIndex(index)
                    break
            return [preferred_id] if preferred_id else []
        
class GetValuesFromComboBox:
    def _get_selected_status_id_from_combobox(comboBox):
        selected_index = comboBox.currentIndex()
        id_s = []
        if selected_index != -1:
            selected_id = comboBox.itemData(selected_index)
            id_s.append(selected_id)
            return id_s
        return None


    # Retrieving the selected item's value
    def _get_selected_status_name_from_combobox(comboBox):
        selected_index = comboBox.currentIndex()
        if selected_index != -1:
            selected_text = comboBox.currentText()
            return selected_text
        return None