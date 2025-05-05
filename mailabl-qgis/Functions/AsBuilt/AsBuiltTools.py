import os
import re

from PyQt5.QtCore import Qt

from types import MethodType
from .NotesEditor import NotesEditor
from PyQt5.QtWidgets import (
    QDialog,QCheckBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QVBoxLayout, QGroupBox
)

from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...config.settings import Filepaths, FilesByNames
from ...config.SetupModules.AsBuitSettings import AsBuiltDrawings, DraggableFrame
from ...Functions.AsBuilt.ASBuilt import AsBuiltQueries
from ...utils.DataExtractors.DataExtractors import DataExtractor
from PyQt5.QtCore import QPropertyAnimation
from .AsBuiltHelpers import AsBuiltHelpers, NotesTableGenerator

class AsBuiltTools():

    def __init__(self, parent, table) -> None:
        self.dialog = parent
        self.table = table
        self.notes_editor = NotesEditor()        

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

        widget.pbAddNote.clicked.connect(lambda: NotesEditor.add_note_row_from_button(widget))

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
            notes = self.collect_note_data(widget)
            html_notes = NotesTableGenerator.update_notes_table(notes)
            print(f"Updated HTML:\n{html_notes}")
            selected_indexes = self.table.selectionModel().selectedRows()
            if not selected_indexes:
                print("❌ No row selected.")
                return False

            selected_row = selected_indexes[0].row()
            model = self.table.model()
            
            property_id = model.data(model.index(selected_row, 0), Qt.DisplayRole)
            existing_descriptions = AsBuiltQueries._query_AsBuilt_by_id(property_id=property_id)
            print(f"Existing descriptions are:")
            print(existing_descriptions)

            combined_html = self.patch_notes_table_in_html(existing_descriptions, html_notes)
            print(f"Combined HTML:\n{combined_html}")

            res = AsBuiltQueries._update_AsBuilt_by_id(property_id=property_id, description=combined_html)



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

        self.notes_editor.add_frame(widget, data)

    def extract_notes_table_data(self, existing_html: str) -> list:
        #print("🔎 Scanning incoming HTML for notes...")
        #print(f"HTML:\n{existing_html}")
        # Match the full notes table HTML block based on section title + <table>
        notes_table_pattern = re.compile(
            r'🗒️\s*Märkused\s+ja\s+kommentaarid.*?<table[^>]*?>(.*?)</table>',
            re.DOTALL | re.IGNORECASE
        )
        match = notes_table_pattern.search(existing_html)
        if not match:
            print("❌ Notes table not found.")
            return []

        table_html = match.group(1)

        # Match all <tr> blocks (rows)
        rows = re.findall(r'<tr[^>]*?>(.*?)</tr>', table_html, re.DOTALL)
        if not rows or len(rows) <= 1:
            print("⚠️ No note rows found in table.")
            return []

        data_rows = rows[1:]  # skip header row

        td_pattern = re.compile(r'<td[^>]*?>(.*?)</td>', re.DOTALL)

        def clean_cell(cell_html):
            return re.sub(r'<[^>]+>', '', cell_html).strip()

        def checkbox_checked(cell_html: str) -> bool:
            return 'checked="checked"' in cell_html.lower()
        
        parsed_rows = []
        for row_html in data_rows:
            cells = td_pattern.findall(row_html)
            if len(cells) == 4:
                parsed_rows.append({
                    "date": clean_cell(cells[0]),
                    "note": clean_cell(cells[1]),
                    "resolved": checkbox_checked(cells[2]),
                    "resolved_date": clean_cell(cells[3]),
                })

        #print(f"✅ Parsed {len(parsed_rows)} notes from HTML.")
        return parsed_rows
    

    def collect_note_data(self, widget) -> list:
        notes_frame = widget.findChild(QFrame, "frame")
        if not notes_frame:
            print("❌ Notes frame not found!")
            return []

        notes_layout = notes_frame.layout()
        if not notes_layout:
            print("❌ Notes layout not found!")
            return []

        collected_notes = []

        for i in range(notes_layout.count()):
            group_box = notes_layout.itemAt(i).widget()
            if not isinstance(group_box, QGroupBox):
                continue

            date_title = group_box.title().strip()
            note_date = date_title if date_title != "📅 Kuupäev puudub" else ""

            group_layout = group_box.layout()
            if not group_layout:
                continue

            for j in range(group_layout.count()):
                row_frame = group_layout.itemAt(j).widget()
                if not isinstance(row_frame, QFrame):
                    continue

                row_layout = row_frame.layout()
                if not row_layout or row_layout.count() < 3:
                    continue

                note_edit = row_layout.itemAt(0).widget()
                checkbox_container = row_layout.itemAt(1).widget()
                resolved_date_edit = row_layout.itemAt(2).widget()

                if not all([note_edit, checkbox_container, resolved_date_edit]):
                    continue

                # Extract QCheckBox from checkbox_container frame
                checkbox = checkbox_container.findChild(QCheckBox)
                if not checkbox:
                    continue

                row_data = {
                    "date": note_date,
                    "note": note_edit.toPlainText().strip(),
                    "resolved": checkbox.isChecked(),
                    "resolved_date": resolved_date_edit.text().strip()
                }

                collected_notes.append(row_data)

        return collected_notes


    @staticmethod
    def patch_notes_table_in_html(existing_html: str, new_notes_html: str) -> str:
        """
        Replaces the full 'Märkused ja kommentaarid' section, no matter how it's styled.
        Ensures only one block exists.
        """
        pattern = re.compile(
            r"""
            <p[^>]*?>\s*(<strong>)?🗒️\s*Märkused\s+ja\s+kommentaarid(</strong>)?\s*</p>  # header line
            \s*<div[^>]*?>\s*<table.*?</table>\s*</div>\s*<p>\s*</p>   # full table block
            """,
            re.DOTALL | re.IGNORECASE | re.VERBOSE
        )

        if pattern.search(existing_html):
            updated_html = pattern.sub(new_notes_html.strip(), existing_html)
            print("🔁 Replaced existing notes section.")
        else:
            updated_html = existing_html.strip() + "\n" + new_notes_html.strip()
            print("➕ Appended new notes section.")

        return updated_html
