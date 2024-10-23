from app.infraestructure.db.utils.mongo_session import engine

async def get_mongo_db():
    try:
        yield engine
    finally:
        pass