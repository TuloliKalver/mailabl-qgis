#utils/DataExtractors/DataExtractor.py
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...KeelelisedMuutujad.modules import Module


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
            headers = {
            HeaderKeys.HEADER_ID: node.get("id", ""),
            HeaderKeys.HEADER_PARENT_ID: node.get("parentID", ""),
            HeaderKeys.HEADER_TYPE: (node.get("type", {}).get("name")) or "",
            HeaderKeys.HEADER_FLAG: (node.get("priority") or "").lower(),
            HeaderKeys.HEADER_NAME: node.get("name") or node.get("title") or "",
            HeaderKeys.HEADER_DEADLINE: node.get("dueAt", "") or "",
            HeaderKeys.HEADER_STATUSES: status.get("name", "") if status else "",
            HeaderKeys.COLOR_NAME: status.get("color", "") if status else "",
            HeaderKeys.HEADER_PROPERTY_NUMBER: ", ".join(cadastral_numbers) if cadastral_numbers else "",
            HeaderKeys.HEADER_PROPERTIES_ICON: "",
            HeaderKeys.HEADER_WEB_LINK_BUTTON: "",
            HeaderKeys.HEADER_DOCUMENTS: node.get("filesPath", "") or "",
            HeaderKeys.HEADER_FILE_PATH: "",
            HeaderKeys.HEADER_RESPONSIBLE: ", ".join(responsible_names) if responsible_names else "",
            }
            
        else:
            headers = {            
            HeaderKeys.HEADER_ID: node.get("id", ""),
            HeaderKeys.HEADER_PARENT_ID: node.get("parentID", ""),
            HeaderKeys.HEADER_NUMBER: node.get("number", "") or (node.get("type", {}).get("name")) or "",
            HeaderKeys.HEADER_NAME: node.get("name") or node.get("title") or "",
            HeaderKeys.HEADER_DEADLINE: node.get("dueAt", "") or "",
            HeaderKeys.HEADER_STATUSES: status.get("name", "") if status else "",
            HeaderKeys.COLOR_NAME: status.get("color", "") if status else "",
            HeaderKeys.HEADER_PROPERTY_NUMBER: ", ".join(cadastral_numbers) if cadastral_numbers else "",
            HeaderKeys.HEADER_PROPERTIES_ICON: "",
            HeaderKeys.HEADER_WEB_LINK_BUTTON: "",
            HeaderKeys.HEADER_DOCUMENTS: node.get("filesPath", "") or "",
            HeaderKeys.HEADER_FILE_PATH: "",
            HeaderKeys.HEADER_RESPONSIBLE: ", ".join(responsible_names) if responsible_names else "",}
        return headers