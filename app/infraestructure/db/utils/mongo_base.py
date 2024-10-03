from odmantic import Field, Model
from uuid import UUID, uuid4

class MongoBase(Model):
    id: UUID = Field(default_factory=uuid4, primary_field=True)
