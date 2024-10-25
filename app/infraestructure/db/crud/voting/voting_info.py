from app.infraestructure.db.crud.application.type.base import ApplicationTypeBaseCrud
from app.infraestructure.db.models.voting.voting_info import VotingInfo
from app.schemas.voting.voting_info import VotingInfoCreate, VotingInfoUpdate


class VotingInfoCrud(ApplicationTypeBaseCrud[VotingInfo, VotingInfoCreate, VotingInfoUpdate]):
    pass

voting_info_crud = VotingInfoCrud(VotingInfo)