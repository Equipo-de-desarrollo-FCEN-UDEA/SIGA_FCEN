from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class UserRolBase(BaseModel):
    rol_id: int
    user_id: int
    observation:str
    
    
class UserRolCreate(UserRolBase):
    ...
    
class UserRolUpdate(BaseModel):
    ...
    
class UserRolInDB(GeneralResponse, UserRolBase):
    ...