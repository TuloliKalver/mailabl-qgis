

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QCoreApplication
import pandas as pd
from ...utils.DataExtractors.DataExtractors import DataExtractor
from ...KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ...KeelelisedMuutujad.modules import Module

class DataModelBuilder:
    def __init__(self):
        self.data_model = None

    def build_model_from_records(data, language="et", module=None):
        """
        Builds a QStandardItemModel from a list of node-like records.

        Args:
            data (List[Dict]): Raw records, usually from GraphQL (each should include a 'node' key or be a flat dict)
            headers (List[str]): Ordered list of data keys
            display_headers (Dict[str, str]): Mapping of keys to localized column names
            language (str): Language used in localization and extraction

        Returns:
            QStandardItemModel: Fully populated Qt model ready for use in QTableView
        """
        if module == Module.ASBUILT:
            headers = HeaderKeys.TASKS_HEADER_KEYS
        else:
            headers = HeaderKeys.ALL_HEADER_KEYS
        display_headers = TableHeaders_new(language)

        df_data = []

        for item in data:
            node = item.get("node", item)  # Fallback in case data is already flattened
            extracted = DataExtractor.extract_row_data_from_node(node, language=language, module=module)
            df_data.append(extracted)

        QCoreApplication.processEvents()  # Keep UI responsive during large loads
        df = pd.DataFrame(df_data)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([display_headers.get(key) for key in headers])

        for _, row_data in df.iterrows():
            row_items = [
                QStandardItem(str(row_data.get(key, "")))
                for key in headers
            ]
            model.appendRow(row_items)


        return model
