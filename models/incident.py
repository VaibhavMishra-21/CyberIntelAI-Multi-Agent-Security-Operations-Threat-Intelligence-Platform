from pydantic import BaseModel

class Incident(BaseModel):

    incident_id: str

    threat_type: str

    risk_score: float

    recommendation: str
