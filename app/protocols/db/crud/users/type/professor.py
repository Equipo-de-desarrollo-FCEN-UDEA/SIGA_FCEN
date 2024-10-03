from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.type.professor import Professor
from app.schemas.users.type.professor import ProfessorCreate, ProfessorUpdate

class CRUDProfessorProtocol(CRUDProtocol[Professor, ProfessorCreate, ProfessorUpdate]):
    ...