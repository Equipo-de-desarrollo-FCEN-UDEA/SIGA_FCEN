from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.organization.program import Program
from app.schemas.organization.program import ProgramCreate, ProgramUpdate

class ProgramCrud (CRUDBase[Program, ProgramCreate, ProgramUpdate]):
    pass

program_crud = ProgramCrud(Program)
    