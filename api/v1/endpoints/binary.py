from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException
from db import get_database, DatabaseManager
import json
from hashlib import sha256
from os.path import splitext


router = APIRouter(prefix="/bin", tags=["Binary"])


@router.post("/{fileName}")
async def upload_file(file : bytes, fileName : str, db: DatabaseManager = Depends(get_database)):
    hash = sha256(file).hexdigest()
    try:
        (_, ext) = splitext(fileName)
        file_to_save = hash + ext
        with open(file_to_save, "wb") as output:
            output.write(file)
        return {"status" : hash if await db.put_binary(hash, fileName) else "Database error"} 
    except:
        print("Failed to save file to disk")
        return {"status" : "Failed to save file on disk"}

@router.get("/{fileName}")
async def download_file(fileName : str, db: DatabaseManager = Depends(get_database)):
    saved_hash = await db.get_binary(fileName)
    (_, ext) = splitext(fileName)
    file_to_read = saved_hash + ext
    data = b""
    try:
        with open(file_to_read, "rb") as file:
            data = file.read()
    except:
        print("Failed to save file to disk")
        return HTTPException(404, detail="File not found")

    new_hash = sha256(data).hexdigest
    if saved_hash != new_hash:
        raise HTTPException(status_code=400, detail="File was damaged")

    return FileResponse(file_to_read, media_type=f"image/{ext[1:]}")