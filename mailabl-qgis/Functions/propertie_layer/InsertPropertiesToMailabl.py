from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from qgis.core import QgsProject
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from ...config.ui_directories import PathLoader, plugin_dir_path, UI_multiline_Statusbar
from ...utils.TableUtilys.TableHelpers import ColumnResizer
from ...KeelelisedMuutujad.messages import Headings
from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus

pealkiri = Headings()


class PropertiesLayerFunctions:

    def generate_table_from_selected_map_items(self, view_item, layer_name):
        input_layer = QgsProject.instance().mapLayersByName(layer_name)[0]    
        features = input_layer.selectedFeatures()
                        
        headers = [
            Katastriyksus.tunnus, #'TUNNUS', 
            Katastriyksus.hkood, #'MK_kood', 
            Katastriyksus.ov_nimi, #'OV_NIMI', 
            Katastriyksus.ay_nimi,#'AY_NIMI', 
            Katastriyksus.l_aadress, #'L_AADRESS'
            ]

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(headers)
        model.setHorizontalHeaderItem(len(headers), QStandardItem('Address'))
        view_item.setModel(model)
        QCoreApplication.processEvents()
        view_item.verticalHeader().setDefaultSectionSize(20)
        resizer = ColumnResizer(view_item)
        columns = [1, 5]
        column_widths = [125,400]
        resizer.setColumnWidths(columns, column_widths)
        columns_to_hide = [1, 2, 3, 4]
        # Hide the specified columns
        for column_index in columns_to_hide:
            view_item.hideColumn(column_index)

        view_item.verticalHeader().setVisible(False)
        
        view_item.update()  # Refresh the view
        
        # Populate the model with data
        row = 0  # Initialize row index
        main_row = 0
        for feature in features:
            address_value = f"{feature[Katastriyksus.mk_nimi]} {feature[Katastriyksus.ov_nimi]} {feature[Katastriyksus.ay_nimi]} {feature[Katastriyksus.l_aadress]}"

            # Add data to the model
            for idx, field in enumerate(headers):
                item = QStandardItem(str(feature[field]))
                model.setItem(row, idx, item)

            # Add the concatenated 'Address' value to the model
            address_item = QStandardItem(address_value)
            model.setItem(row, len(headers), address_item)
            row += 1

            main_row += 1
            QCoreApplication.processEvents()  # Process events to allow GUI updates
        #print(f"row item: {row_items}")

        
    @staticmethod
    def _create_model_for_selected_map_features(features, fields):
        model = QStandardItemModel()

        # Set the horizontal header labels
        model.setHorizontalHeaderLabels(fields)

        # Add a new 'Address' column
        model.setHorizontalHeaderItem(len(fields), QStandardItem('Address'))

        # Populate the model with data
        for feature in features:
            address_value = f"{feature[Katastriyksus.mk_nimi]} {feature[Katastriyksus.ov_nimi]} {feature[Katastriyksus.ay_nimi]} {feature[Katastriyksus.l_aadress]}"

            # Add data to the model
            for idx, field in enumerate(fields):
                item = QStandardItem(str(feature[field]))
                model.setItem(0, idx, item)

            # Add the concatenated 'Address' value to the model
            address_item = QStandardItem(address_value)
            model.setItem(0, len(fields), address_item)
        return model
