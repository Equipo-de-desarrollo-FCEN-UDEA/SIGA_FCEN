from fastapi import APIRouter, Depends, HTTPException

from app.schemas.school import SchoolCreate, SchoolUpdate, SchoolInDB
from app.services.school import school_svc

router = APIRouter()

@router.post("", response_model=SchoolInDB, status_code=201)
def create_school(*, new_school: SchoolCreate) -> SchoolInDB:
    school = school_svc.create(obj_in=new_school)
    return school

@router.get("", response_model=list[SchoolInDB], status_code=200)
def get_all_school(*, skip: int=0, limit: int=10) -> list[SchoolInDB]:
    return school_svc.get_multi(skip=skip, limit=limit)