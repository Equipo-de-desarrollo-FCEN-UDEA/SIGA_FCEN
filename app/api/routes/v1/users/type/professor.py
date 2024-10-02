from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.schemas.users.type.professor import ProfessorCreate, ProfessorUpdate, ProfessorInDB, ProfessorResponse
from app.infraestructure.db.models.user.type.professor import Professor
from app.schemas.users.user import UserInDB
from app.services.users.type.professor import professor_svc
from app.services.users.user import user_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from app.api.middleware.mongo_db import get_mongo_db
from app.api.middleware.postgres_db import get_db


router = APIRouter()

@router.post("/create", response_model=ProfessorInDB, status_code=201)
async def create_professor(*, obj_in: ProfessorCreate, db = Depends(get_mongo_db)) -> ProfessorInDB:
    try:
        professor_create = await professor_svc.create(obj_in=Professor(**dict(obj_in)), db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return professor_create

@router.get("/get/{id}", response_model=ProfessorResponse, status_code=200)
async def get_professor(*, 
                        id: UUID, 
                        mongo_db = Depends(get_mongo_db), 
                        postgres_db= Depends(get_db)) -> ProfessorResponse:
    professor = await professor_svc.get(id=id, db=mongo_db)
    if not professor:
        raise HTTPException(404, "Professor not found")
    user_in_db = user_svc.get(id=professor.id_postgres, db=postgres_db)
    user = UserInDB.model_validate(user_in_db)
    professor_dict = professor.dict()
    response = ProfessorResponse(
        **dict(user),
        professor=professor_dict
    )
    
    return response

@router.get("/get-all", response_model=list[ProfessorInDB], status_code=200)
async def get_all_professor(*, mongo_db = Depends(get_mongo_db)) -> list[ProfessorInDB]:
    return await professor_svc.get_multi(db=mongo_db)
