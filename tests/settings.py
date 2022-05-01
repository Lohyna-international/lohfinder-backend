import requests as re

class Settings:
    API_V1_STR: str = "api/v1"
    BACKEND_CORS_ORIGINS = ["http://localhost:8000"]

BACKEND_ADDRESS = Settings.BACKEND_CORS_ORIGINS[0]
API_PREFIX = Settings.API_V1_STR