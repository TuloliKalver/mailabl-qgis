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
        self.aluskiht_puudu = (f"Laetavate kinnistute kiht {input_layer_name} on puudu.\nJätkamiseks lae algandmed.")
        self.juurdepaas_ei = "Juurdepääsuluba ei leitud"        
        self.linn_kyla_valimata = "Jätkamiseks vali ja kinnita linn või küla"
        self.maakond_valimata = "Jätkamiseks vali ja kinnita maakond"
        self.omavalitsus_valimata = "Jätkamiseks vali ja kinnita omavalitsus"        
        self.SHPfaili_laadimine = (
                "Lae õige fail! SHP_KATASTRIÜKSUS.SHP\n"
                "Uued andmed saad Maa-ametist kasutades Sätete nenüüst valikut 'Maa-ametisse'"
            )
        self.error = "Midagi läks valesti"
        text = "Ühtegi kinnistut ei leitud"
        self.andmed_valimata = "Andmeid ei ole valitud"
        self.kinnistu_valimata = "Vali importimiseks vähemalt üks kinnistu"
        self.kinnistud_MLBs_olemas = "Kõik valitud kinnistud on juba Mailablis"
        self.kinnistuid_MLBs_pole = "Valitud kinnistuid Mailablis ei ole"
        text = "Nimetus on vigane või lisamata" #mille nimetus?
        self.logimise_ebaonnestus = ("Autentimine ebaõnnestus.\nKontrolli kasutajanime ja parooli")
        self.logimise_ebaonnestus = ("Autentimise pöördumine ebaõnnestus.\nProovi mõne hetke pärast uuesti")
        self.projektide_laadimine_error = ("Ala on projektide laadimiseks liiga suur\nZoomi lähemale")
        self.GraphQL_päring_error = (f"GraphQL päring ebaõnnestus:\n{error_message}")
        self.error = ("Midagi läks valesti.\nPöördu admini poole")
        self.kasutaja_puudub = "Puudub kasutaja"
        self.projekt_valimata = "Vali projekt"
        self.projekt_valimata = "Jätkamiseks ava projekt"
        self.protsess_peatatud = "Kasutaja tühistas kausta valiku. Protsess on peatatud"        
        self.error = "Seekord nii ja homme naa"
        self.fail_kustutatud = (f"Varasem samanimeline fail kustutati:\n{output_file_path}")

class InfoTexts:
    def __init__(self):
        

class KriitilisedTexts:
    def __init__(self):
        text = ""

class EdukuseTexts:
    def __init__(self):
        self.koik_ok = "Tubli! Kõik on tehtud"
        self.koik_ok = "Kõik sai salvestatud"


        
