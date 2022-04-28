from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from core.config import settings
from db.db_manager_base import DatabaseManager
from typing import List
from schemas.users_schema import UserSchema, Token


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, path):
        """Connect to MONGO DB"""
        print(f"Connecting to mongodb at {path}")
        self.client = AsyncIOMotorClient(path, maxPoolSize=10, minPoolSize=10)
        self.db = self.client.lohfinder  # lohfinder is mongodb database name
        print(f"Connected to mongo at {path}")

    async def close(self):
        """Close MongoDB Connection"""
        print("Closing connection with MongoDB")
        self.client.close()
        print("Closed connection with MongoDB")

    async def get_users_list(self) -> List[UserSchema]:
        users_list = []
        async for user in self.db.users.find():
            users_list.append(UserSchema(**user, id=user["_id"]))
        return users_list
