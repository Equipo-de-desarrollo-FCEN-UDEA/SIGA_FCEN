from app.services.base import ServiceBase
from app.schemas.users.represent_academic_unit import RepresentAcademicUnitCreate, RepresentAcademicUnitUpdate
from app.protocols.db.models.users.represent_academic_unit import RepresentAcademicUnit
from app.protocols.db.crud.users.represent_academic_unit import CRUDRepresentAcademicUnitProtocol

class RepresentAcademicUnitService(ServiceBase[RepresentAcademicUnit, RepresentAcademicUnitCreate, RepresentAcademicUnitUpdate, CRUDRepresentAcademicUnitProtocol]):
    ...


represent_academic_unit_svc =  RepresentAcademicUnitService()