from app.infraestructure.db.crud.mongo_base import CRUDBase
from app.infraestructure.db.models.user.type.professor import Professor
from app.schemas.users.type.professor import ProfessorCreate, ProfessorUpdate

class ProfessorCrud(CRUDBase[Professor, ProfessorCreate, ProfessorUpdate]):
    ...


professor_crud = ProfessorCrud(Professor)