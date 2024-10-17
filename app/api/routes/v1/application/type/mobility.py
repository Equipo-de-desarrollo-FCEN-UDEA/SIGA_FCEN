from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.api.middleware.bearer import get_current_active_user
from app.schemas.application.type.mobility import MobilityCreate

from app.schemas.application.user_application import UserApplicationCreate

from app.schemas.users.user import User
from app.infraestructure.db.models.application.type.mobility import Mobility
from app.services.application.type.mobility import mobility_svc
from app.services.application.user_application import user_application_svc

from app.api.routes.v1.utils.base_router import BaseRouter

from app.api.middleware.mongo_db import get_mongo_db
from app.api.middleware.postgres_db import get_db


router = APIRouter()

@router.post("/create", response_model=MobilityCreate, status_code=201)
async def create_mobility(*, 
                          obj_in: MobilityCreate, 
                          db_mongo = Depends(get_mongo_db), 
                          db_postgres = Depends(get_db),
                          current_user: Annotated[User, Depends(get_current_active_user)]
                          ) -> MobilityCreate:
    user_application = UserApplicationCreate(user_id=current_user.id, application_id="256f22e1-cd04-4fc2-97e0-d13b26bffa9e")

    user_application_in_db = user_application_svc.create(obj_in=user_application, db=db_postgres)
    obj_in.id_postgres = user_application_in_db.id

    print (f"OBJETO: {obj_in}")

    mobility_create = await mobility_svc.create(obj_in=Mobility(**dict(obj_in)), db=db_mongo)

    return mobility_create