from services.gemini_service import ask_gemini

class ThreatIntelAgent:

    def analyze(self, alert):

        prompt = f"""
        Analyze this security alert:

        {alert}

        Identify:

        1. Threat Type
        2. Possible Attack Vector
        3. Likely Impact
        """

        return ask_gemini(prompt)
