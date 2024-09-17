from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.administrative_type import AdministrativeType
from app.schemas.users.administrative_type import AdministrativeTypeCreate, AdministrativeTypeUpdate

class CRUDAdministrativeTypeProtocol(CRUDProtocol[AdministrativeType, AdministrativeTypeCreate, AdministrativeTypeUpdate]):
    ...