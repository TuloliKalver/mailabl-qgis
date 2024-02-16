import os

plugin_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder_name = "widgets"

UI_multiline_Statusbar = "WStatusBar.ui"
UI_projects_connector = "Properties_connector.ui"

#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widget_multiText_Statusbar_path = os.path.normpath(os.path.join(plugin_dir_path, widgets_folder_name, UI_multiline_Statusbar))
#ui_file_path = f"C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\kataster\app\widgets\WStatusBar.ui"

widget_projects_toolsWidget_path = os.path.normpath(os.path.join(plugin_dir_path, widgets_folder_name, UI_projects_connector))

class PathLoaderSimple:
    def widget_statusBar_path(self):
        return widget_multiText_Statusbar_path


class PathLoader:
    def __init__(self, plugin_dir_path, UI_multiline_Statusbar):
        self.plugin_dir = plugin_dir_path
        self.widgets_folder_name = widgets_folder_name
        self.UI_multiline_Statusbar = UI_multiline_Statusbar
        self.UI_projects_connector = UI_projects_connector
        
    def get_absolute_path(self, *args):
        """Get the absolute path by joining the plugin directory with the provided arguments."""
        return os.path.abspath(os.path.join(self.plugin_dir, *args))

    def get_widgets_path(self, *args):
        """Get the absolute path for widgets by joining the plugin directory with the 'widgets' folder and provided arguments."""
        widgets_folder = "widgets"
        return self.get_absolute_path(widgets_folder, *args)

    def get_ui_path(self, *args):
        """Get the absolute path for UI files by joining the plugin directory with the 'ui' folder and provided arguments."""
        ui_folder = "ui"
        return self.get_absolute_path(ui_folder, *args)