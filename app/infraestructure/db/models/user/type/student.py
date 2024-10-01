from odmantic import Model
from uuid import UUID

class Student(Model):
    id_postgres: UUID
    email: str
    hashed_password: str