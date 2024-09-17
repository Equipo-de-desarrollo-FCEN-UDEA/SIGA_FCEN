from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class StudentBase(BaseModel):
    user_id: UUID
    program_id: UUID
    
class StudentCreate(StudentBase):
    ...

class StudentUpdate(BaseModel):
    ...

class StudentDB(GeneralResponse, StudentBase):
    ...

