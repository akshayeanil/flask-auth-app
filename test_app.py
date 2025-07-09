import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_register_and_login(client):
    client.post("/register", json={"username": "testuser", "password": "testpass"})
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
