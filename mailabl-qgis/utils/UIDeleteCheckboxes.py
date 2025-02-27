from .UIActions import UIActions


class UIDeleteCheckboxes():
    def __init__(self, cbDel_ChooseAll_Data_properties, cbDel_ChooseAll_Data_include_Allroads, cbDel_ChooseAll_Data_transport, cbDel_ChooseAll_States, cbDel_ChooseAll_Cities):
        self.cbDel_ChooseAll_Data_properties = cbDel_ChooseAll_Data_properties
        self.cbDel_ChooseAll_Data_include_Allroads = cbDel_ChooseAll_Data_include_Allroads
        self.cbDel_ChooseAll_Data_transport = cbDel_ChooseAll_Data_transport
        self.cbDel_ChooseAll_States = cbDel_ChooseAll_States
        self.cbDel_ChooseAll_Cities = cbDel_ChooseAll_Cities

    def checkboxes_on_load(self):
        checkboxes = [self.cbDel_ChooseAll_Data_properties,
                        self.cbDel_ChooseAll_Data_include_Allroads,
                        self.cbDel_ChooseAll_Data_transport,
                        self.cbDel_ChooseAll_States,
                        self.cbDel_ChooseAll_Cities]
        UIActions.hider(self, checkboxes)
        UIActions.block_signals_True(self, checkboxes)
        UIActions.check_box_states_False(self, checkboxes)
        UIActions.block_signals_False(self, checkboxes)

    def checkboxes_on_after_county(self):
        checkboxes = [
                self.cbDel_ChooseAll_States
                ]
        UIActions.shower(self, elements=checkboxes)



    def checkboxes_on_after_state(self):
        checkboxes = [
                self.cbDel_ChooseAll_Cities
                ]
        UIActions.shower(self, elements=checkboxes)
        self.cbDel_ChooseAll_Cities.hide()

    def checkboxes_on_after_city(self):
        checkboxes = [
                self.cbDel_ChooseAll_Data_properties,
                self.cbDel_ChooseAll_Data_include_Allroads,
                self.cbDel_ChooseAll_Data_transport
                ]
        UIActions.shower(self, elements=checkboxes)
        #actions.block_signals_True(self, checkboxes)
        UIActions.check_box_states_True(self, checkboxes)