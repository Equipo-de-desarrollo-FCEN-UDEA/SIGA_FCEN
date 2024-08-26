from fastapi import APIRouter, HTTPException

from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentInDB
from app.services.department import department_svc
from app.services.school import school_svc

router = APIRouter()

@router.post("", response_model=DepartmentInDB, status_code=201)
def create_deparment(*, new_department: DepartmentCreate) -> DepartmentInDB:
    department = department_svc.create(obj_in=new_department)
    return department
