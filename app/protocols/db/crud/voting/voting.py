from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.voting.voting import Voting
from app.schemas.voting.voting import VotingCreate, VotingUpdate

class CRUDVotingProtocol(CRUDProtocol[Voting, VotingCreate, VotingUpdate]):
    pass