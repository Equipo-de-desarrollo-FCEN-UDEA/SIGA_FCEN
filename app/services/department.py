from app.protocols.db.models.department import Department
from app.protocols.db.crud.deparment import CRUDDepartmentProtocol

from app.services.base import ServiceBase
from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentInDB

class DepartmentService(ServiceBase[Department, DepartmentCreate, DepartmentUpdate, CRUDDepartmentProtocol]):
    ...

department_svc = DepartmentService()                                
