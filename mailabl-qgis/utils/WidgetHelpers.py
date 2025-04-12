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
        """
        Automatically resets and inserts new data based on the widget type.

        Args:
            elements: A single UI element or a list of UI elements.
            data: The data to insert (optional). If None, only clears elements.
            state: Optional enabled/disabled state to apply.
            headers: Optional headers (for TableViews).
        """
        if not isinstance(elements, list):
            elements = [elements]

        for element in elements:
            if state is not None:
                element.setEnabled(state)

            # QListWidget
            if isinstance(element, QListWidget):
                element.clear()
                if data is not None and isinstance(data, list):
                    element.addItems(data)

            # QTableWidget
            elif isinstance(element, QTableWidget):
                element.clearContents()
                element.setRowCount(0)
                if data is not None and isinstance(data, list) and all(isinstance(row, list) for row in data):
                    element.setRowCount(len(data))
                    element.setColumnCount(len(data[0]) if data else 0)
                    for row_idx, row in enumerate(data):
                        for col_idx, value in enumerate(row):
                            item = QTableWidgetItem(value)
                            element.setItem(row_idx, col_idx, item)

            # QListView
            elif isinstance(element, QListView):
                model_data = data if isinstance(data, list) else []
                element.setModel(QStringListModel(model_data))

            # QTableView
            elif isinstance(element, QTableView):
                if data is not None:
                    TableHelper.insert_data_into_tableview(element=element, data=data, headers=headers, feature_ids=None)
                    gc.collect()
                else:
                    # Clear table view (set empty model)
                    TableHelper.insert_data_into_tableview(element=element, data=[], headers=headers, feature_ids=None)

            # QCheckBox
            elif isinstance(element, QCheckBox):
                element.setChecked(bool(data))

            # QLineEdit, QTextEdit, QComboBox
            elif isinstance(element, (QLineEdit, QTextEdit, QComboBox)):
                element.clear()
                if isinstance(element, QComboBox) and isinstance(data, list):
                    element.addItems(data)


    # Function that uses the mapping to build the expression and update the map view
    @staticmethod
    def update_map_with_expression(list_widget: QListWidget, refresh: bool = False, zoom_to: bool = False):
        progres_steps = 6
        progress = ProgressDialogModern(title="Andmete laadimine...", value=0, maximum=progres_steps)
        progress.update(1, text1="Palun oota...")

        try:
            flow_state = PropertiesProcessStage.current_flow_stage
            mapping = Expressions.FLOW_EXPRESSION_MAPPING.get(flow_state, {})
            next_flow = mapping.get("next_flow")
            mapping_afther = Expressions.FLOW_EXPRESSION_MAPPING.get(next_flow, {})

            builder = mapping.get("builder")
            if not builder:
                print("🚫 No builder configured for flow stage.")
                return

            expression = builder(PropertiesProcessStage.cache)
            field = mapping.get("field")
            extra_field = mapping.get("extra_field")
            target_field = extra_field if extra_field else mapping_afther.get("target_field")

            progress.update(2)

            if flow_state == FlowStages.PREVIEW:
                selected_text = ListSelections.get_selected_item_texts(list_widget)
                button_name = ['pbConfirmAction']
                buttons = ButtonHelper.get_button_objects(button_name)

                if not selected_text:
                    WidgetAndWievHelpers.reset_and_set_data(buttons, data=[], state=False)
                    progress.update(5)
                    return

                table = TableHelper.get_table_by_name('tvSelectedMapItems')
                table.setEnabled(True)

                data, feature_ids, fields = MapDataFlowHelper.get_layer_data_by_defined_fields(expression, zoom_to=zoom_to)
                progress.update(4)

                TableHelper.insert_data_into_tableview(table, data, headers=fields, feature_ids=feature_ids)
                TableHelper.select_all_items(table)
                WidgetAndWievHelpers.reset_and_set_data(buttons, data=[], state=True)

            else:
                data = MapDataFlowHelper.get_sorted_unique_values_from_filtered_layer(
                    field=target_field,
                    expression=expression,
                    refresh_layer=refresh,
                    zoom_to=zoom_to
                )
                WidgetAndWievHelpers.reset_and_set_data(list_widget, data=data, state=True)

            progress.update(5)

        finally:
            progress.close()
            gc.collect()

        
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
