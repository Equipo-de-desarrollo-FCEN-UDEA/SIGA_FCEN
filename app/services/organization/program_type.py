from app.services.base import ServiceBase
from app.schemas.organization.program_type import ProgramTypeCreate, ProgramTypeUpdate
from app.protocols.db.models.organization.program_type import ProgramType
from app.protocols.db.crud.organization.program_type import CRUDProgramTypeProtocol

class ProgramTypeService(ServiceBase[ProgramType, ProgramTypeCreate, ProgramTypeUpdate, CRUDProgramTypeProtocol]):
    pass

program_type_svc = ProgramTypeService()