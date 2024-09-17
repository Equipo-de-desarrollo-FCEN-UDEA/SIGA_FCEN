from app.services.base import ServiceBase
from app.schemas.users.administrative_type import AdministrativeTypeCreate, AdministrativeTypeUpdate
from app.protocols.db.models.users.administrative_type import AdministrativeType
from app.protocols.db.crud.users.administrative_type import CRUDAdministrativeTypeProtocol

class AdministrativeTypeService(ServiceBase[AdministrativeType, AdministrativeTypeCreate, AdministrativeTypeUpdate, CRUDAdministrativeTypeProtocol]):
    ...


administrative_type_svc =  AdministrativeTypeService()