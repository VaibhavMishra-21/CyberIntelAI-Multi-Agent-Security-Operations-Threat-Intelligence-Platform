class RiskAgent:

    def assess(self, classification):

        high_risk = [
            "Ransomware",
            "Credential Theft"
        ]

        medium_risk = [
            "Malware"
        ]

        if classification in high_risk:
            return "HIGH"

        elif classification in medium_risk:
            return "MEDIUM"

        return "LOW"
