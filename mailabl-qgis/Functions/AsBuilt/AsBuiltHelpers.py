import os
import re
from typing import Optional
from datetime import datetime

from qgis.PyQt.QtWidgets import QFileDialog


from ...utils.DataExtractors.DataExtractors import DataExtractor
from .TableStyle import TableStyle


class AsBuiltHelpers:
    html = ""

    @staticmethod
    def _handle_drawTool(notes_table=True):
        print(f"Notes table value: {notes_table}")
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()

            html = """
            <div style="width: 100%; font-family: Roboto, Arial, sans-serif;">
            """ + AsBuiltHelpers.generate_file_table_section(file_paths)

            if notes_table is True:
                print("Adding notes table")
                html += NotesTableGenerator.generate_empty_table()

            html += """
            </div>
            """

            AsBuiltHelpers.html = html




    def find_existing_file_table(existing_html: str) -> Optional[re.Match]:
        """
        Searches for a table that includes 'Faili nimi' and 'Asukoht' headers.
        Returns the match object or None if no such table is found.
        """
        if not existing_html:
            return None

        table_pattern = re.compile(
            r'(<table[^>]*>.*?<tr[^>]*>.*?Faili nimi.*?Asukoht.*?</tr>)(.*?)(</table>)',
            re.DOTALL | re.IGNORECASE
        )
        return table_pattern.search(existing_html)
    
    @staticmethod
    def find_existing_notes_table_in_html(existing_html: str) -> bool:
        """
        Searches for a table that includes 'Märkused' and 'Kommentaarid' headers.
        Returns the match object or None if no such table is found.
        """
        pattern = re.compile(
            r"""
            <p[^>]*?>\s*(<strong>)?🗒️\s*Märkused\s+ja\s+kommentaarid(</strong>)?\s*</p>  # header line
            \s*<div[^>]*?>\s*<table.*?</table>\s*</div>\s*<p>\s*</p>   # full table block
            """,
            re.DOTALL | re.IGNORECASE | re.VERBOSE
        )

        if pattern.search(existing_html):
            ret = True
        else:
            ret = False
        return ret



    def merge_file_table_with_existing(file_table_html: str, existing_html: str, notes_table=False) -> str:
        if existing_html is None:
            print("➕ No existing HTML — inserting new table.")
            return file_table_html.strip()

        match = AsBuiltHelpers.find_existing_file_table(existing_html)

        if not match:
            print("➕ No matching table found, inserting full new table on top.")
            return f"{file_table_html.strip()}\n\n{existing_html.strip()}"

        table_start, existing_rows, table_end = match.groups()

        existing_links = set(DataExtractor.extract_links_from_description(existing_html))

        new_rows_match = re.search(r"<tbody[^>]*?>(.*?)</tbody>", file_table_html, re.DOTALL | re.IGNORECASE)
        if new_rows_match:
            candidate_rows = re.findall(r"<tr[^>]*>.*?</tr>", new_rows_match.group(1), re.DOTALL)
        else:
            candidate_rows = re.findall(r"<tr[^>]*>.*?</tr>", file_table_html, re.DOTALL)[1:]

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
        updated_html = re.sub(re.escape(match.group(0)), updated_table, existing_html, count=1)

        return updated_html




    @staticmethod
    def generate_file_table_section(file_paths):
        name_col = "35%"
        path_col = "30%"
        note_col = "35%"

        html = f"""
        <p style="font-size: 14px; font-weight: bold; color: {TableStyle.text_color}; margin: 10px 0 4px 6px;">📂 Seotud materjalid</p>
        """

        header = f"""
        <tr>
            {TableStyle.build_header_cell("Faili nimi", name_col, "📄")}
            {TableStyle.build_header_cell("Asukoht", path_col, "📁")}
            {TableStyle.build_header_cell("Märkused", note_col, "📝")}
        </tr>
        """

        rows = ""
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            rows += f"""
            <tr>
                <td style="width: {name_col};">
                    <p>{file_name}</p>
                </td>
                <td style="width: {path_col};">
                    <p><a href="file:///{file_path}" style="font-weight: italic; color: {TableStyle.text_color}; text-decoration: none;">{file_path}</a></p>
                </td>
                <td style="width: {note_col};">
                    <p>–</p>
                </td>
            </tr>
            """

        html += TableStyle.shared_table_wrapper(header + rows)
        html += "<p style='height: 14px;'></p>"
        return html

class NotesTableGenerator:
    DATE_COLUMN_WIDTH = "15%"
    NOTES_COLUMN_WIDTH = "65%"
    CHECKBOX_COLUMN_WIDTH = "5px"
    RESOLVED_COLUMN_WIDTH = "15%"

    @staticmethod
    def _strip_html_tags(text: str) -> str:
        return re.sub(r'</?strong>', '', text, flags=re.IGNORECASE)


    @classmethod
    def _render_checkbox_html(cls, is_checked: bool) -> str:
        checked_attr = 'checked="checked"' if is_checked else ""
        data_checked = str(is_checked).lower()
        return f"""
        <ul data-type="taskList">
            <li data-checked="{data_checked}" data-type="taskItem">
                <label><input type="checkbox" {checked_attr}><span></span></label>
                <div><p></p></div>
            </li>
        </ul>
        """
    @classmethod
    def _render_table_row(cls, note: dict) -> str:
        clean_date = cls._strip_html_tags(note["date"])
        clean_note = cls._strip_html_tags(note["note"])
        clean_resolved_date = cls._strip_html_tags(note["resolved_date"])

        return f"""
        <tr>
            <td style="width: {cls.DATE_COLUMN_WIDTH}; padding: {TableStyle.cell_padding}; text-align: center;">
                <p style="font-weight: normal;">{clean_date}</p>
            </td>
            <td style="width: {cls.NOTES_COLUMN_WIDTH}; padding:{TableStyle.cell_padding}"; text-align: left;>
                <p style="font-weight: normal;">{clean_note}</p>
            </td>
            <td style="width: {cls.CHECKBOX_COLUMN_WIDTH}; padding: {TableStyle.cell_padding}; text-align: center; vertical-align: middle;">
                {cls._render_checkbox_html(note["resolved"])}
            </td>
            <td style="width: {cls.RESOLVED_COLUMN_WIDTH}; padding: {TableStyle.cell_padding}; text-align: center;">
                <p style="font-weight: normal;">{clean_resolved_date}</p>
            </td>
        </tr>
        """
    @classmethod
    def _render_table_header(cls) -> str:
        return f"""
        <tr>
            {TableStyle.build_header_cell("", cls.DATE_COLUMN_WIDTH, "📅")}
            {TableStyle.build_header_cell("Märkus", cls.NOTES_COLUMN_WIDTH, "🗒️")}
            <td style="width: {cls.CHECKBOX_COLUMN_WIDTH}; padding: {TableStyle.header_padding}; background: {TableStyle.header_background}; text-align: center;">
                <p>✅</p>
            </td>
            {TableStyle.build_header_cell("Lahendatud", cls.RESOLVED_COLUMN_WIDTH, "📅")}
        </tr>
        """

    @classmethod
    def _wrap_table(cls, body: str) -> str:
        return f"""
        <!-- mailabl:type=notes -->
        <p style="font-size: 13px; font-weight: bold; color: {TableStyle.text_color}; margin: 14px 0 4px 6px;">🗒️ Märkused ja kommentaarid</p>
        {TableStyle.shared_table_wrapper(body)}
        <p></p>
        """

    @classmethod
    def generate_notes_table_from_data(cls, notes: list) -> str:
        print("📋 Generating notes table from data...")
        print("📄 Notes passed in:", notes)

        if not notes:
            print("📝 No notes provided — creating placeholder empty note row.")
            notes = [{
                "date": "",
                "note": "",
                "resolved": False,
                "resolved_date": ""
            }]
        else:
            print(f"✅ {len(notes)} notes found.")

        rows_html = "".join([cls._render_table_row(note) for note in notes])
        full_table = cls._render_table_header() + rows_html
        final_html = cls._wrap_table(full_table)

        print("✅ Notes table generated.")
        return final_html
  
    @classmethod
    def generate_empty_table(cls) -> str:
        today = datetime.today().strftime("%d.%m.%Y")
        placeholder_note = [{
            "date": today,
            "note": "",
            "resolved": False,
            "resolved_date": ""
        }]
        return cls.generate_notes_table_from_data(placeholder_note)

    @classmethod
    def update_notes_table(cls, notes: list) -> str:
        return cls.generate_notes_table_from_data(notes)

