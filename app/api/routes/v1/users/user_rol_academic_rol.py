from fastapi import APIRouter, Depends, HTTPException
from app.api.middleware.postgres_db import get_db

from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnitCreate, UserRolAcademicUnitInDB
from app.services.users.user_rol_academic_unit import user_rol_academic_unit_svc

router = APIRouter()

@router.post("", response_model=UserRolAcademicUnitInDB, status_code=201)
def create_user_rol(*, new_user_rol: UserRolAcademicUnitCreate, db_postgres = Depends(get_db)) -> UserRolAcademicUnitInDB:
    return user_rol_academic_unit_svc.create(obj_in=new_user_rol, db=db_postgres)

@router.get("", response_model=list[UserRolAcademicUnitInDB], status_code=200)
def get_all_rol(*, skip: int=0, limit: int=10, db_postgres = Depends(get_db))-> list[UserRolAcademicUnitInDB]:
    return user_rol_academic_unit_svc.get_multi(skip=skip, limit=limit, db=db_postgres)