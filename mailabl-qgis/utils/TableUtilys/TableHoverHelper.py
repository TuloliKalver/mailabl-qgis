from PyQt5.QtCore import QObject, QTimer, Qt, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QTableView, QDialog, QVBoxLayout, QTextBrowser, QToolTip

from ...KeelelisedMuutujad.TableHeaders import HeaderKeys
from ...utils.TableUtilys.TableHelpers import TableExtractor
from .TableHEaderIndexMap import HeaderIndexMap
from ...Functions.Coordinations.Coordinations import CoordinationsMain
from ...queries.python.projects_pandas import ProjectsQueries
from ...Functions.AsBuilt.ASBuilt import AsBuiltMain
from ...Functions.Contracts.Contracts import ContractsMain
from ...Functions.Easements.Easements import EasementssMain
from ...KeelelisedMuutujad.modules import Module


class TableHoverWatcher(QObject):
    def __init__(self, module, table: QTableView, delay_ms=500):
        super().__init__(table)
        self.table = table
        self.module = module
        self.timer = QTimer()
        self.timer.setInterval(delay_ms)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self._on_hover_triggered)
        self.last_row = None
        self.active_popup = None

        table.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == event.MouseMove:
            index = self.table.indexAt(event.pos())
            if index.isValid():
                row = index.row()
                if row != self.last_row:
                    self.last_row = row
                    self.timer.start()
                    self._close_popup()
            else:
                self.timer.stop()
                self._close_popup()
                self.last_row = None

        elif event.type() == event.Leave:
            self.timer.stop()
            self._close_popup()
            self.last_row = None

        return super().eventFilter(obj, event)

    def _on_hover_triggered(self):
        if self.last_row is None:
            return

        model = self.table.model()
        headers = TableExtractor._extract_headers_from_model(model)
        language = "et"
        idx_map = HeaderIndexMap(headers, language)

        # pick which headers to show based on module
        if self.module == Module.COORDINATION:
            keys = {
                "id": HeaderKeys.HEADER_ID,
                "number": HeaderKeys.HEADER_NUMBER,
                "deadline": HeaderKeys.HEADER_DEADLINE,
                "responsible": HeaderKeys.HEADER_RESPONSIBLE,
            }

        else:
            # fallback minimal display
            keys = {
                "id": HeaderKeys.HEADER_ID,
                "title": HeaderKeys.HEADER_NAME,
                "start": HeaderKeys.HEADER_DEADLINE,
                "manager": HeaderKeys.HEADER_RESPONSIBLE,
            }

        # build index lookup
        index_dict = {
            name: model.index(self.last_row, idx_map[hk])
            for name, hk in keys.items()
        }
        data = {
            name: model.data(idx) or ""
            for name, idx in index_dict.items()
        }

        # Now pull in the detail rows + terms
        id_value = data.get("id")
        
        if self.module == Module.COORDINATION:
            table_rows = CoordinationsMain.load_coordinations_details(id_value)
            colspan = "6"
        elif self.module == Module.ASBUILT:
            colspan = "4"
            table_rows = AsBuiltMain.load_asBuilt_details(id_value)
        elif self.module == Module.PROJECT:
            table_rows = ProjectsQueries._fetch_projects_details(id_value)
            colspan = "6"
        elif self.module == Module.CONTRACT:
            table_rows = ContractsMain._query_contract_details(id_value)
            colspan = "6"
        elif self.module == Module.EASEMENT:
            table_rows = EasementssMain.load_easements_details(id_value)
            colspan = "4"
        else:
            print("Unknown module:", self.module)
            colspan = "2"
            table_rows = "", ""

        # Build HTML message
        message = f"""
        <div style="
            font-family: 'Segoe UI', Roboto, sans-serif;
            font-size: 13px;
            color: #e0e0e0;
            background-color: #2e2e2e;
            padding: 10px 14px;
            border-radius: 10px;
            border: 1px solid #4a90e2;
            box-shadow: 0 0 12px rgba(74, 144, 226, 0.4);
            line-height: 1.6;
        ">
            <div style="font-size: 15px; font-weight: bold; color: #4ecdc4;">
                👀 Mis siin peidus on?
            </div>
        """
        print(f"Setting overall colsmap to {colspan}")
        message += f"""
        <div style="margin-top:6px;">
        <table border="0" cellspacing="0" cellpadding="4" width="100%"
            style="border-color:#444;
                    font-family:'Segoe UI';
                    font-size:12px;">
        <tr>
            <td colspan="{colspan}" style="height:1px; background-color:#444; padding:0; cellpadding:0;"></td>
        </tr>
        {table_rows}
        </table>
        </div>
        """

        # show the popup
        global_pos = QCursor.pos()
        self._close_popup()
        self.active_popup = HoverPopup(message, self.table)
        self.active_popup.move(global_pos + QPoint(12, 12))
        self.active_popup.show()
        self.active_popup.adjustSize()

        popup_size = self.active_popup.size()
        mouse_pos = QCursor.pos()
        x = mouse_pos.x() - (popup_size.width() // 2)
        y = mouse_pos.y() + 16

        screen_geom = self.table.screen().geometry()
        if y + popup_size.height() > screen_geom.bottom():
            y = mouse_pos.y() - popup_size.height() - 16

        self.active_popup.move(QPoint(x, y))

    def _close_popup(self):
        if self.active_popup:
            self.active_popup.close()
            self.active_popup = None


class HoverPopup(QDialog):
    def __init__(self, message: str, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.ToolTip)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)

        self.browser = QTextBrowser()
        self.browser.setFocusPolicy(Qt.NoFocus)
        self.browser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.browser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.browser.setOpenExternalLinks(True)
        self.browser.setStyleSheet("""
            QTextBrowser {
                background-color: #2c2c2c;
                color: white;
                border: 1px solid #4a90e2;
                border-radius: 6px;
                padding: 6px;
                font-size: 12px;
            }
        """)
        self.browser.setHtml(message)
        layout.addWidget(self.browser)

        # force reflow to compute height
        self.browser.document().setTextWidth(self.browser.viewport().width())
        doc_height = self.browser.document().size().height()
        buffer = 20
        total_height = int(doc_height + buffer)

        #print(f"Doc Height: {doc_height} → Total: {total_height}")
        self.browser.setMinimumHeight(total_height)
        self.browser.setMinimumWidth(600)
        self.adjustSize()
