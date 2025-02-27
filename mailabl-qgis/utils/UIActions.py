from PyQt5.QtWidgets import QListView


class UIActions:

    def hider(self, elements):
        for element in elements:
            element.hide()

    def shower(self, elements):
        for element in elements:
            element.show()

    def cleaner (self, elements):
        for element in elements:
            element.clear()

    def selection_extended(self, elements):
        for element in elements:
            element.setSelectionMode(QListView.ExtendedSelection)

    def check_box_states_False(self, elements):
        for element in elements:
            element.setChecked(False)


    def check_box_states_True(self, elements):
        for element in elements:
            element.setChecked(True)


    def block_signals_False(self, elements):
        for element in elements:
            element.blockSignals(False)

    def block_signals_True(self, elements):
        for element in elements:
            element.blockSignals(True)