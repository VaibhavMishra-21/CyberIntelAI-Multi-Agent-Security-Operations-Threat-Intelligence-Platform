from pydantic import BaseModel

class Alert(BaseModel):

    alert_id: str

    source: str

    severity: str

    description: str
