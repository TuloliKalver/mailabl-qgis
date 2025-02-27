from .UIActions import UIActions


class UIDeleteButtonsManager():
    def __init__(self, pbDel_State, pbDel_City, pbDel_PreConfirm):
        self.pbDel_State = pbDel_State
        self.pbDel_City = pbDel_City
        self.pbDel_PreConfirm = pbDel_PreConfirm


    def buttons_on_load(self):
        hide_buttons = [
            self.pbDel_State,
            self.pbDel_City,
            self.pbDel_PreConfirm,
        ]
        UIActions.hider(self,elements=hide_buttons)

    def buttons_show_after_county(self):
        show_buttons = [
            self.pbDel_State
        ]
        UIActions.shower(self, elements=show_buttons)
        self.pbDel_City.hide()




    def buttons_show_after_state(self):
        show_buttons = [
            self.pbDel_City
            ]
        UIActions.shower(self, elements=show_buttons)



    def buttons_show_after_city(self):
        show_buttons = [
            self.pbDel_PreConfirm
        ]
        UIActions.shower(self, elements=show_buttons)



    def delete_buttons_signal_blocked(self):
        buttons = [
            self.pbDel_State,
            self.pbDel_City,
            self.pbDel_PreConfirm,

        ]
        buttons.blockSignals(True)

    def delete_buttons_signal_reactivated(self):
        buttons = [
            self.pbDel_State,
            self.pbDel_City,
            self.pbDel_PreConfirm,
        ]
        buttons.blockSignals(False)