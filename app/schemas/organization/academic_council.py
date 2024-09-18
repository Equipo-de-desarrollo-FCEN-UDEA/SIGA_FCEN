from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse

class AcademicCouncilBase(BaseModel):
    name: str
    description: str | None
    academic_unit_id: UUID

class AcademicCouncilCreate(AcademicCouncilBase):
    pass

class AcademicCouncilUpdate(BaseModel):
    name: str | None
    description: str | None

class AcademicCouncilInDB(GeneralResponse, AcademicCouncilBase):
    pass