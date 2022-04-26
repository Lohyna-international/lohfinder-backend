import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.v1.api import api_v1_router
from core.config import settings
from db import db

app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
async def on_app_start():
    """Anything that needs to be done while app starts"""
    await db.connect_to_database(settings.MONGO_URL)


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown"""
    await db.close_database_connection()


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_v1_router, prefix=settings.API_V1_STR)
