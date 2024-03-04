from PyQt5.QtWidgets import QMessageBox, QPushButton

class Headings:
    def __init__(self):
        self.warningSimple = "Hoiatus" # Assuming you have a stacked widget as an instance attribute
        self.warningCritical = "Oi Oi Oi!"
        self.informationSimple = "Tähelepanu"
        self.informationSimple = "Infoks"
        self.informationSimple = "Teadmiseks"
        self.heading = "Hoiatus"
        self.success = "Supper"
        self.success1 = "Vingelt tehtud"
        self.success2 = "Info"
        
class HoiatusTexts:
    def __init__(self):       
        
        self.juurdepaas_ei = "Juurdepääsuluba ei leitud"        
        self.linn_kyla_valimata = "Jätkamiseks vali ja kinnita linn või küla"
        self.maakond_valimata = "Jätkamiseks vali ja kinnita maakond"
        self.omavalitsus_valimata = "Jätkamiseks vali ja kinnita omavalitsus"        
        self.SHPfaili_laadimine = (
                "Lae õige fail! SHP_KATASTRIÜKSUS.SHP\n"
                "Uued andmed saad Maa-ametist kasutades Sätete nenüüst valikut 'Maa-ametisse'"
            )
        self.error = "Midagi läks valesti"
        self.kinnistuid_ei_leidnud = "Ühtegi kinnistut ei leitud"
        self.andmed_valimata = "Andmeid ei ole valitud"
        self.kinnistu_valimata = "Vali importimiseks vähemalt üks kinnistu"
        self.kinnistud_MLBs_olemas = "Kõik valitud kinnistud on juba Mailablis"
        self.kinnistuid_MLBs_pole = "Valitud kinnistuid Mailablis ei ole"
        text = "Nimetus on vigane või lisamata" #mille nimetus?
        self.logimise_ebaonnestus = ("Autentimine ebaõnnestus.\nKontrolli kasutajanime ja parooli")
        self.logimise_ebaonnestus = ("Autentimise pöördumine ebaõnnestus.\nProovi mõne hetke pärast uuesti")
        self.projektide_laadimine_error = ("Ala on projektide laadimiseks liiga suur\nZoomi lähemale")
        
        self.error = ("Midagi läks valesti.\nPöördu admini poole")
        self.kasutaja_puudub = "Puudub kasutaja"
        self.projekt_valimata = "Vali projekt"
        self.projekt_valimata = "Jätkamiseks ava projekt"
        self.protsess_peatatud = "Kasutaja tühistas kausta valiku. Protsess on peatatud"        
        self.error = "Seekord nii ja homme naa" #selle võiks asendada
        
        self.laadimine_error = "Laadimine on katkestatud"
        
        self.projekti_ei_leidnud = "Antud numbriga projekti ei leitud"
        self.projektid_puuduvad = "Piirkonnas puuduvad teadaolevad projektid"
        
        self.kihil_kinnistu_valik = "Vali kaardikihil vähemalt üks kinnistu"
        #self.???(f"Lepingule\n{project_name}\nlisatud {total_returned_ids}/{total_ids_Table}")
        #self.???(f"Projektile\n{project_name}\nlisatud\n{total_returned_ids}/{total_ids_Table}")

class HoiatusTextsAuto:
    def __init__(self): 
        self.aluskiht_puudu = (f"Laetavate kinnistute kiht {input_layer_name} on puudu.\nJätkamiseks lae algandmed.")
        self.GraphQL_päring_error = (f"GraphQL päring ebaõnnestus:\n{error_message}")
        self.fail_kustutatud = (f"Samanimeline fail on kustutatud:\n{output_file_path}")
        self.kiht_error = (f"Kihi salvestamine ebaõnnestus:\n{error_message}")
        self.kiht_error = (f"Error loading the new layer from:\n{output_file_path}") #kihi laadimine ebaõnnestus...???
        self.GPKG_fail_ei_leitud = (f"'GPKG' tüüpi faili asukohas:\n{output_file_path} ei leitud")
        self.kasutaja_tuvastatud = (f"Kasutaja\n{len(matching_users)}\ntuvastatud")

class InfoTexts:
    def __init__(self):
        self.indekseerimine = (f"Paremaks toimimiseks toimub kihi:\n{new_layer_name} indekseerimine")
        self.kinnistud_eemaldatud = (f"Valitud kinnitsud eemaldati Mailablist ja kihilt {active_cadastral_layer_name}")
        self.kaardikiht_lisatud = (f"Kaardikiht on lisatud kaardikihtide alamgruppi 'Mailabl settings/Uued kinnistud:/n{new_layer.name}'")
        self.andmed_imporditud = (f"Andmed on edukalt imporditud ja lisatud '{import_subgroup_layer_name}' grupi kihile")
        self.andmed_laetud = "Andmed on laetud ja kaardikihile kantud"

class KriitilisedTexts:
    def __init__(self):
        pass

class EdukuseTexts:
    def __init__(self):
        self.tehtud = "Tubli! Kõik on tehtud"
        self.salvestatud = "Kõik on salvestatud"
        
        
        
         
        


        
