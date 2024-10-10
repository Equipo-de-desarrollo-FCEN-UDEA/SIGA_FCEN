from app.services.base import ServiceBase
from app.schemas.voting.voting import VotingCreate, VotingUpdate
from app.protocols.db.models.voting.voting import Voting
from app.protocols.db.crud.voting.voting import CRUDVotingProtocol

class VotingService(ServiceBase[Voting, VotingCreate, VotingUpdate, CRUDVotingProtocol]):
    pass

voting_svc = VotingService()