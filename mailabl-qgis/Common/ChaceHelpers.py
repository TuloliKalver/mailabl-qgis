from .app_state import PropertiesProcessStage, FlowStages
from PyQt5.QtWidgets import QListWidget, QListView


class CacheUpdater:
    def update_slected_items_cache(element):
        """
        Updates the AppState.cache based on the widget that triggered the selection.

        - For lvCounty: Clears the cache and stores only 'selected_counties'.
        - For lvState: Updates the cache with 'selected_state' only if 'selected_counties' is already present.
        - For lvSettlement: Updates the cache with 'selected_settlements' only if both 'selected_counties'
        and 'selected_state' are already present.
        
        :param element: The list widget element (QListWidget or QListView).
        :param selected_text: List of selected items' text.
            """
        if not isinstance(PropertiesProcessStage.cache, dict):
            PropertiesProcessStage.cache = {}

        widget_name = element.objectName() if hasattr(element, "objectName") else None

        if isinstance(element, QListWidget):
            selected_items = [item.text() for item in element.selectedItems()]
        elif isinstance(element, QListView):
            selected_items = [index.data() for index in element.selectionModel().selectedIndexes()]
        else:
            print("Unsupported element type")
            return
        
        #print(f"selected items are: {selected_items}")

        if widget_name == 'lvCounty':
            PropertiesProcessStage.cache.clear()  # Clear the entire cache.
            PropertiesProcessStage.cache['selected_counties'] = selected_items
            PropertiesProcessStage.current_flow_stage = FlowStages.PRE_STATE
        elif widget_name == 'lvState':
            if 'selected_counties' in PropertiesProcessStage.cache and PropertiesProcessStage.cache['selected_counties']:
                PropertiesProcessStage.cache['selected_state'] = selected_items
                PropertiesProcessStage.current_flow_stage = FlowStages.PRE_MUNICIPALITY
            else:
                return
                #print("Cannot update state selection without counties.")
        elif widget_name == 'lvSettlement':
            if ('selected_counties' in PropertiesProcessStage.cache and PropertiesProcessStage.cache['selected_counties']) and \
            ('selected_state' in PropertiesProcessStage.cache and PropertiesProcessStage.cache['selected_state']):
                PropertiesProcessStage.cache['selected_settlements'] = selected_items#selected_text
                PropertiesProcessStage.current_flow_stage = FlowStages.PREVIEW
            else:
                return
                #print("Cannot update settlement selection without counties and state.")
        else:
            print("Unknown widget name:", widget_name)
            return
