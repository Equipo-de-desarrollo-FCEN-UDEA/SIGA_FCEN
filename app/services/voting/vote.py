from app.services.base import ServiceBase
from app.schemas.voting.vote import VoteCreate, VoteUpdate
from app.protocols.db.models.voting.vote import Vote
from app.protocols.db.crud.voting.vote import CRUDVoteProtocol

class VoteService(ServiceBase[Vote, VoteCreate, VoteUpdate, CRUDVoteProtocol]):
    pass

vote_svc = VoteService()