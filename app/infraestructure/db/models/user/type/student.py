from uuid import UUID
from app.infraestructure.db.utils.mongo_base import MongoBase

class Student(MongoBase):
    id_postgres: UUID
    semester: int