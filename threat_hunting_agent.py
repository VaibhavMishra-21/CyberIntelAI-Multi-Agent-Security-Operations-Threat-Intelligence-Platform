from services.gemini_service import ask_gemini


class ThreatHuntingAgent:

    def hunt(self, alert):

        prompt = f"""
        Security Alert:

        {alert}

        Suggest:

        1. Additional logs to inspect
        2. Threat hunting queries
        3. Related indicators
        """

        return ask_gemini(prompt)
