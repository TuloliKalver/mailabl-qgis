import os
import re

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QDialog, QFrame, QLabel, QCheckBox, QLineEdit, QTextBrowser
    )
from types import MethodType
from qgis.PyQt.QtWidgets import QFileDialog


from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...config.settings import Filepaths, FilesByNames
from ...config.SetupModules.AsBuitSettings import AsBuiltDrawings, DraggableFrame
from ...Functions.AsBuilt.ASBuilt import AsBuiltQueries
from ...utils.DataExtractors.DataExtractors import DataExtractor
from PyQt5.QtCore import QPropertyAnimation

class AsBuiltTools():

    def __init__(self, parent) -> None:
        self.dialog = parent
        

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

        widget.Drawingtool.clicked.connect(lambda: somethinghere._handle_drawTool(widget))

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
            #print("Accepted")
            property_id = "30"
            existing_descriptions = AsBuiltQueries._query_AsBuilt_by_id(property_id=property_id)
            #print(f"Existing descriptions: {existing_descriptions}")
            # 3. Merge: put file table first, then append all descriptions
        
            #res = AsBuiltQueries._update_AsBuilt_by_id(property_id=property_id, description=combined_html)
            
            AsBuiltTools.html = ""

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

class somethinghere:
    def merge_file_table_with_existing(file_table_html: str, existing_html: str) -> str:
        #print("🔍 Merging file table with existing content...")

        table_pattern = re.compile(
            r'(<table[^>]*>.*?<tr[^>]*>.*?Faili nimi.*?Asukoht.*?</tr>)(.*?)(</table>)',
            re.DOTALL | re.IGNORECASE
        )

        match = table_pattern.search(existing_html)
        if match:
            #print("✅ Existing table found (flexible header match), injecting rows...")

            table_start, existing_rows, table_end = match.groups()
         
            # ✅ Correct link extraction
            existing_links = set(DataExtractor.extract_links_from_description(existing_html))
            #print(f"🔎 Existing links: {existing_links}")


            # Try <tbody> first
            new_rows_match = re.search(r"<tbody[^>]*?>(.*?)</tbody>", file_table_html, re.DOTALL | re.IGNORECASE)
            if new_rows_match:
                candidate_rows = re.findall(r"<tr[^>]*>.*?</tr>", new_rows_match.group(1), re.DOTALL)
            else:
                candidate_rows = re.findall(r"<tr[^>]*>.*?</tr>", file_table_html, re.DOTALL)[1:]  # skip header

            unique_rows = []
            for row in candidate_rows:
                link_match = re.search(r'href="file:///([^"]+)"', row, re.IGNORECASE)
                if not link_match:
                    continue
                file_path = link_match.group(1)
                if file_path not in existing_links:
                    unique_rows.append(row)

            if not unique_rows:
                print("⚠️ No unique rows to merge.")
                return existing_html

            new_rows_html = "\n".join(unique_rows)
            print(f"📥 Injecting {len(unique_rows)} new rows.")

            updated_table = f"{table_start}{existing_rows}{new_rows_html}{table_end}"
            updated_html = table_pattern.sub(updated_table, existing_html, count=1)
            return updated_html
        else:
            print("➕ No matching table found, inserting full new table on top.")
            return f"{file_table_html.strip()}\n\n{existing_html.strip()}"



