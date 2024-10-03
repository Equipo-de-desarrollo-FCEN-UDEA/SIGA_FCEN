from app.infraestructure.db.crud.mongo_base import CRUDBase
from app.infraestructure.db.models.user.type.administrative import Administrative
from app.schemas.users.type.administrative import AdministrativeCreate, AdministrativeUpdate

class AdministrativeCrud(CRUDBase[Administrative, AdministrativeCreate, AdministrativeUpdate]):
    ...


administrative_crud = AdministrativeCrud(Administrative)