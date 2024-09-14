from pydantic import BaseModel

from app.schemas.model import GeneralResponse

class SchoolBase(BaseModel):
    name:str
    description:str | None
    cost_center: int
    email_dean: str
    direction: str
    contact: str
    dean: str
    
    
class SchoolCreate(SchoolBase):
    ...
    
class SchoolUpdate(BaseModel):
    ...
    
class SchoolInDB(GeneralResponse, SchoolBase):
    ...
    