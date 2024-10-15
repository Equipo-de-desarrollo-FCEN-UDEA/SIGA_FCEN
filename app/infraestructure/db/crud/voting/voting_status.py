from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.voting.voting_status import VotingStatus
from app.schemas.voting.voting_status import VotingStatusCreate, VotingStatusUpdate

class VotingCrud(CRUDBase[VotingStatus, VotingStatusCreate, VotingStatusUpdate]):
    pass

voting_status_crud = VotingCrud(VotingStatus)