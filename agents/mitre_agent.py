from services.mitre_service import MitreService


class MitreAgent:

    def map_attack(self, classification):

        data = MitreService.load_attack_data()

        return data.get(
            classification,
            {
                "technique": "Unknown",
                "name": "Unknown"
            }
        )
