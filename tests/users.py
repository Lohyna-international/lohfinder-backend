from settings import *

def get_users_test():
    users = re.get(f"{BACKEND_ADDRESS}/{API_PREFIX}/users").text
    assert len(users) != 0, "Failed user test"


get_users_test()
