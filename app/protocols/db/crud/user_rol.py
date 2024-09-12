from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.user_rol import UserRol
from app.schemas.user_rol import UserRolCreate, UserRolUpdate

class CRUDUserRolProtocol(CRUDProtocol[UserRol, UserRolCreate, UserRolUpdate]):
    ...