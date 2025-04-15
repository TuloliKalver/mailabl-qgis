class Headings:
    WARNING_SIMPLE = "Hoiatus!" 
    WARNING_CRITICAL = "Oi Oi Oi!"
    TUBLI = "Tubli!" 
    inFO_SIMPLE = "Info"
    ADDING_PROPERTIOES = "Lisan kinnistuid"
    KATASTRID_LAETUD = "Katastrid laetud"
    NIMEKIRJA_KOOSTAMINE = "Koostan linnade/külade nimekirja!"


    def __init__(self):
        self.warningSimple = "Hoiatus!" 
        self.warningCritical = "Oi Oi Oi!"
        self.tubli = "Tubli!" 
        self.infoSimple = "Info"
        self.lisan_kinnistuid = "Lisan kinnistuid"
        self.katastrid_laetud = "Katastrid laetud"
        self.nimekirja_koostamine = "Koostan linnade/külade nimekirja!"



class HoiatusTexts:
    def __init__(self):       
        self.puudulik_kinnistute_seadistus = "Kontrolli kinnistute seadistusi"
        self.juurdepaas_ei = "Juurdepääsuluba ei leitud"
        self.kasutaja_oigused_puuduvad = "Õigused puuduvad." "\n" "Loe täpsemalt: " "\n" "abikesksust"
        self.linn_kyla_valimata = "Jätkamiseks vali ja kinnita linn või küla"
        self.maakond_valimata = "Jätkamiseks vali ja kinnita maakond"
        self.omavalitsus_valimata = "Jätkamiseks vali ja kinnita omavalitsus"        
        self.SHPfaili_laadimine = (
                "Laadi õige fail! SHP_KATASTRIÜKSUS.SHP\n"
                "Uued andmed saad Maa-ametist kasutades Seadete menüüst valikut 'Maa-ametisse'"
            )
        self.vigane_voti = "Viga andmeühendusel.\nProovi hiljem uuesti!"
        self.error = "Midagi läks valesti"        
        self.kinnistuid_ei_leidnud = "Ühtegi kinnistut ei leitud"
        self.andmed_valimata = "Andmeid ei ole valitud"
        self.otsing_puudu = "Otsingu lahtris andmed puuduvad"
        self.korrigeeri_sümbolit = "Sümbol ei vasta standardile"
        self.puudulikud_andmed = "Andmed puuduvad"
        self.kinnistud_MLBs_olemas = "Kõik valitud kinnistud on juba Mailablis"
        self.kinnistuid_MLBs_pole = "Valitud kinnistuid Mailablis ei ole"
        self.kihinimetus_lisamata = "Kihinimetus on vigane või lisamata"
        self.logimise_ebaonnestus = "Autentimine ebaõnnestus.\nKontrolli kasutajanime ja parooli"
        self.logimise_ebaonnestus = "Autentimise pöördumine ebaõnnestus.\nProovi mõne hetke pärast uuesti"
        self.zoom_ala_liiga_suur = "Ala on projektide laadimiseks liiga suur\nZoomi lähemale"
        self.zoom_siin_ei_ole_midagi = "Selles alas puuduvad kinnistud"
        self.kasutaja_on_juba_autentitud = "Kasutaja on juba autentitud"   
        self.kasutaja_puudub = "Puudub kasutaja"
        self.projekt_valimata = "Vali projekt"
        self.QGIS_projekt_puudu = "Jätkamiseks ava projekt"
        self.kasutaja_peatas_protsessi = "Tegevused on tühistatud ja protsess peatatud"               
        self.laadimine_error = "Laadimine on katkestatud"        
        self.projekti_ei_leidnud = "Antud numbriga projekti ei leitud"
        self.projektid_puuduvad = "Piirkonnas puuduvad teadaolevad projektid"        
        self.kihil_kinnistu_valik = "Vali vähemalt üks kinnistu"
        self.ostingu_tulemused_puuduvad = "Otsingule vastavaid tulemused puuduvad"
        self.Liiga_palju_kinnistuid = "Valitud on rohkem kui üks objekt. \n Palun valige uuesti.\n Hetkel on toetatud ainult üksiku kinnistu valik!"


class HoiatusTextsAuto:        
    @staticmethod
    # Kuvab kihi nimetust mis laadimisel jäeb puudu - kommentaati vaja lisada kasutuskoht. ise ei mäleta. 
    def strange_usage_folder(folder_name):
        return f"Nädis nimetus {folder_name}"

    @staticmethod
    def no_match_for_this(lable_text):
        text = (f"Märksõnale {lable_text} ei leitud ühtegi vastet")
        return text

    def input_layer_missing(layer_name_text):
        aluskiht_puudu = f"Laaditavate kinnistute kiht {layer_name_text} on puudu.\nJätkamiseks lae algandmed."
        return aluskiht_puudu

    @staticmethod
    def generated_layer_in_subgroup (new_layer_name, group_layer_name):
        text = (f"Kaardikiht on lisatud kaardikihtide alamgruppi 'Mailabl settings/{group_layer_name}':/n{new_layer_name}")
        return text
    
    #Viga kui andmepäring Mailabli API suunal saab errori
    @staticmethod
    def warning_message_qraphql_error(error_message):
        GraphQL_päring_error = f"GraphQL päring ebaõnnestus:\n{error_message}"    
        return GraphQL_päring_error

    def layer_indexing (layer_name):
        text = (f"Paremaks toimimiseks toimub kihi:\n{layer_name}\nindekseerimine")
        return text

    @staticmethod
    def deleted_output_file_sucess (output_file_path):
        fail_kustutatud = (f"Olemasolev fail on edukalt kustutatud:\n{output_file_path}")
        return fail_kustutatud
    
    @staticmethod
    def save_layer_error (error_message):
        kiht_error = (f"Kihi salvestamine ebaõnnestus:\n{error_message}")
        return kiht_error
    
    @staticmethod
    def load_layer_error (output_file_path):
        kiht_error = (f"Uue kihi laadimine failist:\n\n{output_file_path}\n\nebaõnnetsus") #kihi laadimine ebaõnnestus...???
        return kiht_error
    
    def load_gpkg_file_error(output_file_path):
        GPKG_fail_ei_leitud = (f"'GPKG' tüüpi faili asukohas:\n{output_file_path} ei leitud")
        return GPKG_fail_ei_leitud

    def some_user_message(matching_users):
        kasutaja_tuvastatud = (f"Kasutaja\n{len(matching_users)}\ntuvastatud")
        return kasutaja_tuvastatud
    
    def unable_to_delete_output_file (output_file_path, e):
        text = f"Ei saa faili '{output_file_path}' kustutada: {e}"
        return text

class LabelsTexts:
    def name_number_by_module(module_text):
        text = f"{module_text} number ja nimetus"
        return text


class InfoTexts:
    @staticmethod
    def properties_successfully_added(project_name, total_returned_ids,total_ids_table):
        if total_returned_ids <= 1:
            end_text = "1 kinnistu"
        else:
            end_text = f"{total_returned_ids}/{total_ids_table} kinnistut"
        text = f"Projektile  <b>{project_name}</b> \n lisatud {end_text}!"
        return text

    @staticmethod
    def error_adding_properties(element_name):
        text = f"<b>{element_name}</b>\n kinnistute salvestamine ebaõnnestus"
        return text
class KriitilisedTexts:
    def __init__(self):
        self.error = "Midagi läks valesti.\nPöördu admini poole"

class EdukuseTexts:
    TEHTUD = "Toiming edukalt lõpetatud"
    SALVESTATUD = "Kõik on salvestatud"
    

    def __init__(self):
        self.tehtud = EdukuseTexts.TEHTUD
        self.salvestatud = EdukuseTexts.SALVESTATUD
        

class Salvestamisel:

    def __init__(self):
        self.vali_kausta_asukoht ="Valik asukoht kuhu aluskaardi fail salvestatakse!"