from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse
from app.protocols.db.models.application.application_status import ApplicationStatusType

class ApplicationStatus(BaseModel):
    name: ApplicationStatusType

class ApplicationStatusCreate(ApplicationStatus):
    pass

class ApplicationStatusUpdate(BaseModel):
    name: ApplicationStatusType | None
