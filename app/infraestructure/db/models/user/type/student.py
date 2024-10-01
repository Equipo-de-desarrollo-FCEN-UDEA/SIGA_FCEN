from odmantic import Field, Model
from uuid import UUID

class Student(Model):
    id_postgres: UUID = Field(primary_field=True) 
    semester: int