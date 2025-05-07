import os
import re


from qgis.PyQt.QtWidgets import QFileDialog


from ...utils.DataExtractors.DataExtractors import DataExtractor
from .TableStyle import TableStyle


class AsBuiltHelpers:
    html = ""

    @staticmethod
    def _handle_drawTool(notes_table=True):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()

            html = """
            <div style="width: 100%; font-family: Roboto, Arial, sans-serif;">
            """ + AsBuiltHelpers.generate_file_table_section(file_paths)

            if notes_table:
                html += NotesTableGenerator.generate_empty_table()

            html += """
            </div>
            <p></p>
            """

            AsBuiltHelpers.html = html


    def merge_file_table_with_existing(file_table_html: str, existing_html: str) -> str:
        #print("🔍 Merging file table with existing content...")
        print(f"Existing_html value: {existing_html}")
        if existing_html == None:
            print("➕ No matching table found, inserting full new table on top.")
            return f"{file_table_html.strip()}"


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


        if not notes:
            notes = [{
                "date": "",
                "note": "",
                "resolved": False,
                "resolved_date": ""
            }]
        rows_html = "".join([cls._render_table_row(note) for note in notes])
        full_table = cls._render_table_header() + rows_html
        return cls._wrap_table(full_table)

    @classmethod
    def generate_empty_table(cls) -> str:
        return cls.generate_notes_table_from_data([])

    @classmethod
    def update_notes_table(cls, notes: list) -> str:
        return cls.generate_notes_table_from_data(notes)

