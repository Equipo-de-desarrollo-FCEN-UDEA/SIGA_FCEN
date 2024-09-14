from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.rol import Rol
from app.schemas.users.rol import RolCreate, RolUpdate

class CRUDRolProtocol(CRUDProtocol[Rol, RolCreate, RolUpdate]):
    ...