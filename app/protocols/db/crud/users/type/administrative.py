from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.type.administrative import Administrative
from app.schemas.users.type.administrative import AdministrativeCreate, AdministrativeUpdate

class CRUDAdministrativeProtocol(CRUDProtocol[Administrative, AdministrativeCreate, AdministrativeUpdate]):
    ...