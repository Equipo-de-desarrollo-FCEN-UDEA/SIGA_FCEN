from app.services.base import ServiceBase
from app.schemas.user_rol import UserRolCreate, UserRolUpdate, UserRolInDB
from app.protocols.db.models.user_rol import UserRol
from app.protocols.db.crud.user_rol import CRUDUserRolProtocol

class UserRolService(ServiceBase[UserRol, UserRolCreate, UserRolUpdate, CRUDUserRolProtocol]):
    ...

user_rol_svc = UserRolService()
