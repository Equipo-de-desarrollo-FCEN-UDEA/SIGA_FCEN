from fastapi import APIRouter, Depends, HTTPException

from app.schemas.rol import RolCreate, RolUpdate, RolInDB
from app.services.rol import rol_svc

router = APIRouter()

@router.post("", response_model=RolInDB, status_code=201)
def create_rol(*, new_rol: RolCreate) -> RolInDB:
    rol= rol_svc.create(obj_in=new_rol)
    return rol

@router.get("", response_model=list[RolInDB], status_code=200)
def get_all_rol(*, skip: int=0, limit: int=10) -> list[RolInDB]:
    return rol_svc.get_multi(skip=skip, limit=limit)

