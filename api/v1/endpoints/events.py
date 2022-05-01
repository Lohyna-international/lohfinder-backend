from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException, Body
from db import get_database, DatabaseManager
import json
from bson.objectid import ObjectId
from schemas.events_schema import EventsSchema

router = APIRouter(prefix="/events", tags=["Events"])


@router.get("/all")
async def get_all_events(db: DatabaseManager = Depends(get_database)):
    events = await db.get_events()
    if events is not None:
        return events
    else:
        raise HTTPException(500, "Failed to get events!")


@router.post("/create")
async def create_event(
    event_info: EventsSchema, db: DatabaseManager = Depends(get_database)
):
    result = await db.create_event(event_info.dict())
    if result:
        return {"id": result}
    else:
        raise HTTPException(500, "Failed to create event!")


@router.post("/delete/{id}")
async def delete_event(id, db: DatabaseManager = Depends(get_database)):
    if await db.delete_event(ObjectId(id)):
        return {}
    else:
        raise HTTPException(400, "Event not found")
