from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse
from app.protocols.db.models.application.application import ApplicationType

class ApplicationBase(BaseModel):
    name: ApplicationType
    description: str
    academic_unit_id: UUID

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    name: ApplicationType | None
    description: str | None
    academic_unit_id: UUID | None
