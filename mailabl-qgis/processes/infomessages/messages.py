from PyQt5.QtWidgets import QMessageBox, QPushButton

class Headings:
    def __init__(self):
        self.warningSimple = "Hoiatus" # Assuming you have a stacked widget as an instance attribute
        self.warningCritical = "Oi Oi Oi!"
        self.informationSimple = "Tähelepanu"
        self.heading = "Hoiatus"
        self.success = "Supper!"
        
class HoiatusTexts:
    def __init__(self):
        self.SimpleOK = "Tubli! Kõik on tehtud."
        self.aluskiht_puudu = (f"Laetavate kinnistute kiht {input_layer_name} on puudu.\nJätkamiseks lae algandmed.")
        text = ("Juurdepääsuluba ei leitud")        
        self.linn_voi_kyla_valimata = ("Jätkamiseks vali ja kinnita linn või küla")
        self.maakond_valimata = ("Jätkamiseks vali ja kinnita maakond")
        self.omavalitsus_valimata = ("Jätkamiseks vali ja kinnita omavalitsus")
        text = ("Jätkamiseks ava projekt")
        text = (
                "Lae õige fail! SHP_KATASTRIÜKSUS.SHP\n"
                "Uued andmed saad Maa-ametist kasutades Sätete nenüüst valikut 'Maa-ametisse'"
            )
        text = ("Midagi läks valesti")
        text = ("Ühtegi kinnistut ei leitud")
        text = ("Andmeid ei ole valitud")
        text = ("Vali importimiseks vähemalt üks kinnistu")
        text = ("Kõik valitud kinnistud on juba Mailablis")
        text = ("Valitud kinnistuid Mailablis ei ole")
        text = ("Nimetus on vigane või lisamata")
        text = ("Autentimine ebaõnnestus.\nKontrolli kasutajanime ja parooli")
        text = ("Autentimise pöördumine ebaõnnestus.\nProovi mõne hetke pärast uuesti")
        text = ("Ala on projektide laadimiseks liiga suur\nZoomi lähemale")
        text = (f"GraphQL päring ebaõnnestus:\n{error_message}")
        text = ("Midagi läks valesti.\nPöördu admini poole")
        text = ("Puudub kasutaja")
        text = ("Vali projekt")
        Text = ("Kasutaja tühistas kausta valiku. Protsess on peatatud")
        text = "Kõik sai salvestatud"
        text = "Seekord nii ja homme naa"
        text = (f"Varasem samanimeline fail kustutati:\n{output_file_path}")

class InfoTexts:
    def __init__(self):
        text = ""

class KriitilisedTexts:
    def __init__(self):
        text = ""


        
