from fastapi import APIRouter, Depends
from db import get_database, DatabaseManager
from core.helpers import parse_json
import json


router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users(db: DatabaseManager = Depends(get_database)):
    users = await db.get_users_list()
    return users
