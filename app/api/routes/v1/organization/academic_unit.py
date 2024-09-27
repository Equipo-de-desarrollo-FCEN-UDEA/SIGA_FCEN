from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.organization.academic_unit import AcademicUnitCreate, AcademicUnitInDB, AcademicUnitUpdate
from app.services.organization.academic_unit import academic_unit_svc
from app.api.routes.v1.utils.base_router import BaseRouter

router = APIRouter()

BaseRouter(
    schem_in_db=AcademicUnitInDB,
    schem_create=AcademicUnitCreate,
    schem_update=AcademicUnitUpdate,
    service=academic_unit_svc,
    router=router,
    methods=["create", "get-all", "get", "update"]
)