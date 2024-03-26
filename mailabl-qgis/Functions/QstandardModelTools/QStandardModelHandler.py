from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel


class CombineModels:
    @staticmethod
    def TableModelCombiner(model_table1:QStandardItemModel, model_table2:QStandardItemModel, target_model:QStandardItemModel, column_names: list) -> QStandardItemModel:
        for model_name, model_instance in (("Table1", model_table1), ("Table2", model_table2)):
            #print(f"Rows in {model_name} model:")
            for row in range(model_instance.rowCount()):
                new_row = []
                for column_name in column_names:
                    # Find the item corresponding to the column name in the row
                    column_index = column_names.index(column_name)
                    item = model_instance.item(row, column_index)
                    if item is not None:
                        new_row.append(item.text())
                    else:
                        new_row.append("")
                # Add the new row to the model
                target_model.appendRow([QStandardItem(value) for value in new_row])
        return target_model

class ModelHeadersGenerator:
    @staticmethod
    def generateHeadersFromExistingModel(existing_model: QStandardItemModel) -> list: 
            # Get column names from the model
        input_table_column_names = []
        for column in range(existing_model.columnCount()):
            input_table_column_names.append(existing_model.headerData(column, Qt.Horizontal, Qt.DisplayRole))
        return input_table_column_names

class DevelopmentPrinters:
    @staticmethod
    def prinItemssOfTheModelsBasedOnHeaders (model1: QStandardItemModel, model2: QStandardItemModel, header_names: list) ->None:
        for model_name, model_instance in (("Table1", model1), ("Table2", model2)):
            print(f"Rows in {model_name} model:")
            for row in range(model_instance.rowCount()):
                print(f"Row {row}:")
                for column_name in header_names:
                    # Find the item corresponding to the column name in the row
                    item = model_instance.item(row, header_names.index(column_name))
                    if item is not None:
                        print(f"    {column_name}: {item.text()}")
                    else:
                        print(f"    {column_name}: No item found")
                        
    @staticmethod
    def printItemsOfSingleModelBasedOnHeaders(model: QStandardItemModel, header_names: list) -> None:
        print(f"Rows in the model:")
        for row in range(model.rowCount()):
            print(f"Row {row}:")
            for column_name in header_names:
                # Find the item corresponding to the column name in the row
                column_index = header_names.index(column_name)
                item = model.item(row, column_index)
                if item is not None:
                    print(f"    {column_name}: {item.text()}")
                else:
                    print(f"    {column_name}: No item found")

class DataExtractors:
    @staticmethod
    def ExtractCadastralNrDataFromModel(model: QStandardItemModel, header_data: list) -> list:
        units = []
        # Define column names
        cadastral_column_name = "TUNNUS"
        # Get the column indexes based on column names
        cadastral_number_index = header_data.index(cadastral_column_name) if cadastral_column_name in header_data else -1
        # Retrieve property data from the selected row's columns
        for row in range(model.rowCount()):
            #print(f"Row {row}:")
            # Find the item corresponding to the column name in the row
            item = model.item(row, cadastral_number_index)
            if item is not None:
                #print(f"    {cadastral_column_name}: {item.text()}")
                #item_text = item.text()
                #print(f"    {cadastral_column_name}: {item.text()}")
                # Append the item_text enclosed in single quotes to the units list
                units.append(item.text())
            else:
                #print(f"    {cadastral_column_name}: No item found")
                pass
        return  units
    
    @staticmethod
    def CadasterMatcher(cadastral_unit: str ,model: QStandardItemModel, header_data: list) ->None:
        cadastral_column_name = "TUNNUS"
        # Get the column indexes based on column names
        cadastral_number_index = header_data.index(cadastral_column_name) if cadastral_column_name in header_data else -1
        #if cadastral_number_index == -1:
        #    print("Cadastral column not found")
        #    return
        # List to store row indices of matching rows
        matching_rows = []    
        # Retrieve property data from the selected row's columns
        for row in range(model.rowCount()):
            #print(f"Row {row}:")
            # Find the item corresponding to the column name in the row
            item = model.item(row, cadastral_number_index)
            item_text = item.text()
            if item_text == cadastral_unit:
                #print(f"    {cadastral_column_name}: {item.text()}")
                matching_rows.append(row)
            else:
                #print(f"    {cadastral_column_name}: No item found")
                pass
        return matching_rows