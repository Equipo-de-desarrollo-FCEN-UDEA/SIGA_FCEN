from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.administrative import Administrative
from app.schemas.users.administrative import AdministrativeCreate, AdministrativeUpdate

class CRUDAdministrativeProtocol(CRUDProtocol[Administrative, AdministrativeCreate, AdministrativeUpdate]):
    ...