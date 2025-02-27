from .UIActions import UIActions


class UIDeleteListViews():
    def __init__(self,lwDel_State_Names,lwDelete_Cities_Names, lwDelete_County_Names):
        self.lwDel_State_Names = lwDel_State_Names
        self.lwDelete_Cities_Names = lwDelete_Cities_Names
        self.lwDelete_County_Names = lwDelete_County_Names

    def clear_all_views(self):
        items= [self.lwDel_State_Names,
                self.lwDelete_Cities_Names,
                self.lwDelete_County_Names
                ]
        UIActions.cleaner(self, items)

    def clear_after_county(self):
        items= [self.lwDel_State_Names,
                self.lwDelete_Cities_Names
                ]
        UIActions.cleaner(self, items)

    def clear_after_state(self):
        items= [
                self.lwDelete_Cities_Names
                ]
        UIActions.cleaner(self, items)


    def selection_model_views_on_load(self):
        items= [self.lwDel_State_Names,
                self.lwDelete_Cities_Names,
                ]
        UIActions.selection_extended(self, items)

    def listViews_on_load(self):
        list_views = [self.lwDel_State_Names,
                    self.lwDelete_Cities_Names]
        UIActions.hider(self, elements=list_views)