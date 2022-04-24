from db.mongodb import get_database


async def get_users_list():
    db = await get_database()
    users_collection = await db.users.find().to_list(length=None)
    print(users_collection)
    return users_collection
