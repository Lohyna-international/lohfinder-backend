from fastapi import APIRouter
from api.v1.endpoints import user

api_v1_router = APIRouter()
api_v1_router.include_router(user.router)
