from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.organization.program_type import ProgramType
from app.schemas.organization.program_type import ProgramTypeCreate, ProgramTypeUpdate

class CRUDProgramTypeProtocol(CRUDProtocol[ProgramType, ProgramTypeCreate, ProgramTypeUpdate]):
    pass