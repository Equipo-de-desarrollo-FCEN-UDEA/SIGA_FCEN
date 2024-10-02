from enum import Enum
from uuid import UUID
from odmantic import Field, Model

class ProfessorType(str, Enum):
    VINCULADO = "vinculado"
    OCACIONAL = "ocacional"
    CATEDRATICO = "catedratico"

class Professor(Model):
    id_postgres: UUID = Field(primary_field=True) 
    type: str