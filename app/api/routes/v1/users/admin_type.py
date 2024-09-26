from app.schemas.users.administrative_type import AdministrativeTypeCreate, AdministrativeTypeDB, AdministrativeTypeUpdate
from app.services.users.administrative_type import administrative_type_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from fastapi import APIRouter

router = APIRouter()

BaseRouter(
    schem_in_db=AdministrativeTypeDB,
    schem_create=AdministrativeTypeCreate,
    schem_update=AdministrativeTypeUpdate,
    service=administrative_type_svc,
    router=router,
    methods=["create", "get-all", "get", "update"]
)