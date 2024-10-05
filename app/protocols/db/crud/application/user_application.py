from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.application.user_application import UserApplication
from app.schemas.application.user_application import UserApplicationCreate, UserApplicationUpdate

class CRUDUserApplicationProtocol(CRUDProtocol[UserApplication, UserApplicationCreate, UserApplicationUpdate]):
    ...