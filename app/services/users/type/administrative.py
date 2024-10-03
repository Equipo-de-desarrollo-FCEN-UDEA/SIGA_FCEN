from app.services.base import ServiceBase
from app.protocols.db.crud.users.type.administrative import CRUDAdministrativeProtocol
from app.schemas.users.type.administrative import AdministrativeCreate, AdministrativeUpdate
from app.protocols.db.models.users.type.administrative import Administrative

class AdministrativeService(ServiceBase[Administrative, AdministrativeCreate, AdministrativeUpdate, CRUDAdministrativeProtocol]):
    ...


administrative_svc = AdministrativeService()