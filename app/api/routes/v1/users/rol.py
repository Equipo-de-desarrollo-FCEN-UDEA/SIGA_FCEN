from fastapi import APIRouter, Depends, HTTPException

from app.schemas.users.rol import RolCreate, RolUpdate, RolInDB
from app.services.users.rol import rol_svc
from app.api.routes.v1.utils.base_router import BaseRouter


router = APIRouter()

BaseRouter(
    schem_in_db=RolInDB,
    schem_create=RolCreate,
    schem_update=RolUpdate,
    service=rol_svc,
    router=router,
    methods=["create", "get-all", "get", "update"]
)


# @router.post("", response_model=RolInDB, status_code=201)
# def create_rol(*, new_rol: RolCreate) -> RolInDB:
#     print(new_rol)
#     rol= rol_svc.create(obj_in=new_rol)
#     return rol

# @router.get("", response_model=list[RolInDB], status_code=200)
# def get_all_rol(*, skip: int=0, limit: int=10) -> list[RolInDB]:
#     return rol_svc.get_multi(skip=skip, limit=limit)

