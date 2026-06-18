import json

class MitreService:

    @staticmethod
    def load_attack_data():

        with open(
            "threat_data/mitre_attack.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)
