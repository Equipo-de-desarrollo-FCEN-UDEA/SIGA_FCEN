from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse

class AcademicUnitBase(BaseModel):
    name:str
    email: str
    academic_unit_id: UUID | None = None
    academic_unit_type_id: UUID
    
class AcademicUnitCreate(AcademicUnitBase):
    ...
    
class AcademicUnitUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    academic_unit_id: UUID | None = None
    academic_unit_type_id: UUID | None = None
    
class AcademicUnitInDB(GeneralResponse, AcademicUnitBase):
    ...
    
class AcademicUnit(BaseModel):
    name: str
    
    class Config:
        orm_mode = True
        from_attributes = True