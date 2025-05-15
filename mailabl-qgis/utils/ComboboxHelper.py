#ComboBoxHelper.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListView, QComboBox, QPushButton
from typing import Any
from ..KeelelisedMuutujad.messages import Headings
from ..core.module.TypeManager import TypeModuleSetup
from ..core.module.TypeManager import ModuleStatuses
from ..utils.messagesHelper import ModernMessageDialog

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
        pass

    def populate_comboBox_smart(self, module: str =None, context: Any =None, button: QPushButton =None, 
                                comboBox: QComboBox=None, preferred_items: bool=False, simple_fill: bool=True,
                                groupComboBox: QComboBox=None, 
                                group_value: bool=False):
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


        # --- Case 1: Simple fill ---
        if not simple_fill:
            comboBox.clear()
            for item_text, item_id in context:
                if test == True:
                    print(f"Adding item: {item_text} ({item_id})")
                comboBox.addItem(item_text)
                comboBox.setItemData(comboBox.count() - 1, item_id)
            comboBox.setView(QListView())
            return None 

        # --- Case 2: Preferred types (multi-check combo) ---

        if preferred_items:
            type_manager = TypeModuleSetup(module)
            types = type_manager._get_types_for_module(module)
            if group_value is True:
                groups = {}
                for item_text, item_id in types:
                    if " - " not in item_text:
                        continue  # skip ungrouped items

                    group_label = item_text.split(" - ")[0]
                    if group_label not in groups:
                        groups[group_label] = []
                    groups[group_label].append((item_text, item_id))

                groupComboBox.clear()
                for group_name in sorted(groups.keys()):
                    groupComboBox.addItem(group_name)

                return
            comboBox.clear()
            for item_text, item_id in types:
                comboBox.addItem(item_text)
                comboBox.setItemData(comboBox.count() - 1, item_id)
            
            preferred = type_manager._get_preferred_item_ids_or_names(module)
            #print(f"preferred_items_raw: {preferred}")            
            if preferred == "Määramata":
                print("no preferred items")
            else:
                # Set check state for matching item IDs
                for i in range(comboBox.count()):
                    item_data = comboBox.itemData(i)
                    if item_data in preferred:
                        comboBox.setItemCheckState(i, Qt.Checked)
                    else:
                        comboBox.setItemCheckState(i, Qt.Unchecked)

                return preferred

        # --- Case 3: Status mode (single select) ---
        else:
            comboBox.clear()
            status_manager = ModuleStatuses(module)
            statuses = status_manager._get_all_statuses_for_module(module)
            
            if test == True:
                print("All statuses:", statuses)
            for item_text, item_id in statuses:
                comboBox.addItem(item_text)
                comboBox.setItemData(comboBox.count() - 1, item_id)
            comboBox.setView(QListView())

            preferred_status = status_manager._get_preferred_item_ids_or_names(module, name=True)
            comboBox.setCurrentText (preferred_status)          
    @staticmethod
    def refresh_combo_box_with_group_values(comboBox, module: str, group_values: set):
        type_manager = TypeModuleSetup(module)
        types = type_manager._get_types_for_module(module)

        comboBox.clear()

        for item_text, item_id in types:
            if " - " not in item_text:
                continue  # skip ungrouped

            group, sep, subtype = item_text.partition(" - ")
            if group in group_values:
                comboBox.addItem(subtype)
                comboBox.setItemData(comboBox.count() - 1, item_id)
    @staticmethod
    def setup_group_to_type_filtering(cmbtypesgroups, cmbtypes, module):
        def update_types_after_group_selection():
            # Read selected group values from cmbtypesgroups
            selected_groups = {
                cmbtypesgroups.itemText(i)
                for i in range(cmbtypesgroups.count())
                if cmbtypesgroups.itemData(i, Qt.CheckStateRole) == Qt.Checked
            }

            print(f"✅ Group selection changed: {selected_groups}")
            ComboBoxHelper.refresh_combo_box_with_group_values(
                comboBox=cmbtypes,
                module=module,
                group_values=selected_groups
            )
        cmbtypesgroups.model().itemChanged.connect(lambda _: update_types_after_group_selection())

class GetValuesFromComboBox:
    def _get_selected_id_from_combobox(comboBox):
        selected_index = comboBox.currentIndex()
        id_s = []
        if selected_index != -1:
            selected_id = comboBox.itemData(selected_index)
            id_s.append(selected_id)
            return id_s
        return None


    # Retrieving the selected item's value
    def _get_selected_name_from_combobox(comboBox):
        selected_index = comboBox.currentIndex()
        if selected_index != -1:
            selected_text = comboBox.currentText()
            return selected_text
        return None
    