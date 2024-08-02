from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.school import School
from app.schemas.school import SchoolCreate, SchoolUpdate

class CRUDSchoolProtocol(CRUDProtocol[School, SchoolCreate, SchoolUpdate]):
    ...