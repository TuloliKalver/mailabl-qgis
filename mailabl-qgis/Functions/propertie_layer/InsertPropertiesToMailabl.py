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
        
        total = len(features)
        paths = PathLoader(plugin_dir_path, UI_multiline_Statusbar)
        
        widget = paths.UI_multiline_Statusbar
        widget_path = paths.get_widgets_path(widget)
        progress_widget = loadUi(widget_path)
        progress_bar = progress_widget.testBar
        progress_bar.setMaximum(total)  # Set the maximum value of the progress bar
        progress_widget.setWindowTitle("Koostan kinnistute nimekirja!")
        progress_widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        progress_widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        progress_widget.setAttribute(Qt.WA_TranslucentBackground)
        progress_widget.setAttribute(Qt.WA_DeleteOnClose)
        progress_widget.show()
                        
        quarter_point = total // 4  # Calculate the quarter point
        halfway_point = total // 2  # Calculate the halfway point
        three_quarter_point = total * 3 // 4  # Calculate the three-quarter point
        
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
            progress_bar.setValue(main_row)
            # Update the label content at different progress points
            if row == quarter_point:
                progress_widget.label_2.setText("Kas teadsid, et:")
                progress_widget.label_3.setText("98% meie kodumaa jõgedest on joogikõlbuliku veega")
                
            elif row == halfway_point:
                progress_widget.label_3.setText("Eestis on 56-s linnatüüpi asulat")
            elif row == three_quarter_point:
                progress_widget.label_3.setText("Inimese keha sisaldab 65% vett.")
            QCoreApplication.processEvents()  # Process events to allow GUI updates
        #print(f"row item: {row_items}")

        progress_widget.close() 

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
