from ..app.workspace_handler import WorkSpaceHandler


from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import  QVBoxLayout




class ToggleHandler(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main = main_window


    def handle_toggle(self, state):
        if state:
            print("started False toggle setup")
            self.main.ToggleStatus.setText("Olen üldjuhendiga tuttav")
            self.main.teWelcomeContent.setVisible(True)
            self.main.setLayout(self.main.layout1)
            WorkSpaceHandler().swWorkSpace_Home(self.main)
            print("started 'swWorkspace_home'")
        else:
            print("started True toggle setup")
            self.main.ToggleStatus.setText("Nita kirjelduset")
            self.main.teWelcomeContent.setVisible(False)
            self.main.setLayout(self.main.layout2)
            WorkSpaceHandler().swWorkSpace_Properties(self.main, state)
            print("started 'swWorkspace_Proerties'")
        print(f"Toggle switch is {'ON' if state else 'OFF'}")





    def main_window_toggle_option(self):
        label_for_toggle = self.ToggleStatus
        self.togglebutton = ToggleSwitch(label_for_toggle)
        self.toggle_value = StoreValues_Toggle().get_toggle_status()
        print(f"toggle_value before clicked: {self.toggle_value}")

        self.frame1 = self.fToggleHolder
        self.frame2 = self.freopenToggle
        self.layout1 = QVBoxLayout(self.frame1)
        self.layout2 = QVBoxLayout(self.frame2)

        # Initially add the toggle button to frame1's layout
        self.layout1.addWidget(self.togglebutton)
        toggle_value_on_load = StoreValues_Toggle().get_toggle_status()
        print(f"toggle_value before clicked: {toggle_value_on_load}")
        self.handle_toggle(toggle_value_on_load)
        # Connect the toggled signal
        self.togglebutton.toggled.connect(self.handle_toggle)


    def handle_toggle(self, state):
        if state:
            #print("started False toggle setup")
            self.ToggleStatus.setText("Järgmisel laadimisel ära enam seda juhendit näita")
            self.layout2.removeWidget(self.togglebutton)
            self.togglebutton.setParent(self.frame1)
            self.layout1.addWidget(self.togglebutton)
            self.set_start_page_based_on_toggle_and_preferred_settings()
            #print("started 'swWorkspace_home'")
        else:
            #print("started True toggle setup")
            self.ToggleStatus.setText("Näita kirjeldust")
            self.layout1.removeWidget(self.togglebutton)
            self.togglebutton.setParent(self.frame2)
            self.layout2.addWidget(self.togglebutton)
            WorkSpaceHandler.swWorkSpace_Properties(self)
            #print("started 'swWorkspace_Proerties'")
        #print(f"Toggle switch is {'ON' if state else 'OFF'}")





