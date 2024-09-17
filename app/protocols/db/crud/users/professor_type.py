from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.professor_type import ProfessorType
from app.schemas.users.professor_type import ProfessorTypeCreate, ProfessorTypeUpdate

class CRUDProfessorTypeProtocol(CRUDProtocol[ProfessorType, ProfessorTypeCreate, ProfessorTypeUpdate]):
    ...