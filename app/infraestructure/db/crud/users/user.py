from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.users.user import User
from app.schemas.users.user import UserCreate, UserUpdate


class UserCrud(CRUDBase[User, UserCreate, UserUpdate]):
    ...


user_crud = UserCrud(User)