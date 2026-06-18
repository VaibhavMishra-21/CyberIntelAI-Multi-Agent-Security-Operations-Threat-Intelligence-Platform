from services.gemini_service import ask_gemini

class ReportAgent:

    def generate_report(
        self,
        threat_analysis,
        malware_analysis,
        risk,
        response_plan
    ):

        prompt = f"""
        Threat Analysis:
        {threat_analysis}

        Malware Analysis:
        {malware_analysis}

        Risk:
        {risk}

        Response Plan:
        {response_plan}

        Create a professional SOC report.
        """

        return ask_gemini(prompt)
