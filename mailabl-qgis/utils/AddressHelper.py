#AddressHelper.py

from ..KeelelisedMuutujad.Maa_amet_fields import Katastriyksus

import re


class AddressHelper:
    @staticmethod
    def _get_address_details_from_street(street: str) -> dict:
        data = {}
         # Handle None, QVariant, "NULL", etc.
        if not street or str(street).upper() == "NULL":
            data['street'] = ""
            data['house'] = ""
            return data

        # 💡 Case: building-like code (e.g., "L1", "T2")
        if re.fullmatch(r'^[A-Za-z]{1,2}\d{1,2}$', street):
            #print("📦 Detected building-like code → treat as full street")
            data['street'] = street
            return data

        # 💡 Check for street + number (or fancy house number)
        match = re.match(r'^(.*?)(\d+.*)$', street)
        if match:
            possible_street = match.group(1).strip()
            possible_house = match.group(2).strip()
            #print(f"🔧 Regex match → street: '{possible_street}', house: '{possible_house}'")

            if re.match(r'^\d+', possible_house):
                #print("✅ House part starts with number → valid house number")
                data['street'] = possible_street
                data['house'] = possible_house
            else:
                #print("⚠️ House part doesn't start with number → fallback to full string as street")
                data['street'] = street
        else:
            #print("❌ No match found → fallback to full string as street")
            data['street'] = street

        #print(f"✅ Final parsed result: {data}")
        return data

    @staticmethod
    def _extract_intended_use_data(layer_data: dict) -> dict:
        usage_data = []
        num_siht_items = 3

        siht_field = Katastriyksus.siht1
        prts_field = Katastriyksus.so_prts1
        siht_base = siht_field[:-1]
        prts_base = prts_field[:-1]

        for i in range(1, num_siht_items + 1):
            siht_name = f"{siht_base}{i}"
            so_prts_name = f"{prts_base}{i}"

            purpouse = layer_data.get(siht_name)

            # ✅ Skip immediately if siht_name is empty or null
            if not purpouse or str(purpouse).strip().upper() == "NULL":
                continue

            so_prts_data = layer_data.get(so_prts_name)

            intended_use = {
                "sortOrder": i,
                "name": AddressHelper._normalize_purpose_name(purpouse),
                "percentage": so_prts_data,
            }

            usage_data.append(intended_use)

        return usage_data

    @staticmethod
    def _normalize_purpose_name(raw_name: str) -> str:
        if not raw_name:
            return ""

        # Step 1: Lowercase and replace underscores
        raw_name = raw_name.replace("_", " ").lower().strip()

        # Step 2: Split into words
        words = raw_name.split()

        # Step 3: Capitalize only the first word
        if words:
            words[0] = words[0].capitalize()

        # Step 4: Optional Estonian mapping on first word
        estonian_fixes = {
            "Uhiskondlike": "Ühiskondlike",
            "Toostusmaa": "Tööstusmaa",
            "Jaatmehoidla": "Jäätmehoidla",
            "Maetoostusmaa": "Mäetööstusmaa",
            "Turbatoostusmaa": "Turbatööstsmaa",
            "üldkastutatav": "üldkasutatav"
            # Add more if needed
        }


        for word in words:
            word = estonian_fixes.get(word)

        return " ".join(words)