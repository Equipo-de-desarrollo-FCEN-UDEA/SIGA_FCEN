from app.services.base import ServiceBase
from app.protocols.db.crud.application.type.mobility import CRUDMobilityProtocol
from app.schemas.application.type.mobility import MobilityCreate, MobilityUpdate
from app.protocols.db.models.application.type.mobility import Mobility

class MobilityService(ServiceBase[Mobility, MobilityCreate, MobilityUpdate, CRUDMobilityProtocol]):
    pass

mobility_svc = MobilityService()