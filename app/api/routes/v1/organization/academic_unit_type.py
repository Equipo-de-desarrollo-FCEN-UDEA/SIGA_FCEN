from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.schemas.organization.academic_unit_type import AcademicUnitTypeCreate, AcademicUnitTypeInDB, AcademicUnitTypeUpdate

from app.services.organization.academic_unit_type import academic_unit_type_svc

from uuid import UUID

router = APIRouter()

@router.post("create", response_model=AcademicUnitTypeInDB, status_code=201)
def create_academic_unit_type(*, academic_unit_type_create: AcademicUnitTypeCreate) -> AcademicUnitTypeInDB:
    return academic_unit_type_svc.create(obj_in=academic_unit_type_create)

@router.get("get_all", response_model=list[AcademicUnitTypeInDB], status_code=200)
def get_all_academic_unit_type(*, skip: int=0, limit: int=10) -> list[AcademicUnitTypeInDB]:
    return academic_unit_type_svc.get_multi(skip=skip, limit=limit)

@router.get("/get/{academic_unit_type_id}", response_model=AcademicUnitTypeInDB, status_code=200)
def get_academic_unit_type(*, academic_unit_type_id: UUID) -> AcademicUnitTypeInDB:
    academic_unit_type = academic_unit_type_svc.get(id=academic_unit_type_id)
    if academic_unit_type is None:
        raise HTTPException(status_code=404, detail="Academic unit type not found")
    return academic_unit_type

@router.patch("/update/{academic_unit_type_id}", response_model=None, status_code=200)
def update_academic_unit_type(*, academic_unit_type_id: UUID, academic_unit_type_update: AcademicUnitTypeUpdate) -> None:
    academic_unit_type_svc.update(id=academic_unit_type_id, obj_in=academic_unit_type_update)
    return  JSONResponse(status_code=200, content={"message": "Academic unit type updated"})

@router.delete("/delete/{academic_unit_type_id}", response_model=None, status_code=204)
def delete_academic_unit_type(*, academic_unit_type_id: UUID) -> None:
    academic_unit_type = academic_unit_type_svc.delete(academic_unit_type_id)
    if not academic_unit_type:
        raise HTTPException(status_code=404, detail="Academic unit type not found")
    return JSONResponse(status_code=204, content={"message": "Academic unit type deleted"})