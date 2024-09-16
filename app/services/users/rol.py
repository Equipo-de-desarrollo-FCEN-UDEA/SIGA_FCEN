from app.services.base import ServiceBase
from app.schemas.users.rol import RolCreate, RolUpdate
from app.protocols.db.models.users.rol import Rol
from app.protocols.db.crud.users.rol import CRUDRolProtocol

class RolService(ServiceBase[Rol, RolCreate, RolUpdate, CRUDRolProtocol]):
    ...


rol_svc = RolService()