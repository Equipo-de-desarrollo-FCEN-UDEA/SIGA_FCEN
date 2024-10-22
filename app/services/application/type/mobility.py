from app.errors.base import BaseErrors
from app.services.application.type.base import ApplicationTypeBaseService
from app.protocols.db.crud.application.type.mobility import CRUDMobilityProtocol
from app.schemas.application.type.mobility import MobilityCreate, MobilityUpdate
from app.protocols.db.models.application.type.mobility import Mobility

class MobilityService(ApplicationTypeBaseService[Mobility, MobilityCreate, MobilityUpdate, CRUDMobilityProtocol]):
    pass

mobility_svc = MobilityService()