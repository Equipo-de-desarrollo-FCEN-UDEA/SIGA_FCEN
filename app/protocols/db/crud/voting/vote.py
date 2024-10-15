from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.voting.vote import Vote
from app.schemas.voting.vote import VoteCreate, VoteUpdate

class CRUDVoteProtocol(CRUDProtocol[Vote, VoteCreate, VoteUpdate]):
    pass