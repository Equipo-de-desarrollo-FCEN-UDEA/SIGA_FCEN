from app.schemas.users.professor_type import ProfessorTypeCreate, ProfessorTypeDB, ProfessorTypeUpdate
from app.services.users.professor_type import professor_type_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from fastapi import APIRouter

router = APIRouter()

BaseRouter(
    schem_in_db=ProfessorTypeDB,
    schem_create=ProfessorTypeCreate,
    schem_update=ProfessorTypeUpdate,
    service=professor_type_svc,
    router=router,
    methods=["create", "get-all", "get", "update"]
)