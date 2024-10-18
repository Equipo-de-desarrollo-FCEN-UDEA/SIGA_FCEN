from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends, Security

from app.api.middleware.bearer import get_current_active_user
from app.schemas.application.application import ApplicationCreate
from app.services.application.application import application_svc
from app.services.application.application import application_svc

from app.api.middleware.postgres_db import get_db


router = APIRouter()

@router.post("/create", response_model=ApplicationCreate, status_code=201)
def create_application(*, obj_in: ApplicationCreate, db = Depends(get_db), user = Security(get_current_active_user, scopes=["admin"])) -> ApplicationCreate:
    try:
        application_create = application_svc.create(obj_in=obj_in, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return application_create