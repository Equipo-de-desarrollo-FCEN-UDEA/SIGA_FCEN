from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse
from app.protocols.db.models.application.application_status import ApplicationStatusType

class ApplicationStatus(BaseModel):
    user_application_id: UUID
    status: str

class ApplicationStatusCreate(ApplicationStatus):
    pass

class ApplicationStatusUpdate(BaseModel):
    user_application_id: UUID | None = None
    status: str | None = None
