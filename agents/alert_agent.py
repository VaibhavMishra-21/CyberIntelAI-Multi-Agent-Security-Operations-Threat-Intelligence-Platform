class AlertAgent:

    def classify(self, alert):

        alert = alert.lower()

        if "ransomware" in alert:

            return "Ransomware"

        elif "phishing" in alert:

            return "Phishing"

        elif "malware" in alert:

            return "Malware"

        elif "credential" in alert:

            return "Credential Theft"

        return "Unknown Threat"
