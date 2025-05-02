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
            # 1. Get current QTextBrowser content (your file table)
            prepared_text = somethinghere.prepare_description_from_textbrowser(widget.textBrowser)
            #print(f"Textbrowser content: {prepared_text}")
            # 2. Fetch descriptions from Mailabl (already done)
            existing_descriptions = AsBuiltQueries._query_AsBuilt_by_id(property_id=property_id)
            #print(f"Existing descriptions: {existing_descriptions}")
            # 3. Merge: put file table first, then append all descriptions
            #combined_html = prepared_text.strip()
            combined_html = prepared_text + "\n\n" + existing_descriptions
            #combined_html = somethinghere.merge_file_table_with_existing(prepared_text, existing_descriptions)


            res = AsBuiltQueries._update_AsBuilt_by_id(property_id=property_id, description=combined_html)
            # 4. Preview the result
            #print("✅ Final prepared HTML to save:\n")
            #print(combined_html)



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
    def _handle_drawTool(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        #file_dialog.setNameFilter("Shapefiles (*.shp)")
        if file_dialog.exec_():
                file_paths = file_dialog.selectedFiles()
                text_browser = self.textBrowser
                text_browser.clear()


        html = """
        <!-- mailabl:type=joonised -->
        <table border="0" cellspacing="0" cellpadding="3" width="100%">
            <thead>
                <tr>
                    <th align="left"><p>Faili nimi</p></th>
                    <th align="left"><p></p></th>
                    <th align="left"><p>Asukoht</p></th>
                </tr>
            </thead>
            <tbody>
        """


        for file_path in file_paths:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            html += f"""
            <tr>
                <td><p><b>{file_name}</b></p></td>
                <td><p>📁</p></td>
                <td><p><a href="file:///{file_path}">{file_path}</a></p></td>
            </tr>
            """

        html += """
            </tbody>
        </table>
        <p></p>
        """
        text_browser.setHtml(html)



    @staticmethod
    def prepare_description_from_textbrowser(text_browser: QTextBrowser) -> str:
        """
        Extracts and cleans inner HTML content from QTextBrowser (no <html><body> wrapper).
        Safe for saving in QGIS environments.
        """
        raw_html = text_browser.toHtml().strip()

        # Try to extract only what’s inside <body> if it exists
        body_match = re.search(r"<body[^>]*>(.*?)</body>", raw_html, re.DOTALL | re.IGNORECASE)
        if body_match:
            inner_html = body_match.group(1).strip()
        else:
            inner_html = raw_html  # fallback

        return inner_html

    @staticmethod
    def merge_file_table_with_existing(prepared_text: str, existing_descriptions: list[str]) -> str:
        # Clean leading/trailing whitespace from browser content
        prepared_html = prepared_text.strip()
        merged_parts = [prepared_html]

        for desc in existing_descriptions:
            desc_clean = desc.strip()

            if desc_clean and desc_clean != prepared_html:
                # Don't add empty or duplicate descriptions
                merged_parts.append(desc_clean)

        return "\n\n".join(merged_parts)