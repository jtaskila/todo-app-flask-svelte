import random

def test_register_failure_empty_post(tester):
    response = tester.post("/")
    assert response.status_code == 405

def test_register_failure_invalid_post(tester):
    post_data = {
        "username": "",
        "password": "testpassword"
    }

    response = tester.post("/register", json=post_data)
    assert response.status_code == 400

def test_register_success(tester):
    # generating random username for registering
    # because same usernames are not allowed
    post_data = {
        "name": "testaccount"+str(random.randint(0,9999)),
        "password": "testpassword"
    }

    response = tester.post("/register", json=post_data)
    assert response.status_code == 200


def test_register_taken_username(tester):
    post_data = {
        "name": "testaccount",
        "password": "testpassword"
    }

    response = tester.post("/register", json=post_data)
    assert response.status_code == 409
