from pydantic import BaseModel

from app.schemas.model import GeneralResponse

class DepartmentBase(BaseModel):
    name:str
    description:str | None
    coord_email:str
    school_id:int
    cost_center:str | None
    director:str | None
    
class DepartmentCreate(DepartmentBase):
    ...
    
class DepartmentUpdate(BaseModel):
    ...
    
class DepartmentInDB(GeneralResponse, DepartmentBase):
    ...