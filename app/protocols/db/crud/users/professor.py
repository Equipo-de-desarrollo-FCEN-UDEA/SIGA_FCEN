from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.professor import Professor
from app.schemas.users.professor import ProfessorCreate, ProfessorUpdate

class CRUDProfessorProtocol(CRUDProtocol[Professor, ProfessorCreate, ProfessorUpdate]):
    ...