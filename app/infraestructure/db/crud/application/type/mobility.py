from app.infraestructure.db.crud.mongo_base import CRUDBase
from app.infraestructure.db.models.application.type.mobility import Mobility
from app.schemas.application.type.mobility import MobilityCreate, MobilityUpdate

class MobilityCrud(CRUDBase[Mobility, MobilityCreate, MobilityUpdate]):
    ...

mobility_crud = MobilityCrud(Mobility)