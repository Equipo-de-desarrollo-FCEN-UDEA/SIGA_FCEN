from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.schemas.application.type.mobility import MobilityCreate

from app.schemas.application.user_application import UserApplicationCreate

from app.services.application.type.mobility import MobilityService
from app.services.application.user_application import UserApplicationService

from app.api.routes.v1.utils.base_router import BaseRouter

from app.api.middleware.mongo_db import get_mongo_db
from app.api.middleware.postgres_db import get_db


router = APIRouter()

@router.post("/create", response_model=MobilityCreate, status_code=201)
async def create_mobility(*, obj_in: MobilityCreate, db_mongo = Depends(get_mongo_db), db_postgres = Depends(get_db)) -> MobilityCreate:
    user_application = UserApplicationCreate(user_id="", application_id="")

    

    try:
        mobility_create = await MobilityService.create(obj_in=obj_in, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return mobility_create