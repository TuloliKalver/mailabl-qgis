from PyQt5.QtWidgets import QMessageBox, QPushButton

class Headings:
    def __init__(self) -> None:
        self.warningSimple = "Oi Oi Oi" # Assuming you have a stacked widget as an instance attribute
        self.warningCritical = "Oi oi oi oi"
        self.informationSimple = "Tasub teada"
        
class Messages:
    def __init__(self) -> None:
        self.SimpleOK = "Tubli kõik tehtud"
