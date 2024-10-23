from uuid import UUID

from fastapi import HTTPException
from app.schemas.application.user_application_academic_unit import UserApplicationAcademicUnitCreate
from app.schemas.voting.voting import VotingCreate
from app.services.application.user_application_academic_unit import user_application_academic_unit_svc
from app.services.application.type.mobility import mobility_svc
from app.services.voting.voting import voting_svc


async def current_status(user_application_id: UUID, db_mongo, svc) -> str:
    obj_in_mongo = await svc.get(db = db_mongo, id = user_application_id)
    if not obj_in_mongo:
        raise HTTPException(404, "User Application not found")
    
    obj_dict = obj_in_mongo.dict()
    current_status = obj_dict["status"][-1]["name"]
    
    return current_status

    
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