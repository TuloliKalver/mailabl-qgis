from .UIActions import UIActions


class UIDeleteFrames():
    def __init__(self,frDel_Main_Selected_Data_Overview, fr_Del_bottom):
        self.frDel_Main_Selected_Data_Overview = frDel_Main_Selected_Data_Overview
        self.fr_Del_bottom = fr_Del_bottom

    def frames_on_load(self):
        frame_tables = [self.fr_Del_bottom,
                        self.frDel_Main_Selected_Data_Overview
                        ]
        UIActions.hider(self, elements = frame_tables)

    def frames_after_city(self):
        frame_tables = [self.fr_Del_bottom,
                        self.frDel_Main_Selected_Data_Overview
                        ]
        UIActions.shower(self, elements = frame_tables)