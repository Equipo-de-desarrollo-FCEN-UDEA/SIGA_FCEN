from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.application.user_application_academic_unit import UserApplicationAcademicUnit
from app.schemas.application.user_application import UserApplicationCreate, UserApplicationUpdate

class CRUDUserApplicationAcademicUnitProtocol(CRUDProtocol[UserApplicationAcademicUnit, UserApplicationCreate, UserApplicationUpdate]):
    pass