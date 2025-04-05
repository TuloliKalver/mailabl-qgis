import gc
from..Common.app_state import PropertiesProcessStage, FlowStages, Expressions
from .ButtonsHelper import ButtonHelper
from ..utils.TableUtilys.TableHelpers import TableHelper
from ..utils.ProgressHelper import ProgressDialogModern
from ..utils.CheckBoxHelper import CheckboxHelper
from .MapHelpers import MapDataFlowHelper
from ..Common.ChaceHelpers import CacheUpdater
from ..utils.ListHelper import ListSelections
from PyQt5.QtWidgets import (
    QListWidget, QTableWidget, QTableWidgetItem, QCheckBox, QLineEdit, QComboBox, QTextEdit,
    QListView, QTableView
)
from PyQt5.QtCore import QStringListModel



class WidgetAndWievHelpers:
    """ Smart UI Helper that detects widget type and applies the correct reset & data insertion logic. """
    dialog = None
    @staticmethod
    def set_dialog(main_dialog):
        """Sets the main dialog reference for ButtonHelper."""
        WidgetAndWievHelpers.dialog = main_dialog

    @staticmethod
    def reset_and_set_data(elements, data=None, state=None, headers=None) -> None:
        #print(f"elemets: {elements} /n data: {data} /n desired state {state}")
        """
        Automatically resets and inserts new data based on the widget type.

        :param elements: A single UI element or a list of UI elements.
        :param data: The data to insert (list[str] for list-based widgets, list[list[str]] for tables).
        """
        # Ensure elements is always a list (even if a single element is passed)
        if not isinstance(elements, list):
            elements = [elements]

        for element in elements:
            if state is not None:
                element.setEnabled(state)

            # ** Handle QListWidget **
            if isinstance(element, QListWidget):
                element.clear()
                if isinstance(data, list):
                    element.addItems(data)

            # ** Handle QTableWidget **
            elif isinstance(element, QTableWidget):
                element.clearContents()
                element.setRowCount(0)
                if isinstance(data, list) and all(isinstance(row, list) for row in data):
                    element.setRowCount(len(data))
                    element.setColumnCount(len(data[0]) if data else 0)
                    for row_idx, row in enumerate(data):
                        for col_idx, value in enumerate(row):
                            item = QTableWidgetItem(value)
                            element.setItem(row_idx, col_idx, item)

            # ** Handle QListView **
            elif isinstance(element, QListView):
                model = QStringListModel(data if isinstance(data, list) else [])
                element.setModel(model)

            # ** Handle QTableView **
            elif isinstance(element, QTableView):
                TableHelper.insert_data_into_tableview(element=element, data=data, headers=headers, feature_ids=None)
                gc.collect()
            # ** Handle QCheckBox **
            elif isinstance(element, QCheckBox):
                element.setChecked(bool(data))

            # ** Handle QLineEdit, QTextEdit, QComboBox **
            elif isinstance(element, (QLineEdit, QTextEdit, QComboBox)):
                element.clear()
                if isinstance(element, QComboBox) and isinstance(data, list):
                    element.addItems(data)



    # Function that uses the mapping to build the expression and update the map view
    @staticmethod
    def update_map_with_expression(list_widget: QListWidget, 
                                   refresh: bool = False, 
                                   zoom_to: bool = False):

        # Get total feature count for progress tracking
        progres_steps = 6
        start_value = 0

        progress = ProgressDialogModern(title="Andmete laadimine...", value=0, maximum=progres_steps)
        progress.update(1, text1="Palun oota...")
 
        flow_state = PropertiesProcessStage.current_flow_stage
        # Get the mapping for the current flow state
        mapping = Expressions.FLOW_EXPRESSION_MAPPING.get(flow_state, {})
        next_flow = mapping.get("next_flow")
        
        mapping_afther = Expressions.FLOW_EXPRESSION_MAPPING.get(next_flow, {})

        # Check if a builder function is configured for this state
        builder = mapping.get("builder")
        if builder:
            field = mapping.get("field")
            target_field = mapping_afther.get("target_field")
            extra_field = mapping.get("extra_field")

            expression = builder(PropertiesProcessStage.cache)
            progress.update(2)
            #print(f"extra field: {extra_field}")
            if extra_field is not None and extra_field != '':
                target_field = extra_field
                #print("reset target field to extra field")

            else:
                # Get map items using the field and generated expression
                data = MapDataFlowHelper.get_sorted_unique_values_from_filtered_layer(field=target_field, expression=expression, refresh_layer=refresh, zoom_to=zoom_to)
                
                progress.update(3)
            # Update the UI widget with the retrieved map items
            if flow_state == FlowStages.PREVIEW:
                button_name = ['pbConfirmAction']
                buttons = ButtonHelper.get_button_objects(button_name)    
                selected_text = ListSelections.get_selected_item_texts(list_widget)

                if not selected_text:
                    flow_state = PropertiesProcessStage.current_flow_stage
                    WidgetAndWievHelpers.reset_and_set_data(buttons, data=[], state=False)
                    progress.update(5)
                    progress.close()
                    gc.collect()
                else:
                    table_name = 'tvSelectedMapItems'
                    table = TableHelper.get_table_by_name(table_name)
                    table.setEnabled(True)
                    data, feature_ids, fields = MapDataFlowHelper.get_layer_data_by_defined_fields(expression, zoom_to=zoom_to)                
                    progress.update(4)
                    TableHelper.insert_data_into_tableview(element=table, data=data, headers=fields, feature_ids=feature_ids)
                    TableHelper.select_all_items(table=table)
                    WidgetAndWievHelpers.reset_and_set_data(buttons, data=[], state=True)
                    progress.update(5)
                    progress.close()
                    gc.collect()
            else:
                WidgetAndWievHelpers.reset_and_set_data(list_widget, data=data, state=True)
                progress.update(5)
                progress.close()
                gc.collect()
        else:
            #print("No expression builder is configured for this state.")
            return
        


class ListSelectionHandler:
    dialog = None  # Class-level variable to store the dialog reference
    
    @staticmethod
    def set_dialog(main_dialog):
        """Sets the main dialog reference for ButtonHelper."""
        ListSelectionHandler.dialog = main_dialog

    @classmethod
    #def handle_selection(element, flow_state) -> list:
    def handle_selection(cls) -> list:
        """
        Handles selection behavior for QListWidget and QListView.
        Enables buttons dynamically if a valid selection is made.

        :return: List of selected items' text.
        """
        # Retrieve the sender of the signal.
        element = ListSelectionHandler.dialog.sender()

        selected_text = ListSelections.get_selected_item_texts(element)
        checkbox_name = 'chkToggleRoadSelection'
        checkbox = CheckboxHelper.get_checkbox_by_name(checkbox_name)

        if not selected_text:
            table_name = 'tvSelectedMapItems'
            checkbox.setEnabled(False)
            table = TableHelper.get_table_by_name(table_name)
            TableHelper.reset_and_set_tableView(table)
            return
        
        CacheUpdater.update_slected_items_cache(element)
        FlowStages.forward_stage()
        checkbox.setEnabled(True)
