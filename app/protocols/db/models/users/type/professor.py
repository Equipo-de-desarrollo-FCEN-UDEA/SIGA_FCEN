from typing import Protocol
from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID


from enum import Enum

class ProfessorType(str, Enum):
    VINCULADO = "vinculado"
    OCACIONAL = "ocacional"
    CATEDRATICO = "catedratico"
    
class Professor(LinkModel):
    id_postgres: UUID
    type: str