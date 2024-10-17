from odmantic import Field, Model
from datetime import datetime
from uuid import UUID

from app.protocols.db.models.application.type.mobility import Process, MobilityType, MobilityPurpose

class Mobility(Model):
    id_postgres: UUID = Field(primary_field=True)
    process: str
    type: str
    purpose: str
    destination_country: str
    destination_institution: str
    date_start: datetime
    date_end: datetime
    total_time: int
    date_report: datetime