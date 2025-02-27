from ..utils.UIActions import UIActions


class UIDeleteTables():
    def __init__(self,tbl_Delete_streets, tbl_Delete_properties):
        self.tbl_Delete_streets = tbl_Delete_streets
        self.tbl_Delete_properties = tbl_Delete_properties

    def tables_on_load(self):
        object_tables = [self.tbl_Delete_streets,
                        self.tbl_Delete_properties]
        UIActions.hider(self,elements=object_tables)



    def table_after_city(self):
        object_tables = [self.tbl_Delete_streets,
                        self.tbl_Delete_properties]
        UIActions.shower(self,elements=object_tables)