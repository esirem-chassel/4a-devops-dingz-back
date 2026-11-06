from fastapi.testclient import TestClient

from main import app

testClient = TestClient(app)

def test_home():
    response = testClient.get("/")
    assert response.status_code == 200
    assert "version" in response.json()
