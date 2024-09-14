from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate


class DepartmentCrud(CRUDBase[Department, DepartmentCreate, DepartmentUpdate]):
    ...
    
department_crud = DepartmentCrud(Department)