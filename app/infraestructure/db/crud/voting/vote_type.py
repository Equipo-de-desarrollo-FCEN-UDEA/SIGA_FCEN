from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.voting.vote_type import VoteType
from app.schemas.voting.vote_type import VoteTypeCreate, VoteTypeUpdate

class VoteTypeCrud(CRUDBase[VoteType, VoteTypeCreate, VoteTypeUpdate]):
    pass

vote_type_crud = VoteTypeCrud(VoteType)