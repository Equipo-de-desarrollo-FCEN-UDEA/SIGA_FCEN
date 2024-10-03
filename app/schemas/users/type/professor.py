from enum import Enum
from pydantic import BaseModel
from uuid import UUID

from app.schemas.users.user import UserInDB


class ProfessorType(str, Enum):
    VINCULADO = "vinculado"
    OCACIONAL = "ocacional"
    CATEDRATICO = "catedratico"

class ProfessorBase(BaseModel):
    id_postgres: UUID
    type: ProfessorType

class ProfessorCreate(ProfessorBase):
    ... 

class ProfessorUpdate(BaseModel):
    ...

class ProfessorInDB(ProfessorBase):
    ...

class ProfessorResponse(UserInDB):
    professor: ProfessorInDB