from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from bson import UuidRepresentation

USERNAME = "root"
PASSWORD = "root"

MONGO_URI = f"mongodb://{USERNAME}:{PASSWORD}@mongo-db-auth:27017"
DATABASE_NAME = "siga"


client = AsyncIOMotorClient(MONGO_URI, uuidRepresentation="standard")
engine = AIOEngine(client=client, database=DATABASE_NAME)