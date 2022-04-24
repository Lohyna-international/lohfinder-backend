from pydantic import BaseSettings, AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Lohfinder"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:8000"]
    MONGO_URL: str = "mongodb+srv://lohyna:4fKHPUizesfSsDrZ@lohfindercluster.u7ln4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


settings = Settings()
