# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
import os
from qgis.utils import iface
from qgis.core import QgsProject

from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTableView
from PyQt5.uic import loadUi
from ..KeelelisedMuutujad.messages import Headings

from ..utils.progres_bar_operations import run_with_progress

pealkiri = Headings()

plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#Status bar widget folder
widgets_folder = "widgets"  
#widgets_path = os.path.join(plugin_dir,widgets_folder, "WStatusBar.ui")
widgets_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "WStatusBar.ui"))

projects_toolsWidget_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "Properties_connector.ui"))
contracts_toolsWidget_path = os.path.normpath(os.path.join(plugin_dir, widgets_folder, "ContractsPropertiesConnector.ui"))

model = QStandardItemModel()

class ToolsProject:
    def projects_toolWidget(self, Project_name, Project_number):
        projects_ToolsWidget = loadUi(projects_toolsWidget_path)
        projects_ToolsWidget.lblProjectName.setText(Project_name)
        projects_ToolsWidget.lblProjectNumber.setText(Project_number)
        return projects_ToolsWidget    

class ToolsContract:
    def contract_toolWidget(self, Contract_name, Contract_number):
        contract_ToolsWidget = loadUi(contracts_toolsWidget_path)
        contract_ToolsWidget.lblContractName.setText(Contract_name)
        contract_ToolsWidget.lblContractNumber.setText(Contract_number)
        return contract_ToolsWidget    


class shp_tools_MOVE_TOOL:
    
    @staticmethod
    def activateLayer_zoomTo_MOVE_TOOL(layer):
        #input_layer = QgsProject.instance().mapLayersByName(layer)[0]
        iface.setActiveLayer(layer)
        iface.zoomToActiveLayer()
        QCoreApplication.processEvents()
        
    
class LayerProcessor:
    @staticmethod
    def process_layer_with_progress(layer_name, filter_function, process_function=None, progress_messages=None):
        """
        A universal function to process layers with progress updates.

        Parameters:
        - layer_name: The name of the layer to process.
        - filter_function: A function defining the filtering condition (returns True/False).
        - process_function: (Optional) A function to process each filtered feature.
        - progress_messages: (Optional) A dictionary for customizing progress messages at different stages.

        Returns:
        - The processed and filtered unique data.
        """

        # Default progress messages
        default_progress_messages = {
            'quarter': "Uhh kui palju tööd:",
            'halfway': "Olen juba veerandi läbinud",
            'three_quarters': "Ära noki nina!"
        }
        progress_messages = progress_messages or default_progress_messages

        def task(progress_handler):
            input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
            processed_data = []
            
            for feature in input_layer.getFeatures():
                if filter_function(feature):
                    if process_function:
                        processed_data.append(process_function(feature))
                    else:
                        processed_data.append(feature)
                progress_handler.increment_progress(1)

            #print(f"Processed data before filtering unique values: {processed_data}")

            # Filter for unique values and sort
            unique_sorted_data = sorted(set(processed_data))
            #print(f"Unique sorted data: {unique_sorted_data}")

            return unique_sorted_data  # Return unique sorted values

        result = run_with_progress(task_function=task, window_title="Processing")
        #print(f"Final result from process_layer_with_progress: {result}")
        return result or []
