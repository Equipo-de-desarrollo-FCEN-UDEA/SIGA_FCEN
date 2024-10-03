from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.core.config import Settings

settings = Settings()

client = AsyncIOMotorClient(settings.mongo_url, uuidRepresentation="standard")
engine = AIOEngine(client=client, database=settings.mongo_db)