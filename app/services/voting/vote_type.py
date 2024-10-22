from app.services.base import ServiceBase
from app.schemas.voting.vote_type import VoteTypeCreate, VoteTypeUpdate
from app.protocols.db.models.voting.vote_type import VoteType
from app.protocols.db.crud.voting.vote_type import CRUDVoteTypeProtocol

class VoteTypeService(ServiceBase[VoteType, VoteTypeCreate, VoteTypeUpdate, CRUDVoteTypeProtocol]):
    pass

vote_type_svc = VoteTypeService()