from app.infraestructure.db.crud.application.type.base import ApplicationTypeBaseCrud
from app.infraestructure.db.models.application.type.mobility import Mobility
from app.schemas.application.type.mobility import MobilityCreate, MobilityUpdate



class MobilityCrud(ApplicationTypeBaseCrud[Mobility, MobilityCreate, MobilityUpdate]):
    pass

mobility_crud = MobilityCrud(Mobility)