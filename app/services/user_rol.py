from app.services.base import ServiceBase
from app.schemas.users.user_rol import UserRolCreate, UserRolUpdate, UserRolInDB
from app.protocols.db.models.users.user_rol import UserRol
from app.protocols.db.crud.users.user_rol import CRUDUserRolProtocol

class UserRolService(ServiceBase[UserRol, UserRolCreate, UserRolUpdate, CRUDUserRolProtocol]):
    ...

user_rol_svc = UserRolService()
