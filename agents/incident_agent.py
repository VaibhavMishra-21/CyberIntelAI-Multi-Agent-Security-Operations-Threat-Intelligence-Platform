from services.gemini_service import ask_gemini

class IncidentAgent:

    def create_response_plan(
        self,
        threat,
        risk
    ):

        prompt = f"""
        Threat:

        {threat}

        Risk Level:

        {risk}

        Generate:

        1. Containment Steps
        2. Eradication Steps
        3. Recovery Steps
        """

        return ask_gemini(prompt)
