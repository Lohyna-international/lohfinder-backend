import pytest
import os
from db import db
from core.config import settings
import requests as re


class Settings:
    API_V1_STR: str = "api/v1"
    BACKEND_CORS_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]
    DEBUG = False


@pytest.fixture
def base_url():
    BACKEND_ADDRESS = (
        Settings.BACKEND_CORS_ORIGINS[0]
        if Settings.DEBUG
        else Settings.BACKEND_CORS_ORIGINS[1]
    )
    API_PREFIX = Settings.API_V1_STR
    return os.path.join(BACKEND_ADDRESS, API_PREFIX)


@pytest.fixture
def user():
    user_info = {
        "password": "test_password",
        "username": "test_username",
        "fullName": "test_fullbane",
        "city": "test_city",
    }
    return user_info


@pytest.fixture
def event():
    event = {
        "createdBy": "me",
        "city": "Lviv",
        "title": "test event",
        "mainPhoto": "empty",
        "photos": "",
        "description": "test description",
    }
    return event


@pytest.fixture
def token(user, base_url):
    response = re.post(f"{base_url}/users/signup/", json=user)
    token = {"Authorization": "Bearer " + response.json()["access_token"]}
    return token
