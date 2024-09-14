from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate

class CRUDDepartmentProtocol(CRUDProtocol[Department, DepartmentCreate, DepartmentUpdate]):
    ...

