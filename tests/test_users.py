from email.mime import base
import requests as re


def test_get_users(base_url, token):
    response = re.get(f"{base_url}/users", headers=token)
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_user_registration(base_url, user):
    response = re.post(f"{base_url}/users/signup/", json=user)
    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()
    assert len(response.json()["access_token"]) != 0
    assert response.json()["token_type"] == "bearer"


def test_user_login(base_url, user):
    signup_response = re.post(f"{base_url}/users/signup/", json=user)
    assert signup_response.status_code == 200

    login_response = re.post(
        f"{base_url}/users/login/",
        data={"username": user["username"], "password": user["password"]},
    )
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    assert "token_type" in login_response.json()
