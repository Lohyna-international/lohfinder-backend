from db.db_manager_base import DatabaseManager
from db.mongodb import MongoManager

db = MongoManager()


async def get_database() -> DatabaseManager:
    return db
