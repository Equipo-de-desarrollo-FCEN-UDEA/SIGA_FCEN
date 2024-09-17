from app.services.base import ServiceBase
from app.schemas.users.professor import ProfessorCreate, ProfessorUpdate
from app.protocols.db.models.users.professor import Professor
from app.protocols.db.crud.users.professor import CRUDProfessorProtocol

class ProfessorService(ServiceBase[Professor, ProfessorCreate, ProfessorUpdate, CRUDProfessorProtocol]):
    ...


professor_svc =  ProfessorService()