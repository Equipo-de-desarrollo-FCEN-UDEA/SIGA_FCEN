from app.services.base import ServiceBase
from app.protocols.db.crud.users.type.professor import CRUDProfessorProtocol
from app.schemas.users.type.professor import ProfessorCreate, ProfessorUpdate
from app.protocols.db.models.users.type.professor import Professor

class ProfessorService(ServiceBase[Professor, ProfessorCreate, ProfessorUpdate, CRUDProfessorProtocol]):
    ...


professor_svc = ProfessorService()