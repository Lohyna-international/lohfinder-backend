from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from core.config import settings
from db.db_manager_base import DatabaseManager
from typing import List
from schemas.users_schema import UserSchema
from schemas.bin_schema import BinSchema
from schemas.events_schema import EventsSchema


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

    async def put_binary(self, key, name) -> bool:
        try:
            await self.db.bin.insert_one(BinSchema(key = key, name = name).dict())
            return True
        except Exception as e:
            print("Failed to add bin data to database : " + str(e))
            return False

    async def get_binary(self, name) -> str:
        try:
            result = await self.db.bin.find_one({"name" : name})
            return result['key'] if result else ""
        except:
            print("Failed to find file in database")
            return ""
    
    async def get_events(self) -> List[EventsSchema]:
        try:
            events = []
            async for event in self.db.events.find():
                events.append(EventsSchema(**event))
                events[-1].id = str(event["_id"])
            return events
        except Exception as e:
            print("Failed to find events : " + str(e))
            return None

    async def create_event(self, event_info):
        try:
            await self.db.events.insert_one(event_info)
            return str((await self.db.events.find_one(event_info))["_id"])
        except:
            print("Failed to insert event!")
            return None

    async def delete_event(self, id):
        try:
            await self.db.events.delete_one({"_id" : id})
            return True
        except Exception as e:
            print("Failed to delete event : " + str(e))
            return False
            