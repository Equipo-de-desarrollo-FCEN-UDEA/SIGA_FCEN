from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.voting.vote  import Vote
from app.schemas.voting.vote import VoteCreate, VoteUpdate

class VoteCrud(CRUDBase[Vote, VoteCreate, VoteUpdate]):
    pass

vote_crud = VoteCrud(Vote)