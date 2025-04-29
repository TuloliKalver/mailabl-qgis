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
        
        if module == Module.ASBUILT:
            #print("node data:")
            #print(node)
            description = node.get("description", "")
            due_at = DataExtractor.date_converter(node)

            headers = {
            HeaderKeys.HEADER_ID: node.get("id", ""),
            HeaderKeys.HEADER_PARENT_ID: node.get("parentID", ""),
            HeaderKeys.HEADER_TYPE: (node.get("type", {}).get("name")) or "",
            HeaderKeys.HEADER_FLAG: (node.get("priority") or "").lower(),
            HeaderKeys.HEADER_NAME: node.get("name") or node.get("title") or "",
            HeaderKeys.HEADER_DEADLINE: due_at,
            HeaderKeys.HEADER_STATUSES: status.get("name", "") if status else "",
            HeaderKeys.COLOR_NAME: status.get("color", "") if status else "",
            HeaderKeys.HEADER_PROPERTY_NUMBER: ", ".join(cadastral_numbers) if cadastral_numbers else "",
            HeaderKeys.HEADER_PROPERTIES_ICON: "",
            HeaderKeys.HEADER_WEB_LINK_BUTTON: "",
            HeaderKeys.HEADER_DOCUMENTS: DataExtractor.extract_links_from_description(description) or "",
            HeaderKeys.HEADER_FILE_PATH: "",
            HeaderKeys.HEADER_RESPONSIBLE: ", ".join(responsible_names) if responsible_names else "",
            }


            return headers

            
        else:
            due_at = DataExtractor.date_converter(node)
            headers = {            
            HeaderKeys.HEADER_ID: node.get("id", ""),
            HeaderKeys.HEADER_PARENT_ID: node.get("parentID", ""),
            HeaderKeys.HEADER_NUMBER: node.get("number", "") or (node.get("type", {}).get("name")) or "",
            HeaderKeys.HEADER_NAME: node.get("name") or node.get("title") or "",
            
            HeaderKeys.HEADER_DEADLINE: due_at,
            HeaderKeys.HEADER_STATUSES: status.get("name", "") if status else "",
            HeaderKeys.COLOR_NAME: status.get("color", "") if status else "",
            HeaderKeys.HEADER_PROPERTY_NUMBER: ", ".join(cadastral_numbers) if cadastral_numbers else "",
            HeaderKeys.HEADER_PROPERTIES_ICON: "",
            HeaderKeys.HEADER_WEB_LINK_BUTTON: "",
            HeaderKeys.HEADER_DOCUMENTS: node.get("filesPath", "") or "",
            HeaderKeys.HEADER_FILE_PATH: "",
            HeaderKeys.HEADER_RESPONSIBLE: ", ".join(responsible_names) if responsible_names else "",
            }    
            
            
            return headers

    @staticmethod


    def extract_links_from_description(description: str) -> list:
        """
        Extract links or file paths from a <table> containing 'Joonised' using only built-in tools.

        Args:
            description (str): HTML content (raw)

        Returns:
            list[str]: Extracted file paths and URLs
        """
        if not description or "Joonised" not in description:
            return []

        links = []

        # Find the "Joonised" table using simple regex
        table_pattern = re.compile(r'<table.*?>.*?Joonised.*?</table>', re.DOTALL | re.IGNORECASE)
        match = table_pattern.search(description)
        if not match:
            return []

        table_html = match.group()

        # Find all <td> inside that table
        td_pattern = re.compile(r'<td.*?>(.*?)</td>', re.DOTALL)
        td_matches = td_pattern.findall(table_html)

        for td in td_matches:
            # Remove possible <p> inside <td>
            clean_text = re.sub(r'<.*?>', '', td).strip()
            if clean_text:
                links.append(clean_text)

        return links


    def date_converter(node:dict):
        print("date converter:", node)
        raw_due_at = node.get("dueAt", "")
        # Unpack if it's a tuple like ('2022-07-21',)
        if isinstance(raw_due_at, tuple) and raw_due_at:
            raw_due_at = raw_due_at[0]

        # Try to format if it's a valid date string
        try:
            due_at = datetime.strptime(raw_due_at, "%Y-%m-%d").strftime("%d.%m.%Y")
        except Exception:
            due_at = ""  # fallback if invalid or missing

        print("due_at:", due_at)
        return due_at
