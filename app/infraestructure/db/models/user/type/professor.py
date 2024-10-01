from uuid import UUID
from odmantic import Field, Model

class Professor(Model):
    id_postgres: UUID = Field(primary_field=True) 
    type: str