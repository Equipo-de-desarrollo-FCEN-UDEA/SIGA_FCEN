from app.services.base import ServiceBase
from app.schemas.users.administrative import AdministrativeCreate, AdministrativeUpdate
from app.protocols.db.models.users.administrative import Administrative
from app.protocols.db.crud.users.administrative import CRUDAdministrativeProtocol

class AdministrativeService(ServiceBase[Administrative, AdministrativeCreate, AdministrativeUpdate, CRUDAdministrativeProtocol]):
    ...

administrative_svc =  AdministrativeService()