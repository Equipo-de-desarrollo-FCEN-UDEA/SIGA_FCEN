from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.application.user_application import UserApplication
from app.schemas.application.user_application import UserApplicationCreate, UserApplicationUpdate

class UserApplicationCrud(CRUDBase[UserApplication, UserApplicationCreate, UserApplicationUpdate]):
    pass

user_application_crud = UserApplicationCrud(UserApplication)