from fastapi import APIRouter, Depends, HTTPException

from app.schemas.users.type.professor import ProfessorCreate, ProfessorUpdate, ProfessorInDB
from app.infraestructure.db.models.user.type.professor import Professor
from app.services.users.type.professor import professor_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from app.api.middleware.mongo_db import get_mongo_db


router = APIRouter()

@router.post("/create", response_model=ProfessorInDB, status_code=201)
async def create_professor(*, obj_in: ProfessorCreate, db = Depends(get_mongo_db)) -> ProfessorInDB:
    try:
        professor_create = await professor_svc.create(obj_in=Professor(**dict(obj_in)), db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return professor_create
