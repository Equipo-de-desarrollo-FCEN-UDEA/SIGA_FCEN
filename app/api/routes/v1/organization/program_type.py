from app.schemas.organization.program_type import ProgramTypeCreate, ProgramTypeInDB, ProgramTypeUpdate
from app.services.organization.program_type import program_type_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from fastapi import APIRouter

router = APIRouter()

BaseRouter(
    schem_in_db=ProgramTypeInDB,
    schem_create=ProgramTypeCreate,
    schem_update=ProgramTypeUpdate,
    service=program_type_svc,
    router=router,
    methods=["create", "get-all", "get", "update"]
)