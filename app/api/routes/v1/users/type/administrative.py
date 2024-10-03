from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.schemas.users.type.administrative import (AdministrativeCreate, AdministrativeUpdate, 
                                                   AdministrativeInDB, AdministrativeResponse)
from app.infraestructure.db.models.user.type.administrative import Administrative
from app.schemas.users.user import UserInDB
from app.services.users.type.administrative import administrative_svc
from app.services.users.user import user_svc
from app.api.routes.v1.utils.base_router import BaseRouter

from app.api.middleware.mongo_db import get_mongo_db
from app.api.middleware.postgres_db import get_db


router = APIRouter()

@router.post("/create", response_model=AdministrativeInDB, status_code=201)
async def create_administrative(*, obj_in: AdministrativeCreate, db = Depends(get_mongo_db)) -> AdministrativeInDB:
    try:
        administrative_create = await administrative_svc.create(obj_in=Administrative(**dict(obj_in)), db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return administrative_create

@router.get("/get/{id}", response_model=AdministrativeResponse, status_code=200)
async def get_administrative(*, 
                        id: UUID, 
                        mongo_db = Depends(get_mongo_db), 
                        postgres_db= Depends(get_db)) -> AdministrativeResponse:
    administrative = await administrative_svc.get(id=id, db=mongo_db)
    if not administrative:
        raise HTTPException(404, "Administrative not found")
    user_in_db = user_svc.get(id=administrative.id_postgres, db=postgres_db)
    user = UserInDB.model_validate(user_in_db)
    administrative_dict = administrative.dict()
    response = AdministrativeResponse(
        **dict(user),
        administrative=administrative_dict
    )
    
    return response

@router.get("/get-all", response_model=list[AdministrativeInDB], status_code=200)
async def get_all_administrative(*, mongo_db = Depends(get_mongo_db)) -> list[AdministrativeInDB]:
    return await administrative_svc.get_multi(db=mongo_db)
