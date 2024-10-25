from typing import TypeVar
from app.errors.base import BaseErrors
from app.services.base import ServiceBase
from app.schemas.utils.base_model import CreateSchemaType, UpdateSchemaType

from app.protocols.db.crud.application.user_application import CRUDUserApplicationProtocol

ModelType = TypeVar("ModelType")

CrudType = TypeVar("CrudType", bound=CRUDUserApplicationProtocol)

class ApplicationTypeBaseService(ServiceBase[ModelType, CreateSchemaType, UpdateSchemaType, CrudType]):
    def create(self, *, 
                obj_in, 
                db_mongo,
                db_postgres,
                current_user,
                application_id
               ):
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.create(obj_in=obj_in, db_mongo=db_mongo, db_postgres=db_postgres, current_user=current_user, application_id=application_id)
    
    def add_status(self, *, new_status, db_mongo, user_application_id):
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.add_status(new_status=new_status, db_mongo=db_mongo, user_application_id=user_application_id)