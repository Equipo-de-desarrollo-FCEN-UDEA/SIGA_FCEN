from fastapi import APIRouter, Depends, HTTPException

from app.schemas.users.type.student import StudentCreate, StudentUpdate, StudentInDB
from app.infraestructure.db.models.user.type.student import Student
from app.services.users.type.student import student_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from app.api.middleware.mongo_db import get_mongo_db


router = APIRouter()

@router.post("/create", response_model=StudentInDB, status_code=201)
async def create_student(*, obj_in: StudentCreate, db = Depends(get_mongo_db)) -> StudentInDB:
    try:
        student_create = await student_svc.create(obj_in=Student(**dict(obj_in)), db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return student_create
