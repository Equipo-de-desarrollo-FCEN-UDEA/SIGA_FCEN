from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class UserRolAcademicUnitBase(BaseModel):
    rol_id: UUID
    user_id: UUID
    academic_unit_id: UUID
    is_active: bool| None = True
    
    
class UserRolAcademicUnitCreate(UserRolAcademicUnitBase):
    ...
    
class UserRolAcademicUnitUpdate(BaseModel):
    ...
    
class UserRolAcademicUnitInDB(GeneralResponse, UserRolAcademicUnitBase):
    ...

class UserRolAcademicUnit(UserRolAcademicUnitBase):
    id: UUID
    
    class Config:
        orm_mode = True