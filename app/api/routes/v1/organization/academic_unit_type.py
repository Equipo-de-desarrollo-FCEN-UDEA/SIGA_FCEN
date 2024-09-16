from fastapi import APIRouter, Depends, HTTPException

from app.schemas.organization.academic_unit_type import AcademicUnitTypeCreate, AcademicUnitTypeInDB

from app.services.organization.academic_unit_type import academic_unit_type_svc

router = APIRouter()

@router.get("", response_model=list[AcademicUnitTypeInDB], status_code=200)
def get_all_academic_unit_type(*, skip: int=0, limit: int=10) -> list[AcademicUnitTypeInDB]:
    return academic_unit_type_svc.get_multi(skip=skip, limit=limit)