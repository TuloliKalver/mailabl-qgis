# ListHelper.py
from PyQt5.QtCore import Qt
from typing import List
from PyQt5.QtWidgets import QListWidget

def check_all_items(list_widget):
    """
    Set check state of all items in a QListWidget to Checked.
    """
    for i in range(list_widget.count()):
        item = list_widget.item(i)
        item.setCheckState(Qt.Checked)

def uncheck_all_items(list_widget):
    """
    Set check state of all items in a QListWidget to Unchecked.
    """
    for i in range(list_widget.count()):
        item = list_widget.item(i)
        item.setCheckState(Qt.Unchecked)


def select_all_items(list_widget):
    """
    Select all items in a QListWidget.
    """
    list_widget.selectAll()

def deselect_all_items(list_widget):
    """
    Deselect all items in a QListWidget.
    """
    list_widget.clearSelection()


def get_checked_itme_count(list_widget):
    """
    Return the number of checked items in a QListWidget.
    """
    return sum(
        1 for i in range(list_widget.count())
        if list_widget.item(i).checkState() == Qt.Checked
    )

def get_cheked_items(list_widget):
    """
    Return a list of texts for the checked items in a QListWidget.
    """
    return [
        list_widget.item(i).text()
        for i in range(list_widget.count())
        if list_widget.item(i).checkState() == Qt.Checked
    ]



class ListSelections:
    def select_all_items(widget: QListWidget) -> None:
        """
        Select all items in a QListWidget.
        """
        widget.selectAll()

    def deselect_all_items(widget: QListWidget) -> None:
        """
        Deselect all items in a QListWidget.
        """
        widget.clearSelection()

    def get_selected_item_count(widget: QListWidget) -> int:
        """
        Return the number of selected items (via the selection model) in a QListWidget.
        """
        return len(widget.selectedItems())

    def get_selected_item_texts(widget: QListWidget) -> List:
        """
        Return a list of texts for the items that are selected (via the selection model) in a QListWidget.
        If no items are selected, return None.
        """
        selected_texts = [item.text() for item in widget.selectedItems()]
        return selected_texts if selected_texts else None
