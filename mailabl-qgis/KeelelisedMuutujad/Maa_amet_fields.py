from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsProject, QgsField
from PyQt5.QtCore import QVariant, QCoreApplication


from ..config.settings import SettingsDataSaveAndLoad
from ..utils.messagesHelper import ModernMessageDialog
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ..utils.ProgressHelper import ProgressDialogModern

class Katastriyksus:
    #fid = "fid"               # Baasis olev id
    tunnus = "tunnus"          # Katastriüksuse tunnus
    hkood = "hkood"            # Asustusüksuse kood
    mk_nimi = "mk_nimi"        # Maakonna nimetus
    ov_nimi = "ov_nimi"        # Omavalitsuse nimetus
    ay_nimi = "ay_nimi"        # Asustusüksuse nimetus
    l_aadress = "l_aadress"    # Lahiaadress
    registr = "registr"        # Katastriüksuse esmaregistreerimise kuupäev
    muudet = "muudet"          # Katastriüksuse viimase muudatuse kuupäev
    siht1 = "siht1"            # 1. sihtostarve
    siht2 = "siht2"            # 2. sihtostarve
    siht3 = "siht3"            # 3. sihtostarve
    so_prts1 = "so_prts1"      # 1. sihtostarbe protsent
    so_prts2 = "so_prts2"      # 2. sihtostarbe protsent
    so_prts3 = "so_prts3"      # 3. sihtostarbe protsent
    pindala = "pindala"        # Katastriüksuse pindala
    haritav = "haritav"        # Haritava maa kõlvik
    rohumaa = "rohumaa"        # Loodusliku rohumaa kõlvik
    mets = "mets"              # Metsamaa kõlvik
    ouemaa = "ouemaa"          # Õuemaa kõlvik
    muumaa = "muumaa"          # Muu maa kõlvik
    kinnistu = "kinnistu"      # Kinnistu registriosa number
    #muutpohjus = "muutpohjus" # Katatastriüksuse viimane muudatus   new
    omvorm = "omvorm"          # Katastriüksuse omandivorm  
    maks_hind = "maks_hind"    # Maatüki maksustamishind
    marked = "marked"          # Katastriüksuse märked
    #ads_oid = "ads_oid"        # ADS objekti identifikaator, identifitseerib objekti läbi versioonide. new
    #adob_id = "adob_id"        # Aadressiobjekti versiooni unikaalne identifikaator (unikaalne üle kõikide objektide kõikide versioonide).   new
    #oiguslik_alus = "oiguslik_alus"  # Katastriüksuse viimase muudatuse õiguslik alus  new
    eksport = "eksport"        # Andmete väljavõtte kuupäev


    FieldsForTables = [tunnus, registr, ay_nimi, l_aadress, siht1, so_prts1, siht2, so_prts2, siht3, so_prts3, omvorm]

    search_field = "search_field"
    # Define a list of field names
    search_field_items = [tunnus, l_aadress, ay_nimi, ov_nimi, mk_nimi ]



class Puprpouse:
    transport = "TRANSPORDIMAA"


class OldKatastriyksus:
    tunnus = "TUNNUS"                            # Katastriüksuse tunnus
    hkood = "HKOOD"                              # Haldusüksuse kood
    mk_nimi = "MK_NIMI"                          # Maakonna nimetus
    ov_nimi = "OV_NIMI"                          # Omavalitsuse nimetus
    ay_nimi = "AY_NIMI"                          # Asustusüksuse nimetus
    l_aadress = "L_AADRESS"                      # Lahiaadress
    registr = "REGISTR"                          # Katastriüksuse esmaregistreerimise kuupäev
    muudet = "MUUDET"                            # Katastriüksuse viimase muudatuse kuupäev
    siht1 = "SIHT1"                              # 1. sihtostarve
    siht2 = "SIHT2"                              # 2. sihtostarve
    siht3 = "SIHT3"                              # 3. sihtostarve
    so_prts1 = "SO_PRTS1"                        # 1. sihtostarbe protsent
    so_prts2 = "SO_PRTS2"                        # 2. sihtostarbe protsent
    so_prts3 = "SO_PRTS3"                        # 3. sihtostarbe protsent
    pindala = "PINDALA"                          # Katastriüksuse pindala
    #Ruumikuju_pindala = "RUUMPIND"              # Katastriüksuse ruumikuju pindala  new
    #Registreeritud_yhik = "REG_YHIK"            # Pindala registreerimise ühik  new
    haritav = "HARITAV"                          # Haritava maa kõlvik
    rohumaa = "ROHUMAA"                          # Loodusliku rohumaa kõlvik
    mets = "METS"                                # Metsamaa kõlvik
    ouemaa = "OUEMAA"                            # Õuemaa kõlvik
    muumaa = "MUUMAA"                            # Muu maa kõlvik
    kinnistu = "KINNISTU"                        # Kinnistu registriosa number
    #Moodustatud = "MOODUST"                     # Maamõõtmise kuupäev   new
    #Moodistaja = "MOOTJA"                       # Maamõõtja nimetus   new
    #Moodustamisviis = "MOOTVIIS"                # Moodustamisviis   new
    #Registreerimisviis = "OMVIIS"               # Katastriüksuse registreerimise viis   new
    omvorm = "OMVORM"                            # Katastriüksuse omandivorm
    maks_hind = "MAKS_HIND"                      # Maa-ameti arvutatud maaüksuse maksustamishind €
    marked = "MARKETEKST"
    eksport = "EKSPORT"                        # Katastriüksuse märked

class KatasterMappings:
    # Field mapping between OldKatastriyksus and Katastriyksus
    field_mapping = {
        OldKatastriyksus.tunnus: Katastriyksus.tunnus,
        OldKatastriyksus.hkood: Katastriyksus.hkood,
        OldKatastriyksus.mk_nimi: Katastriyksus.mk_nimi,
        OldKatastriyksus.ov_nimi: Katastriyksus.ov_nimi,
        OldKatastriyksus.ay_nimi: Katastriyksus.ay_nimi,
        OldKatastriyksus.l_aadress: Katastriyksus.l_aadress,
        OldKatastriyksus.registr: Katastriyksus.registr,
        OldKatastriyksus.muudet: Katastriyksus.muudet,
        OldKatastriyksus.siht1: Katastriyksus.siht1,
        OldKatastriyksus.siht2: Katastriyksus.siht2,
        OldKatastriyksus.siht3: Katastriyksus.siht3,
        OldKatastriyksus.so_prts1: Katastriyksus.so_prts1,
        OldKatastriyksus.so_prts2: Katastriyksus.so_prts2,
        OldKatastriyksus.so_prts3: Katastriyksus.so_prts3,
        OldKatastriyksus.pindala: Katastriyksus.pindala,
        OldKatastriyksus.haritav: Katastriyksus.haritav,
        OldKatastriyksus.rohumaa: Katastriyksus.rohumaa,
        OldKatastriyksus.mets: Katastriyksus.mets,
        OldKatastriyksus.ouemaa: Katastriyksus.ouemaa,
        OldKatastriyksus.muumaa: Katastriyksus.muumaa,
        OldKatastriyksus.kinnistu: Katastriyksus.kinnistu,
        OldKatastriyksus.omvorm: Katastriyksus.omvorm,
        OldKatastriyksus.maks_hind: Katastriyksus.maks_hind,
        OldKatastriyksus.marked: Katastriyksus.marked,
        OldKatastriyksus.eksport: Katastriyksus.eksport
    }



class RemapPropertiesLayer:
    def __init__(self):
        self.active_layer_name = SettingsDataSaveAndLoad().load_target_cadastral_name()
        self.layer = self.get_layer_by_name(self.active_layer_name)
        self.field_mapping = KatasterMappings.field_mapping

    def get_layer_by_name(self, layer_name):
        layer = QgsProject.instance().mapLayersByName(layer_name)
        if not layer:
            raise ValueError(f"No layer found with the name {layer_name}")
        return layer[0]

    def validate_layer(self):
        if not isinstance(self.layer, QgsVectorLayer):
            raise ValueError("Expected a QgsVectorLayer object.")

    def update_attribute_table(self):
        
        progress = ProgressDialogModern(title="Andmestruktuuri uuendamine", value=0)
        progress.update(1, purpouse=f"{self.layer.name()} andmete struktuuri uuendateakse", text1="Palun oota...", maximum=3)
        
        self.validate_layer()
        iface.setActiveLayer(self.layer)
        #print(f"Layer_name: {self.layer.name()}")
        self.layer.startEditing()
        layer_fields = self.layer.fields()
        temp_field_mapping = self.rename_fields_temporarily(layer_fields)
        self.rename_fields_to_final(layer_fields, temp_field_mapping)
        progress.update(2)

        # Apply the change using the field calculator
        
        features = list(self.layer.getFeatures())
        total = len(features)
        progress.update(maximum=total)
        for i, feature in enumerate(features, start=1):
            modified = False  # Track if we change anything

            for field_name in [Katastriyksus.siht1, Katastriyksus.siht2, Katastriyksus.siht3]:
                value = feature[field_name]
                if value is not None:
                    value_str = str(value).upper().replace(" ", "_")
                    if value_str != value:
                        feature[field_name] = value_str
                        modified = True

            if modified:
                self.layer.updateFeature(feature)

            # Update progress
            progress.update(value=i, text2=f"{i} / {total}")
            QCoreApplication.processEvents()
            
        if self.layer.commitChanges():
            #print("Stage I committed successfully.")
            pass
        else:
            heading = Headings().warningSimple
            message = "Veeru nimede uuendamisel tekkis viga."
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, message )
            print("Error committing changes.")
            progress.close()
            return
        
        self.remove_temp_suffix()
        self.add_missing_fields()
        
        progress.close()


    def rename_fields_temporarily(self, layer_fields):
        temp_field_mapping = {}
        for old_field, new_field in self.field_mapping.items():
            if layer_fields.indexFromName(old_field) != -1:
                temp_name = new_field + '_temp'
                idx = layer_fields.indexFromName(old_field)
                self.layer.renameAttribute(idx, temp_name)
                temp_field_mapping[temp_name] = new_field
                print(f"Temporarily renamed field {old_field} to {temp_name}")
        return temp_field_mapping

    def rename_fields_to_final(self, layer_fields, temp_field_mapping):
        for temp_name, new_field in temp_field_mapping.items():
            if layer_fields.indexFromName(temp_name) != -1:
                idx = layer_fields.indexFromName(temp_name)
                self.layer.renameAttribute(idx, new_field)
                print(f"Renamed field {temp_name} to {new_field}")

    def add_missing_fields(self):
        self.layer.startEditing()

        new_fields = {
            "muutpohjus": ("muutpohjus", QVariant.String, 200, "Katatastriüksuse viimane muudatus"),
            "ads_oid": ("ads_oid", QVariant.String, 200, "ADS objekti identifikaator, identifitseerib objekti läbi versioonide."),
            "adob_id": ("adob_id", QVariant.Int, 0, "Aadressiobjekti versiooni unikaalne identifikaator (unikaalne üle kõikide objektide kõikide versioonide)."),
            "oiguslik_alus": ("oiguslik_alus", QVariant.String, 1000, "Katastriüksuse viimase muudatuse õiguslik alus"),
                    }

        for field_name, (field_alias, field_type, field_length, field_comment) in new_fields.items():
#            if layer_fields.indexFromName(field_name) == -1:
            new_field = QgsField(field_name, field_type, "", field_length)
            self.layer.addAttribute(new_field)

        if self.layer.commitChanges():
            heading = Headings().infoSimple
            message = EdukuseTexts().salvestatud
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, message)
            print("Stage I committed successfully.")
            pass
        else:
            heading = Headings().infoSimple
            message = HoiatusTexts().error
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, message)
            print("Error committing changes.")
            return

    def remove_temp_suffix(self):
        self.validate_layer()

        self.layer.startEditing()
        #print("Layer editing started.")

        layer_fields = self.layer.fields()
        #print(f"Current Fields: {layer_fields.names()}")

        for field in layer_fields:
            if '_temp' in field.name():
                new_name = field.name().replace('_temp', '')
                idx = layer_fields.indexFromName(field.name())
                self.layer.renameAttribute(idx, new_name)
                #print(f"Renamed field {field.name()} to {new_name}")

        if self.layer.commitChanges():
            #print("Changes committed successfully.")
            pass
        else:
            #print("Error committing changes.")
            self.layer.rollBack()

        #print("Finished cleaning up temporary field names.")

