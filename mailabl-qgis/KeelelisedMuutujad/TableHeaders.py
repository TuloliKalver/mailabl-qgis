# TableHeaders.py
from typing import ClassVar, List, Dict

class HeaderKeys:
    HEADER_ID = "id"
    HEADER_NUMBER = "number"
    HEADER_JOB_NUMBER = "jobNumber"
    HEADER_TYPE = "type"
    HEADER_FLAG = "flag"
    HEADER_NAME = "name"
    HEADER_JOB_NAME = "jobName"
    HEADER_DEADLINE = "tähtaeg"
    COLOR_NAME = "color"
    HEADER_RESPONSIBLE = "responsible"
    HEADER_PROPERTY_NUMBER = "property_number"
    HEADER_PROPERTIES_ICON = "properties_icon"
    HEADER_PARENT_ID = "parent_id"
    HEADER_WEB_LINK_BUTTON = "web_link_button"
    HEADER_DOCUMENTS = "documents"
    HEADER_FILE_PATH = "file_path"
    HEADER_STATUSES = "statuses"
    

    ALL_HEADER_KEYS: ClassVar[List[str]] = [
        HEADER_ID,
        HEADER_NUMBER,
        HEADER_NAME,
        HEADER_DEADLINE,
        COLOR_NAME,
        HEADER_RESPONSIBLE,
        HEADER_PROPERTY_NUMBER,
        HEADER_PROPERTIES_ICON,
        HEADER_PARENT_ID,
        HEADER_WEB_LINK_BUTTON,
        HEADER_DOCUMENTS,
        HEADER_FILE_PATH,
        HEADER_STATUSES,
    ]

    TASKS_HEADER_KEYS: ClassVar[List[str]] = [
        HEADER_ID,
        HEADER_FLAG,
        HEADER_TYPE,
        HEADER_NAME,
        HEADER_DEADLINE,
        COLOR_NAME,
        HEADER_RESPONSIBLE,
        HEADER_PROPERTY_NUMBER,
        HEADER_PROPERTIES_ICON,
        HEADER_PARENT_ID,
        HEADER_WEB_LINK_BUTTON,
        HEADER_DOCUMENTS,
        HEADER_FILE_PATH,
        HEADER_STATUSES,
    ]

    COORDINATIONS_HEADER_KEYS: ClassVar[List[str]] = [
        HEADER_ID,
        HEADER_NUMBER,
        HEADER_TYPE,
        HEADER_JOB_NAME,
        HEADER_JOB_NUMBER,
        HEADER_DEADLINE,
        COLOR_NAME,
        HEADER_RESPONSIBLE,
        HEADER_PROPERTY_NUMBER,
        HEADER_PROPERTIES_ICON,
        HEADER_PARENT_ID,
        HEADER_WEB_LINK_BUTTON,
        HEADER_DOCUMENTS,
        HEADER_FILE_PATH,
        HEADER_STATUSES,
    ]

    WORKS_HEADER_KEYS: ClassVar[List[str]] = [
        HEADER_ID,
        HEADER_FLAG,
        HEADER_TYPE,
        HEADER_NAME,
        HEADER_DEADLINE,
        COLOR_NAME,
        HEADER_RESPONSIBLE,
        HEADER_PROPERTY_NUMBER,
        HEADER_PROPERTIES_ICON,
        HEADER_PARENT_ID,
        HEADER_WEB_LINK_BUTTON,
        HEADER_STATUSES,
    ]

class QueryHeaders:
    """
    Keys used to extract data from query results (e.g., GraphQL node dicts).
    Mirrors HeaderKeys, but represents internal API or DB field names.
    """
    QUERY_ID = HeaderKeys.HEADER_ID
    QUERY_NUMBER = HeaderKeys.HEADER_NUMBER
    QUERY_JOB_NUMBER = HeaderKeys.HEADER_JOB_NUMBER
    QUERY_NAME = HeaderKeys.HEADER_NAME
    QUERY_JOB_NAME = HeaderKeys.HEADER_JOB_NAME
    QUERY_FLAG = HeaderKeys.HEADER_FLAG
    QUERY_TYPE = HeaderKeys.HEADER_TYPE
    QUERY_DEADLINE = HeaderKeys.HEADER_DEADLINE
    QUERY_COLOR = HeaderKeys.COLOR_NAME
    QUERY_RESPONSIBLE = HeaderKeys.HEADER_RESPONSIBLE
    QUERY_PROPERTY_NUMBER = HeaderKeys.HEADER_PROPERTY_NUMBER
    QUERY_PROPERTIES_ICON = HeaderKeys.HEADER_PROPERTIES_ICON
    QUERY_PARENT_ID = HeaderKeys.HEADER_PARENT_ID
    QUERY_WEB_LINK_BUTTON = HeaderKeys.HEADER_WEB_LINK_BUTTON
    QUERY_DOCUMENTS = HeaderKeys.HEADER_DOCUMENTS
    QUERY_FILE_PATH = HeaderKeys.HEADER_FILE_PATH
    QUERY_STATUSES = HeaderKeys.HEADER_STATUSES

    ALL_QUERY_KEYS: ClassVar[List] = [
        QUERY_ID,
        QUERY_NUMBER,
        QUERY_NAME,
        QUERY_DEADLINE,
        QUERY_COLOR,
        QUERY_RESPONSIBLE,
        QUERY_PROPERTY_NUMBER,
        QUERY_PROPERTIES_ICON,
        QUERY_WEB_LINK_BUTTON,
        QUERY_DOCUMENTS,
        QUERY_FILE_PATH,
        QUERY_STATUSES,
    ]

    TASKS_QUERY_KEYS: ClassVar[List] = [
        QUERY_ID,
        QUERY_FLAG,
        QUERY_TYPE,
        QUERY_NAME,
        QUERY_DEADLINE,
        QUERY_COLOR,
        QUERY_RESPONSIBLE,
        QUERY_PROPERTY_NUMBER,
        QUERY_PROPERTIES_ICON,
        QUERY_WEB_LINK_BUTTON,
        QUERY_DOCUMENTS,
        QUERY_FILE_PATH,
        QUERY_STATUSES,
    ]

    COORDINATIONS_QUERY_KEYS: ClassVar[List] = [
        QUERY_ID,
        QUERY_JOB_NUMBER,
        QUERY_NAME,
        QUERY_JOB_NAME,
        QUERY_DEADLINE,
        QUERY_COLOR,
        QUERY_RESPONSIBLE,
        QUERY_PROPERTY_NUMBER,
        QUERY_PROPERTIES_ICON,
        QUERY_WEB_LINK_BUTTON,
        QUERY_DOCUMENTS,
        QUERY_FILE_PATH,
        QUERY_STATUSES,
    ]

    WORKS_QUERY_KEYS: ClassVar[List] = [
        QUERY_ID,
        QUERY_JOB_NUMBER,
        QUERY_NAME,
        QUERY_JOB_NAME,
        QUERY_DEADLINE,
        QUERY_COLOR,
        QUERY_RESPONSIBLE,
        QUERY_PROPERTY_NUMBER,
        QUERY_PROPERTIES_ICON,
        QUERY_WEB_LINK_BUTTON,
        QUERY_STATUSES,
    ]

class TableHeaders_new:
    """
    Localized display values for header keys.
        """
    def __init__(self, language: str = "et"):
        self.language = language
        self._headers: Dict[str, str] = self._get_labels(language)

    def _get_labels(self, lang: str = "et") -> Dict[str, str]:
        if lang == "et":
            return {
                HeaderKeys.HEADER_ID: "ID",
                HeaderKeys.HEADER_NUMBER: "Number",
                HeaderKeys.HEADER_JOB_NUMBER: "Töö number",
                HeaderKeys.HEADER_TYPE: "Liik",
                HeaderKeys.HEADER_FLAG: "",
                HeaderKeys.HEADER_JOB_NAME: "Töö nimetus",
                HeaderKeys.HEADER_NAME: "Nimetus",
                HeaderKeys.HEADER_DEADLINE: "Tähtaeg",
                HeaderKeys.COLOR_NAME: "Color_name",
                HeaderKeys.HEADER_RESPONSIBLE: "Vastutaja",
                HeaderKeys.HEADER_PROPERTY_NUMBER: "Kataster",
                HeaderKeys.HEADER_PROPERTIES_ICON: "Properties_icon",
                HeaderKeys.HEADER_PARENT_ID: "Parent_id",
                HeaderKeys.HEADER_WEB_LINK_BUTTON: "Mailabl_icon",
                HeaderKeys.HEADER_DOCUMENTS: "Dokumendid",
                HeaderKeys.HEADER_FILE_PATH: "Dok_icon",
                HeaderKeys.HEADER_STATUSES: "Staatus",
            }
        elif lang == "en":
            return {
                HeaderKeys.HEADER_ID: "ID",
                HeaderKeys.HEADER_NUMBER: "Number",
                HeaderKeys.HEADER_JOB_NUMBER: "Job Number",
                HeaderKeys.HEADER_TYPE: "Type",
                HeaderKeys.HEADER_FLAG: "",
                HeaderKeys.HEADER_NAME: "Name",
                HeaderKeys.HEADER_JOB_NAME: "Job Name",
                HeaderKeys.HEADER_DEADLINE: "Deadline",
                HeaderKeys.COLOR_NAME: "Color name",
                HeaderKeys.HEADER_RESPONSIBLE: "Responsible",
                HeaderKeys.HEADER_PROPERTY_NUMBER: "Property",
                HeaderKeys.HEADER_PROPERTIES_ICON: "Icon",
                HeaderKeys.HEADER_PARENT_ID: "Parent ID",
                HeaderKeys.HEADER_WEB_LINK_BUTTON: "Web",
                HeaderKeys.HEADER_DOCUMENTS: "Docs",
                HeaderKeys.HEADER_FILE_PATH: "File",
                HeaderKeys.HEADER_STATUSES: "Status",
            }
        elif lang == "code":
            return {
                HeaderKeys.HEADER_ID: HeaderKeys.HEADER_ID,
                HeaderKeys.HEADER_NUMBER: HeaderKeys.HEADER_NUMBER,
                HeaderKeys.HEADER_JOB_NUMBER: HeaderKeys.HEADER_JOB_NUMBER,
                HeaderKeys.HEADER_NAME: HeaderKeys.HEADER_NAME,
                HeaderKeys.HEADER_JOB_NAME: HeaderKeys.HEADER_JOB_NAME,
                HeaderKeys.HEADER_TYPE: HeaderKeys.HEADER_TYPE,
                HeaderKeys.HEADER_FLAG: HeaderKeys.HEADER_FLAG,
                HeaderKeys.HEADER_DEADLINE: HeaderKeys.HEADER_DEADLINE,
                HeaderKeys.COLOR_NAME: HeaderKeys.COLOR_NAME,
                HeaderKeys.HEADER_RESPONSIBLE: HeaderKeys.HEADER_RESPONSIBLE,
                HeaderKeys.HEADER_PROPERTY_NUMBER: HeaderKeys.HEADER_PROPERTY_NUMBER,
                HeaderKeys.HEADER_PROPERTIES_ICON: HeaderKeys.HEADER_PROPERTIES_ICON,
                HeaderKeys.HEADER_PARENT_ID: HeaderKeys.HEADER_PARENT_ID,
                HeaderKeys.HEADER_WEB_LINK_BUTTON: HeaderKeys.HEADER_WEB_LINK_BUTTON,
                HeaderKeys.HEADER_DOCUMENTS: HeaderKeys.HEADER_DOCUMENTS,
                HeaderKeys.HEADER_FILE_PATH: HeaderKeys.HEADER_FILE_PATH,
                HeaderKeys.HEADER_STATUSES: HeaderKeys.HEADER_STATUSES,
            }


    def get(self, key: str) -> str:
        #if key not in self._headers:
            #raise KeyError(f"Header key '{key}' not defined for language '{self.language}'")
        return self._headers[key]

    def __getitem__(self, key: str) -> str:
        return self.get(key)

    def items(self):
        return self._headers.items()
