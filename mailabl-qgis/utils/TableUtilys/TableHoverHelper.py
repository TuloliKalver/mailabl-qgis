from PyQt5.QtCore import QObject, QTimer, Qt, QPoint
from PyQt5.QtGui import QCursor, QTextOption
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QTextBrowser
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys
from ...utils.TableUtilys.TableHelpers import  TableExtractor
from .TableHEaderIndexMap import HeaderIndexMap
from ...Functions.Coordinations.Coordinations import CoordinationsMain

class TableHoverWatcher(QObject):
    def __init__(self, table: QTableView, delay_ms=500):
        super().__init__(table)
        self.table = table
        self.timer = QTimer()
        self.timer.setInterval(delay_ms)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self._on_hover_triggered)
        self.last_row = None
        self.active_popup = None  # 👈 Track the currently shown popup

        table.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == event.MouseMove:
            index = self.table.indexAt(event.pos())
            if index.isValid():
                row = index.row()
                if row != self.last_row:
                    self.last_row = row
                    self.timer.start()
                    self._close_popup()  # 👈 close old popup on new move
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

        # Get indexes of the fields we want to show
        try:
            model = self.table.model()
            header_labels = TableExtractor._extract_headers_from_model(model)
            language = "et"
            index_map = HeaderIndexMap(header_labels, language)

            id_index = self.table.model().index(self.last_row, index_map[HeaderKeys.HEADER_ID])
            number_index = self.table.model().index(self.last_row, index_map[HeaderKeys.HEADER_NUMBER])
            deadline_index = self.table.model().index(self.last_row, index_map[HeaderKeys.HEADER_DEADLINE])
            responsible_index = self.table.model().index(self.last_row, index_map[HeaderKeys.HEADER_RESPONSIBLE])

        
        except Exception as e:
            print(f"⚠️ Failed to get index map values: {e}")
            return

        # Extract the data from model
        id_value = self.table.model().data(id_index, Qt.DisplayRole)

        #print (f"notes_text: {notes_text}")
        #print(f" terms_text: {terms_text}")
        number = self.table.model().data(number_index, Qt.DisplayRole)
        deadline = self.table.model().data(deadline_index, Qt.DisplayRole)
        responsible = self.table.model().data(responsible_index, Qt.DisplayRole)


        table_rows, desc_and_terms = CoordinationsMain.load_coordinations_details(id_value)

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
                👀 Mis siin peidus on
            </div>
            <hr style="border: 0; height: 1px; background: #4a90e2; margin: 6px 0;" />
            
            <div style="margin-top: 6px;">
                 {table_rows}
            </div>
            <div>
                {desc_and_terms}
            </div>
        </div>
        """


        #print("📌 Hover Info:\n", message)

        global_pos = QCursor.pos()
        self._close_popup()
        self.active_popup = HoverPopup(message, self.table)
        self.active_popup.move(global_pos + QPoint(12, 12))  # slight offset to avoid overlapping
        self.active_popup.show()
        
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

        # ✅ Force layout update
        self.browser.document().setTextWidth(self.browser.viewport().width())
        self.browser.document().adjustSize()

        # Get document height and add a small buffer
        doc_height = self.browser.document().size().height()
        buffer = 20  # adjust as needed for safety margin
        total_height = int(doc_height + buffer)

        # Optionally print it
        print(f"Doc Height: {doc_height} → Total: {total_height}")

        # Set minimum/maximum heights based on calculated value
        self.browser.setMinimumHeight(total_height)
        self.browser.setMinimumWidth(600)
        
        self.adjustSize()