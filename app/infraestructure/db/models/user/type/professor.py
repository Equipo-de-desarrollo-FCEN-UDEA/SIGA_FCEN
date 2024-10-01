from uuid import UUID
from app.infraestructure.db.utils.mongo_base import MongoBase

class Professor(MongoBase):
    id_postgres: UUID
    type: str