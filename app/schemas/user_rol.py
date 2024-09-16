from pydantic import BaseModel

<<<<<<< HEAD:app/schemas/user_rol.py
from app.schemas.model import GeneralResponse
=======
from app.schemas.utils.base_model import GeneralResponse
>>>>>>> develop:app/schemas/users/user_rol.py

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