from app.services.base import ServiceBase
from app.schemas.application.user_application import UserApplicationCreate, UserApplicationUpdate
from app.protocols.db.models.application.user_application import UserApplication
from app.protocols.db.crud.application.user_application import CRUDUserApplicationProtocol

class UserApplicationService(ServiceBase[UserApplication, UserApplicationCreate, UserApplicationUpdate, CRUDUserApplicationProtocol]):
    pass

user_application_svc = UserApplicationService()

