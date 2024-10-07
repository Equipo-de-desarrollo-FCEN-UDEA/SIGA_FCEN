from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.application.application import Application
from app.schemas.application.application import ApplicationCreate, ApplicationUpdate

class CRUDApplicationProtocol(CRUDProtocol[Application, ApplicationCreate, ApplicationUpdate]):
    pass