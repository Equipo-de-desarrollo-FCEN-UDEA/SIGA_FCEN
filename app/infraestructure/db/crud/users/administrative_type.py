from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.users.administrative_type import AdministrativeType
from app.schemas.users.administrative_type import AdministrativeTypeCreate, AdministrativeTypeUpdate


class AdministrativeTypeCrud(CRUDBase[AdministrativeType, AdministrativeTypeCreate, AdministrativeTypeUpdate]):
    ...


administrative_type_crud = AdministrativeTypeCrud(AdministrativeType)