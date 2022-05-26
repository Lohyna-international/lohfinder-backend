import requests as re

from tests.conftest import base_url


def test_create_event(base_url, token, event):
    result = re.post(f"{base_url}/events/create", json=event, headers=token)
    assert result.status_code == 200


def test_get_all_events(base_url, token):
    events = re.get(f"{base_url}/events/all", headers=token)
    assert events.status_code == 200
    assert len(events.json()) != 0


def test_event_removal(base_url, token):
    events = re.get(f"{base_url}/events/all", headers=token)
    for event_id in [e["id"] for e in events.json()]:
        res = re.post(f"{base_url}/events/delete/{event_id}", headers=token)
        assert res.status_code == 200
