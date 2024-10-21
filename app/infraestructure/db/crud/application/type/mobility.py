from datetime import datetime
from fastapi import HTTPException
from app.core.exceptions import ORMError
from pymongo.errors import PyMongoError
from app.infraestructure.db.crud.mongo_base import CRUDBase
from app.infraestructure.db.models.application.type.mobility import Mobility, Status
from app.schemas.application.type.mobility import MobilityCreate, MobilityUpdate

from app.services.application.user_application import user_application_svc
from app.infraestructure.db.models.application.user_application import UserApplication
from app.schemas.application.user_application import UserApplicationCreate
from app.protocols.db.models.application.application_status import ApplicationStatusType

from app.schemas.users.user import User

from odmantic.session import AIOSession
from sqlalchemy.orm import Session



class MobilityCrud(CRUDBase[Mobility, MobilityCreate, MobilityUpdate]):
    async def create(self, db_mongo: AIOSession,
                     *, obj_in: MobilityCreate,
                     db_postgres: Session,
                     current_user: User
                     ) -> Mobility:
        user_application = UserApplicationCreate(user_id=current_user.id, application_id="1c779ce5-ce77-49ea-87e2-69a2388e53f2")
        obj_in_data = user_application.model_dump()
        db_obj = UserApplication(**obj_in_data)
        try:
            with db_postgres:
                db_postgres.add(db_obj)
                db_postgres.flush()
                
                obj_in.id_postgres = db_obj.id

                status = ApplicationStatusType.CREATE.value
                obj_in.status += [Status(name=status, updated_by=current_user.name, date=datetime.now())]
                mobility_create = await super().create(db_mongo, obj_in=Mobility(**dict(obj_in)))
                db_postgres.commit()

        except Exception as e:
            db_postgres.rollback()
            raise ORMError(str(e))
        
        except PyMongoError as e:
            db_postgres.rollback()
            raise HTTPException(status_code=400, detail= "Error: " + str(e))

        
        return mobility_create

mobility_crud = MobilityCrud(Mobility)