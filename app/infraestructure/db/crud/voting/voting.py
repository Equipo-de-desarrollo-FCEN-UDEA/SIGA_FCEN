from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.voting.voting import Voting
from app.schemas.voting.voting import VotingCreate, VotingUpdate

class VotingCrud(CRUDBase[Voting, VotingCreate, VotingUpdate]):
    pass

voting_crud = VotingCrud(Voting)