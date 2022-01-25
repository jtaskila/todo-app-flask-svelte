

# Test the default endpoint of the app
# It should only accept get requests and return status 200
def test_homepage_status(tester):
    response = tester.get("/")
    assert response.status_code == 200

    response = tester.post("/")
    assert response.status_code == 405

def test_api_content_type(tester):
    response = tester.get("/")
    assert response.content_type == "application/json"
