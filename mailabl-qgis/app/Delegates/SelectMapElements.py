from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from ...Functions.item_selector_tools import properties_selectors
from ...queries.python.projects_pandas import GetProjectsWhere


class SelectMapElementsDelegate(QStyledItemDelegate):
    def __init__(self, ID_column_index, parent=None):
        super(SelectMapElementsDelegate, self).__init__(parent)
        self.ID_column_index = ID_column_index

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                # Retrieve the ID_column_index value from the model
                id_value = str(model.data(model.index(index.row(), self.ID_column_index), Qt.DisplayRole))
                values = GetProjectsWhere.query_projects_related_properties(self, id_value)
                layer_type = "active"
                properties_selectors.show_connected_cadasters(values, layer_type)
                return True
        return super().editorEvent(event, model, option, index)
        