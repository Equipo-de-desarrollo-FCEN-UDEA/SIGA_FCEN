from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.organization.program_type import ProgramType
from app.schemas.organization.program_type import ProgramTypeCreate, ProgramTypeUpdate

class ProgramTypeCrud(CRUDBase[ProgramType, ProgramTypeCreate, ProgramTypeUpdate]):
    pass

program_type_crud = ProgramTypeCrud(ProgramType)
