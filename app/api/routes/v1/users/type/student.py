from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.schemas.users.type.student import StudentCreate, StudentUpdate, StudentInDB, StudentResponse
from app.schemas.users.user import UserInDB
from app.infraestructure.db.models.user.type.student import Student
from app.services.users.type.student import student_svc
from app.services.users.user import user_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from app.api.middleware.mongo_db import get_mongo_db
from app.api.middleware.postgres_db import get_db


router = APIRouter()

@router.post("/create", response_model=StudentInDB, status_code=201)
async def create_student(*, obj_in: StudentCreate, db = Depends(get_mongo_db)) -> StudentInDB:
    try:
        student_create = await student_svc.create(obj_in=Student(**dict(obj_in)), db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return student_create

@router.get("/get/{id}", response_model=StudentResponse, status_code=200)
async def get_student(*, id: UUID, mongo_db = Depends(get_mongo_db), postgres_db = Depends(get_db)) -> StudentResponse:
    student = await student_svc.get(id=id, db=mongo_db)
    if not student:
        raise HTTPException(404, "Student not found")
    
    user_in_db = user_svc.get(id=student.id_postgres, db=postgres_db)

    user = UserInDB.model_validate(user_in_db)
    print(f"USUARIO: {user}")

    student_dict = student.dict()  # Convertir la instancia de Student a un diccionario

    response = StudentResponse(
        **dict(user),
        student=student_dict  # Pasar el diccionario en lugar de la instancia
    )
    
    return response

@router.get("/get-all", response_model=list[StudentInDB], status_code=200)
async def get_all_student(*, mongo_db = Depends(get_mongo_db)) -> list[StudentInDB]:
    return await student_svc.get_multi(db=mongo_db)