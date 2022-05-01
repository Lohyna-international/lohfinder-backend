from fileinput import filename
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from pydantic import FilePath
from db import get_database, DatabaseManager
import json
from hashlib import sha256
from os.path import splitext,exists
from os import mkdir, remove



router = APIRouter(prefix="/bin", tags=["Binary"])

files_path = "files"

@router.post("/")
async def upload_file(file : UploadFile, db: DatabaseManager = Depends(get_database)):
    fileName = file.filename
    data = await file.read()
    hash = sha256(data).hexdigest()
    try:
        if not exists(files_path):
            mkdir(files_path)
        (_, ext) = splitext(fileName)
        file_to_save = f"{files_path}/{hash}{ext}"
        with open(file_to_save, "wb") as output:
            output.write(data)
        if await db.put_binary(hash, fileName):
            return {"sha256" : hash}
        else:
            remove(file_to_save)
            raise HTTPException(501, "Database error")
    except:
        print("Failed to save file to disk")
        return {"status" : "Failed to save file on disk"}

@router.get("/{fileName}")
async def download_file(fileName : str, db: DatabaseManager = Depends(get_database)):
    saved_hash = await db.get_binary(fileName)
    (_, ext) = splitext(fileName)
    file_to_read = f"{files_path}/{saved_hash}{ext}"
    print(file_to_read)
    data = b""
    try:
        with open(file_to_read, "rb") as file:
            data = file.read()
    except:
        print("Failed to read file")
        return HTTPException(404, detail="File not found")

    new_hash = sha256(data).hexdigest()
    if saved_hash != new_hash:
        raise HTTPException(status_code=500, detail="File was damaged")
    return FileResponse(file_to_read, media_type=f"image/{ext[1:]}")
