from ..app.workspace_handler import WorkSpaceHandler
from ..app.MainMenuController import MenuModules
from ..KeelelisedMuutujad.modules import Module

class WidgetInfo:
    @staticmethod
    def get_stacked_widget_info(stacked_widget):
        widget_info = []
        for i in range(stacked_widget.count()):
            widget = stacked_widget.widget(i)

            # Get page order index
            page_index = i

            # Get original name (assigned during widget creation)
            original_name = widget.objectName()

            # Get accessible name (if applicable)
            accessible_name = ""
            if hasattr(widget, 'accessibleName'):  # Check for accessible name
                accessible_name = widget.accessibleName()

            widget_info.append({
                'page_index': page_index,
                'original_name': original_name,
                'accessibleName': accessible_name
            })

        print(f"widget_info: {widget_info}")
        return widget_info
            
    @staticmethod
    def create_visible_name_dropdown(stacked_widget_info, comboBox, index_id):
        comboBox.clear()

        for info in stacked_widget_info:
            visible_name = info.get('accessibleName', "")
            page_index = info.get ('page_index', "")
            if visible_name== "None":  # Check if accessible_name exists and is not empty
                pass
        
            else:
                comboBox.addItem(visible_name)
                comboBox.setItemData(comboBox.count()-1, page_index)

                        # Find the index of the item with the provided status_id
        for index in range(comboBox.count()):
            if comboBox.itemData(index) == index_id:
                comboBox.setCurrentIndex(index)
                break

    # Retrieving the selected item's ID
    @staticmethod
    def get_selected_index(comboBox):
        selected_index = comboBox.currentIndex()
        if selected_index != -1:
            selected_id = comboBox.itemData(selected_index)
            
            return selected_id
        return None
    
    def mapped_indexes_functions(self):

        return {
            0: lambda: WorkSpaceHandler.swWorkSpace_Easements(self),
            1: None,
            2: lambda: WorkSpaceHandler.swWorkSpace_Contracts(self),
            3: lambda: WorkSpaceHandler.swWorkSpace_Controller(self, menu_module=MenuModules.TEOSTUS, module=Module.ASBUILT),
            4: None,
            5: lambda: WorkSpaceHandler.swWorkSpace_Home(self),
            6: lambda: WorkSpaceHandler.swWorkSpace_Properties(self),
            7: lambda: WorkSpaceHandler.swWorkspace_Projects(self),
            8: None
        }
