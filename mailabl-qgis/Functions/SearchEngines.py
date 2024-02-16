from qgis.core import QgsProject
from ..Functions.item_selector_tools import properties_selectors

class General:
    @staticmethod
    def search_cadastral_items_by_values(self):
        layer_type = "import"
        self.tabWidget_Propertie_list.setCurrentIndex(0)
        self.cbChooseAllAdd_properties.setChecked(False)
        self.cbChooseAllAdd__street_properties.setChecked(False)
        search_items = self.leSearch_Add.displayText()
        items_list = [item.strip() for item in search_items.split(',')]
        items_str = ', '.join('"{}"'.format(item) for item in items_list)
        properties_selectors.show_connected_cadasters(items_str, layer_type)
