import os
import re

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QDialog, QLabel, QCheckBox, QTextEdit, QHBoxLayout, QFrame, QLineEdit
from types import MethodType
from qgis.PyQt.QtWidgets import QFileDialog


from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...config.settings import Filepaths, FilesByNames
from ...config.SetupModules.AsBuitSettings import AsBuiltDrawings, DraggableFrame
from ...Functions.AsBuilt.ASBuilt import AsBuiltQueries
from ...utils.DataExtractors.DataExtractors import DataExtractor
from PyQt5.QtCore import QPropertyAnimation

class AsBuiltTools():

    def __init__(self, parent, table) -> None:
        self.dialog = parent
        self.table = table
        

    def load_asBuiltTools(self):
        widget_name = Filepaths._get_widget_name(FilesByNames().asBuitTools_UI)
        widget = Filepaths.load_ui_file(widget_name)
        
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool) #| Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)


        drag_frame = widget.findChild(QFrame, "dragFrame")
        if drag_frame:
            # Inject drag behavior via method patching
            drag_frame.mousePressEvent = MethodType(DraggableFrame.mousePressEvent, drag_frame)
            drag_frame.mouseMoveEvent = MethodType(DraggableFrame.mouseMoveEvent, drag_frame)
            drag_frame._drag_pos = None
            drag_frame.setCursor(Qt.OpenHandCursor)   

        res = self.make_Notes(widget)
        if res == False:
            return 

        widget.pbAddNote.clicked.connect(lambda: self.add_note_row_from_button(widget))

        widget.pbSave.clicked.connect(lambda: AsBuiltTools._handle_save(widget))
        widget.pbCancel.clicked.connect(lambda: AsBuiltTools._handle_cancel(widget))

        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        AsBuiltDrawings.replace_frame(
            widget,
            "FrameMain",
            style=AnimatedGradientBorderFrame.GENTLEMAN,
        )

        result = widget.exec_()

        if result == QDialog.Accepted:

            widget.setAttribute(Qt.WA_DeleteOnClose)
            
            return True
        else:
            widget.setAttribute(Qt.WA_DeleteOnClose)
            return None

    @staticmethod
    def _handle_save(dialog):
        dialog.accept()

    @staticmethod
    def _handle_cancel(dialog):
        dialog.reject()


    def make_Notes(self, widget):
        table = self.table
        #print(f"Table name is {table}")

        selected_indexes = table.selectionModel().selectedRows()
        if not selected_indexes:
            print("❌ No row selected.")
            return False

        selected_row = selected_indexes[0].row()
        model = table.model()
        
        property_id = model.data(model.index(selected_row, 0), Qt.DisplayRole)
        #print("Property ID is:")
        #print(property_id)

        existing_descriptions = AsBuiltQueries._query_AsBuilt_by_id(property_id=property_id)
        #print(f"existing_descriptions")
        #print(existing_descriptions)
        data = self.extract_notes_table_data(existing_descriptions)
        print("Notes data returned!")
        print(data)
        self.add_frame(widget, data)
    def extract_notes_table_data(self, existing_html: str) -> list:
        notes_table_pattern = re.compile(
            r'<p[^>]*?>\s*🗒️ Märkused ja kommentaarid\s*</p>\s*<div[^>]*?>\s*<table[^>]*?>(.*?)</table>',
            re.DOTALL | re.IGNORECASE
        )
        match = notes_table_pattern.search(existing_html)
        if not match:
            return []

        table_html = match.group(1)
        rows = re.findall(r'<tr[^>]*?>(.*?)</tr>', table_html, re.DOTALL)
        data_rows = rows[1:]  # skip header

        td_pattern = re.compile(r'<td[^>]*?>(.*?)</td>', re.DOTALL)

        def clean_cell(cell_html):
            return re.sub(r'<.*?>', '', cell_html).strip()

        def checkbox_checked(cell_html):
            return 'checked' in cell_html.lower()

        parsed_rows = []
        for row_html in data_rows:
            cells = td_pattern.findall(row_html)
            if len(cells) == 4:
                parsed_rows.append({
                    "date": clean_cell(cells[0]),
                    "note": clean_cell(cells[1]),
                    "resolved": checkbox_checked(cells[2]),
                    "resolved_date": clean_cell(cells[3])
                })

        return parsed_rows
    
    

    def add_frame(self, widget, data):
        notes_frame = widget.findChild(QFrame, "frame")
        notes_layout = notes_frame.layout()
        if not notes_layout:
            print("❌ 'Notes' layout not found!")
            return

        # Header row
        headings_frame = QFrame()
        headings_layout = QHBoxLayout()
        headings_layout.setContentsMargins(0, 0, 0, 0)
        headings_layout.setSpacing(10)

        heading_date_label = QLabel("📅 Kuupäev")
        heading_note_label = QLabel("🗒️ Märkus")
        heading_resolved_label = QLabel("✅ Staatus")
        heading_resolved_date_label = QLabel("📅 Lahendatud")

        # Fixed widths for alignment
        heading_date_label.setFixedWidth(100)
        heading_note_label.setFixedWidth(300)
        heading_resolved_label.setFixedWidth(60)
        heading_resolved_date_label.setFixedWidth(100)

        headings_layout.addWidget(heading_date_label)
        headings_layout.addWidget(heading_note_label)
        headings_layout.addWidget(heading_resolved_label)
        headings_layout.addWidget(heading_resolved_date_label)

        headings_frame.setLayout(headings_layout)
        notes_layout.addWidget(headings_frame)

        # Data rows
        for row in data:
            self.add_note_row(notes_layout, row)


    def add_note_row(self, notes_layout, row_data=None):
        frame = QFrame()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        date_text = row_data["date"] if row_data else ""
        note_text = row_data["note"] if row_data else ""
        resolved = row_data["resolved"] if row_data else False
        resolved_date_text = row_data["resolved_date"] if row_data else ""

        date_edit = QLineEdit(date_text)
        date_edit.setFixedWidth(100)

        note_edit = QTextEdit()
        note_edit.setText(note_text)
        note_edit.setFixedWidth(300)
        note_edit.setFixedHeight(50)
        note_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        note_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        checkbox = QCheckBox()
        checkbox.setChecked(resolved)
        checkbox.setFixedWidth(60)
        checkbox.setStyleSheet("margin-left: 8px;")

        resolved_date_edit = QLineEdit(resolved_date_text)
        resolved_date_edit.setFixedWidth(100)

        layout.addWidget(date_edit)
        layout.addWidget(note_edit)
        layout.addWidget(checkbox)
        layout.addWidget(resolved_date_edit)

        frame.setLayout(layout)
        notes_layout.addWidget(frame)

    def add_note_row_from_button(self, widget):
        notes_frame = widget.findChild(QFrame, "frame")
        if not notes_frame:
            print("❌ 'frame' container not found!")
            return

        notes_layout = notes_frame.layout()
        if not notes_layout:
            print("❌ 'Notes' layout not found!")
            return

        self.add_note_row(notes_layout)  # Adds an empty row
