#DataMapperHelper.py

from ..KeelelisedMuutujad.MaaAmetFieldFormater import date_formatter_for_Mailabl_insertion
from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ..config.mylabl_API.settings import AreaUnit
from .AddressHelper import AddressHelper


class DataMapperHelper:

    @staticmethod
    def _map_properties_main_details_from_input(layer_data: dict) -> dict:

        siht1 = layer_data.get(Katastriyksus.siht1)
        #print(f"siht1 {siht1}")
        if siht1 in ("TRANSPORTIMAA", "KAITSEALUNE_MAA"):
            #print("Extracting address details from street as transpordimaa or kaitsealune maa...")
            street = layer_data.get(Katastriyksus.l_aadress)
            house_number = ""
        else:
            #print("Extracting address details from street...")
            street_data = layer_data.get(Katastriyksus.l_aadress)
            data = AddressHelper._get_address_details_from_street(street_data)
            street = data.get("street")
            house_number = data.get("house", "")


        prepared_data = {
            "immovableNumber": layer_data.get(Katastriyksus.hkood),
            "cadastralUnit": {
                "number": layer_data.get(Katastriyksus.tunnus),

                "firstRegistration": date_formatter_for_Mailabl_insertion(layer_data.get(Katastriyksus.registr)),
                "lastUpdated": date_formatter_for_Mailabl_insertion(layer_data.get(Katastriyksus.muudet))
            },
            "address": {
                "street": street,
                "houseNumber": house_number,  # Can extract this later if needed
                "city": layer_data.get(Katastriyksus.ay_nimi),
                "state": layer_data.get(Katastriyksus.ov_nimi),
                "county": layer_data.get(Katastriyksus.mk_nimi)
            },
            "area": {
                "size": layer_data.get(Katastriyksus.pindala),
                "unit": AreaUnit.M
            }
        }

        usage_data = AddressHelper._extract_intended_use_data(layer_data)
        return prepared_data, usage_data