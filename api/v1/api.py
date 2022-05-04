from fastapi import APIRouter
from api.v1.endpoints import user, binary, events


api_v1_router = APIRouter()
for router in [user, binary, events]:
    api_v1_router.include_router(router.router)
