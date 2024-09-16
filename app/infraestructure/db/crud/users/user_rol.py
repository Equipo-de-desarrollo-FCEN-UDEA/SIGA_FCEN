from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.users.user_rol import UserRol
from app.schemas.users.user_rol import UserRolCreate, UserRolUpdate

class UserRolCrud(CRUDBase[UserRol, UserRolCreate, UserRolUpdate]):
    ...
    
user_rol_crud = UserRolCrud(UserRol)