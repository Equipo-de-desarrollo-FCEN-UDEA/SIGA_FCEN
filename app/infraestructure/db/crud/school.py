from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import School
from app.schemas.school import SchoolCreate, SchoolUpdate

class SchoolCrud(CRUDBase[School, SchoolCreate, SchoolUpdate]):
    ...

school_crud = SchoolCrud(School)