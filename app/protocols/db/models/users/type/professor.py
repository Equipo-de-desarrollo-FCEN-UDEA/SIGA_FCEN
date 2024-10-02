from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID
from enum import Enum

class ProfessorType(str, Enum):
    VINCULADO = "vinculado"
    OCACIONAL = "ocacional"
    CATEDRATICO = "catedratico"

class Position(str, Enum):
    AUXILIAR = "auxiliar"
    ASISTENTE = "asistente"
    ASOCIADO = "asociado"
    TITULAR = "titular"
    
class Professor(LinkModel):
    id_postgres: UUID
    type: ProfessorType
    position: Position