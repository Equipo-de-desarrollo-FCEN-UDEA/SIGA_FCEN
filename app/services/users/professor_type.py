from app.services.base import ServiceBase
from app.schemas.users.professor_type import ProfessorTypeCreate, ProfessorTypeUpdate
from app.protocols.db.models.users.professor_type import ProfessorType
from app.protocols.db.crud.users.professor_type import CRUDProfessorTypeProtocol

class ProfessorTypeService(ServiceBase[ProfessorType, ProfessorTypeCreate, ProfessorTypeUpdate, CRUDProfessorTypeProtocol]):
    ...


professor_type_svc =  ProfessorTypeService()