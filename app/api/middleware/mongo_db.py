from app.infraestructure.db.utils.mongo_session import engine

async def get_mongo_db():
    try:
        db = engine.session()
        await db.start()
        yield db
    finally:
        await db.end()