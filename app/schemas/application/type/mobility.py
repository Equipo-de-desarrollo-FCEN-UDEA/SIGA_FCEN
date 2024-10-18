from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.protocols.db.models.application.type.mobility import Process, MobilityType, MobilityPurpose

class Status(BaseModel):
    name: str
    updated_by: str
    date: datetime

class MobilityBase(BaseModel):
    id_postgres: UUID | None = None
    process: Process
    type: MobilityType
    purpose: MobilityPurpose
    destination_country: str
    destination_institution: str
    date_start: datetime
    date_end: datetime
    total_time: int #tiempo total en meses
    date_report: datetime
    status: list[Status] | None = []

class MobilityCreate(MobilityBase):
    pass

class MobilityUpdate(BaseModel):
    process: Process | None = None
    type: MobilityType | None = None
    purpose: MobilityPurpose | None = None
    destination_country: str | None = None
    destination_institution: str | None = None
    date_start: datetime | None = None
    date_end: datetime | None = None
    total_time: int | None = None
    date_report: datetime | None = None
    
