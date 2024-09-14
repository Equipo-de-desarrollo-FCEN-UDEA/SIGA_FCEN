from pydantic import BaseModel
from uuid import UUID

from app.schemas.base_model import GeneralResponse

class AcademicUnitBase(BaseModel):
    name: str
    description: str | None

class AcademicUnitCreate(AcademicUnitBase):
    ...

class AcademicUnitUpdate(BaseModel):
    academic_unit_type_id: UUID
    academic_unit_id: UUID