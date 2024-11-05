from uuid import UUID

from app.schemas.voting.voting import VotingResponse
from app.services.application.type.mobility import mobility_svc

async def get_application_in_mongo(*,
    voting,
    db) -> dict:
    user_application_id = voting.user_application_id
    application_type = voting.user_application.application.name
    
    voting = VotingResponse.model_validate(voting)
    voting = VotingResponse.model_dump(voting)

    if application_type == 'MOVILIDAD':
        mobility = {"mobility": await mobility_svc.get(id=user_application_id, db=db)}
        if mobility is None:
            raise ValueError(f"La solicitud de movilidad con id {user_application_id} no existe")        
        return voting['user_application'] | mobility