from pydantic import BaseSettings, AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Lohfinder"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:8000"]
    MONGO_URL: str = "mongodb+srv://lohyna:4fKHPUizesfSsDrZ@lohfindercluster.u7ln4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    SECRET_KEY: str = "7f1e5baaef44bf34e3584a90cfc81a09ced9998db45d7c17f72c19c82b255453"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60  # 24 hours


settings = Settings()
