from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.represent_academic_unit import RepresentAcademicUnit
from app.schemas.users.represent_academic_unit import RepresentAcademicUnitCreate, RepresentAcademicUnitUpdate

class CRUDRepresentAcademicUnitProtocol(CRUDProtocol[RepresentAcademicUnit, RepresentAcademicUnitCreate, RepresentAcademicUnitUpdate]):
    ...