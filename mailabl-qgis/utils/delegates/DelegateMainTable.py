# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module
import webbrowser
import requests
from PyQt5.QtGui import QColor, QBrush, QPen, QIcon
from PyQt5.QtCore import Qt, QRect, QRectF
from PyQt5.QtWidgets import QStyledItemDelegate
from ...queries.python.projects_pandas import  ProjectsQueries
from ...Functions.Easements.EasementsWhere import getEasementsWhere
from ...Functions.item_selector_tools import properties_selectors
from ...queries.python.ContractWhere import getContractsWhere                    
from ...config.iconHandler import iconHandler
from ...config.settings import Filepaths, IconsByName, OpenLink, MailablWebModules
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...utils.TableUtilys.TableHelpers import TableExtractor

class CustomRoles:
    # custom roles for the delegate to use in the view
    BackgroundColor = Qt.UserRole + 10
    ForegroundColor = Qt.UserRole + 20
    TooltipText = Qt.UserRole + 30
    StatusValue = Qt.UserRole + 40


class DelegateHelpers:

    def icon_setter_for_delegate(painter, icon, option):
        painter.save()
        painter.setRenderHint(painter.Antialiasing)
        # Icon size and position
        icon_size = min(option.rect.width(), option.rect.height()) - 4
        x = option.rect.x() + (option.rect.width() - icon_size) // 2
        y = option.rect.y() + (option.rect.height() - icon_size) // 2
        icon_rect = QRect(x, y, icon_size, icon_size)
        # Paint the icon
        icon.paint(painter, icon_rect, Qt.AlignCenter)
        painter.restore()

class FancyStatusDelegate(QStyledItemDelegate):
    def __init__(self, color_column_index, parent=None):
        super().__init__(parent)
        self.color_column_index = color_column_index

    def paint(self, painter, option, index):
        color_index = index.model().index(index.row(), self.color_column_index)
        color_code = color_index.data(Qt.DisplayRole)
        text = index.data(Qt.DisplayRole)

        if color_code:
            from ..ColorUtils import ColorUtils

            padding_x = 5
            padding_y = 3
            rect = option.rect.adjusted(padding_x, padding_y, -padding_x, -padding_y)
            radius = rect.height() * 0.35

            rgb = ColorUtils.hex_to_rgb(color_code)
            halo = ColorUtils.soften_edge(rgb)
            text_color = ColorUtils._get_text_color_for_background(rgb)

            from PyQt5.QtGui import QRadialGradient

            center_x = rect.x() + rect.width() * 0.89
            center_y = rect.y() + rect.height() * 0.23
            
            gradient = QRadialGradient(center_x, center_y, radius)

            #gradient = QRadialGradient(rect.center().x() + 10, rect.center().y() -10, rect.width() * 0.6)
            gradient.setColorAt(0, QColor(*rgb))
            gradient.setColorAt(1, QColor(*halo))

            # 🎯 Second glow — bottom left (opposite side)
            center_x2 = rect.x() + rect.width() * 0.11
            center_y2 = rect.y() + rect.height() * 0.77
            gradient2 = QRadialGradient(center_x2, center_y2, radius)
            gradient2.setColorAt(0, QColor(*rgb))
            gradient2.setColorAt(1, QColor(*halo))

            painter.save()
            painter.setRenderHint(painter.Antialiasing)
            painter.setBrush(QBrush(gradient))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(QRectF(rect), radius, radius)

            painter.setPen(QPen(text_color))
            text_rect = rect.adjusted(8, 1, -8, -1)
            painter.drawText(text_rect, Qt.AlignCenter, text)
            painter.restore()
        else:
            super().paint(painter, option, index)

class FileDelegate(QStyledItemDelegate):
    def __init__(self, file_column_index, parent=None):
        super().__init__(parent)
        self.file_column_index = file_column_index

    def paint(self, painter, option, index):
        # Get file path from data source column
        file_index = index.model().index(index.row(), self.file_column_index)
        file_path = file_index.data(Qt.DisplayRole)

        if file_path:
            icon = QIcon(iconHandler.set_document_icon_based_on_item(file_path))
            DelegateHelpers.icon_setter_for_delegate(painter, icon, option)
        else:
            super().paint(painter, option, index)
    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease and event.button() == Qt.LeftButton:
            file_index = model.index(index.row(), self.file_column_index)
            file_path = file_index.data(Qt.DisplayRole)
            if file_path:
                self.open_folder_in_local_file_browser(file_path)
                return True
        return super().editorEvent(event, model, option, index)
    def open_folder_in_local_file_browser(self, file_path):
        import subprocess
        subprocess.Popen(['explorer', file_path.replace('/', '\\')], shell=True)

class SelectByModuleElementsOnMapDelegate(QStyledItemDelegate):
    def __init__(self, ID_column_index, parent=None, module=None, properties_column_index=None):
        super(SelectByModuleElementsOnMapDelegate, self).__init__(parent)
        self.ID_column_index = ID_column_index
        self.module = module
        self.properties_column_index = properties_column_index
        
        
    def paint(self, painter, option, index):
        # Get file path from data source column
        idx = index.model().index(index.row(), self.properties_column_index)
        has_value = idx.data(Qt.DisplayRole)

        if has_value:
            icon = QIcon(Filepaths.get_icon(IconsByName().icon_show_on_map))
            DelegateHelpers.icon_setter_for_delegate(painter, icon, option)
        else:
            super().paint(painter, option, index)


    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                id_value = str(model.data(model.index(index.row(), self.ID_column_index), Qt.DisplayRole))
                if id_value != None:
                    if self.module == MailablWebModules.PROJECTS:
                        values = ProjectsQueries.query_projects_related_properties(self, id_value)
                    elif self.module == MailablWebModules.CONTRACTS:
                        values = getContractsWhere.query_contracts_related_properties(self, id_value)
                    elif self.module == MailablWebModules.EASEMENTS:
                        values = getEasementsWhere().query_easement_related_properties(self, id_value)
                    else:
                        return False
                    layer_type = "active"
                    properties_selectors.show_connected_properties_on_map(values, layer_type)
                    return True
                return False
        return super().editorEvent(event, model, option, index)

class OpenMailablItemByModule(QStyledItemDelegate):
    def __init__(self, id_column_index, parent=None, module=None):
        super(OpenMailablItemByModule, self).__init__(parent)
        self.id_column_index = id_column_index
        self.module = module

    def paint(self, painter, option, index):
        # Get file path from data source column
        id_index = index.model().index(index.row(), self.id_column_index)
        id = id_index.data(Qt.DisplayRole)

        if id:
            icon = QIcon(Filepaths.get_icon(IconsByName().Mailabl_icon_name))

            DelegateHelpers.icon_setter_for_delegate(painter, icon, option)
            
        else:
            super().paint(painter, option, index)

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                id_value = model.data(model.index(index.row(), self.id_column_index), Qt.DisplayRole)
                self.open_mailabl_item(id_value)
                return True
        return super().editorEvent(event, model, option, index)
    def open_mailabl_item(self, id):
        web_link = OpenLink.weblink_by_module(self.module)
        link = f"{web_link}{id}"
        response = requests.get(link, verify=False)
        webbrowser.open(response.url)

class DelegatesForTables():
    @staticmethod
    def setup_delegates_by_module(table, header_labels, module, language="et"):
        display_headers = TableHeaders_new(language)
    
        ID_column_index = header_labels.index(display_headers[HeaderKeys.HEADER_ID])
        webButton_Column_index = header_labels.index(display_headers[HeaderKeys.HEADER_WEB_LINK_BUTTON])
        dokAddress_column_index = header_labels.index(display_headers[HeaderKeys.HEADER_DOCUMENTS])
        cadastralButton_Column_index = header_labels.index(display_headers[HeaderKeys.HEADER_PROPERTIES_ICON])
        dokButton_column_index = header_labels.index(display_headers[HeaderKeys.HEADER_FILE_PATH])
        status_column_index = header_labels.index(display_headers[HeaderKeys.HEADER_STATUSES])
        color_column_index = header_labels.index(display_headers[HeaderKeys.COLOR_NAME])
        properties_column_index = header_labels.index(display_headers[HeaderKeys.HEADER_PROPERTY_NUMBER])

        show_onMap_delegate = SelectByModuleElementsOnMapDelegate(ID_column_index, table, module, properties_column_index)
        table.setItemDelegateForColumn(cadastralButton_Column_index, show_onMap_delegate)

        web_link_delegate = OpenMailablItemByModule(ID_column_index, table, module)
        table.setItemDelegateForColumn(webButton_Column_index, web_link_delegate)

        file_delegate = FileDelegate(dokAddress_column_index, table)
        table.setItemDelegateForColumn(dokButton_column_index, file_delegate)

        table.setItemDelegateForColumn(status_column_index, FancyStatusDelegate(color_column_index))
