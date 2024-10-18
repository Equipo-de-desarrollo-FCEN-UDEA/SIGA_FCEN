from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse

class VotingBase(BaseModel):
    academic_unit_id: UUID
    application_id: UUID

class VotingCreate(VotingBase):
    pass

class VotingUpdate(BaseModel):
    academic_unit_id: UUID | None
    application_id: UUID | None