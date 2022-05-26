import requests as re


def test_get_users(base_url, token):
    response = re.get(f"{base_url}/users", headers=token)
    assert response.status_code == 200
    assert len(response.json()) != 0
