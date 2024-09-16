from app.services.base import ServiceBase
from app.schemas.organization.program import ProgramCreate, ProgramUpdate
from app.protocols.db.models.organization.program import Program
from app.protocols.db.crud.organization.program import CRUDProgramProtocol

class ProgramService(ServiceBase[Program, ProgramCreate, ProgramUpdate, CRUDProgramProtocol]):
    pass

program_svc = ProgramService()