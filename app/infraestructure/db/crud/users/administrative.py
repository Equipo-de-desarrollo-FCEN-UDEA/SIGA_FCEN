from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.users.administrative import Administrative
from app.schemas.users.administrative import AdministrativeCreate, AdministrativeUpdate


class AdministrativeCrud(CRUDBase[Administrative, AdministrativeCreate, AdministrativeUpdate]):
    ...


administrative_crud = AdministrativeCrud(Administrative)