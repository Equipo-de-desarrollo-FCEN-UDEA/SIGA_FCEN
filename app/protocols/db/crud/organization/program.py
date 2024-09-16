from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.organization.program import Program
from app.schemas.organization.program import ProgramCreate, ProgramUpdate

class CRUDProgramProtocol(CRUDProtocol[Program, ProgramCreate, ProgramUpdate]):
    pass