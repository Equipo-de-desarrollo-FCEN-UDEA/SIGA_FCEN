from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "siga"

client = AsyncIOMotorClient(MONGO_URI)
engine = AIOEngine(motor_client=client, database=DATABASE_NAME)