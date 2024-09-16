from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse

class AcademicUnitBase(BaseModel):
    name:str
    description: str
    academic_unit_type_id: UUID
    
class AcademicUnitCreate(AcademicUnitBase):
    ...
    
class AcademicUnitUpdate(BaseModel):
    ...
    
class AcademicUnitInDB(GeneralResponse, AcademicUnitBase):
    ...
    