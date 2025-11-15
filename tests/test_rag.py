from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query():
    resp = client.post("/query", json={"question": "What is this about?"})
    assert resp.status_code == 200
