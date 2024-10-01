from pydantic import BaseModel
from uuid import UUID


from app.schemas.utils.base_model import GeneralResponse

class StudentBase(BaseModel):
    id_postgres: UUID
    semester: int

class StudentCreate(StudentBase):
    pass 

class StudentUpdate(BaseModel):
    ...

class StudentInDB(StudentBase):
    pass