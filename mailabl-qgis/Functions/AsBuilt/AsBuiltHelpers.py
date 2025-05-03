import os
import re

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QDialog, QFrame, QLabel, QCheckBox, QLineEdit, QTextBrowser
    )
from qgis.PyQt.QtWidgets import QFileDialog


from ...utils.DataExtractors.DataExtractors import DataExtractor



class AsBuiltHelpers:
    html = ""

    @staticmethod
    def generate_file_table_section(file_paths):
        name_col = "35%"
        path_col = "30%"
        note_col = "35%"

        html = f"""
        <p style="font-size: 14px; font-weight: bold; color: #243a4e; margin: 10px 0 4px 6px;">📂 Seotud materjalid</p>
        <div style="display: flex; justify-content: center;">
        <table style="
            border-collapse: collapse;
            width: 90%;
            background-color: #dfe3e1;
            border-radius: 6px;
            box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.15);
            transition: all 0.3s ease-in-out;
            text-align: left;">
            <tr>
                <td style="font-weight: bold; font-size: 12px; padding: 2px 3px; width: {name_col}; color: white; background: #47a5b1;">
                    <p><strong>📄 Faili nimi</strong></p>
                </td>
                <td style="font-weight: bold; font-size: 12px; padding: 2px 3px; width: {path_col}; color: white; background: #47a5b1;">
                    <p><strong>📁 Asukoht</strong></p>
                </td>
                <td style="font-weight: bold; font-size: 12px; padding: 2px 3px; width: {note_col}; color: white; background: #47a5b1;">
                    <p><strong>📝 Märkused</strong></p>
                </td>
            </tr>
        """
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            html += f"""
            <tr>
                <td style="padding: 1px 10px; background-color: #dfe3e1; color: #243a4e; width: {name_col};">
                    <p>{file_name}</p>
                </td>
                <td style="padding: 1px 10px; background-color: #dfe3e1; width: {path_col};">
                    <p><a href="file:///{file_path}" style="font-weight: italic; color: #243a4e; text-decoration: none;">{file_path}</a></p>
                </td>
                <td style="padding: 1px 10px; background-color: #dfe3e1; color: #4f636f; width: {note_col};">
                    <p>–</p>
                </td>
            </tr>
            """
        html += """
        </table>
        </div>
        <p style="height: 14px;"></p>
        """
        return html


    @staticmethod
    def generate_notes_table():
        date_column = "15%"
        notes_column = "65%"
        checkbox_column = "5%"
        resolved_column = "15%"

        return f"""
        <p style="font-size: 13px; font-weight: bold; color: #243a4e; margin: 14px 0 4px 6px;">🗒️ Märkused ja kommentaarid</p>
        <div style="display: flex; justify-content: center;">
            <table style="
                border-collapse: collapse;
                width: 90%;
                table-layout: fixed;
                background-color: #dfe3e1;
                border-radius: 6px;
                box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.15);
                transition: all 0.3s ease-in-out;
                text-align: left;">
                <tr>
                    <td style="width: {date_column}; font-weight: bold; font-size: 12px; padding: 2px 3px; color: white; background: #47a5b1;">
                        <p><strong>📅</strong></p>
                    </td>
                    <td style="width: {notes_column}; font-weight: bold; font-size: 12px; padding: 2px 3px; color: white; background: #47a5b1;">
                        <p><strong>🗒️ Märkus</strong></p>
                    </td>
                    <td style="width: {checkbox_column}; padding: 2px 3px; background: #47a5b1;">
                        <p>✅</p>
                    </td>
                    <td style="width: {resolved_column}; font-weight: bold; font-size: 12px; padding: 2px 3px; color: white; background: #47a5b1;">
                        <p><strong>📅 Lahendatud</strong></p>
                    </td>
                </tr>
                <tr>
                    <td style="width: {date_column}; padding: 1px 10px; background-color: #dfe3e1; color: #243a4e;">01.01.2022</td>
                    <td style="width: {notes_column}; padding: 1px 10px; background-color: #dfe3e1; color: #243a4e;">Suur märkus, sest siin on jama</td>
                    <td style="width: {checkbox_column}; padding: 1px 10px; background-color: #dfe3e1;">
                        <ul data-type="taskList">
                            <li data-checked="false" data-type="taskItem">
                                <label><input type="checkbox"><span></span></label>
                            </li>
                        </ul>
                    </td>
                    <td style="width: {resolved_column}; padding: 1px 10px; background-color: #dfe3e1; color: #4f636f;"></td>
                </tr>
            </table>
        </div>
        <p></p>
        """

    def _handle_drawTool(self, notes_table=True):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()

            html = """
            <div style="width: 100%; font-family: Roboto, Arial, sans-serif;">
            """ + AsBuiltHelpers.generate_file_table_section(file_paths)

            if notes_table:
                html += AsBuiltHelpers.generate_notes_table()

            html += """
            </div>
            <p></p>
            """

            AsBuiltHelpers.html = html




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





