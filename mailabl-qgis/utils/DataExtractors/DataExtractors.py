#utils/DataExtractors/DataExtractor.py

import re


from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...KeelelisedMuutujad.modules import Module
from datetime import datetime

class DataExtractor:
    def __init__(self):
        pass

    @staticmethod
    def extract_row_data_from_node(node: dict, language="et", page_info=None, module=None) -> dict:
        TableHeaders_new(language)
        properties = node.get("properties", {}).get("edges", [])
        cadastral_numbers = [prop["node"].get("cadastralUnitNumber", "") for prop in properties]
        if page_info:
            properties_page_info = node.get("properties",{}).get('pageInfo',{})   
        responsibles = node.get("responsible", {}).get("edges", [])
        responsible_names = [r["node"].get("displayName", "") for r in responsibles]
        status = node.get("status", {})

        def safe(value):
            return value if value is not None else ""


        if module == Module.ASBUILT:
            description = safe(node.get("description"))
            due_at = DataExtractor.date_converter(node)

            headers = {
                HeaderKeys.HEADER_ID: safe(node.get("id")),
                HeaderKeys.HEADER_PARENT_ID: safe(node.get("parentID")),
                HeaderKeys.HEADER_TYPE: safe((node.get("type") or {}).get("name")),
                HeaderKeys.HEADER_FLAG: safe((node.get("priority") or "").lower()),
                HeaderKeys.HEADER_NAME: safe(node.get("name") or node.get("title")),
                HeaderKeys.HEADER_DEADLINE: safe(due_at),
                HeaderKeys.HEADER_STATUSES: safe((status or {}).get("name")),
                HeaderKeys.COLOR_NAME: safe((status or {}).get("color")),
                HeaderKeys.HEADER_PROPERTY_NUMBER: ", ".join(cadastral_numbers) if cadastral_numbers else "",
                HeaderKeys.HEADER_PROPERTIES_ICON: "",
                HeaderKeys.HEADER_WEB_LINK_BUTTON: "",
                HeaderKeys.HEADER_DOCUMENTS: safe(DataExtractor.extract_links_from_description(description)),
                HeaderKeys.HEADER_FILE_PATH: "",
                HeaderKeys.HEADER_RESPONSIBLE: ", ".join(responsible_names) if responsible_names else "",
            }


            return headers

        if module == Module.COORDINATION:
            
            due_at = DataExtractor.date_converter(node)
            names = DataExtractor.get_responsible_for_coordinations(node)
            headers = {
                    HeaderKeys.HEADER_ID: safe(node.get("id")),
                    HeaderKeys.HEADER_PARENT_ID: safe(node.get("parentID")),
                    HeaderKeys.HEADER_NUMBER: safe(node.get("number")) or safe((node.get("type") or {}).get("name")),
                    HeaderKeys.HEADER_TYPE: safe((node.get("type") or {}).get("name")),
                    HeaderKeys.HEADER_JOB_NUMBER: safe(node.get("jobNumber")),
                    HeaderKeys.HEADER_JOB_NAME: safe(node.get("jobName")),
                    HeaderKeys.HEADER_DEADLINE: safe(due_at),
                    HeaderKeys.HEADER_STATUSES: safe(status.get("name")) if status else "",
                    HeaderKeys.COLOR_NAME: safe(status.get("color")) if status else "",
                    HeaderKeys.HEADER_PROPERTY_NUMBER: ", ".join(cadastral_numbers) if cadastral_numbers else "",
                    HeaderKeys.HEADER_PROPERTIES_ICON: "",
                    HeaderKeys.HEADER_WEB_LINK_BUTTON: "",
                    HeaderKeys.HEADER_DOCUMENTS: safe(node.get("filesPath")),
                    HeaderKeys.HEADER_FILE_PATH: "",
                    HeaderKeys.HEADER_RESPONSIBLE: ", ".join(names) if names else "",
                }
            
            return headers


        else:
            due_at = safe(DataExtractor.date_converter(node))

            headers = {
                HeaderKeys.HEADER_ID: safe(node.get("id")),
                HeaderKeys.HEADER_PARENT_ID: safe(node.get("parentID")),
                HeaderKeys.HEADER_NUMBER: safe(node.get("number")) or safe((node.get("type") or {}).get("name")),
                HeaderKeys.HEADER_NAME: safe(node.get("name")) or safe(node.get("title")),
                HeaderKeys.HEADER_DEADLINE: due_at,
                HeaderKeys.HEADER_STATUSES: safe(status.get("name")) if status else "",
                HeaderKeys.COLOR_NAME: safe(status.get("color")) if status else "",
                HeaderKeys.HEADER_PROPERTY_NUMBER: ", ".join(cadastral_numbers) if cadastral_numbers else "",
                HeaderKeys.HEADER_PROPERTIES_ICON: "",
                HeaderKeys.HEADER_WEB_LINK_BUTTON: "",
                HeaderKeys.HEADER_DOCUMENTS: safe(node.get("filesPath")),
                HeaderKeys.HEADER_FILE_PATH: "",
                HeaderKeys.HEADER_RESPONSIBLE: ", ".join(responsible_names) if responsible_names else "",
            }
            
            return headers

    @staticmethod
    def extract_links_from_description(description: str) -> list:
        """
        Extract links from a <table> that contains headers 'Faili nimi' and 'Asukoht'.
        It works even if the tags use <td> or have nested elements like <strong> or <span>.
        """
        #print("===== START EXTRACTING LINKS =====")
        if not description or "Faili nimi" not in description or "Asukoht" not in description:
            #print("❌ Header markers not found.")
            return []

        #print("✅ Recognized table header structure...")
        #print(f"Description: {description[:300]}...")  # trimmed for readability

        # Find all tables
        table_blocks = re.findall(r"<table.*?>.*?</table>", description, re.DOTALL | re.IGNORECASE)

        for table in table_blocks:
            if "Faili nimi" in table and "Asukoht" in table:
                #print("✅ Matched a valid table.")
                td_pattern = re.compile(r"<td[^>]*>(.*?)</td>", re.DOTALL | re.IGNORECASE)
                td_matches = td_pattern.findall(table)

                links = []
                for td in td_matches:
                    # Strip HTML tags inside the <td> cell
                    clean_text = re.sub(r"<.*?>", "", td).strip()
                    if clean_text and ("file:///" in clean_text or "\\" in clean_text or "/" in clean_text):
                        links.append(clean_text)

                #print(f"✅ Extracted links: {links}")
                return links

        #print("❌ Matching table not found.")
        return []





    def date_converter(node:dict):
        #print("date converter:", node)
        raw_due_at = node.get("dueAt", "")
        # Unpack if it's a tuple like ('2022-07-21',)
        if isinstance(raw_due_at, tuple) and raw_due_at:
            raw_due_at = raw_due_at[0]

        # Try to format if it's a valid date string
        try:
            due_at = datetime.strptime(raw_due_at, "%Y-%m-%d").strftime("%d.%m.%Y")
        except Exception:
            due_at = ""  # fallback if invalid or missing

        #print("due_at:", due_at)
        return due_at

    def get_responsible_for_coordinations(node:dict):
        responsible_edges = node.get("members", {}).get("edges", [])
        responsible_names = [
            edge["node"]["displayName"]
            for edge in responsible_edges
            if edge.get("isResponsible") and edge.get("node")
        ]

        return responsible_names
