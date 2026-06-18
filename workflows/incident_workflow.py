from agents.alert_agent import AlertAgent
from agents.threat_intel_agent import ThreatIntelAgent
from agents.malware_agent import MalwareAgent
from agents.risk_agent import RiskAgent
from agents.incident_agent import IncidentAgent
from agents.report_agent import ReportAgent
from agents.supervisor_agent import SupervisorAgent

from agents.mitre_agent import MitreAgent
from agents.ioc_agent import IOCAgent
from agents.threat_hunting_agent import ThreatHuntingAgent

from services.report_service import ReportService


alert_agent = AlertAgent()

threat_agent = ThreatIntelAgent()

malware_agent = MalwareAgent()

risk_agent = RiskAgent()

incident_agent = IncidentAgent()

report_agent = ReportAgent()

supervisor_agent = SupervisorAgent()

mitre_agent = MitreAgent()

ioc_agent = IOCAgent()

hunting_agent = ThreatHuntingAgent()


def run_incident_workflow(alert):

    classification = alert_agent.classify(alert)

    threat_analysis = threat_agent.analyze(alert)

    malware_analysis = malware_agent.investigate(alert)

    risk = risk_agent.assess(classification)

    mitre = mitre_agent.map_attack(
        classification
    )

    iocs = ioc_agent.extract(alert)

    hunting = hunting_agent.hunt(alert)

    response_plan = (
        incident_agent.create_response_plan(
            classification,
            risk
        )
    )

    report = report_agent.generate_report(
        threat_analysis,
        malware_analysis,
        risk,
        response_plan
    )

    validation = (
        supervisor_agent.validate(risk)
    )

    report_file = (
        ReportService.save_report(
            report
        )
    )

    return {
        "classification": classification,
        "risk": risk,
        "mitre": mitre,
        "iocs": iocs,
        "threat_hunting": hunting,
        "response_plan": response_plan,
        "report": report,
        "validation": validation,
        "report_file": report_file
    }
