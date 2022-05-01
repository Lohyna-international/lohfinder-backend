from settings import *

def create_event_test():
    event = {"createdBy" : "me", "city" : "Lviv", "title" : "test event", "mainPhoto" : "empty", "photos" : "", "description" : "test description"}
    result = re.post(f"{BACKEND_ADDRESS}/{API_PREFIX}/events/create", json=event)
    assert result.status_code == 200, "Failed to create event!"


def get_events_test():
    events = re.get(f"{BACKEND_ADDRESS}/{API_PREFIX}/events/all")
    print("Total events : " + str(len(events.json())))
    assert events.status_code == 200, "Failed to get events!"

def clean_up():
    events = re.get(f"{BACKEND_ADDRESS}/{API_PREFIX}/events/all")
    for event_id in [e['id'] for e in events.json()]:
        res = re.post(f"{BACKEND_ADDRESS}/{API_PREFIX}/events/delete/{event_id}")
        assert res.status_code == 200, "Failed to delete event!"



create_event_test()
get_events_test()
clean_up()
get_events_test()
