from pydantic import BaseModel
from uuid import UUID


from app.schemas.users.user import UserInDB

class StudentBase(BaseModel):
    id_postgres: UUID
    semester: int

class StudentCreate(StudentBase):
    pass 

class StudentUpdate(BaseModel):
    ...

class StudentInDB(StudentBase):
    ...

class StudentResponse(UserInDB):
    student: StudentInDB