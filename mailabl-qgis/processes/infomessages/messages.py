from PyQt5.QtWidgets import QMessageBox, QPushButton

class Headings:
    def __init__(self):
        self.warningSimple = "Oi Oi Oi" # Assuming you have a stacked widget as an instance attribute
        self.warningCritical = "Oi oi oi oi"
        self.informationSimple = "Tasub teada"


    #Siin on näha kuida on võimalik kasutada erinevaid teksti viise.
    @classmethod
    def example_usage(self):
        QMessageBox.warning(None, Headings.warningSimple, Headings.informationSimple)
        
class Messages:
    def __init__(self):
        self.SimpleOK = "Tubli kõik tehtud"
        