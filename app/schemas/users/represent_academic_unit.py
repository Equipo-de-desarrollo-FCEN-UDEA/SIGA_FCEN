from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class RepresentAcademicUnitBase(BaseModel):
    user_id: UUID
    academic_unit_id: UUID
    
class RepresentAcademicUnitCreate(RepresentAcademicUnitBase):
    ...

class RepresentAcademicUnitUpdate(BaseModel):
    ...

class RepresentAcademicUnitDB(GeneralResponse, RepresentAcademicUnitBase):
    ...
