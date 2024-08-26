from app.protocols.db.models.school import School
from app.protocols.db.crud.school import CRUDSchoolProtocol

from app.services.base import ServiceBase
from app.schemas.school import SchoolCreate, SchoolUpdate

class SchoolService(ServiceBase[School, SchoolCreate, SchoolUpdate, CRUDSchoolProtocol]):
    ...

school_svc = SchoolService()