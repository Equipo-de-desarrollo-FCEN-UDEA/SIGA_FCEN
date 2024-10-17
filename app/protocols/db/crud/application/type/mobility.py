from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.application.type.mobility import Mobility
from app.schemas.application.type.mobility import MobilityCreate, MobilityUpdate

class CRUDMobilityProtocol(CRUDProtocol[Mobility, MobilityCreate, MobilityUpdate]):
    ...