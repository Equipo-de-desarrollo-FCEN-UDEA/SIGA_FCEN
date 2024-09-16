from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.users.rol import Rol
from app.schemas.users.rol import RolCreate, RolUpdate


class UserCrud(CRUDBase[Rol, RolCreate, RolUpdate]):
    ...


rol_crud = UserCrud(Rol)