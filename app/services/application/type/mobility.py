from app.errors.base import BaseErrors
from app.services.base import ServiceBase
from app.protocols.db.crud.application.type.mobility import CRUDMobilityProtocol
from app.schemas.application.type.mobility import MobilityCreate, MobilityUpdate
from app.protocols.db.models.application.type.mobility import Mobility

class MobilityService(ServiceBase[Mobility, MobilityCreate, MobilityUpdate, CRUDMobilityProtocol]):
    def create(self, *, 
               obj_in, 
               db_mongo,
               db_postgres,
               current_user
               ):
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.create(obj_in=obj_in, db_mongo=db_mongo, db_postgres=db_postgres, current_user=current_user)

mobility_svc = MobilityService()