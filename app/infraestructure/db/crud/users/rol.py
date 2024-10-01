from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.user.rol import Rol
from app.schemas.users.rol import RolCreate, RolUpdate


class UserCrud(CRUDBase[Rol, RolCreate, RolUpdate]):
    ...


rol_crud = UserCrud(Rol)