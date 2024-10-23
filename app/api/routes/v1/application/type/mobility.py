from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session

from app.api.middleware.bearer import get_current_active_user
from app.schemas.application.type.mobility import MobilityCreate, Mobility, MobilityUpdate


from app.schemas.application.user_application import UserApplicationStatus
from app.schemas.users.user import User

from app.services.application.type.mobility import mobility_svc

from app.api.middleware.mongo_db import get_mongo_db, get_mongo_engine
from app.api.middleware.postgres_db import get_db

from app.protocols.db.models.application.application import ApplicationStatusType

from app.schemas.application.user_application_academic_unit import UserApplicationAcademicUnitCreate
from app.services.application.user_application_academic_unit import user_application_academic_unit_svc

from app.schemas.voting.voting import VotingCreate
from app.services.voting.voting import voting_svc


router = APIRouter()

@router.post("/create", response_model=MobilityCreate, status_code=201)
async def create_mobility(*, 
                          obj_in: MobilityCreate, 
                          db_mongo = Depends(get_mongo_db), 
                          db_postgres: Session = Depends(get_db),
                          current_user: Annotated[User, Depends(get_current_active_user)]
                          ) -> MobilityCreate:

    mobility_create = await mobility_svc.create(
        db_mongo=db_mongo,
        obj_in=obj_in,
        db_postgres=db_postgres,
        current_user=current_user,
        application_id="1c779ce5-ce77-49ea-87e2-69a2388e53f2"
    )


    return mobility_create

async def current_status(user_application_id: UUID, db_mongo) -> str:
    mobility = await mobility_svc.get(db = db_mongo, id = user_application_id)
    if not mobility:
        raise HTTPException(404, "User Application not found")
    
    mobility_dict = mobility.dict()
    current_status = mobility_dict["status"][-1]["name"]
    
    return current_status

def next_status(current_status: str) -> str:
    if current_status == ApplicationStatusType.CREATE.value:
        return ApplicationStatusType.IN_INSTITUTE.value
    else:
        return None
    
def send_to_academic_unit(*, academic_unit_id: UUID, user_application_id: UUID, db) -> None:
    user_application_to_send = UserApplicationAcademicUnitCreate(
        user_application_id=user_application_id,
        academic_unit_id=academic_unit_id
    )

    user_application_academic_unit_svc.create(obj_in=user_application_to_send, db=db)

def create_voting(*, academic_unit_id, user_application_id, db) -> None:
    voting_to_create = VotingCreate(
        academic_unit_id=academic_unit_id,
        user_application_id=user_application_id
    )

    voting_svc.create(obj_in=voting_to_create, db=db)

async def create_status(*, next_status: str, academic_unit_id, user_application_id, db_mongo, db_postgres, current_user:User) -> str:
    if next_status == ApplicationStatusType.IN_INSTITUTE.value:
        send_to_academic_unit(academic_unit_id=academic_unit_id, user_application_id=user_application_id, db=db_postgres)
        create_voting(academic_unit_id=academic_unit_id, user_application_id=user_application_id, db=db_postgres)
        status = UserApplicationStatus(name=next_status, updated_by=current_user.id, date=datetime.now())
        new_status = await mobility_svc.add_status(
            db_mongo=db_mongo,
            new_status=status,
            user_application_id=user_application_id
        )

        return "terminado"

    else:
        return next_status


@router.patch("/update/{id}", response_model=str, status_code=200)
async def update_status(*, 
                          id: UUID,
                          academic_unit_id: UUID,
                          db_mongo = Depends(get_mongo_db), 
                          db_postgres: Session = Depends(get_db),
                          current_user: Annotated[User, Depends(get_current_active_user)]
                          ) -> Mobility:

    _current_status = await current_status(id, db_mongo)
    _next_status = next_status(_current_status)

    _create_status = await create_status(
        next_status=_next_status,
        academic_unit_id=academic_unit_id,
        user_application_id=id,
        db_mongo=await get_mongo_engine(),
        db_postgres=db_postgres,
        current_user=current_user
    )

    return "Hola"