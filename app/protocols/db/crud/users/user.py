from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.user import User
from app.schemas.users.user import UserCreateInDB, UserUpdate


class CRUDUserProtocol(CRUDProtocol[User, UserCreateInDB, UserUpdate]):
    def get_by_email(self, *, email: str) -> User:
        ...