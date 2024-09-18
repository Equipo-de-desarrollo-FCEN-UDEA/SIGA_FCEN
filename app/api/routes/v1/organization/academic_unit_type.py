from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.schemas.organization.academic_unit_type import AcademicUnitTypeCreate, AcademicUnitTypeInDB, AcademicUnitTypeUpdate

from app.services.organization.academic_unit_type import academic_unit_type_svc

from app.api.routes.v1.utils.base_router import BaseRouter

router = APIRouter()

BaseRouter(
    schem_in_db=AcademicUnitTypeInDB,
    schem_create=AcademicUnitTypeCreate,
    schem_update=AcademicUnitTypeUpdate,
    service=academic_unit_type_svc,
    router=router,
    methods=["create", "get-all", "get", "update", "delete"]
)


# @router.delete("/delete/{academic_unit_type_id}", response_model=None, status_code=204)
# def delete_academic_unit_type(*, academic_unit_type_id: UUID) -> None:
#     academic_unit_type = academic_unit_type_svc.delete(academic_unit_type_id)
#     if not academic_unit_type:
#         raise HTTPException(status_code=404, detail="Academic unit type not found")
#     return JSONResponse(status_code=204, content={"message": "Academic unit type deleted"})