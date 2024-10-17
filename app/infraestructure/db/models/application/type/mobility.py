from odmantic import Field, Model
from datetime import datetime
from uuid import UUID

from app.protocols.db.models.application.type.mobility import Process, MobilityType, MobilityPurpose

class Mobility(Model):
    id_postgres: UUID = Field(primary_field=True)
    proccess: Process
    type: MobilityType
    purpose: MobilityPurpose
    destination_country: str
    destination_institution: str
    date_start: datetime
    date_end: datetime
    total_time: int
    date_report: datetime