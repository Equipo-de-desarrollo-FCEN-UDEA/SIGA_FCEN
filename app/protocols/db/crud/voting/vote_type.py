from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.voting.vote_type import VoteType
from app.schemas.voting.vote_type import VoteTypeCreate, VoteTypeUpdate

class CRUDVoteTypeProtocol(CRUDProtocol[VoteType, VoteTypeCreate, VoteTypeUpdate]):
    pass